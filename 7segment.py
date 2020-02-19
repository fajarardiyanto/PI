from RPi import GPIO
import time
import csv

GPIO.setmode(GPIO.BCM)

segments =  (11,4,23,8,7,10,18,25)

GPIO.setup(segments, GPIO.OUT, initial=0)
GPIO.setwarnings(False)

digits = (22,27,17,24)

GPIO.setup(digits, GPIO.OUT, initial=1)

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
elif 30 <= nilai <=50:
    count = 5555
elif 10 <= nilai <-30:
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