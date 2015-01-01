from __future__ import print_function

import sys
import socket

class Matrix(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def send(self, stuff):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            sys.stderr.write("[ERROR] %s\n" % msg[1])
            sys.exit(1)

        try:
            sock.connect((self.ip, self.port))
        except socket.error, msg:
            sys.stderr.write("[ERROR] %s\n" % msg[1])
            sys.exit(2)

        # Send the data
        sock.send(stuff)

        # Wait for reply
        data = sock.recv(16)
        string = ""
        while len(data):
            string = string + data
            data = sock.recv(16)

        assert string.strip() == "OK"

        sock.close()

    def off(self):
        self.setBrightness(0)

    def setBrightness(self, brightness):
        data = bytearray()
        data.append(brightness)
        self.send(data)

    def rgb(self, r, g, b):
        data = bytearray()
        data.append(r)
        data.append(g)
        data.append(b)
        self.send(data)