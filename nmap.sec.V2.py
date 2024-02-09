import subprocess
import sys

# Check if the target IP is provided as a command line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <target_ip>")
    sys.exit(1)

# Get the target IP from the command line argument
target_ip = sys.argv[1]

# Define the ports
#ports = "53,80,88,135,139,389,445,464,593,636,3268,3269,5985,8443,9389,47001,49664,49665,49666,49667,49673,49686,49687,49689,49694,49698,49702,50563,50574"

# Define the nmap flags (commented for demonstration)
flags = "-sCV"

# Build the nmap command
nmap_command = ["nmap", flags]

# Uncomment the flags if needed
#nmap_command.append(flags)

# Add the target IP and ports
# -p- define all TCP ports to be inspected
# So you can specify -p- to
# scan ports from 1 through 65535. Scanning port zero is allowed if you specify it explicitly. For IP protocol scanning (-sO), this option specifies
# the protocol numbers you wish to scan for (0–255).
nmap_command.extend(["-p-", target_ip])

try:
    # Execute the nmap command
    result = subprocess.run(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Print the nmap output
    print(result.stdout)
    
    # Check for errors
    if result.returncode != 0:
        print(f"nmap command failed with error: {result.stderr}")
except Exception as e:
    print(f"Error executing nmap command: {str(e)}")
