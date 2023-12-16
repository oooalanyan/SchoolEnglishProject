import PyQt5
from test import Ui_MainWindow

from PyQt5 import QtWidgets
from PyQt5.QtMultimedia import QSound
import sys

sound_file0 = '../pythonProject/audio/0.wav'
sound0 = PyQt5.QtMultimedia.QSound(sound_file0)
sound_file1 = '../pythonProject/audio/1.wav'
sound1 = PyQt5.QtMultimedia.QSound(sound_file1)
sound_file2 = '../pythonProject/audio/2.wav'
sound2 = PyQt5.QtMultimedia.QSound(sound_file2)
sound_file3 = '../pythonProject/audio/3.wav'
sound3 = PyQt5.QtMultimedia.QSound(sound_file3)
sound_file4 = '../pythonProject/audio/4.wav'
sound4 = PyQt5.QtMultimedia.QSound(sound_file4)



class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyApp,self).__init__(parent)
        self.setupUi(self)
        self.first.clicked.connect(self.show_vis)
        self.second.clicked.connect(self.show_vis2)
        self.third.clicked.connect(self.show_vis3)
        self.forth.clicked.connect(self.show_vis4)

    def show_vis(self):
        sound0.stop()
        sound2.stop()
        sound3.stop()
        sound4.stop()
        sound1.play()
    def show_vis2(self):
        sound0.stop()
        sound1.stop()
        sound3.stop()
        sound4.stop()
        sound2.play()
    def show_vis3(self):
        sound0.stop()
        sound1.stop()
        sound2.stop()
        sound4.stop()
        sound3.play()
    def show_vis4(self):
        sound0.stop()
        sound1.stop()
        sound3.stop()
        sound2.stop()
        sound4.play()



if __name__==('__main__'):
    app=QtWidgets.QApplication(sys.argv)
    window =MyApp()
    window.showFullScreen()
    sys.exit(app.exec())
