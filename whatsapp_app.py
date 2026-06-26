import streamlit as st

st.set_page_config(page_title="QuickChat WhatsApp Linker", page_icon="💬", layout="centered")

st.markdown("<h1 style='text-align: center; color: #25d366;'>💬 QuickChat Linker</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #64748b; font-size: 14px;'>Message any phone number directly without saving it to your contacts.</h3>", unsafe_allow_html=True)

st.write("---")

# Input field for the phone number
phone_number = st.text_input("📞 Enter phone number (Include country code, e.g., 2348101607576):", placeholder="234...")

# Input field for an optional default text message
custom_message = st.text_input("📝 Optional: Type a default message to open with the chat:", placeholder="Hello, I want to buy your product...")

if st.button("Generate Direct Chat Link ✨", use_container_width=True):
    if not phone_number:
        st.error("❌ Please enter a phone number first!")
    else:
        # Clean up any spaces or '+' signs the user typed
        clean_number = phone_number.replace("+", "").replace(" ", "")
        
        # Build the official WhatsApp API link string
        encoded_message = custom_message.replace(" ", "%20")
        whatsapp_api_url = f"https://wa.me{clean_number}?text={encoded_message}"
        
        st.success("🎉 Direct WhatsApp Bridge Generated Successfully!")
        st.info("⚠️ SUPPORT REQURED: Click the sponsor verification button below to activate the secure message line.")
        
        # 💵 YOUR HIGH-PAYING ADSTERRA SMARTLINK
        adsterra_money_link = "https://effectivecpmnetwork.com"
        
        # 1. THE AD BUTTON (Your friends must click this first)
        st.markdown(f"""
            <a href="{adsterra_money_link}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#ef4444; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold; cursor:pointer; margin-bottom:15px;">
                    🚀 SPONSOR: Click to Verify and Unlock Direct Chat Link
                </div>
            </a>
        """, unsafe_allow_html=True)

        # 2. THE REAL WHATSAPP ACTION LINK
        st.markdown(f"""
            <a href="{whatsapp_api_url}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25d366; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold; cursor:pointer;">
                    💬 CLICK HERE TO OPEN DIRECT WHATSAPP CHAT
                </div>
            </a>
        """, unsafe_allow_html=True)
