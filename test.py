from math import sqrt
from time import sleep
from flask import Flask, render_template
import os
import http.server
import socketserver

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

PORT = int(os.getenv('VCAP_APP_PORT', '8000'))

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
