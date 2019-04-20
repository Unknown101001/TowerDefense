# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:33:46 2017

@author: timbu
"""
import karte_data
import numpy as np
from PIL import Image
turm1 = Image.open("Turm1.png")
weg = Image.open("Weg.png")
burg = Image.open("Burg.png")
nichts = Image.open("Nichts.png")

def setzeBild(n,m):
    if (karte_data.matrix[n][m] == 0):
        return nichts
    elif ((karte_data.matrix[n][m] >= 1) and (karte_data.matrix[n][m] <= 65)):
        return weg
    elif ((karte_data.matrix[n][m] == 66)):
        return burg
    elif (karte_data.matrix[n][m] == 99):
        return turm1

imageWidth=900
imageHeight=700

im = Image.new("RGB", (imageWidth, imageHeight))

for i in range(18):
    for j in range(14):
        im.paste(setzeBild(j,i), (50*i,50*j))

im.show()
im.save("aktuelle_karte.png","PNG")