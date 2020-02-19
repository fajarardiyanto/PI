import tkinter as tk
import RPi.GPIO as GPIO
import time
import pyrebase
import firebase_admin

from tkinter import *
from tkinter import font as tkfont

from firebase_admin import credentials
from tkinter import messagebox

tk = Tk()
tk.title("Aplikasi Rahasia")
tk.resizable(width=False,height=False)
Kanvas = Canvas(tk,width=720,height=350, background="white")
background_image = PhotoImage(file = "E:\\Programing\\ML\\TestingPI\\test_images\\bg.gif")
background_label = Label(tk, image=background_image)
background_label.place(x=0, y=35, relwidth=1, relheight=1)

lebar_home = 520
tinggi_home = 320

tk.configure(width=lebar_home,height=tinggi_home)
frame1 = Frame(tk,width=lebar_home,height=tinggi_home)

lebar_tampilan = tk.winfo_screenwidth()
tinggi_tampilan = tk.winfo_screenheight()
x = (lebar_tampilan/2)-(lebar_home/2)
y = (tinggi_tampilan/2)-(tinggi_home/2)
tk.geometry("%dx%d+%d+%d" % (lebar_home,tinggi_home,x,y))

def unduh_file():
        cred=credentials.Certificate('E:\\Programing\\ML\\TestingPI\\path\\to\\serviceAccountKey.json')
        config = {
            "apiKey": "AIzaSyBzbmPBjwSwZgnhwEM76fM3XklCtM3lU5Q",
            "authDomain": "countingcars-4a603.firebaseapp.com",
            "databaseURL": "https://countingcars-4a603.firebaseio.com",
            "projectId": "countingcars-4a603",
            "storageBucket": "countingcars-4a603.appspot.com",
            "messagingSenderId": "691798674025"
        }
        firebase = pyrebase.initialize_app(config)

        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        storage.child("file/laporan.csv").download("download_csv/laporan.csv")

        msg = messagebox.showinfo( "Download File", "File Berhasil di Unduh")

def lampu():
    input_file = open("./download_csv/laporan.csv","r+")
    reade_file = csv.reader(input_file)

    nilai = len(list(reade_file))

    def liteon(pin,tiim):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(tiim)
    def liteoff(pin,tiim):
        GPIO.output(pin, GPIO.LOW)
        time.sleep(tiim)
        return

    if 100 <= nilai <= 200:
        merah = 10
        kuning = 1
        hijau = 20
    elif 20 <= nilai <= 100:
        merah = 8
        kuning = 1
        hijau = 15
    elif 10 <= nilai <= 20:
        merah = 5
        kuning = 1
        hijau = 10
    else:
        merah = 2
        kuning = 1
        hijau = 5

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    for i in range(0,5):
        liteon(11,merah)
        liteoff(11,.1)
        liteon(12,kuning)
        liteoff(12,.1)
        liteon(13,hijau)
        liteoff(13,0.5)
    print("Selesai")
    GPIO.cleanp()

space = Label(tk,
              text="",
              bg='#fff')
space1 = Label(tk,
              text="",
              bg='#fff')
space2 = Label(tk,
              text="",
              bg='#fff')
judul = Label(tk,
              text="Applikasi Lampu Lalu Lintas",
              font="Arial 15 bold",
              bd=16,
              relief="groov",
              pady=10)
mulai = Button(tk,
                 text= "Nyalakan Lampu",
                 font="Verdana 12 bold",
                 bg='deep sky blue',
                 fg='white',
                 width=20,
                 command = lampu)
unduh = Button(tk,
                 text= "Unduh File",
                 font="Verdana 12 bold",
                 bg='deep sky blue',
                 fg='white',
                 width=20,
                 command = unduh_file)
keluar = Button(tk,
                text= "Keluar",
                font="Verdana 8 bold",
                bg='red',
                fg='white',
                height=2,
                command = frame1.quit)

judul.pack(side=TOP,fill=X)
space.pack(side=TOP)
mulai.pack(side=TOP)
space1.pack(side=TOP)
unduh.pack(side=TOP)
space2.pack(side=TOP)
keluar.pack(side=TOP)
Kanvas.pack()
tk.mainloop()