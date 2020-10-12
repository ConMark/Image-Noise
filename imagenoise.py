from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageOps
from matplotlib import image, pyplot
import numpy as np
from numpy import asarray
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pylab as plt

root = Tk()

def browse():
    root = Tk()
    root.withdraw()
    global file_path
    file_path = filedialog.askopenfilename()
    root.destroy()

B = Button(root, text ="Select Image", command = browse)
B.pack()

randbut = IntVar()
ijkbut = IntVar()
rbut = Checkbutton(root, text = "random", variable = randbut, \
        onvalue = 1, offvalue = 0, height=5, \
        width = 20)
ibut = Checkbutton(root, text = "i,j,k based", variable = ijkbut, \
        onvalue = 1, offvalue = 0, height=5, \
        width = 20)
rbut.pack()
ibut.pack()

if randbut.get() == 1:
    ijkbut.get() == 0
if ijkbut.get() == 1:
    randbut.get() == 0

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
                if randbut.get() == 1:
                    data2[i,j,k] = data[i,j,k] + random.randint(-30,30)
                if ijkbut.get() == 1:
                    data2[i,j,k] = data[i,j,k] - i*2 + j*3 - k*4
            
    pyplot.figure()
    pyplot.imshow(data2.astype('uint8'))
    pyplot.show()
P = Button(root, text ="Process", command = process)
P.pack()

root.mainloop()