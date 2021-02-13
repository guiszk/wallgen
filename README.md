# wallgen
Tools to generate wallpapers.

## requirements
First, install requirements with `pip install -r requirements.txt`

`fortune` should also be installed to work with `inspiropaper.py`.

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
`python wallpaper.py [-h] [-q [SEQUENCE]] [-s [SQUARE]] [-c [COLOR]] width height`

Example with random colors

![example image](./wallpapers/pattern_colored.jpg)

Example with `--color` option

![example image](./wallpapers/pattern_black.jpg)

The resulting wallpaper is saved at `wallpapers/pattern.jpg`.

## joydivision
Create wallpapers with lines, somewhat inspired by Joy Division's "Unknown Pleasures"

### Usage
`python joydivision.py <width> <height>`

Additional settings can be tweaked inside the script.

![example image](./wallpapers/unknownpleasures.jpg)

The resulting wallpaper is saved at `wallpapers/unknownpleasures.jpg`.

## mountains
Create wallpapers with gradient mountains, inspired by Campo Santo's "Firewatch"

### Usage
`python mountains.py <width> <height> [<*color name/hex>]`

Additional settings can also be tweaked inside the script.

![example image](./wallpapers/mountains_black.jpg)

The wallpaper is saved at `wallpapers/mountains_black.jpg`.

