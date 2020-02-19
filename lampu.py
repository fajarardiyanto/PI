import tkinter as tk
import RPi.GPIO as GPIO
import time
import pyrebase
import firebase_admin
import csv

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

def waktu():
    segments =  (11,4,23,8,7,10,18,25)
    digits = (22,27,17,24)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(digits, GPIO.OUT, initial=1)
    GPIO.setup(segments, GPIO.OUT, initial=0)

    num = {' ':(0,0,0,0,0,0,0,0),
        '0':(1,1,1,1,1,1,0,0),
        '1':(0,1,1,0,0,0,0,0),
        '2':(1,1,0,1,1,0,1,0),
        '3':(1,1,1,1,0,0,1,0),
        '4':(0,1,1,0,0,1,1,0),
        '5':(1,0,1,1,0,1,1,0),
        '6':(1,0,1,1,1,1,1,0),
        '7':(1,1,1,0,0,0,0,0),
        '8':(1,1,1,1,1,1,1,0),
        '9':(1,1,1,1,0,1,1,0),
        'b':(0,0,1,1,1,1,1,0),
        'y':(0,1,1,1,0,1,1,0),
        'E':(1,0,0,1,1,1,1,0),
        'A':(1,1,1,0,1,1,1,0),
        'L':(0,0,0,1,1,1,0,0),
        'X':(0,1,1,0,1,1,1,0)}

    def seg():
        for digit in range(4):
            GPIO.output(segments, (num[display_string[digit]]))
            GPIO.output(digits[digit],0)
            time.sleep(0.001)
            GPIO.output(digits[digit], 1)

    input = open("./path/laporan.csv","r+")
    read_file = csv.reader(input)
    nilai = len(list(read_file))

    if 50 <= nilai <= 100:
        count = 9999
    elif 30 <= nilai <= 50:
        count = 5555
    elif 10 <= nilai <= 30:
        count = 1000
    else:
        count = 500

    try:
        n = count
        while n >= 0:
            display_string = str(n).rjust(4)
            if n == 0:
                display_string = ' byE'
            seg()
            n -= 1
        n = 1000
        while n >= 100:
            if n <= 5:
                display_string = 'LEXA'
            seg()
            n -= 1
    finally:
        GPIO.cleanup()

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
              text="Applikasi Waktu Lampu Lalu Lintas",
              font="Arial 15 bold",
              bd=16,
              relief="groov",
              pady=10)
mulai = Button(tk,
                 text= "Nyalakan Waktu",
                 font="Verdana 12 bold",
                 bg='deep sky blue',
                 fg='white',
                 width=20,
                 command = waktu)
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