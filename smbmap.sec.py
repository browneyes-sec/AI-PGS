import subprocess

def enumerate_smb_null_session(host):
    try:
        # Construct the smbmap command
        smbmap_command = ["smbmap", "-H", host, "-u", "\"\""]

        # Run the smbmap command and capture its output
        result = subprocess.run(smbmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Print the smbmap output
        print(result.stdout)

        # Check for errors
        if result.returncode != 0:
            print(f"smbmap command failed with error: {result.stderr}")
    except Exception as e:
        print(f"Error running smbmap command: {str(e)}")

if __name__ == "__main__":
    target_host = "10.10.11.222"
    enumerate_smb_null_session(target_host)
