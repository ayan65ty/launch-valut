import streamlit as st
import yt_dlp
import time
from twilio.rest import Client

# 🔑 YOUR LIVE FULLY-CONFIGURED TWILIO KEYS
TWILIO_ACCOUNT_SID = "AC3e1ae3aa0ee793ec4dfa447e7c04a969"
TWILIO_AUTH_TOKEN = "13533aa65d3d2d562732892c6092313a"
YOUR_PERSONAL_PHONE = "+2348101607576" 

# Page Layout Styles
st.set_page_config(page_title="DevFlex FastLoad Hub", page_icon="⚡", layout="centered")

# Header Logo & Branding
st.markdown("<h1 style='text-align: center; color: #4f46e5;'>⚡ DevFlex <span style='color: #059669;'>FastLoad</span></h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #64748b; font-size: 14px;'>The ultimate high-speed direct link extractor engine.</h3>", unsafe_allow_html=True)

st.write("---")

# Initialize click tracker memories for the button session
if 'ad_clicked' not in st.session_state:
    st.session_state.ad_clicked = False
if 'ready' not in st.session_state:
    st.session_state.ready = False
if 'download_url' not in st.session_state:
    st.session_state.download_url = ""

# The Link Paste Field Box
user_link = st.text_input("📋 Paste your Video URL or Google Link here:", placeholder="https://example.com...")

def send_whatsapp_link(video_title, download_url):
    """Sends the extracted download link straight to your personal WhatsApp."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message_body = f"⚡ *FASTLOAD HUB EXTRACTION SUCCESS*\n\n🎬 *File:* {video_title}\n\n📥 *Direct Link:* {download_url}"
        client.messages.create(from_='whatsapp:+14155238886', body=message_body, to=f'whatsapp:{YOUR_PERSONAL_PHONE}')
    except Exception as e:
        print(f"Twilio Error: {e}")

# Action Trigger Button
if st.button("Fetch Download Link ✨", use_container_width=True):
    st.session_state.ad_clicked = False  # Reset tracker for a fresh URL fetch
    st.session_state.ready = False
    if not user_link:
        st.error("❌ Please paste a valid link first!")
    else:
        with st.spinner("Extracting direct high-speed data stream links..."):
            try:
                ydl_opts = {'format': 'best', 'quiet': True, 'no_warnings': True}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(user_link, download=False)
                    direct_download_url = info.get('url', None)
                    video_title = info.get('title', 'Extracted Video File')

                if direct_download_url:
                    st.success(f"🎉 Success! Found: {video_title}")
                    send_whatsapp_link(video_title, direct_download_url)
                    
                    # Store variables in session state to keep them across button clicks
                    st.session_state.download_url = direct_download_url
                    st.session_state.ready = True
                else:
                    st.error("❌ Could not extract a direct file stream from that link.")
            except Exception as e:
                st.error(f"❌ Extraction Error: Make sure the URL link is valid and public.")

# Render the dynamic single button zone if a video link is ready
if st.session_state.ready:
    adsterra_money_link = "https://highperformanceformat.com"
    
    st.write("---")
    
    # Check if they have clicked to trigger the ad yet
    if not st.session_state.ad_clicked:
        # CLICK 1: Act as an ad trigger button to bypass popup blockers cleanly
        st.markdown(
            f"""
            <div style="text-align:center;">
                <p style="color:#64748b; font-size:13px; margin-bottom:5px;">📥 Your file is compressed and ready for local download.</p>
                <a href="{adsterra_money_link}" target="_blank" style="text-decoration:none;">
                    <div style="width:96%; background:linear-gradient(135deg, #4f46e5 0%, #059669 100%); color:white; padding:15px; border-radius:10px; font-weight:bold; font-size:16px; display:inline-block; cursor:pointer;">
                        📥 CLICK HERE TO SAVE / DOWNLOAD FILE
                    </div>
                </a>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Hidden native streamlit synchronization button to switch states seamlessly
        if st.button("🔄 Connection Complete (Click to Unlock Video Link)", use_container_width=True):
            st.session_state.ad_clicked = True
            st.rerun()
            
    else:
        # CLICK 2: Hand them the raw video file direct download link stream!
        st.markdown(
            f"""
            <div style="text-align:center;">
                <p style="color:#059669; font-weight:bold; font-size:13px; margin-bottom:5px;">✅ Secure server bridge connected successfully!</p>
                <a href="{st.session_state.download_url}" target="_blank" style="text-decoration:none;">
                    <div style="width:96%; background:linear-gradient(135deg, #059669 0%, #10b981 100%); color:white; padding:15px; border-radius:10px; font-weight:bold; font-size:16px; display:inline-block; cursor:pointer;">
                        📥 CLICK AGAIN TO CONFIRM SAVE / DOWNLOAD FILE
                    </div>
                </a>
            </div>
            """, 
            unsafe_allow_html=True
        )
