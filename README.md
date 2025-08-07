📡 Wi-Fi Sentinel
Wi-Fi Sentinel is a lightweight Wi-Fi Intrusion Detection System (WIDS) designed for home users and small businesses. 
It detects and displays all connected devices to your custom Wi-Fi hotspot and immediately alerts you when unknown devices connect. 
You can also block/unblock devices in real-time through a web dashboard.

🚀 Features
✅ Turns your Linux machine into a Wi-Fi Access Point (AP)
✅ Real-time device monitoring with automatic scanning
✅ Visual dashboard (Flask UI)
✅ SMS/email alert integration (Twilio or Notification API)
✅ Block and unblock devices instantly from the dashboard
✅ Trusted/blocked device tracking
✅ Logging and audit trails

📂 Project Structure
wifi_sentinel/
├── app.py                # Main Flask server
├── scanner.py            # Scans and lists connected devices
├── alert_notification.py # Sends alerts via email/SMS
├── utils.py              # Utility functions
├── db.py                 # SQLite DB handler
├── config.py             # Configurations (e.g., Notification API)
├── setup_ap.py           # Script to turn your adapter into AP
├── templates/
│   └── index.html        # Dashboard UI
├── static/               # Static assets (optional)
├── trusted_devices.json  # Stores allowed MACs
├── blocked_devices.json  # Stores blocked MACs
├── wifi_sentinel.db      # SQLite DB (auto-created)
├── wifi_sentinel.log     # Logging
├── README.md             # You are here
└── requirements.txt      # Python dependencies

**🛠 Requirements**
1. Ubuntu 20.04 or 22.04 LTS (tested)
2. External USB Wi-Fi adapter that supports AP mode (e.g., RTL8192EU) or Router_With_API_Interface
3. Python 3.8+
4. hostapd, dnsmasq, iptables (Linux_Tools)

**⚙️ Setup Guide**
1️⃣ Step 1 – Clone the repo
git clone https://github.com/Dini-Fernando/wifi_sentinel.git
cd wifi_sentinel

2️⃣ Step 2 – Install Python dependencies
pip3 install -r requirements.txt
Or manually:
pip3 install flask netifaces requests

3️⃣ Step 3 – Configure the Wi-Fi Access Point
Run the setup script to create your custom Wi-Fi network:
sudo python3 setup_ap.py

This:
Sets your Wi-Fi adapter to AP mode
Creates a network (e.g., WiFiSentinelNet)
Assigns IP address & DHCP
Enables internet sharing via Ethernet

**Make sure to:**
Change wifi_iface, ethernet_iface, SSID, and password inside setup_ap.py to match your system

📡 Start the Sentinel

sudo python3 app.py
=> Open your browser and visit: http://localhost:5000
==> You’ll see the dashboard showing connected, trusted, and blocked devices

💻 Dashboard Functions
✅ Trust device – Adds device to trusted list
🚫 Block device – Blocks device using iptables
🔓 Unblock device – Removes iptables block
🔄 Refresh – Pulls latest device list from hotspot
📩 Alert System - Alerts are sent when an unknown device connects. 

You can configure:
Option A: Email/SMS via Notification API

Update your keys in config.py:

NOTIFICATION_API_KEY = "your_api_key"
EMAIL = "you@example.com"
PHONE = "+9471XXXXXXX"
Option B: Twilio (optional)
If using Twilio, configure alert_notification.py accordingly.

🚫 Blocked Devices
Blocked devices are:

- Stored in blocked_devices.json
- Automatically dropped using iptables
- Displayed in the dashboard under "Blocked Devices"

**🔄 Running on Startup (Optional)**
If you want the AP to auto-configure after each adapter connection:

Add this to crontab or startup script:

sudo python3 setup_ap.py

Then launch Flask app:
sudo python3 app.py

**🧪 Testing**
> Connect your phone to WiFiSentinelNet
> Observe device appear on dashboard
> Click "Block" and test connectivity
> Click "Unblock" to restore access

**🧰 Troubleshooting**
=> Problem	Solution <== Only If There any Following Error appears

Port 5000 already in use?
sudo lsof -i :5000 → kill <PID>

Flask dashboard not updating?
Refresh page or restart app.py

Device not blocking?
Ensure iptables rules are applied

Adapter not detected?
Use supported USB Wi-Fi adapters

No internet on client devices?	
Check eth0 internet, iptables, NAT

📦 Packaging
To zip and move this for demo:
zip -r wifi_sentinel_project.zip wifi_sentinel/

👨‍💻 Authors
👤 Dinithi Fernando
🔐 Final year Cybersecurity project – Wrexham University



📄 License
This project is for academic/demonstration use. No liability for misuse.
