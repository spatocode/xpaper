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
