#!/bin/python
import sys
import socket
from datetime import  datetime

#define our target
if len(sys.argv) ==2:
    target =socket.gethostbyname(sys.argv[1]) #translate hostname to IPV4
else:
    print("invalid argument")
    print("Syntax: python3 scanner.py <ip>")
    
print("_" *50)
print(" scanning target"+target)
print("Time started:"+str(datetime.now))
print("_"*50)
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port)) #error are indicated 
        if result==0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("could not connect to the server")
    sys.exit()