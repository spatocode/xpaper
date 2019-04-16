import sys
import ctypes

SPI_SETDESKWALLPAPER = 0x0014
SPI_GETDESKWALLPAPER = 0x0073

def setfromfile(imagepath):
    if sys.version_info[0] is 2:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imagepath, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagepath, 3)
