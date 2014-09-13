#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import random
from PyQt4 import QtGui, QtCore

class dialog(QtGui.QWidget):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self)
		
		self.setWindowTitle(u"龙王山最强王者联盟队内训练专用")

		grid = QtGui.QGridLayout()
		
		self.text    = QtGui.QLabel(u'豪华旗舰版') 
		self.button  = QtGui.QPushButton(u'点击分队！')
		self.name_1  = QtGui.QLineEdit(u'陈森')
		self.name_2  = QtGui.QLineEdit(u'姚耀')
		self.name_3  = QtGui.QLineEdit(u'宋伟')
		self.name_4  = QtGui.QLineEdit(u'郑义')
		self.name_5  = QtGui.QLineEdit(u'赵应')
		self.name_6  = QtGui.QLineEdit(u'鲍兴宇')
		self.name_7  = QtGui.QLineEdit(u'何靖康')
		self.name_8  = QtGui.QLineEdit(u'张俊杰')
		self.name_9  = QtGui.QLineEdit(u'赵逸峰')
		self.name_10 = QtGui.QLineEdit(u'李欣宇')
		self.result  = QtGui.QTextBrowser()

		self.text.setAlignment(QtCore.Qt.AlignRight) 
		
		grid.addWidget(self.text, 8, 1, 1, 1)
		grid.addWidget(self.name_1,  1, 0, 1, 1)
		grid.addWidget(self.name_2,  1, 1, 1, 1)
		grid.addWidget(self.name_3,  2, 0, 1, 1)
		grid.addWidget(self.name_4,  2, 1, 1, 1)
		grid.addWidget(self.name_5,  3, 0, 1, 1)
		grid.addWidget(self.name_6,  3, 1, 1, 1)
		grid.addWidget(self.name_7,  4, 0, 1, 1)
		grid.addWidget(self.name_8,  4, 1, 1, 1)
		grid.addWidget(self.name_9,  5, 0, 1, 1)
		grid.addWidget(self.name_10, 5, 1, 1, 1)
		grid.addWidget(self.button,  6, 0, 1, 2)
		grid.addWidget(self.result, 7, 0, 1, 2)
		
		self.setLayout(grid)
		self.resize(400, 300)				
		self.button.clicked.connect(self.divide)

	
	def divide(self):
		name_1  = self.name_1.text()
		name_2  = self.name_2.text()
		name_3  = self.name_3.text()
		name_4  = self.name_4.text()
		name_5  = self.name_5.text()
		name_6  = self.name_6.text()
		name_7  = self.name_7.text()
		name_8  = self.name_8.text()
		name_9  = self.name_9.text()
		name_10 = self.name_10.text()
		namelist = [name_1,name_2,name_3,name_4,name_5,name_6,name_7,name_8,name_9,name_10]
		# namelist = [u"郑义", u"俊杰", u"靖康", u"陈森", u"姚耀", u"灰灰", u"暴暴", u"耗子", u"安妮", u"赵应"]
		tmp = ""
		self.result.clear()
		if namelist == ['', '', '', '', '', '', '', '', '', '']:
		    self.result.clear()
		else:
		    for i in range(0, 10):
			    # if i == 4:
				    # self.result.append("VS")
			    num = random.randrange(0, 10-i)
			    tmp = tmp + namelist.pop(num) + " "
			    if i == 4:
				    self.result.append(tmp)
				    self.result.append("                          VS")
				    tmp = ""
		    self.result.append(tmp)
			    # self.result.append(tmp)


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = dialog()
	main.show()
	sys.exit(app.exec_())
