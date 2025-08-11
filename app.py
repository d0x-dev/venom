# app.py
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Honor PORT env var if provided by the platform
    port = int(os.environ.get("PORT", 5000))
    # Bind to 0.0.0.0 so the host/proxy can reach it
    app.run(host="0.0.0.0", port=port)
