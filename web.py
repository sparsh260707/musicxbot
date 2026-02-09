from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Music Bot Running"

@app.route("/health")
def health():
    return "OK"

def run_bot():
    os.system("bash start")

if __name__ == "__main__":
    Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
