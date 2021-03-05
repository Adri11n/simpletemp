import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def banner():
    if platform.system() == "Windows":
        os.system("type banner\\banner.txt")
    else:
        os.system("cat banner/banner.txt")