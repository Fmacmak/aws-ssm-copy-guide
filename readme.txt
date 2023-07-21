Steps to copy from '/dev' to '/beta' in SSM using credentials from saml2aws and aws-ssm-copy. For more info see https://github.com/binxio/aws-ssm-copy
NOTE: >python == v.3.6 is needed to use aws-ssm-copy
This is a sample dry run command = "aws-ssm-copy -r --dry-run --target-path /destination /source"

Steps.

1. Login with saml2aws. replace profile with your saml2aws profile.
$ saml2aws login -a <profile> --mfa Auto

2. Create a .env file and populate with credentials using
$ saml2aws script

3. Modify the command you intend to run with aws credentials on Line 8 of command.py.

4. Create a virtual environment .venv
$ python3 -m venv .venv
$ source .venv/bin/activate

5. Or activate the virtual env using 
$ source .venv/bin/activate

6. Install the required packages in the requirements.txt
$(.venv) pip install -r requirements.txt

7. Execute the intended command using
$(.venv) python3 command.py


