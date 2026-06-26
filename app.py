import streamlit as st
import streamlit.components.v1 as components
import yt_dlp
from twilio.rest import Client

# 🔑 YOUR LIVE FULLY-CONFIGURED TWILIO KEYS
TWILIO_ACCOUNT_SID = "AC3e1ae3aa0ee793ec4dfa447e7c04a969"
TWILIO_AUTH_TOKEN = "13533aa65d3d2d562732892c6092313a"
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
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message_body = f"⚡ *FASTLOAD HUB EXTRACTION SUCCESS*\n\n🎬 *File:* {video_title}\n\n📥 *Direct Link:* {download_url}"
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
                    
                                        # 💵 ✅ THE ACTIVE CLEAN REVENUE ZONE (Streamlit Secured)
                    st.write("✨ Sponsored Content Below:")
                    
                    # This HTML layout embeds your Adsterra banner inside a secure frame
                    adsterra_html = """
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
                        <script type="text/javascript" src="https://highperformanceformat.com"></script>
                    </body>
                    </html>
                    """
                    
                    # Forces the ad banner to render flawlessly on mobile and desktop
                    components.html(adsterra_html, height=100, scrolling=False)

                    
                    # The Final Link Download Button
                    st.markdown(
                        f"<a href='{direct_download_url}' target='_blank'><button style='width:100%; background:linear-gradient(135deg, #4f46e5 0%, #059669 100%); color:white; border:none; padding:15px; border-radius:10px; font-weight:bold; cursor:pointer;'>📥 CLICK TO SAVE / DOWNLOAD FILE</button></a>", 
                        unsafe_allow_html=True
                    )
                else:
                    st.error("❌ Could not extract a direct file stream from that link.")
            except Exception as e:
                st.error(f"❌ Extraction Error: Make sure the URL link is valid and public.")
