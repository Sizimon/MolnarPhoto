# IMPORTS
import os
from flask import Flask, render_template

# FLASK TEMPLATE SETUP

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/photography")
def photography():
    return render_template("photography.html")


@app.route("/videography")
def videography():
    return render_template("videography.html")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
