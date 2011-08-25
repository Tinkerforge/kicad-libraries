#!/usr/bin/python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from form import Ui_PinGenerator

import sys

def mm_in_mil(mm):
	return int(mm*39.3700787*10)

class MainWindow(QMainWindow, Ui_PinGenerator):
	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.direction.insertItems(0,["North","South","East","West"])

		self.connect(self.generate, SIGNAL('clicked()'), self, SLOT('generate()'))

	@pyqtSlot()
	def generate(self):
		
		pad_x = mm_in_mil(float(self.pad_size_x.text()))
		pad_y = mm_in_mil(float(self.pad_size_y.text()))
		pitch = mm_in_mil(float(self.pitch.text()))
		pins = int(self.number_pins.text())
		start_x = mm_in_mil(float(self.start_x.text()))
		start_y = mm_in_mil(float(self.start_y.text()))
		direction = self.direction.currentIndex()

		pinList = self.pinPosList(start_x, start_y, pins, pitch, direction)

		text = ""

		for x in pinList:
			text += "$PAD\nSh \""+ str(20) + "\" R " + str(pad_x) + " " + str(pad_y) + " 0 0 0\nDr 0 0 0\nAt SMD N 00888000\nNe 0 \"\"\nPo " + str(x[0]) + " " + str(x[1]) + "\n$EndPAD\n"


		self.textEdit.append(str(text))
	
	def pinPosList(self, start_x, start_y, pins, pitch, direction):
		pinList = []

		if direction == 0:
			for i in range(0, pins):
				pinList.append((start_x, start_y + pitch * i))
		elif direction == 1:
			for i in range(0, pins):
				pinList.append((start_x, start_y - pitch * i))
		elif direction == 2:
			for i in range(0, pins):
				pinList.append((start_x + pitch * i, start_y))
		else:
			for i in range(0, pins):
				pinList.append((start_x - pitch * i, start_y))

		return pinList


if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())

