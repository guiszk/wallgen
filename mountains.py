from PIL import Image, ImageDraw, ImageFont, ImageFilter
from colour import Color
import random
import sys

if(len(sys.argv) < 3):
    print(f"{sys.argv[0]} <width> <height> [<*color name/hex>]")
    sys.exit(1)

w, h = int(sys.argv[1]), int(sys.argv[2])
im = Image.new("RGB", (w, h))
draw = ImageDraw.Draw(im)
full = [(0, 0), (w, h)]
draw.rectangle(full, fill='#ffffff')

numlines = random.randint(3, 12)
numiter = random.randint(7, 20)
maxdiv = random.randint(300,900)
width = 10

grad = [(1/numlines)*i for i in range(1, numlines)]

if(len(sys.argv) > 3):
    fill = Color(sys.argv[3])
else:
    fill = Color(pick_for=random.randrange(256))

for i in range(1, numlines):
    nh = h/numlines*(i)
    pasth = nh
    fill.luminance = grad[-i]
    for j in range(numiter):
        nw = w/numiter*(j)
        linepath = [(), (), (), ()]
        linepath = [(w, h), (w, 1000), (1000, 1000), (1000, h)]
        currh = nh + (random.randint(-maxdiv, maxdiv)/10)

        linepath[0] = (nw, h) #V
        linepath[1] = (nw, pasth)
        linepath[2] = ((w/numiter*(j+1)), currh)
        linepath[3] = ((w/numiter*(j+1)), h)

        pasth = currh
        draw.polygon(linepath, fill=fill.hex)

im.save("wallpapers/mountains.jpg")
print("Image saved to wallpapers/mountains.jpg")
