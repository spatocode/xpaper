#!/usr/bin/env python
# Copyright (c) 2019, Ekene Izukanne
# Xpaper is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.


import subprocess
import os
import sys

def setwallpaper(imagepath):
    desktop_session = os.environ.get("DESKTOP_SESSION")
    if desktop_session is not None:
        desktop_session = desktop_session.lower()
        command = None
        if desktop_session in ["gnome", "ubuntu", "unity", "cinnamon", "pantheon"]:
            command = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "'file://%s'" % imagepath]
        elif desktop_session == "mate":
            try:
                command = ["dconf", "write", "/org/mate/desktop/background/picture-filename", imagepath]
            except:
                command = ["gsettings", "set", "org.mate.background", "picture-filename", "'%s'" % imagepath]
            finally:
                command = ["mateconftool-2","-t","string","--set","/desktop/mate/background/picture_filename",'"%s"' % imagepath]
        elif desktop_session == "lxde":
            try:
                command = ["pcmanfm", "-w", imagepath]
            except:
                command = ["pcmanfm --set-wallpaper %s --wallpaper-mode=scaled" % imagepath]
        elif desktop_session == "xfce" or desktop_session.startswith("xubuntu"):
            command = ["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/workspace0/last-image", "-s", imagepath]
        elif desktop_session in ["kde", "kde3", "trinity"]:
            command = ["dcop kdesktop KBackgroundIface setWallpaper 0 '%s' 6" % imagepath]
        elif desktop_session in ["fluxbox", "jwm", "openbox", "afterstep"]:
            try:
                command = ["fbsetbg", imagepath]
            except:
                sys.stderr.write("ERROR: Failed to set wallpaper with fbsetbg!\n")
                sys.stderr.write("Please make sure you have fbsetbg installed.\n")
        elif desktop_session == "blackbox":
            command = ["bsetbg", "-full", imagepath]
        elif desktop_session == "windowmaker":
            command = ["wmsetbg -s -u %s" % imagepath]
        exec_command(command)

def exec_command(command):
    if not command:
        return
    output = subprocess.check_output(command)
    path = output.decode("utf-8").strip()[1:-1]
    return path

def getwallpaper():
    desktop_session = os.environ.get("DESKTOP_SESSION")
    if desktop_session is not None:
        desktop_session = desktop_session.lower()
        command = None
        if desktop_session in ["gnome", "ubuntu", "unity", "cinnamon", "pantheon"]:
            command = ["gsettings", "get", "org.gnome.desktop.background", "picture-uri"]
        if desktop_session == "XFCE":
            command = ["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/workspace0/last-image"]
        elif desktop_session == "MATE":
            command = ["dconf", "read", "/org/mate/desktop/background/picture-filename"]
        return exec_command(command)
