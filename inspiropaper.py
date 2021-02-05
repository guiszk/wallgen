#!/usr/local/bin/python3.7
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import sys, os

if(len(sys.argv) !=3):
    print("{} <width> <height>".format(sys.argv[0]))
    sys.exit(1)

w, h = int(sys.argv[1]), int(sys.argv[2])
walldir = "images/" #specify directory with images
wall = os.path.join(walldir, random.choice(os.listdir(walldir)))

im = Image.open(wall).convert("RGB")
im = im.resize((w, h), Image.ANTIALIAS) #resize image
im = im.filter(ImageFilter.BoxBlur(50)) #blur image
im = im.point(lambda p: p * 0.75) #darken image
#full = [(0, 0), (w, h)]
draw = ImageDraw.Draw(im)

phrase = os.popen("/usr/local/bin/fortune").read().replace("\t", " ")

fontdir = "fonts/" #specify directory with fonts
font = os.path.join(fontdir, random.choice(os.listdir(fontdir)))

imfont = ImageFont.truetype(font, 40)
tw, th = draw.textsize(phrase, font=imfont)
draw.text(((w-tw)/2, (h-th)/2), phrase, font=imfont, fill=(255, 255, 255))

imgpath = os.path.abspath(str("wallpapers/" + "_".join("".join([i for i in phrase if i.isalpha() or i.isspace()]).split()[:4]).lower() + "_" + os.path.basename(font)[:-4].lower() + ".jpg"))
im.save(imgpath)
os.system("osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"{}\"'".format(imgpath))
