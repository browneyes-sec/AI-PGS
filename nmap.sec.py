import subprocess

# Define the target IP address and ports
target_ip = "10.10.11.222"
ports = "53,80,88,135,139,389,445,464,593,636,3268,3269,5985,8443,9389,47001,49664,49665,49666,49667,49673,49686,49687,49689,49694,49698,49702,50563,50574"

# Define the nmap flags (commented for demonstration)
flags = "-sCV"

# Build the nmap command
nmap_command = ["nmap", flags]

# Uncomment the flags if needed
# nmap_command.append(flags)

# Add the target IP and ports
nmap_command.extend(["-p", ports, target_ip])

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
