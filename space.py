from PIL import Image, ImageDraw
import random
import sys

if(len(sys.argv) < 3):
    print(f"{sys.argv[0]} <width> <height>")
    sys.exit(1)

w, h = int(sys.argv[1]), int(sys.argv[2])

im = Image.new("RGB", (w, h), color=0)
draw = ImageDraw.Draw(im)

def stars():
    total = random.randint(500, 8000)
    print('Total stars:', total)
    rad = random.randint(1, 4)
    for i in range(total): #num of stars
        r = random.randint(1, rad)
        x = random.randint(r, im.width-r)
        y = random.randint(r, im.height-r)
        points = (x-r, y-r, x+r, y+r)
        minc = 180
        maxc = 255
        fill = (random.randint(minc, maxc), random.randint(minc, maxc), random.randint(minc, maxc), random.randint(minc, maxc))
        draw.ellipse(points, fill=fill)

def planets():
    total = random.randint(4, 10)
    maxw = int(im.width/total)

    #sun
    x = -maxw
    r = random.randint(100, maxw*5)
    y = int(im.height/2)
    points = (x-r, y-r, x+r, y+r)
    draw.ellipse(points, fill=(0, 0, 0), outline=(255, 255, 255), width=4)


    x += r + 100
    r = random.randint(10, maxw-100)
    for i in range(total):
        #x = random.randint(r, im.width-r)
        x += r+maxw
        r = random.randint(20, maxw-100)
        y = int(im.height/2)
        points = (x-r, y-r, x+r, y+r)
        draw.ellipse(points, fill=(0, 0, 0), outline=(255, 255, 255), width=4)
stars()
planets()
im.save('wallpapers/space.jpg')
print("Image saved to wallpapers/space.jpg")
