/*
Include **crypto-js** in your HTML:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/crypto-js@3.3.0-1/crypto-js.js"></script>
   
   Create a form to capture the password, hash it using SHA-1, and check it using the Pwned Passwords API
*/


document.getElementById('password-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const password = document.getElementById('password').value;
    const hashedPassword = CryptoJS.SHA1(password).toString(CryptoJS.enc.Hex).toUpperCase();
    checkPasswordPwned(hashedPassword);
});

function checkPasswordPwned(hash) {
    const first5Chars = hash.slice(0, 5);
    fetch(`https://api.pwnedpasswords.com/range/${first5Chars}`)
        .then(response => response.text())
        .then(data => checkIfPasswordIsCompromised(data, hash))
        .catch(error => console.error("Error checking password:", error));
}

function checkIfPasswordIsCompromised(data, fullHash) {
    const lines = data.split('\n');
    let found = false;

    lines.forEach(line => {
        const [suffix, count] = line.split(':');
        if (fullHash.slice(5) === suffix) {
            found = true;
            document.getElementById('password-feedback').innerText = `This password has been exposed ${count} times in breaches!`;
        }
    });

    if (!found) {
        document.getElementById('password-feedback').innerText = "This password is safe to use.";
    }
}
