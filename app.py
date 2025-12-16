import snap7
from snap7.util import get_int

# PLC details (CHANGE IP LATER)
PLC_IP = "192.168.0.1"
RACK = 0
SLOT = 1   # S7-1200 / S7-1500

client = snap7.client.Client()

try:
    print("Connecting to PLC...")
    client.connect(PLC_IP, RACK, SLOT)
    print("Connected ✅")

    data = client.db_read(1, 0, 2)  # DB1, Byte 0, 2 bytes
    value = get_int(data, 0)

    print("PLC Value:", value)

except Exception as e:
    print("Error:", e)

finally:
    client.disconnect()
