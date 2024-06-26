import sys
import math
import random
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from cs100b.module5.tictactoe_game import Game

class mainwindow(QWidget):
    def __init__(self, parent = None):
        #i'm actually making proper comments now because i need to understand this new code!!!
        super(mainwindow, self).__init__(parent)
        #resize adjusts window size
        self.resize(500,500)
        self.setWindowTitle('Tic Tac Toe')

        #create game object using class from tictactoe_game
        self.game = Game()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        qp.setPen(QColor(0,0,0))

        rect = QRect(0, 0, 500, 500)

        colsize = rect.width()//5
        rowsize = rect.height()//5

        qp.drawLine(colsize*2, rowsize, colsize * 2, rowsize*4)
        qp.drawLine(colsize*3, rowsize, colsize * 3, rowsize * 4)
        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)

        #oh!!! this was in the wrong place!!!
        #now, draw the tokens that are on the board
        for r in range(0, 3):
            for c in range(0, 3):
                #use the game object we created, & self.board from Game
                if self.game.board[c][r] == 'X':
                    #what is this drawing letters thing??? (painter, coordinates, scale)???
                    self.drawX(qp, c, r, colsize, rowsize)
                elif self.game.board[c][r] == 'O':
                    self.drawO(qp, c, r, colsize, rowsize)
                    #oh i see!! we're defining the functions!!

    def drawX(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize

        #drawing x
        qp.drawLine(x, y, x+colsize, y+rowsize)
        qp.drawLine(x+colsize, y, x, y+rowsize)

    def drawO(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize

        #drawing o
        qp.drawEllipse(x, y, colsize, rowsize)

        img1 = QPixmap("trfarclio.png")

        qp.drawLine(350, 150, 450, 50)

        brush = QBrush(Qt.GlobalColor.red, Qt.BrushStyle.SolidPattern)
        qp.setBrush(brush)

        qp.drawEllipse(400, 130, 10, 10)
        qp.drawPixmap(215, 310, img1)

        #respond to mousepress events
    def mousePressEvent(self, event):        
        size = self.size()

        colsize = size.width()//5
        rowsize = size.height()//5

        #math.floor rounds down; subtracting 1... ignores empty space?
        col = math.floor((event.position().x() // colsize )) - 1
        row = math.floor((event.position().y() // rowsize)) - 1

        #we finish ignoring empty space... by only dealing with a 3x3 square?
        if col >= 0 and col < 3 and row >= 0 and row < 3:
            self.game.takeTurn(col, row)
        
        #force a repaint
        #i changed this to paintEvent for now? because there's nothing called repaint?
        paintEvent()

#QDialog creates popup window
class WinnerDialog(QDialog):
    #another use of the winner variable from checkforwinner!
    #i guess gameover is just more simple & internal to tictactoe_game 
    def __init__(self, winner):
        super().__init__()
    
        self.setWindowTitle(f/'{winner} has won!')

        self.buttonBox = QDialogBox(qbtn)
        #vertical bar is... bitwise or? WAT?
        #qbtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        #this accept/reject thing... it's too convenient!!!
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()

        lbl = QLabel(f/"Congratulations, {winner}. New Game?")
        self.layout.addWidget(lbl)
        self.layout.addWidget(self.buttonBox)
        self.setlayout(self.layout)
        """
        #see, i would just go like... 
        
        okbtn = qbtn.addButton('OK', QDialogButtonBox.StandardButton)
        xbtn = qbtn.addButton('Cancel', QDialogButtonBox.StandardButton)

        self.buttonBox.okbtn.connect(self.newGame)
        self.buttonBox.xbtn.connect(self.closeDialog)

        if self.newGame:
            game.clearBoard()
            #i'm trying to figure out how to manually close the dialog box...
            #ok true!!! there aren't that many actions besides accept and reject!!!
            #fine, i'll just do the dialog like normal
            #but this is messing with the arguments for takeTurn and i'm not sure why
        """

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    #well, when i try to call this here the program breaks!!!
    #w.clickEvent()
    

    #i still don't EXACTLY get the deal with sys.exit
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
