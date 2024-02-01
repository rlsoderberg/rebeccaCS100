#so i want to make a beige box in the middle of the scroll
#i'm thinking, maybe i can make a qframe, and then give it a black border?
#i'm not sure how to do qframes tho!!!
#now i'm trying to addwidgets to my qframe, and it doesn't like it

#i mean... i could hand paint a background, but that seems like cheating!!!
#and the reason i didn't just use an image of an entire scroll, was i didn't know how to paintevent atop image
#well... i tried setting qpainter to be on the scroll pixmap... and it looks like it's behind everything else
#uh... what if i just put some spacers in the middle? instead of a qvbox?

#ok, now i have to get the game working, and make some message boxes

import sys
import math
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
from pathlib import Path

class MainWindow(QWidget):

    #MainWindow constructor 
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        #set geometry...
        self.setGeometry(100, 100, 100, 100)
        self.setWindowTitle("Tic-Tac-Toe")

        lBorder = QLabel('Left Border', alignment=Qt.AlignmentFlag.AlignLeft)
        border = QPixmap('border.png')
        lBorder.setPixmap(border)

        rBorder = QLabel('Right Border', alignment=Qt.AlignmentFlag.AlignRight)
        rBorder.setPixmap(border)


        scrollt = QLabel('Scroll Top', alignment=Qt.AlignmentFlag.AlignTop)
        scrolltop = QPixmap('scrollt.png')
        scrollt.setPixmap(scrolltop)

        scrollb = QLabel('Scroll Bottom', alignment=Qt.AlignmentFlag.AlignBottom)
        scrollbottom = QPixmap('scrollb.png')
        scrollb.setPixmap(scrollbottom)
        

        layout = QHBoxLayout()
        layout.addWidget(lBorder)

        
        
        layout.addSpacing(500)
        

        layout.addWidget(rBorder)
        self.setLayout(layout)





        #commented out for now since we haven't made it yet
        #self.game = Game()

    #respond to paint event
    def paintEvent(self, event):
        qp = QPainter(self)
        #set pen color
        qp.setPen(QColor(0,0,0))
        pixmap = QPixmap("scroll3.png")
        qp.drawPixmap(self.rect(), pixmap)
        #what is event? where is rect coming from?
        size = event.rect().size()

        #calculate width & height of rows & columnds
        colsize = size.width() // 5
        rowsize = size.height() // 5

        #draw vertical lines
        qp.drawLine(colsize*2, rowsize, colsize*2, rowsize*4)
        qp.drawLine(colsize*3, rowsize, colsize*3, rowsize*4)
        #draw horizontal lines
        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)

    

def main():
    app = QApplication([])
    w = MainWindow()
    w.setStyleSheet(Path('style.qss').read_text())
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()





