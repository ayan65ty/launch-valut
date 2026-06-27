import streamlit as st
import streamlit.components.v1 as components
import yt_dlp
import time
from twilio.rest import Client

# 🔑 YOUR LIVE FULLY-CONFIGURED TWILIO KEYS
TWILIO_ACCOUNT_SID = "AC3e1ae3aa0ee793ec4dfa447e7c04a969"
TWILIO_AUTH_TOKEN = "13533aa65d3d2d562732892c6092313a"
YOUR_PERSONAL_PHONE = "+2348101607576" 

st.set_page_config(page_title="DevFlex FastLoad Hub", page_icon="⚡")

st.markdown("<h1 style='text-align: center; color: #4f46e5;'>⚡ DevFlex FastLoad</h1>", unsafe_allow_html=True)

# Initialize unlock tracker state
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

user_link = st.text_input("📋 Paste your Video URL:", placeholder="https://youtube.com...")

def send_whatsapp_link(video_title, download_url):
    """Sends the extracted download link straight to your personal WhatsApp."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message_body = f"⚡ *FASTLOAD HUB EXTRACTION SUCCESS*\n\n🎬 *File:* {video_title}\n\n📥 *Direct Link:* {download_url}"
        client.messages.create(from_='whatsapp:+14155238886', body=message_body, to=f'whatsapp:{YOUR_PERSONAL_PHONE}')
    except Exception as e:
        print(f"Twilio Error: {e}")

if st.button("Fetch Download Link ✨", use_container_width=True):
    st.session_state.unlocked = False # Reset lock for new URLs
    if not user_link:
        st.error("❌ Please paste a valid link first!")
    else:
        with st.spinner("Extracting high-speed file streams..."):
            try:
                ydl_opts = {'format': 'best', 'quiet': True}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(user_link, download=False)
                    st.session_state.video_url = info.get('url')
                    st.session_state.video_title = info.get('title')

                if st.session_state.video_url:
                    st.success(f"🎉 Success! Found: {st.session_state.video_title}")
                    send_whatsapp_link(st.session_state.video_title, st.session_state.video_url)
                
            except Exception as e:
                st.error("❌ Extraction failed. Please try a different link.")

# 🔒 DLS-STYLE TIMED UNLOCK ZONE
if 'video_url' in st.session_state and st.session_state.video_url:
    st.write("---")
    
    if not st.session_state.unlocked:
        st.warning("🔒 SECURE CONNECTING LINK: Watch the premium sponsored notification below to unlock your direct file.")
        
        # 💵 YOUR REAL ACTIVE SOCIAL BAR CODE (Injected inside a secure HTML sandbox frame)
        social_bar_html = """
        <html>
        <body style="margin:0; padding:0; text-align:center;">
            <script src="https://pl30091878.effectivecpmnetwork.com/4c/3f/54/4c3f5432735759bd6ed5c9b3521dcb30.js"></script>
        </body>
        </html>
        """
        components.html(social_bar_html, height=130, scrolling=False)
        
        # Unskippable action countdown button logic
        if st.button("🚀 CLICK TO ACTIVATE SECURITY DE-ENCRYPTION TIMER", use_container_width=True):
            countdown_placeholder = st.empty()
            for seconds_left in range(10, 0, -1):
                countdown_placeholder.info(f"⏳ Synchronizing server files... Please watch the ad notification. {seconds_left} seconds left.")
                time.sleep(1)
            
            countdown_placeholder.empty()
            st.session_state.unlocked = True
            st.rerun()
            
    else:
        # THE CLEAN FINAL CONVERTED FILE DOWNLOAD LINK BUTTON REVEAL
        st.success("🔓 Server bridge verified successfully! Save your file below:")
        st.markdown(f"""
            <a href="{st.session_state.video_url}" target="_blank" style="text-decoration:none;">
                <div style="width:96%; background:linear-gradient(135deg, #059669 0%, #10b981 100%); color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold; cursor:pointer; font-size:16px;">
                    📥 CLICK HERE TO SAVE / DOWNLOAD VIDEO
                </div>
            </a>
        """, unsafe_allow_html=True)
