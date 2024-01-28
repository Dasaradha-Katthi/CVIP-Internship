from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_time")
def get_time():
    current_time = time.strftime("%H:%M:%S")
    return {"time": current_time}

if __name__ == "__main__":
    app.run(debug=True)
