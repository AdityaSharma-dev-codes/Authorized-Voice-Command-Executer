import os

def exec_command(text):
    if "browser" in text:
        os.system("firefox")

    elif "terminal" in text:
        os.system("gnome-terminal")

    elif "close" in text:
        os.system("xdotool getwindowfocus windowkill")

    elif "shutdown" in text:
        os.system("shutdown now")

    elif "restart" in text or " reboot" in text:
        os.system("reboot")