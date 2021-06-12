import os
import http.server
import socketserver

PORT = int(os.getenv('VCAP_APP_PORT', '8000'))

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
from time import sleep 
for i in range(6):
    msg = "Hello World!"
    sleep(2) 
    print(msg)
print("serving at port", PORT)
httpd.serve_forever()
