# Password Safety Check

**PwnCheck** is a simple, powerful tool that helps businesses and individuals ensure their passwords have not been exposed in data breaches. By checking if a password has been previously compromised in a breach, this tool helps users make more secure choices, improving overall cybersecurity.

## Features
- **Password Compromise Detection**: Checks whether a password has been exposed in a known data breach.
- **Real-Time Feedback**: Provides immediate alerts if a password is compromised, guiding users to stronger, safer alternatives.
- **Privacy-Focused**: Passwords are never transmitted in plain text. The tool uses secure hashing methods to check passwords against the **Have I Been Pwned** API without exposing sensitive information.
- **Seamless Integration**: Easily integrate this tool into your website or application to enhance user security.

## Why Use Password Safety Check?

### **For Businesses**
1. **Improve Account Security**:
   - Prevent users from using compromised passwords, reducing the risk of account takeovers and cyberattacks.
   
2. **Build User Trust**:
   - Enhance customer confidence by demonstrating that you care about their security, offering proactive password safety checks.

3. **Meet Compliance Standards**:
   - Help your business stay compliant with industry regulations and standards (e.g., GDPR, PCI-DSS) that require strong password management.

4. **Reduce Support Costs**:
   - Minimize support requests related to compromised accounts by preventing weak or exposed passwords from being used.

5. **Protect Against Credential Stuffing Attacks**:
   - Protect your system from automated attacks that target known exposed passwords (credential stuffing).


---

## How It Works

**PwnCheck** uses the **Have I Been Pwned** API to check whether a password has been exposed in a known data breach. The tool hashes the password using **SHA-1** (following privacy standards) and checks the first five characters of the hash against the API's database. If the full hash matches any of the known compromised passwords, the password is flagged.

1. **Hashing**: When a user enters their password, it is hashed using SHA-1.
2. **API Query**: The first 5 characters of the hash are sent to the **Pwned Passwords API**, which returns a list of matching hash suffixes.
3. **Feedback**: If the full hash is found, the user is informed that the password has been compromised. Otherwise, they receive a message confirming that the password is safe.

---

## Installation

To use **PwnCheck**, you can either implement the frontend JavaScript solution, or set up the backend using Python, Node.js, or your preferred backend technology.

