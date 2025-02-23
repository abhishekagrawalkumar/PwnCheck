#Install required libraries: - pip install flask requests



from flask import Flask, render_template, request, jsonify
import hashlib
import requests

app = Flask(__name__)

def check_password_pwned(password):
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = hashed_password[:5]
    suffix = hashed_password[5:]
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
    if response.status_code == 200:
        if any(line.split(':')[0] == suffix for line in response.text.splitlines()):
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form['password']
    if check_password_pwned(password):
        return jsonify({'status': 'compromised'})
    else:
        return jsonify({'status': 'safe'})

if __name__ == '__main__':
    app.run(debug=True)
