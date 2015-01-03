from __future__ import print_function, division

import sys
import time
import argparse

import frames
import matrix

parser = argparse.ArgumentParser()
parser.add_argument('img', type=argparse.FileType('r'), 
                    help="Name of an image file (GIF, JPG, PNG etc.)")
parser.add_argument('-b', '--brightness', type=int, default=20,
                    help="Set brightness of display (0-255)")
parser.add_argument('-d', '--delay', type=int, default=200,
                    help='Delay between frames (ms)')
parser.add_argument('-i', '--ipaddr', default='192.168.0.99',
                    help="IP address of matrix display")
parser.add_argument('-p', '--port', type=int, default=1234,
                    help="TCP/IP Port number")
args = parser.parse_args()

# Load file name
images = frames.Frames(args.img)

m = matrix.Matrix(args.ipaddr, args.port)

# Set brightness
b = args.brightness
if b < 0 or b > 255:
    b = 20
m.setBrightness(b)

# Delay
delay = args.delay/1000

try:
    if images.length > 1:
        while True:
            for img in images.images:
                m.send(img.tobytes())
                time.sleep(delay)
    else:
        m.send(images.images[0].tobytes())
        while True:
            x = raw_input("")

except:
    m.off()

sys.exit(0)
