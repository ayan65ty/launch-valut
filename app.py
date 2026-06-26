import streamlit as st
import streamlit.components.v1 as components
import yt_dlp
from twilio.rest import Client

# 🔑 YOUR LIVE TWILIO CONFIGURATION KEYS
# Your Account SID is pre-configured. Paste your secret Auth Token on line 10!
TWILIO_ACCOUNT_SID = "AC3e1ae3aa0ee793ec4dfa447e7c04a969"
TWILIO_AUTH_TOKEN = "6e51d336f3b833e08ea549c0b345eff4"
YOUR_PERSONAL_PHONE = "+2348101607576" 

# Page Layout Styles
st.set_page_config(page_title="DevFlex FastLoad Hub", page_icon="⚡", layout="centered")

# Header Logo & Branding
st.markdown("<h1 style='text-align: center; color: #4f46e5;'>⚡ DevFlex <span style='color: #059669;'>FastLoad</span></h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #64748b; font-size: 14px;'>The ultimate ad-supported direct URL link extractor engine.</h3>", unsafe_allow_html=True)

st.write("---")

# The Link Paste Field Box
user_link = st.text_input("📋 Paste your Video URL or Google Link here:", placeholder="https://example.com...")

def send_whatsapp_link(video_title, download_url):
    """Sends the extracted download link straight to your personal WhatsApp."""
    if "PASTE_YOUR" in TWILIO_AUTH_TOKEN:
        return
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message_body = f"⚡ *FASTLOAD HUB EXTRATION SUCCESS*\n\n🎬 *File:* {video_title}\n\n📥 *Direct Link:* {download_url}"
        client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{YOUR_PERSONAL_PHONE}'
        )
    except Exception as e:
        print(f"Twilio Error: {e}")

# Action Trigger Button
if st.button("Fetch Download Link ✨", use_container_width=True):
    if not user_link:
        st.error("❌ Please paste a valid link first!")
    else:
        with st.spinner("Extracting direct high-speed data stream links..."):
            try:
                ydl_opts = {
                    'format': 'best',
                    'quiet': True,
                    'no_warnings': True,
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(user_link, download=False)
                    direct_download_url = info.get('url', None)
                    video_title = info.get('title', 'Extracted Video File')

                if direct_download_url:
                    st.success(f"🎉 Success! Found: {video_title}")
                    
                    # Send the link to your phone automatically in the background
                    send_whatsapp_link(video_title, direct_download_url)
                                         # 💵 AD ZONE
                    st.write("✨ Sponsored Content Below:")
                    
                    # PASTE YOUR REAL COPIED ADSTERRA SMARTLINK INSIDE THE HREF QUOTES BELOW!
                    st.markdown(
                        f"""
                        <div style="text-align:center; background-color:#f1f5f9; padding:15px; border-radius:10px; border:2px dashed #4f46e5; margin-bottom:15px;">
                            <p style="color:#4f46e5; font-weight:bold; margin-bottom:5px; font-size:14px;">⚡ PREMIUM ACCELERATOR ACTIVE ⚡</p>
                            <p style="color:#64748b; font-size:12px; margin-bottom:10px;">Click the button below to verify your network speed and unlock unlimited bandwidth.</p>
                            <a href="https://www.effectivecpmnetwork.com/m7y1p4z0?key=837524906cbad9df906a2cb5af217894" target="_blank">
                                <button style="background-color:#4f46e5; color:white; border:none; padding:10px 20px; border-radius:5px; font-weight:bold; cursor:pointer;">🚀 ACTIVATE HIGH SPEED DOWNLOAD</button>
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.error("❌ Could not extract a direct file stream from that link.")
            except Exception as e:
                st.error(f"❌ Extraction Error: Make sure the URL link is valid and public.")
