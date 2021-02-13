from PIL import Image, ImageDraw, ImageFont, ImageFilter
import aggdraw
import random
import sys

if(len(sys.argv) !=3):
    print("{} <width> <height>".format(sys.argv[0]))
    sys.exit(1)

w, h = int(sys.argv[1]), int(sys.argv[2])
im = Image.new("RGB", (w, h))
draw = ImageDraw.Draw(im)
full = [(0, 0), (w, h)]
draw.rectangle(full, fill='#ffffff') #change backgroud color

#set these to constant numbers if desired
numlines = random.randint(5, 50)
numiter = random.randint(5, 50)
maxdiv = random.randint(100, 700)
width = random.randint(5, 10)

for i in range(1, numlines):
    nh = h/numlines*(i)
    pasth = nh
    for j in range(numiter):
        linepath = [(), ()]
        currh = nh + (random.randint(-maxdiv, maxdiv)/10)
        linepath[0] = (w/numiter*j, pasth)
        pasth = nh + (random.randint(-maxdiv, maxdiv)/10)
        linepath[1] = (w/numiter*(j+1), currh)
        pasth = currh
        fill = '#' + "".join(random.choices('123456abcdef', k=6))
        #fill = '#000000' #uncomment to make all lines black, or change to desired color
        draw.line(linepath, fill=fill, width=width)
im.save("wallpapers/unknownpleasures.jpg")
print("Image saved to wallpapers/unknownpleasures.jpg")
