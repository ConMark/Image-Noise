import tkinter as tk
from tkinter import *
import PIL
from PIL import Image, ImageTk
from tkinter import filedialog
from matplotlib import image, pyplot
import numpy as np
from numpy import asarray
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pylab as plt
from matplotlib.figure import Figure


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
        browsebut = tk.Button(self, text ="Select Image", command = lambda:[browse(), draworig()])
        browsebut.pack()

        def draworig(): 
            img = Image.open(file_path)
            img = img.resize((int(img.size[0]/10), int(img.size[1]/10)))
            img = ImageTk.PhotoImage(img)
            label = Label(self.master, image=img)
            label.img = img # to keep the reference for the image.
            label.pack()


        itxt = tk.Label(self, text = "I value")
        ival = tk.Entry(self)
        jtxt = tk.Label(self, text = "J value")
        jval = tk.Entry(self)
        ktxt = tk.Label(self, text = "K value")
        kval = tk.Entry(self)

        randtxt = tk.Label(self, text = "Randomize by +/-")
        randval = tk.Entry(self)
        
        def hiderand():
            randtxt.pack_forget()
            randval.pack_forget()
            itxt.pack()
            ival.pack()
            jtxt.pack()
            jval.pack()
            ktxt.pack()
            kval.pack()
        
        def hideijk():
            itxt.pack_forget()
            ival.pack_forget()
            jtxt.pack_forget()
            jval.pack_forget()
            ktxt.pack_forget()
            kval.pack_forget()
            randtxt.pack()
            randval.pack()

        proctype = IntVar()
        randbut = tk.Radiobutton(root, 
              text="Random",
              padx = 20, 
              variable=proctype, 
              value=1, command=hideijk)
        ijkbut = tk.Radiobutton(root, 
              text="I,J,K based",
              padx = 20, 
              variable=proctype, 
              value=2, command=hiderand)
        randbut.pack()
        ijkbut.pack()

        def process():
            im = Image.open(file_path)
            im = im.resize((int(im.size[0]/10), int(im.size[1]/10)))

            data = asarray(im)
            # pyplot.figure()
            # pyplot.imshow(data)

            data2 = np.ndarray(shape=(im.size[1],im.size[0],3), dtype=float, order='F')

            for i in range(0,im.size[1]):
                for j in range(0,im.size[0]):
                    for k in range(0,3):
                        if proctype.get() == 1:
                            data2[i,j,k] = data[i,j,k] + random.randint(-int(randval.get()),int(randval.get()))
                        if proctype.get() == 2:
                            data2[i,j,k] = data[i,j,k] + i*int(ival.get()) + j*int(jval.get()) + k*int(kval.get())         
            # pyplot.figure()
            # pyplot.imshow(data2.astype('uint8'))
            # pyplot.show()

            img = ImageTk.PhotoImage(image=Image.fromarray(data2.astype(np.uint8)))
            label = Label(self.master, image=img)
            label.img = img # to keep the reference for the image.
            label.pack()
        

        P = tk.Button(root, text ="Process", command = process)
        P.pack()

root = tk.Tk()
gui = GUI(root)
root.mainloop()




