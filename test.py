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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
