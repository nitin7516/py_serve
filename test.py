from math import sqrt
from time import sleep
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream():
    def generate():
        for i in range(500):
            yield "{}\n".format(sqrt(i))
            sleep(1)

    return app.response_class(generate(), mimetype="text/plain")
