from flask import Flask, render_template, request
from sms_logic import send_fake_sms

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        number = request.form.get("number")
        count = int(request.form.get("count", 1))
        message = send_fake_sms(number, count)
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
  
