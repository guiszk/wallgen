from PIL import Image, ImageDraw, ImageFont
from colour import Color
import random
import argparse
import sys

parser = argparse.ArgumentParser(description="Generate wallpapers.")
parser.add_argument(dest="w", type=int, default=1920, help="Width")
#parser.add_argument("-w", "--width", nargs=1, type=int, default=1920, help="Width")
parser.add_argument(dest="e", type=int, help="Height")
#parser.add_argument("-e", "--height", nargs=1, type=int, default=1080, help="Height")
parser.add_argument('-q', '--sequence', type=int, nargs='?', default=False, help='Number of squares in sequence')
parser.add_argument('-s', '--square', type=int, nargs='?', default=False, help='Number of squares in center')
parser.add_argument('-g', '--gradient', type=str, nargs='?', const='blue', default=False, help='Make gradient (random color if not specified)')
#parser.add_argument(dest="n", type=int, help="Square side size")
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
        if(args.gradient):
            fill = Color(args.gradient)
            fill.luminance -= 0.08
            fill = fill.hex
        else:
            fill = Color(pick_for=random.randrange(256))
        ImageDraw.Draw(img).rectangle(msquare, fill=fill.hex)
def cont(x):
    if(args.gradient):
        fill = Color(args.gradient)
        #grad = [i+(0.3/x) for i in range(1, x)]
        grad = [(1/x)*i for i in range(1, x+1)]
        print(grad)
    for i in range(x):
        for j in range(x):
            squarel = w*sperc*2/x
            sstart = (square[0][0]+squarel*j, square[0][1]+squarel*i)
            send = (square[0][0]+squarel*(j+1), square[0][1]+squarel*(i+1))
            msquare = [sstart, send]
            if(args.gradient):
                fill.luminance = grad[-j]
                #fill = fill.hex
            else:
                fill = Color(pick_for=random.randrange(256))
            ImageDraw.Draw(img).rectangle(msquare, fill=fill.hex)
if(args.sequence):
    sequence(args.sequence)
elif(args.square):
    cont(args.square)
img.save("wallpapers/pattern.jpg")
print("Image saved to wallpapers/pattern.jpg")
