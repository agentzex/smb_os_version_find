# from smb.SMBConnection import SMBConnection
from smb_build_getter.python3.smb.SMBConnection import SMBConnection


device_name = ""
conn = SMBConnection("", "", "", device_name, use_ntlm_v2 = False)
try:
    conn.connect("192.168.1.30", 139)
except Exception as e:
    if str(e) != "Found build":
        raise e
with open("signature", "rb") as f:
    buf = f.read()

start_index = buf.find(b"NTLMSSP")
start_index = start_index + 48
os_info = buf[start_index: start_index+8]
os_major_info = os_info[0]
os_minor_info = os_info[1]
os_build = int.from_bytes(os_info[2:4], byteorder="little", signed=False)
if os_major_info == 5:
    os_version = "Windows XP"
elif os_major_info == 6 and os_minor_info == 0:
    os_version = "Windows Vista"
elif os_major_info == 6 and os_minor_info == 1:
    os_version = "Windows 7"
elif os_major_info == 6 and os_minor_info == 2:
    os_version = "Windows 8"
elif os_major_info == 6 and os_minor_info == 3:
    os_version = "Windows 8.1"
elif os_major_info == 10:
    os_version = "Windows 10"
else:
    os_version = "Unknown (not Windows)"

print("OS: " + os_version)
print("Version: " + str(os_major_info) + "." + str(os_minor_info))
print("Build: " + str(os_build))
