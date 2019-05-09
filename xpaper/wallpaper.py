#!/usr/bin/env python
# Copyright (c) 2019, Ekene Izukanne
# Xpaper is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.


import sys
from xpaper import windows
from xpaper import linux


def change(imagepath):
    if sys.platform in ["win32", "cygwin"]:
        windows.setwallpaper(imagepath)
    else:
        linux.setwallpaper(imagepath)


def get():
    if sys.platform in ["win32", "cygwin"]:
        return windows.getwallpaper()
    else:
        return linux.getwallpaper()
