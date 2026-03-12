import os

with open("commands.txt", "r") as f:
    text = f.read()

if "browser" in text:
    os.system("firefox")

elif "terminal" in text:
    os.system("gnome-terminal")

elif "close" in text:
    os.system("xdotool getwindowfocus windowkill")

elif "shutdown" in text:
    os.system("shutdown now")

elif "restart" or " reboot" in text:
    os.system("reboot")