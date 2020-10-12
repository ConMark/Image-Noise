import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageOps
from matplotlib import image, pyplot
import numpy as np
from numpy import asarray
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pylab as plt

class GUI(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        self.winfo_toplevel().title("Image Noise")

        def browse():
            root = tk.Tk()
            root.withdraw()
            global file_path
            file_path = filedialog.askopenfilename()
            root.destroy()
        B = tk.Button(self, text ="Select Image", command = browse)
        B.pack()

        proctype = IntVar()
        randbut = tk.Radiobutton(root, 
              text="Random",
              padx = 20, 
              variable=proctype, 
              value=1)
        ijkbut = tk.Radiobutton(root, 
              text="I,J,K based",
              padx = 20, 
              variable=proctype, 
              value=2)
        randbut.pack()
        ijkbut.pack()

        def process():
            im = Image.open(file_path)
            im = im.resize((int(im.size[0]/10), int(im.size[1]/10)))

            data = asarray(im)
            pyplot.figure()
            pyplot.imshow(data)

            data2 = np.ndarray(shape=(im.size[1],im.size[0],3), dtype=float, order='F')

            for i in range(0,im.size[1]):
                for j in range(0,im.size[0]):
                    for k in range(0,3):
                        data2[i,j,k] = data[i,j,k] + random.randint(-30,30)
                        if proctype.get() == 1:
                            data2[i,j,k] = data[i,j,k] + random.randint(-30,30)
                        if proctype.get() == 2:
                            data2[i,j,k] = data[i,j,k] - i*2 + j*3 - k*4         

            pyplot.figure()
            pyplot.imshow(data2.astype('uint8'))
            pyplot.show()
        P = tk.Button(root, text ="Process", command = process)
        P.pack()

root = tk.Tk()
gui = GUI(root)
root.mainloop()




