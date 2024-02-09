import subprocess

def start_openvpn_session():
    try:
        # Use sudo to run OpenVPN without a password prompt
        subprocess.run(["sudo", "/usr/sbin/openvpn", "/home/kali/Downloads/lab_bedotsec.ovpn"])
        print("OpenVPN session started successfully.")
    except Exception as e:
        print(f"Error starting OpenVPN session: {str(e)}")

if __name__ == "__main__":
    start_openvpn_session()
