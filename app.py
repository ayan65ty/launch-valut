import streamlit as st
import yt_dlp
import time
from twilio.rest import Client

# 🔑 APP CONFIGURATION
st.set_page_config(page_title="DevFlex FastLoad Hub", page_icon="⚡")

# 1. AD INTEGRATION (PropellerAds)
# Replace the src link below with your actual ad script URL from PropellerAds
st.markdown("""
    <script async src="https://3nbf4.com/act/files/tag.min.js?z=11212543"></script>
""", unsafe_allow_html=True)

# --- TWILIO KEYS ---
TWILIO_ACCOUNT_SID = "AC3e1ae3aa0ee793ec4dfa447e7c04a969"
TWILIO_AUTH_TOKEN = "13533aa65d3d2d562732892c6092313a"
YOUR_PERSONAL_PHONE = "+2348101607576" 

st.markdown("<h1 style='text-align: center; color: #4f46e5;'>⚡ DevFlex FastLoad</h1>", unsafe_allow_html=True)
st.subheader("Download from YouTube, TikTok, Twitter, Instagram & Facebook")

if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

user_link = st.text_input("📋 Paste your Video URL:", placeholder="https://...")

def send_whatsapp_link(video_title, download_url):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message_body = f"⚡ *FASTLOAD SUCCESS*\n\n🎬 *File:* {video_title}\n\n📥 *Direct Link:* {download_url}"
        client.messages.create(from_='whatsapp:+14155238886', body=message_body, to=f'whatsapp:{YOUR_PERSONAL_PHONE}')
    except Exception as e:
        print(f"Twilio Error: {e}")

if st.button("Fetch Download Link ✨", use_container_width=True):
    st.session_state.unlocked = False
    if not user_link:
        st.error("❌ Please paste a valid link first!")
    else:
        with st.spinner("Analyzing high-speed stream..."):
            try:
                # Universal options to handle various sites
                ydl_opts = {
                    'format': 'best', 
                    'quiet': True,
                    'no_warnings': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(user_link, download=False)
                    st.session_state.video_url = info.get('url')
                    st.session_state.video_title = info.get('title', 'Video Download')

                if st.session_state.video_url:
                    st.success(f"🎉 Success! Found: {st.session_state.video_title}")
                    send_whatsapp_link(st.session_state.video_title, st.session_state.video_url)
                else:
                    st.error("❌ Could not find a download link. The video might be private.")
            except Exception as e:
                st.error(f"❌ Extraction failed. Ensure the link is public.")

if 'video_url' in st.session_state and st.session_state.video_url:
    st.write("---")
    if not st.session_state.unlocked:
        st.warning("🔒 SECURE CONNECTING: Processing stream...")
        if st.button("🚀 CLICK TO ACTIVATE DOWNLOAD", use_container_width=True):
            with st.spinner("Synchronizing server..."):
                time.sleep(5)
                st.session_state.unlocked = True
                st.rerun()
    else:
        st.success("🔓 Server bridge verified!")
        st.markdown(f"""
            <a href="{st.session_state.video_url}" target="_blank" style="text-decoration:none;">
                <div style="width:100%; background:#059669; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold;">
                    📥 CLICK HERE TO SAVE / DOWNLOAD VIDEO
                </div>
            </a>
        """, unsafe_allow_html=True)
