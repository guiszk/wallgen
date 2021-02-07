# wallgen
Tools to generate wallpapers.

## requirements
First, install requirements with `pip install -r requirements.txt`

## inspiropaper
Create inspiring wallpapers with `fortune`.

### Usage
`python inspiropaper.py <width> <height>`

Add new images in the `images` folder, and fonts in the `fonts` folder.

The resulting wallpapers go in the `wallpapers` folder.

![example image](./wallpapers/your_ignorance_cramps_my_moon2.0-bold.jpg)

## wallpaper
Create wallpapers with patterns.

### Usage
`python wallpaper.py [-h] [-q [SEQUENCE]] [-s [SQUARE]] [-g [GRADIENT]] width height`

![example image](./wallpapers/pattern.jpg)

The resulting wallpaper is saved at `wallpapers/pattern.jpg`.
