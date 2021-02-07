from PIL import Image, ImageDraw, ImageFont
from colour import Color
import random
import argparse
import sys

parser = argparse.ArgumentParser(description="Generate wallpapers.")
parser.add_argument(dest="w", type=int, default=1920, help="Width")
parser.add_argument(dest="e", type=int, help="Height")
parser.add_argument('-q', '--sequence', type=int, nargs='?', default=False, help='Number of squares in sequence')
parser.add_argument('-s', '--square', type=int, nargs='?', default=False, help='Number of squares in center')
parser.add_argument('-c', '--color', type=str, nargs='?', default=False, help='Use different shades of same color')
args = parser.parse_args()

def getcol():
    return "#" + "".join(random.sample("ABCDEF123456", 6))

w, h = args.w, args.e
img = Image.new("RGB", (w, h))
shape = [(0, 0), (w, h)]
ImageDraw.Draw(img).rectangle(shape, fill="#FFFFFF")
sperc = 0.2
square = [(w/2-(w*sperc), h/2-(w*sperc)), (w/2+(w*sperc), h/2+(w*sperc))]

def sequence(x):
    for i in range(x+1):
        squarel = w*sperc/x
        sstart = (square[0][0]+squarel*i, square[0][1]+squarel*i)
        send = (sstart[0]+squarel*i, sstart[1]+squarel*i)
        msquare = [sstart, send]
        if(args.color):
            fill = Color(args.color)
            fill.luminance = random.randint(1, 9)/10
        else:
            fill = Color(pick_for=random.randrange(256))
        ImageDraw.Draw(img).rectangle(msquare, fill=fill.hex)
def cont(x):
    if(args.color):
        fill = Color(args.color)
    for i in range(x):
        for j in range(x):
            squarel = w*sperc*2/x
            sstart = (square[0][0]+squarel*j, square[0][1]+squarel*i)
            send = (square[0][0]+squarel*(j+1), square[0][1]+squarel*(i+1))
            msquare = [sstart, send]
            if(args.color):
                fill.luminance = random.randint(1, 9)/10
            else:
                fill = Color(pick_for=random.randrange(256))
            ImageDraw.Draw(img).rectangle(msquare, fill=fill.hex)
if(args.sequence):
    sequence(args.sequence)
elif(args.square):
    cont(args.square)
img.save("wallpapers/pattern.jpg")
print("Image saved to wallpapers/pattern.jpg")
