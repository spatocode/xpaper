# Xpaper

Cross-platform library for changing desktop wallpaper

Works on windows and Linux

Supports all versions of Python


## Install

```
$ pip install xpaper
```


## Usage

```py
from xpaper import wallpaper

wallpaper.change("C:/Users/Spatocode/wallpaper.jpg")    # absolute path to the image

wallpaper.get()     # "/Users/Spatocode/wallpaper.jpg"
```

## API

### .change(imagepath)
Changes the desktop wallpaper

#### imagepath
Type: string

The path to image to be used as desktop wallpaper

### .get()
Returns the path of the current desktop wallpaper.


# LICENSE

MIT License

Copyright (c) 2019 Ekene Izukanne