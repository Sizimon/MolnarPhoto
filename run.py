# IMPORTS
import os
from flask import Flask, render_template

# FLASK TEMPLATE SETUP

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/production")
def production():
    return render_template("production.html")


@app.route("/artsy")
def artsy():
    return render_template("artsy.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
