#well, i removed some of the selfs... and that stopped it giving me an error about endPaint...
#but the screen is still black! what now??? i'm going to try setting the brush to just chartreuse
#oh come on!!! that didn't even work!!!
#how about... i skip this whole graphics scene thing for now


import sys
import math
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
from pathlib import Path
from tictactoe_game import Game

class MainWindow(QWidget):

    #MainWindow constructor 
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        #set geometry...
        self.setGeometry(100, 100, 100, 100)
        self.setFixedSize(560, 370)
        self.setWindowTitle("Runescape Tic-Tac-Toe")

        #images for screen layout
        lBorder = QLabel('Left Border', alignment=Qt.AlignmentFlag.AlignLeft)
        border = QPixmap('border.png')
        lBorder.setPixmap(border)

        rBorder = QLabel('Right Border', alignment=Qt.AlignmentFlag.AlignRight)
        rBorder.setPixmap(border)
        
        layout = QHBoxLayout()
        layout.addWidget(lBorder)
        
        layout.addSpacing(400)
        

        layout.addWidget(rBorder)
        self.setLayout(layout)


        #game from tictactoe_game
        self.game = Game()

    #respond to paint event
    def paintEvent(self, event):

        #set pixmap marker images
        pixmapX = QtGui.QPixmap("water.png")
        pixmapO = QtGui.QPixmap("fire.png")

        graphics = QGraphicsScene()
        qp = QPainter(self)
        loadedPicture = QPixmap("scroll3.png")
 
        brushBackground = QBrush()
        brushBackground.setTexture(loadedPicture)
 
        graphics.setBackgroundBrush(brushBackground)
        
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

        #draw tokens
        for c in range(0, 3):
            for r in range(0, 3):
                if self.game.board[c][r] == 'X':
                    thisPixmap = QPixmap(pixmapX)
                    sceneItem = graphics.addPixmap(thisPixmap)
                    sceneItem.setPos(colsize*self.game.publicX+130, rowsize*self.game.publicY+80)
                elif self.game.board[c][r] == 'O':
                    thisPixmap = QPixmap(pixmapO)
                    sceneItem = self.graphics.addPixmap(thisPixmap)
                    sceneItem.setPos(colsize*self.game.publicX+130, rowsize*self.game.publicY+80)

    #mousePressEvent generates its own event
    def mousePressEvent(self, event):
        #get size of full board
        size = self.size()

        #calculate row & column size
        colsize = size.width() // 5
        rowsize = size.height() // 5

        #mark which col & row were clicked on
        col = math.floor((event.position().x() // colsize)) - 1
        row = math.floor((event.position().y() // rowsize)) - 1

        self.clickx = event.position().x()
        self.clicky = event.position().y()

        #only clicks within board are processed
        if col >= 0 and col < 3 and row >= 0 and row < 3:
            self.game.takeTurn(col, row)
        
        self.repaint()

        winner = self.game.checkForWinner()
        if winner != ' ':
            dlg = WinnerDialog(winner)
            if dlg.exec():
                self.game.clearBoard()

class WinnerDialog(QDialog):
    def __init__(self, winner):
        super().__init__()
    
        #set title
        title = winner + ' has won!'
        if winner == 'C':
            title = "Cat's game"
        self.setWindowTitle(title)

        qbtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(qbtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        msg = "Congratulations " + winner + ". New Game?"
        if winner == 'C':
                msg = "No winner this time. New Game?"

        lbl = QLabel(msg)

        self.layout.addWidget(lbl)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)




def main():
    app = QApplication([])
    w = MainWindow()
    w.setStyleSheet(Path('style.qss').read_text())
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()





