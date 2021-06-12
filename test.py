# from time import time, sleep
# while True:
#     sleep(60 - time() % 60)
import os
import http.server
import socketserver



from time import sleep 
for i in range(10):
    msg = "Hello World!"
    sleep(2) 
    print(msg)

