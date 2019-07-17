#!/usr/bin/env python
# Copyright (c) 2019, Ekene Izukanne
# Xpaper is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.


import sys
from xpaper import windows
from xpaper import linux


def change(imagepath):
    """
    Changes the desktop wallpaper
    ``imagepath``: an absolute path to the image
    """
    if sys.platform in ["win32", "cygwin"]:
        windows.setwallpaper(imagepath)
    else:
        linux.setwallpaper(imagepath)


def get():
    """
    Returns the path to the current desktop wallpaper
    """
    if sys.platform in ["win32", "cygwin"]:
        return windows.getwallpaper()
    else:
        return linux.getwallpaper()
