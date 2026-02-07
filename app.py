import os
from flask import Flask

app = Flask(__name__)

ENV = os.getenv("APP_ENV", "prod")

@app.route("/")
def home():
    return f"🚀 Running in {ENV.upper()} mode"
@app.route("/crash")
def crash():
    return 1 / 0

if __name__ == "__main__":
    debug = True if ENV == "dev" else False
    app.run(host="0.0.0.0", port=5000, debug=debug)
