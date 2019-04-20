# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 12:41:22 2017

@author: timbu
"""
import karte_data
from PIL import Image
import pylab
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
turm1 = mpimg.imread("Turm1.png")
nichts = mpimg.imread("Nichts.png")
weg = mpimg.imread("Weg.png")
burg = mpimg.imread("Burg.png")
def setzeBild(n,m):
    if (karte_data.matrix[n][m] == 0):
        return nichts
    elif ((karte_data.matrix[n][m] >= 1) and (karte_data.matrix[n][m] <= 65)):
        return weg
    elif ((karte_data.matrix[n][m] == 66)):
        return burg
    elif (karte_data.matrix[n][m] == 99):
        return turm1
def erstelle_karte():
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(0,i))
    karte1 = np.concatenate(lst_img,axis=1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(1,i))
    karte2 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(2,i))
    karte3 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(3,i))
    karte4 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(4,i))
    karte5 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(5,i))
    karte6 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(6,i))
    karte7 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(7,i))
    karte8 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(8,i))
    karte9 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(9,i))
    karte10 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(10,i))
    karte11 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(11,i))
    karte12 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(12,i))
    karte13 = np.concatenate(lst_img,axis = 1)
    lst_img = []
    for i in range(18):
            lst_img.append(setzeBild(13,i))
    karte14 = np.concatenate(lst_img,axis = 1)
    karte = np.concatenate((karte1,karte2,karte3,karte4,karte5,karte6,karte7,karte8,karte9,karte10,karte11,karte12,karte13,karte14),axis = 0)
   

    return karte
plt.axis("off")
plt.imshow(erstelle_karte())
pylab.savefig("karte.png")
img = Image.open("karte.png")
img.show()