Steps to copy from '/dev' to '/beta' in SSM using credentials from saml2aws and aws-ssm-copy.

This is a sample dry run command = "aws-ssm-copy -r --dry-run --target-path /destination /source"

Steps.

1. Login with saml2aws 
$ saml2aws login -a terragon --mfa Auto

2. Obtain .env credentials using /
$ saml2aws script

3. Modify the command you intend to run with aws credentials in Line 8 of command.py.

4. Activate/Create a .venv
$ python3 -m venv .venv
$ source .venv/bin/activate

5. Install the required packages in the requirements.txt
$(.venv) pip install -r requirements.txt

6. Execute the intended command using
$(.venv) run python3 command.py


