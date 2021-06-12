# from time import time, sleep
# while True:
#     sleep(60 - time() % 60)
import os
import http.server
import socketserver

PORT = int(os.getenv('VCAP_APP_PORT', '8000'))

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

from time import sleep 
for i in range(10):
    msg = "Hello World!"
    sleep(2) 
    print(msg)
print("serving at port", PORT)
httpd.serve_forever()
