# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:54:43 2024

@author: brian
"""

import tkinter as tk
from tkinter import ttk
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation

def animate(i):
    try:
        data = np.loadtxt('internet_speed.txt',delimiter=',')
        ax.clear()
        ax.plot(data[:,0], data[:,1],label='Download',marker='o',)
        ax.plot(data[:,0], data[:,2],label='Upload',marker='o',)
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Speed (Mbps)')
        ax.legend(loc="upper right")
    except:
        pass
    
class livePlot:
    def __init__(self,window,f):
        self.frame = tk.Frame(window)
        self.frame.grid(row=0,column=0)
        
        self.label = tk.Label(self.frame,text='Internet speed (Download and Upload)')
        self.label.grid(row=0,column=0)
        
        self.frame1 = tk.Frame(window)
        self.frame1.grid(row=1,column=0)
        
        self.cv = FigureCanvasTkAgg(f,master=self.frame1)
        self.cv.draw()
        self.cv.get_tk_widget().pack()
        
f = Figure(figsize=(5,5), dpi=100)
ax = f.add_subplot(111)
window = tk.Tk()
main = livePlot(window,f)
ani = animation.FuncAnimation(f, animate, interval=1000, cache_frame_data=False)    
window.mainloop()