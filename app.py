from flask import Flask, render_template, redirect, url_for
import subprocess
from scanner import get_connected_devices

app = Flask(__name__)

trusted_devices = set()
blocked_devices = set()

@app.route('/')
def index():
    devices = get_connected_devices()
    return render_template('index.html', devices=devices, trusted=trusted_devices, blocked=blocked_devices)

@app.route('/block/<mac>')
def block(mac):
    subprocess.call(['iptables', '-I', 'FORWARD', '-m', 'mac', '--mac-source', mac, '-j', 'DROP'])
    blocked_devices.add(mac)
    trusted_devices.discard(mac)
    return redirect(url_for('index'))

@app.route('/unblock/<mac>')
def unblock(mac):
    subprocess.call(['iptables', '-D', 'FORWARD', '-m', 'mac', '--mac-source', mac, '-j', 'DROP'])
    blocked_devices.discard(mac)
    return redirect(url_for('index'))

@app.route('/trust/<mac>')
def trust(mac):
    trusted_devices.add(mac)
    blocked_devices.discard(mac)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

