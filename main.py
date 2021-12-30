from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("indexx.html")

@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template("success.html")

@app.route("/Chuppa")
def chuppa():
    return render_template("Salon.html")

@app.route("/FejkBuk")
def fejkbuk():
    return render_template("Fejkbuk.html")


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
