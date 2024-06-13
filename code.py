from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,  QVBoxLayout
from PyQt5.QtCore import Qt
from random import randint

dodatok = QApplication([])
win = QWidget()
win.resize(400,300)

win.setWindowTitle("Визначник переможця")

nadpus = QLabel("Натисни, щоб дізнатися переможця")
lineV = QVBoxLayout()

lineV.addWidget(nadpus,alignment = Qt.AlignCenter)

nadpus2 = QLabel("?")
lineV.addWidget(nadpus2,alignment = Qt.AlignCenter)

knopka = QPushButton("Згеренувати")
lineV.addWidget(knopka,alignment = Qt.AlignCenter)

win.setLayout(lineV)


def one():
    nadpus.setText("Переможець")
    nadpus2.setText(str(randint(1,100)))


knopka.clicked.connect(one)
win.show()
dodatok.exec()