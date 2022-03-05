#! /usr/bin/env python3

# Framing server program

import socket, sys, re
sys.path.append("../lib")       # for params
import params


# Sends a message through the given socket
def send_message(s, message):
    # Pack the first 4 bytes as length of message
    message = struct.pack(">i", len(message)) + message
    s.sendall(message)
    

def receive_message(s):
    # Obtain message len
    data_len = s.recv(4)

    # No data len obtained
    if not data_len:   
        return None

    # Create
    data_len = struct.unpack

    
switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )


progname = "framingserver"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets

conn, addr = s.accept()  # wait until incoming connection request (and accept it)
print('Connected by', addr)

while True:
    
