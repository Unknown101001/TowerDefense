# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 15:02:54 2017

@author: timbu
"""

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys


Ui_MainWindow, WindowBaseClass = uic.loadUiType("oberflächeTD2.ui")

class TowerDefense(WindowBaseClass, Ui_MainWindow):
    def __init__(self, parent=None):
        WindowBaseClass.__init__(self, parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.resize(900, 700)
        self.updateGame()
    def make_enemy(self):
        pass
    def make_tower(self):
        pass
    def move_enemy(self):
        pass
    def is_in_range(self,tower,enemy):
        pass
    def nearest_enemy(self,tower):
        pass
    def shoot(self,tower,enemy):
        pass
    def kill_enemy(self,enemy):
        pass
    def get_position_enemy(self):
        pass
        
    def get_position_tower(self):
        pass

    def updateGame(self):
        pass
    def resetGame(self):
        pass
    def quitGame(self):
        pass
if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    dialog = TowerDefense()
    dialog.show()
    sys.exit(app.exec_())