# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 15:12:14 2017

@author: timbu
"""

class gegner():
    farbendic = {1:[255,0,0] ,2:[255,28,0] ,3:[255,57,0] ,4:[255,85,0] ,5:[255,113,0] ,6:[255,142,0] ,7:[255,170,0] ,8:[255,198,0] ,9:[255,227,0] ,10:[255,255,0] ,11:[230,255,0] ,12:[204,255,0] ,13:[179,255,0] ,14:[153,255,0] ,15:[128,255,0] ,16:[102,255,0] ,17:[77,255,0] ,18:[51,255,0] ,19:[26,255,0] ,20:[0,255,0] }
    def __init__(self,leben,geschwindigkeit,name,wert):
        self.leben = leben
        self.geschwindigkeit = geschwindigkeit
        self.name = name
        self.wert = wert
        self.farbe = enemy.farbendic[leben]
        self.last_waypoint = wegpunkt_0
        self.next_waypoint = wegpunkt_1
        # self.position = wegpunkt_0
class turm():
    def __init__(self,name,reichweite,feuerrate,preis,schaden,position):
        self.name = name
        self.reichweite = reichweite
        self.feuerrate = feuerrate
        self.preis = preis
        self.schaden = schaden
        self.position = position
class geschoss():
    def __init__(self,tower,enemy,name):
        self.name = name
        self.schaden = tower.schaden
        self.position = tower.position