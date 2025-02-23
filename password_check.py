import hashlib
import requests

def check_password_leak(password):
    # Step 1: Hash the password using SHA-1
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Step 2: Send the first 5 characters of the hash to the API
    prefix = sha1_hash[:5]
    url = f'https://api.pwnedpasswords.com/range/{prefix}'

    # Step 3: Get the response from the API
    response = requests.get(url)

    # Step 4: Check if the hash is in the response
    if response.status_code == 200:
        # Step 5: Search for the full hash in the response
        hashes = (line.split(':') for line in response.text.splitlines())
        for hash_suffix, count in hashes:
            if hash_suffix == sha1_hash[5:]:
                return True  # Password is leaked
    return False  # Password is not leaked

# Example usage:


password = input("Password: ")
if check_password_leak(password):
    print("This password has been leaked!")
else:
    print("This password is safe.")
