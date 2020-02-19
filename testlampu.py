import tkinter as tk
import pyrebase
import firebase_admin

from tkinter import *
from tkinter import font as tkfont

from firebase_admin import credentials
from tkinter import messagebox

tk = Tk()
tk.title("Aplikasi Waktu Lalu Lintas")
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
    msg = messagebox.showinfo( "Download File", "File Berhasil di Unduh")

def lampu():
    msg = messagebox.showinfo( "Waktu", "Waktu Di Nyalakan")

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
              text="Applikasi Waktu Lalu Lintas",
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