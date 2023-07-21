import subprocess

from dotenv import load_dotenv

load_dotenv()

# Define the command you want to execute (Default below is a dry-run from /dev to /beta)
command = 'aws-ssm-copy -r --dry-run --target-path /beta /dev'

# Execute the command
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Check the result
if result.returncode == 0:
    # Command executed successfully
    print("Command output:")
    print(result.stdout)
else:
    # An error occurred
    print("Command failed with error:")
    print(result.stderr)
