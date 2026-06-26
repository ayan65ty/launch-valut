import time
import urllib.request
from twilio.rest import Client

# 🔑 WHATSAPP CONFIGURATION KEYS
# Paste your secure keys from your free Twilio dashboard here:
TWILIO_ACCOUNT_SID = "YOUR_ACCOUNT_SID_HERE"
TWILIO_AUTH_TOKEN = "YOUR_AUTH_TOKEN_HERE"

# ✅ YOUR PHONE NUMBER PRE-CONFIGURED
YOUR_PERSONAL_PHONE = "+2348101607576" 

# 📋 WEBSITES TO MONITOR
WEBSITES = [
    "https://google.com",
    "https://github.com",
    "https://this-is-a-broken-website-test-link-12345.com"
]

def send_whatsapp_alert(message_body):
    """Sends an instant alert message straight to your personal WhatsApp."""
    if "YOUR_" in TWILIO_ACCOUNT_SID:
        print(f"📢 [Local Warning - Twilio Keys Missing]: {message_body}")
        return

    try:
        # Initialize the Twilio communication client
        client = Client(1111, 8888)
        
        # Trigger the WhatsApp API message route
        message = client.messages.create(
            from_='whatsapp:+14155238886', # The official free Twilio sandbox sender number
            body=message_body,
            to=f'whatsapp:{YOUR_PERSONAL_PHONE}'
        )
        print("📲 WhatsApp alert pushed to your phone successfully!")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp message: {e}")

def check_websites():
    print(f"\n⏱️ [{time.strftime('%H:%M:%S')}] Running website uptime check...")
    
    for url in WEBSITES:
        try:
            # Ping the website with a strict 5-second waiting limit
            response = urllib.request.urlopen(url, timeout=5)
            if response.getcode() == 200:
                print(f"✅ ONLINE: {url}")
        except Exception as e:
            print(f"🚨 OFFLINE: {url}")
            # Format and dispatch the text alert payload
            alert_text = f"🚨 DEV_FLEX ALERT!\nYour website {url} has crashed!\nReason: {str(e)}"
            send_whatsapp_alert(alert_text)

# Continuous monitoring loop
while True:
    check_websites()
    print("💤 Sleeping for 60 seconds before checking again...")
    time.sleep(60)
