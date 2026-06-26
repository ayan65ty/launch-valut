import streamlit as st
import requests
import json
import os
import concurrent.futures
import pandas as pd
import plotly.express as px
from datetime import datetime
from twilio.rest import Client

# --- CONFIGURATION ---
TWILIO_SID = 'YOUR_ACCOUNT_SID_HERE'
TWILIO_TOKEN = 'YOUR_AUTH_TOKEN_HERE'
TWILIO_PHONE = '+1234567890'
DATA_FILE = "sites_data.json"
HISTORY_FILE = "history.json"

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    /* Dark Theme Customization */
    .stApp { background-color: #0e1117; }
    h1 { color: #00f2ff; text-align: center; }
    h3 { color: #ffffff; }
    .stButton>button { 
        width: 100%; 
        border-radius: 5px; 
        border: 1px solid #00f2ff;
        color: #00f2ff;
        background-color: transparent;
    }
    .stButton>button:hover { background-color: #00f2ff; color: #000000; }
    </style>
    """, unsafe_allow_html=True)

# --- CORE FUNCTIONS ---
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return [{"url": "https://google.com", "phone": "+1234567890"}]

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def save_history(url, status):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    history.append({"timestamp": datetime.now().strftime("%H:%M:%S"), "url": url, "status": status})
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def send_sms_alert(to_number, site_url):
    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        client.messages.create(body=f"🚨 ALERT: {site_url} is down!", from_=TWILIO_PHONE, to=to_number)
    except:
        pass

def check_site(site):
    try:
        response = requests.get(site["url"], timeout=5)
        success = response.status_code == 200
        status = "ONLINE" if success else "OFFLINE"
        save_history(site["url"], status)
        if not success: send_sms_alert(site['phone'], site["url"])
        return {"url": site["url"], "status": status, "success": success}
    except:
        save_history(site["url"], "OFFLINE")
        send_sms_alert(site['phone'], site["url"])
        return {"url": site["url"], "status": "OFFLINE", "success": False}

# --- APP UI ---
st.title("🚀 DevFlex Premium Monitor")

if "websites" not in st.session_state: 
    st.session_state.websites = load_data()

# SIDEBAR FOR INPUTS
with st.sidebar:
    st.header("➕ Add New Asset")
    new_url = st.text_input("Website URL", placeholder="https://example.com")
    new_phone = st.text_input("Alert Phone Number", placeholder="+1234567890")
    if st.button("Add to Monitor"):
        if new_url and new_phone:
            st.session_state.websites.append({"url": new_url, "phone": new_phone})
            save_data(st.session_state.websites)
            st.success("Asset Added!")
            st.rerun()

# MAIN AREA
st.subheader("📋 Currently Monitored Assets")
for i, site in enumerate(st.session_state.websites):
    st.write(f"{i+1}. 🌐 **{site['url']}** | 📱 {site['phone']}")

if st.button("🔄 Run Parallel Ping Check"):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(check_site, st.session_state.websites))
    st.success("Ping check completed successfully.")

# CHART
if os.path.exists(HISTORY_FILE):
    df = pd.read_json(HISTORY_FILE)
    st.subheader("📈 Performance Trends")
    fig = px.bar(df, x="timestamp", y="status", color="url", title="Uptime History")
    st.plotly_chart(fig, use_container_width=True)