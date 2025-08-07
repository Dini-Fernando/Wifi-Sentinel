# 📡 Wi-Fi Sentinel

Wi-Fi Sentinel is a lightweight Wi-Fi Intrusion Detection System (WIDS) designed for home users and small businesses.  
It detects and displays all connected devices to your custom Wi-Fi hotspot and immediately alerts you when unknown devices connect.  
You can also block/unblock devices in real-time through a web dashboard.

---

## 🚀 Features

- ✅ Turns your Linux machine into a Wi-Fi Access Point (AP)  
- ✅ Real-time device monitoring with automatic scanning  
- ✅ Visual dashboard (Flask UI)  
- ✅ SMS/email alert integration (Twilio or Notification API)  
- ✅ Block and unblock devices instantly from the dashboard  
- ✅ Trusted/blocked device tracking  
- ✅ Logging and audit trails  

---

## 📂 Project Structure

wifi_sentinel/
├── app.py # Main Flask server
├── scanner.py # Scans and lists connected devices
├── alert_notification.py # Sends alerts via email/SMS
├── utils.py # Utility functions
├── db.py # SQLite DB handler
├── config.py # Configurations (e.g., Notification API)
├── setup_ap.py # Script to turn your adapter into AP
├── templates/
│ └── index.html # Dashboard UI
├── static/ # Static assets (optional)
├── trusted_devices.json # Stores allowed MACs
├── blocked_devices.json # Stores blocked MACs
├── wifi_sentinel.db # SQLite DB (auto-created)
├── wifi_sentinel.log # Logging
├── README.md # You are here
└── requirements.txt # Python dependencies


---

## 🛠 Requirements

1. Ubuntu 20.04 or 22.04 LTS (tested)  
2. External USB Wi-Fi adapter that supports AP mode (e.g., RTL8192EU) or Router_With_API_Interface  
3. Python 3.8+  
4. `hostapd`, `dnsmasq`, `iptables` (Linux tools)  

---

## ⚙️ Setup Guide

### 1️⃣ Step 1 – Clone the Repo

```bash
git clone https://github.com/Dini-Fernando/wifi_sentinel.git
cd wifi_sentinel

2️⃣ Step 2 – Install Python Dependencies
```bash
pip3 install -r requirements.txt

Or manually:
```bash
pip3 install flask netifaces requests

3️⃣ Step 3 – Configure the Wi-Fi Access Point
Run the setup script:
```bash
sudo python3 setup_ap.py
This will:

* Set your Wi-Fi adapter to AP mode
* Create a hotspot (e.g., WiFiSentinelNet)
* Assign IP address and DHCP
* Enable internet sharing via Ethernet

⚠️ Important:
Modify wifi_iface, ethernet_iface, SSID, and password in setup_ap.py to match your system.

📡 Start the Sentinel
```bash
sudo python3 app.py

Open your browser and visit:
http://localhost:5000

You’ll see the dashboard showing:

Connected devices
Trusted devices
Blocked devices

**Dashboard_Functions**

✅ Trust Device – Adds MAC to trusted list
🚫 Block Device – Blocks using iptables
🔓 Unblock Device – Removes block rule
🔄 Refresh – Pulls latest connected list
📩 Alerts – Triggered when unknown device connects

🔔 Alert System Options
Option A: Notification API
Edit config.py

NOTIFICATION_API_KEY = "your_api_key"
EMAIL = "you@example.com"
PHONE = "+9471XXXXXXX"

🚫 Blocked Devices
Stored in blocked_devices.json

Dropped via iptables

Displayed on dashboard under "Blocked Devices"

🔄 Running on Startup (Optional)
To auto-start the AP and Flask app on boot:

Add to crontab or startup script:

sudo python3 setup_ap.py

Then launch Flask app:

sudo python3 app.py


