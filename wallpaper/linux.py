import sys
import ctypes
import subprocess
import os

def setwallper(imagepath):
    desktop_session = os.environ.get("DESKTOP_SESSION")
    if desktop_session is not None:
        desktop_session = desktop_session.lower()
        if desktop_session in ["gnome", "unity", "cinnamon", "pantheon"]:
            subprocess.Popen("gsettings", "set", "org.gnome.desktop.background", "picture-uri", "'file://%s'" % imagepath)
        elif desktop_session == "mate":
            try:
                subprocess.Popen("dconf", "write", "/org/mate/desktop/background/picture-filename", imagepath)
            except:
                subprocess.Popen("gsettings", "set", "org.mate.background", "picture-filename", "'%s'" % imagepath)
            finally:
                 subprocess.Popen("mateconftool-2","-t","string","--set","/desktop/mate/background/picture_filename",'"%s"' % imagepath)
        elif desktop_session == "lxde":
            try:
                subprocess.Popen("pcmanfm", "-w", imagepath)
            except:
                subprocess.Popen("pcmanfm --set-wallpaper %s --wallpaper-mode=scaled" % imagepath)
        elif desktop_session == "xfce" or desktop_session.startswith("xubuntu"):
            subprocess.Popen("xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/workspace0/last-image", "-s", imagepath)       
