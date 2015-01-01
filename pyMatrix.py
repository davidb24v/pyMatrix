from __future__ import print_function

import sys
import time

import frames
import matrix

HOST = '192.168.0.99'
PORT = 1234

images = frames.Frames(sys.argv[1])

m = matrix.Matrix(HOST, PORT)
m.setBrightness(20)
try:
    if images.length > 1:
        while True:
            for img in images.images:
                m.send(img.tobytes())
                time.sleep(0.2)
    else:
        m.send(images.images[0].tobytes())
        while True:
            x = raw_input("")

except:
    m.off()

sys.exit(0)
