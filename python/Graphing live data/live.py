#!/usr/bin/python
# -*- coding: utf-8 -*-
# Said Gourida


import serial
import numpy as np
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt
from drawnow import *


position1=[]
position2=[]
position3=[]
mydata=serial.Serial("com3",1200)
plt.ion()

def drwaing():
        plt.ylim(0,200) # here just put the min and the max 
        plt.grid(True)
        plt.plot(Extra,'ro') #here r is equal to red and o to "circle" as marker
        #"ro" or "bo" or "gb" the parameters of func plot. like plt.plot(obj,color="",marker="")
        #"ro" or "bo" or "gb" its mean to (r=red,b=blue,g=green,o=circle)
        plt.plot(Ordinary,'bo') 
        plt.plot(Light,'go')
        plt.pause(.000001) # here you must put time for the live graph To avoid problems of crashing

while True: # here you must put while to keep verify the data
        y=mydata.readline()
        time=y.decode().strip() 
        time=int(time[:-2]) # del string
        if time<50:
           position1.append(time)
        elif 120<time>50:
           position2.append(time)
        elif 120>time:
           position3.append(time)
        Light=np.array(position3,dtype="i")
        Ordinary=np.array(position2,dtype="i")
        Extra=np.array(position1,dtype="i")
        drawnow(drwaing) # call the func to draw live
