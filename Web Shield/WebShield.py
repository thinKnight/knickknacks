#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os
import sys
from PyQt4 import QtGui, QtCore

class dialog(QtGui.QWidget):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self)
		# Window Title
		self.setWindowTitle("Web Shield")
		# declare Layout
		grid = QtGui.QGridLayout()
		#read hosts
		f = open('/etc/hosts') #'/etc/hosts'
		content = f.read()
		f.close()
		contentNew = re.findall(r'127.0.0.1\s*(\S*)', content)
		text = ""
		for singleLine in contentNew:
			if singleLine != 'localhost':
				text = text + singleLine + '\n\n'
		content = text
		
		self.url      = QtGui.QLineEdit()
		self.text     = QtGui.QTextBrowser()
		self.label_1  = QtGui.QLabel(u'输入需要屏蔽的网站:')
		self.label_2  = QtGui.QLabel(u'已屏蔽的网站：')
		self.button_1 = QtGui.QPushButton(u'屏蔽')
		self.button_2 = QtGui.QPushButton(u'刷新')
		self.button_3 = QtGui.QPushButton(u'撤销所有屏蔽')

		grid.addWidget(self.label_1,  0, 0)
		grid.addWidget(self.url,      1, 0)
		grid.addWidget(self.button_1, 1, 1)
		grid.addWidget(self.label_2,  2, 0)
		grid.addWidget(self.text,     3, 0)
		grid.addWidget(self.button_2, 3, 1)
		grid.addWidget(self.button_3, 4, 0)

		self.text.setPlainText(content) 

		self.setLayout(grid)

		self.resize(550, 400)
		self.button_1.clicked.connect(self.shield)
		self.button_2.clicked.connect(self.refresh)
		self.button_3.clicked.connect(self.cancelAll)

# -------------------------------------------------------
	def shield(self):
		# 1.read the url from line
		url_w = self.url.text()

		# 2.write into the hosts file & save
		tmp = open('/etc/hosts', 'w')
		tmp.write('127.0.0.1   ' + url_w + '\n')
		tmp.close
		self.url.clear()
		
		# 3.refresh
		self.refresh()
# -------------------------------------------------------
	def refresh(self):
		
		f = open('/etc/hosts') #'/etc/hosts'
		content = f.read()
		f.close()
		contentNew = re.findall(r'127.0.0.1\s*(\S*)', content)
		
		text = ""

		for singleLine in contentNew:
			if singleLine != 'localhost': 
				text = text + singleLine + '\n\n'

		content = text

		self.text.setPlainText(content)

# -------------------------------------------------------	
	def cancelAll(self):
		'delete the lines with 127.0.0.1'
		a = open('/etc/hosts', 'r')
		b = open('testTemp.txt', 'w')
		for line in a.readlines():
			if "127.0.0.1" not in line or "localhost" in line:
				b.write(line)
		
		a.close()
		b.close()
		b = open('testTemp.txt', 'r')
		temp = b.read()
		a = open('/etc/hosts', 'w')
		a.truncate()
		a.write(temp)
		a.close()

		self.text.setPlainText("")
		os.remove('testTemp.txt')
# -------------------------------------------------------
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = dialog()
	main.show()
	sys.exit(app.exec_())