import subprocess
import re

def get_connected_devices():
    try:
        output = subprocess.check_output(['iw', 'dev'], text=True)
        iface = re.search(r'Interface\s+(\w+)', output).group(1)
        dev_dump = subprocess.check_output(['iw', 'dev', iface, 'station', 'dump'], text=True)
    except Exception:
        return []

    devices = []
    macs = re.findall(r'Station\s+([0-9A-Fa-f:]{17})', dev_dump)
    for mac in macs:
        ip_output = subprocess.getoutput(f"arp -n | grep {mac}")
        ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', ip_output)
        ip = ip_match.group(1) if ip_match else 'Unknown'
        devices.append({'ip': ip, 'mac': mac})
    return devices

