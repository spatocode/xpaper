import sys
import ctypes

SPI_SETDESKWALLPAPER = 0x0014
SPI_GETDESKWALLPAPER = 0x0073

def setwallpaper(imagepath):
    if sys.version_info[0] is 2:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imagepath, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagepath, 3)


def getwallpaper():
    unicode_buffer = ctypes.create_unicode_buffer(512)
    string_buffer = ctypes.create_string_buffer(512)
    if sys.version_info[0] is 2:
        try:
            ctypes.windll.user32.SystemParametersInfoA(SPI_GETDESKWALLPAPER,len(string_buffer),string_buffer,0)
            return string_buffer.value
        except:
            ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, len(unicode_buffer), unicode_buffer, 0)
            return unicode_buffer.value
    else:
        try:
            ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, len(unicode_buffer), unicode_buffer, 0)
            return unicode_buffer.value
        except:
            ctypes.windll.user32.SystemParametersInfoA(SPI_GETDESKWALLPAPER,len(string_buffer),string_buffer,0)
            return string_buffer.value
