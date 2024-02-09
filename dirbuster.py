import argparse
import subprocess

def run_dirb(target_url, wordlist_path):
    command = f"dirb {target_url} {wordlist_path}"
    subprocess.run(command, shell=True)

def main():
    # Create the command-line argument parser
    parser = argparse.ArgumentParser(description="Python script to run Dirb with specified parameters.")
    
    # Add arguments
    parser.add_argument("target_url", help="Target URL or IP address")
    parser.add_argument("wordlist_path", help="Path to the wordlist file")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Run Dirb with the provided parameters
    run_dirb(args.target_url, args.wordlist_path)

if __name__ == "__main__":
    main()
