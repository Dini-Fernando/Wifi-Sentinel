import sqlite3
from datetime import datetime

DB_NAME = 'wifi_sentinel.db'

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    return conn

def setup_db():
    conn = connect_db()
    cursor = conn.cursor()
    # Table for trusted devices
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trusted_devices (
            mac TEXT PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    # Table for intrusion logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS intrusion_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mac TEXT NOT NULL,
            ip TEXT,
            detected_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_trusted_device(mac, name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO trusted_devices (mac, name) VALUES (?, ?)', (mac.lower(), name))
    conn.commit()
    conn.close()

def remove_trusted_device(mac):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM trusted_devices WHERE mac = ?', (mac.lower(),))
    conn.commit()
    conn.close()

def get_all_trusted_devices():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT mac, name FROM trusted_devices')
    devices = cursor.fetchall()
    conn.close()
    return {mac: name for mac, name in devices}

def log_intrusion(mac, ip):
    conn = connect_db()
    cursor = conn.cursor()
    detected_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO intrusion_logs (mac, ip, detected_at) VALUES (?, ?, ?)', (mac.lower(), ip, detected_at))
    conn.commit()
    conn.close()

def get_intrusion_logs(limit=50):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT mac, ip, detected_at FROM intrusion_logs ORDER BY detected_at DESC LIMIT ?', (limit,))
    logs = cursor.fetchall()
    conn.close()
    return logs

# Initialize database and tables on import
setup_db()
