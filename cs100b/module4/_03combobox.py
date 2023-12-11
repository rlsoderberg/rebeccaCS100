#oops, i think i only went through the first section of the pyqt tutorials
#i'll go through them all later!!! but here's the one on combo boxes, which i will use to get mine working

import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtGui



class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #maybe we could skip this whole screen size thing... maybe there's a way to do negative coords

        #for now... this one seems to give me the correct w&h, but 'cannot unpack non-iterable QRect object'
        geometry = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        print(geometry)
        #this one, i can unpack, but i'm not sure what it's giving me???
        screen = QtGui.QGuiApplication.primaryScreen()
        screenWidth = screen.geometry().width()
        screenHeight = screen.geometry().height()
        print(f'{screenWidth}, {screenHeight}')

        # create a grid layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        cb_label = QLabel('Please select a platform:', self)

        # create a combobox
        self.cb_location = QComboBox(self)
        self.cb_location.addItem('Upper Left')
        self.cb_location.addItem('Upper Right')
        self.cb_location.addItem('Lower Left')
        self.cb_location.addItem('Lower Right')

        self.cb_location.activated.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addWidget(cb_label)
        layout.addWidget(self.cb_location)
        layout.addWidget(self.result_label)

        # show the window
        self.show()

        #when i try to do this, the window disappears instantaneously!!!
        #screen_size = QSize(width(), height())
        #should i put it up here, in mainwindow def?
        #and i don't know how i would pass it into my new window classes, or whatever...

    def update(self):
        if self.cb_location.currentText() == 'Upper Left':
            self.result_label.setText('Upper Left')
        elif self.cb_location.currentText() == 'Upper Right':
            self.result_label.setText('Upper Right')
        elif self.cb_location.currentText() == 'Lower Left':
            self.result_label.setText('Lower Left')
        elif self.cb_location.currentText() == 'Lower Right':
            self.result_label.setText('Lower Right')

#is this REALLY the best way to do it? to make a class for each window location???
class UL_window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("UL Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setGeometry(50, 50, 200, 50)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())