from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/rooms")
def rooms():
    return render_template("rooms.html")

@app.route("/amenities")
def amenities():
    return render_template("amenities.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/contact")
def contactus():
    return render_template("contactus.html")

if __name__ == "__main__":
    app.run(debug=True)