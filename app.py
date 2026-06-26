import streamlit as st
import streamlit.components.v1 as components
import yt_dlp
from twilio.rest import Client

# 🔑 YOUR LIVE FULLY-CONFIGURED TWILIO KEYS
TWILIO_ACCOUNT_SID = "AC3e1ae3aa0ee793ec4dfa447e7c04a969"
TWILIO_AUTH_TOKEN = "13533aa65d3d2d562732892c6092313a"
YOUR_PERSONAL_PHONE = "+2348101607576" 

st.set_page_config(page_title="DevFlex FastLoad Hub", page_icon="⚡")

st.markdown("<h1 style='text-align: center; color: #4f46e5;'>⚡ DevFlex FastLoad</h1>", unsafe_allow_html=True)

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
    if not user_link:
        st.error("❌ Please paste a valid link first!")
    else:
        with st.spinner("Extracting..."):
            try:
                ydl_opts = {'format': 'best', 'quiet': True}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(user_link, download=False)
                    url = info.get('url')
                    title = info.get('title')

                if url:
                    st.success(f"🎉 Found: {title}")
                    
                    # Run the automatic WhatsApp logging notification
                    send_whatsapp_link(title, url)
                    
                    st.info("Support the developer by viewing our sponsor, then download below.")
                    
                    # 💵 YOUR REAL UNBLOCKED ADSTERRA SMARTLINK REVENUE LINK
                    adsterra_smartlink = "https://www.effectivecpmnetwork.com/m7y1p4z0?key=837524906cbad9df906a2cb5af217894"
                    
                    # 1. RED SPONSOR BUTTON (Triggers your high-paying SmartLink)
                    st.markdown(f"""
                        <a href="{adsterra_smartlink}" target="_blank" style="text-decoration:none;">
                            <div style="background-color:#ef4444; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold; cursor:pointer;">
                                📢 SPONSOR: Click to support this free tool (Unlock Payout)
                            </div>
                        </a>
                    """, unsafe_allow_html=True)

                    # 💵 2. VISUAL BANNER AD ZONE (Injected securely into an iframe sandbox)
                    st.write("")
                    banner_html_code = """
                    <html>
                    <body style="margin:0; padding:0; text-align:center;">
                        <script type="text/javascript">
                          atOptions = {
                            'key' : '3c6a9178cea1f2ed2663e8a478ac3476',
                            'format' : 'iframe',
                            'height' : 90,
                            'width' : 728,
                            'params' : {}
                          };
                        </script>
                        <script type="text/javascript" src="https://www.highperformanceformat.com/3c6a9178cea1f2ed2663e8a478ac3476/invoke.js"></script>
                    </body>
                    </html>
                    """
                    components.html(banner_html_code, height=100, scrolling=False)

                    # 3. GREEN DOWNLOAD BUTTON (Delivers the raw video)
                    st.markdown(f"""
                        <a href="{url}" target="_blank" style="text-decoration:none;">
                            <div style="background-color:#059669; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold; cursor:pointer;">
                                📥 DOWNLOAD VIDEO
                            </div>
                        </a>
                    """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error("❌ Extraction failed. Please try a different link.")
