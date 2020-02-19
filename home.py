import tkinter as tk
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import cv2
import numpy as np
import csv
import time
import pyrebase
import firebase_admin

from tkinter import *
from tkinter import font as tkfont

from firebase_admin import credentials
from tkinter import messagebox

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image

from utils import label_map_util
from utils import visualization_utils as vis_util
from utils import visualization_utils_putih as vis_util_putih

tk = Tk()
tk.title("Aplikasi Deteksi Objek")
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

def unggah_file():
    import firebase_admin
    from firebase_admin import credentials, firestore, storage

    cred=credentials.Certificate('E:\\Programing\\ML\\TestingPI\\path\\to\\serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'countingcars-4a603.appspot.com'
    })
    db = firestore.client()
    bucket = storage.bucket()
    blob = bucket.blob('file/laporan.csv')
    outfile='E:\\Programing\\ML\\TestingPI\\data_csv\\laporan.csv'
    blob.upload_from_filename(outfile)

    msg = messagebox.showinfo( "Upload File", "Unggah File Berhasil")

def deteksi_mobil():

    number = []

    with open('./data_csv/laporan.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        csv_line = \
            'Kendaraan'
        writer.writerows([csv_line.split(',')])

    # cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture('./data_vidio/GOPR0058.mp4')
    cap = cv2.VideoCapture('./data_vidio/ddd.mp4')

    total_passed_vehicle = 0

    MODEL_NAME = 'Deteksi_Kendaraan'
    MODEL_FILE = MODEL_NAME + '.tar.gz'
    # DOWNLOAD_BASE = \
    #     'http://download.tensorflow.org/models/object_detection/'

    PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

    PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

    NUM_CLASSES = 90

    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map,
            max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)


    def load_gambar_numpy(image):
        (im_width, im_height) = image.size
        return np.array(image.getdata()).reshape((im_height, im_width,
                3)).astype(np.uint8)


    def object_detection():
        total_passed_vehicle = 0
        size = '.....'
        with detection_graph.as_default():
            with tf.Session(graph=detection_graph) as sess:

                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

                detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

                detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
                detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')

                while cap.isOpened():
                    (ret, frame) = cap.read()

                    if not ret:
                        print ('Selesai...')
                        break

                    input_frame = frame

                    image_np_expanded = np.expand_dims(input_frame, axis=0)

                    (boxes, scores, classes, num) = \
                        sess.run([detection_boxes, detection_scores,
                                detection_classes, num_detections],
                                feed_dict={image_tensor: image_np_expanded})

                    (counter, csv_line) = \
                        vis_util.visualize_boxes_and_labels_on_image_array(
                        cap.get(1),
                        input_frame,
                        np.squeeze(boxes),
                        np.squeeze(classes).astype(np.int32),
                        np.squeeze(scores),
                        category_index,
                        use_normalized_coordinates=True,
                        line_thickness=4,
                        )

                    total_passed_vehicle = total_passed_vehicle + counter

                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(
                        input_frame,
                        'Kendaraan Terdeteksi: ' + str(total_passed_vehicle),
                        (10, 35),
                        font,
                        0.6,
                        (0, 0xFF, 0xFF),
                        2,
                        cv2.FONT_HERSHEY_SIMPLEX,
                        )

                    if counter == 1:
                        cv2.line(input_frame, (0, 200), (640, 200), (0, 0xFF, 0), 5)
                    else:
                        # Detection warna red
                        cv2.line(input_frame, (0, 200), (640, 200), (0, 0, 0xFF), 5)

                    # Input info ke vidio
                    cv2.putText(
                        input_frame,
                        'Garis Hitung',
                        (500, 190),
                        font,
                        0.6, #Ukuran Font
                        (0, 0, 0xFF), #Warna Font
                        2,
                        cv2.LINE_AA, # Jenis Font
                        )
                    cv2.putText(
                        input_frame,
                        ' ' + str(size),
                        (14, 70),
                        font,
                        0.5,
                        (0x00,0x00,0x00),
                        1,
                        cv2.LINE_AA,
                        )

                    cv2.imshow('kendaraan terdeteksi', input_frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                        sys.exit()

                    if csv_line != 'not_available':
                        with open('./data_csv/laporan.csv', 'a', newline='') as f:
                            writer = csv.writer(f)
                            (size) = \
                                csv_line.split(',')
                            writer.writerows([csv_line.split(',')])
                cap.release()
                cv2.destroyAllWindows()

    object_detection()

judul = Label(tk,
              text="Applikasi Object Detection Kendaraan",
              font="Arial 15 bold",
              bd=16,
              relief="groov",
              pady=10)
space = Label(tk,
              text="",
              bg='#fff')
space1 = Label(tk,
              text="",
              bg='#fff')
space2 = Label(tk,
              text="",
              bg='#fff')
deteksi = Button(tk,
                 text= "Mulai",
                 font="Verdana 12 bold",
                 bg='deep sky blue',
                 fg='white',
                 width=20,
                 command = deteksi_mobil)
unggah = Button(tk,
                 text= "Unggah File",
                 font="Verdana 12 bold",
                 bg='deep sky blue',
                 fg='white',
                 width=20,
                 command = unggah_file)
keluar = Button(tk,
                text= "Keluar",
                font="Verdana 8 bold",
                bg='red',
                fg='white',
                height=2,
                command = frame1.quit)

judul.pack(side=TOP,fill=X)
space.pack(side=TOP)
deteksi.pack(side=TOP)
space1.pack(side=TOP)
unggah.pack(side=TOP)
space2.pack(side=TOP)
keluar.pack(side=TOP)
Kanvas.pack()
tk.mainloop()