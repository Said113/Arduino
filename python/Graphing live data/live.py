#!/usr/bin/python
# -*- coding: utf-8 -*-
# Said Gourida


import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *


position1=[]
position2=[]
position3=[]
mydata=serial.Serial("com3",1200)
plt.ion()

def drwaing():
        plt.ylim(0,200)
        plt.grid(True)
        plt.plot(Extra,'ro')
        plt.plot(Ordinary,'bo')
        plt.plot(Light,'go')
        plt.pause(.000001)

while True:
        y=mydata.readline()
        time=y.decode().strip()
        time=int(time[:-2])
        if time<50:
           position1.append(time)
        elif 120<time>50:
           position2.append(time)
        elif 120>time:
           position3.append(time)
        Light=np.array(position3,dtype="i")
        Ordinary=np.array(position2,dtype="i")
        Extra=np.array(position1,dtype="i")
        drawnow(drwaing)
