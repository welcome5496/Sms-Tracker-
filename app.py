# app.py
from flask import Flask, render_template, request
from sms_logic import send_fake_sms
import os

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        number = request.form.get("number")
        try:
            count = int(request.form.get("count", 1))
        except ValueError:
            count = 1
        message = send_fake_sms(number, count)
    return render_template("index.html", message=message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# sms_logic.py
def send_fake_sms(number, count):
    import time
    output = []
    for i in range(count):
        output.append(f"Simulated sending SMS {i+1} to {number}")
        time.sleep(0.2)  # simulate delay
    return "\n".join(output)

# requirements.txt
flask
gunicorn

# Procfile
web: gunicorn app:app

# templates/index.html
<!DOCTYPE html>
<html>
<head>
    <title>SMS Bomber (Educational Only)</title>
</head>
<body>
    <h1>SMS Bomber (Simulated)</h1>
    <form method="post">
        <label>Phone Number:</label>
        <input type="text" name="number" required><br><br>
        <label>Number of Messages:</label>
        <input type="number" name="count" min="1" max="10" value="1"><br><br>
        <button type="submit">Send</button>
    </form>
    {% if message %}
        <h3>Result:</h3>
        <pre>{{ message }}</pre>
    {% endif %}
</body>
</html>
