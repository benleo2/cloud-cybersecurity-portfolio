from flask import Flask
from flask_talisman import Talisman
import logging
import os

app = Flask(__name__)

Talisman(app, force_https=False)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Homepage accessed")

    secret = os.getenv("APP_MODE")

    return f"Secure Cloud App Running - Mode: {secret}"

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
