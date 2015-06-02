#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import datetime


class Oz(QtGui.QWidget):
	"""This is the main class for Oz"""
	def __init__(self):
		super(Oz, self).__init__()
		
		self.initUI()


	def initUI(self):

		self.addWidgets()
		self.calculateScore()

		self.center()
		self.resize(400, 300)
		self.setWindowTitle('Oz')
		self.show()

	def addWidgets(self):

		self.examTypeLbl = QtGui.QLabel('Exam Type:', self)
		
		self.kCetRBtn= QtGui.QRadioButton('K-CET', self)
		self.kCetRBtn.pressed.connect(self.getExamType)
		self.kCetRBtn.click()

		self.jMainsRBtn = QtGui.QRadioButton('Jee-Mains', self)
		self.jMainsRBtn.pressed.connect(self.getExamType)

		self.subjectRBtn = QtGui.QRadioButton('Subjective', self)
		self.subjectRBtn.pressed.connect(self.getExamType)


		self.enterMarksLbl = QtGui.QLabel('Enter Your Marks:', self)

		self.dateLbl = QtGui.QLabel('Date')
		self.dateSelectField = QtGui.QDateEdit(self)
		self.dateSelectField.setDateTime(QtCore.QDateTime.currentDateTime())

		self.rankLbl = QtGui.QLabel('Rank', self)
		self.rankLnEd = QtGui.QLineEdit(self)

		self.mathLbl = QtGui.QLabel('Mathematics', self)
		self.mathLnEd = QtGui.QLineEdit(self)
		self.mathLnEd.textChanged.connect(self.calculateScore)

		self.phyLbl = QtGui.QLabel('Physics', self)
		self.phyLnEd = QtGui.QLineEdit(self)
		self.phyLnEd.textChanged.connect(self.calculateScore)

		self.chemLbl = QtGui.QLabel('Chemistry', self)
		self.chemLnEd = QtGui.QLineEdit(self)
		self.chemLnEd.textChanged.connect(self.calculateScore)

		self.totalLbl = QtGui.QLabel('Total: ', self)
		self.marksCalculated = QtGui.QLabel('', self)

		self.perLbl = QtGui.QLabel('Percentage: ', self)
		self.perCalculated = QtGui.QLabel('', self)

		self.submitButton = QtGui.QPushButton('Submit', self)

		radioBtnGroup = QtGui.QHBoxLayout()
		radioBtnGroup.addWidget(self.kCetRBtn)
		radioBtnGroup.addWidget(self.jMainsRBtn)
		radioBtnGroup.addWidget(self.subjectRBtn)

		dateInput = QtGui.QHBoxLayout()
		dateInput.addWidget(self.dateLbl)
		dateInput.addWidget(self.dateSelectField) 

		rankInput = QtGui.QHBoxLayout()
		rankInput.addWidget(self.rankLbl, 1)
		rankInput.addWidget(self.rankLnEd, 1)

		mathInput = QtGui.QHBoxLayout()
		mathInput.addWidget(self.mathLbl, 1)
		mathInput.addWidget(self.mathLnEd, 1)

		phyInput = QtGui.QHBoxLayout()
		phyInput.addWidget(self.phyLbl, 1)
		phyInput.addWidget(self.phyLnEd, 1)

		chemInput = QtGui.QHBoxLayout()
		chemInput.addWidget(self.chemLbl, 1)
		chemInput.addWidget(self.chemLnEd, 1)

		totalOutput = QtGui.QHBoxLayout()
		totalOutput.addWidget(self.totalLbl)
		totalOutput.addWidget(self.marksCalculated)

		percentageOutput = QtGui.QHBoxLayout()
		percentageOutput.addWidget(self.perLbl)
		percentageOutput.addWidget(self.perCalculated)


		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addWidget(self.examTypeLbl)
		mainLayout.addLayout(radioBtnGroup)
		mainLayout.addWidget(self.enterMarksLbl)
		mainLayout.addLayout(dateInput)
		mainLayout.addLayout(rankInput)
		mainLayout.addLayout(mathInput)
		mainLayout.addLayout(phyInput)
		mainLayout.addLayout(chemInput)
		mainLayout.addLayout(totalOutput)
		mainLayout.addLayout(percentageOutput)
		mainLayout.addWidget(self.submitButton)
		mainLayout.addSpacing(15)

		self.setLayout(mainLayout)



	
	def center(self):
		windowScreen = self.frameGeometry()
		center = QtGui.QDesktopWidget().availableGeometry().center()
		windowScreen.moveCenter(center)
		self.move(windowScreen.topLeft())

	def getExamType(self):
		clickedButton = self.sender()
		self.examType = str(clickedButton.text())
		print self.examType

		

	def calculateScore(self):
		mathMarks = float(self.mathLnEd.text() + '.0')
		phyMarks = float(self.phyLnEd.text() + '.0')
		chemMarks = float(self.chemLnEd.text() + '.0')

		self.total = mathMarks + phyMarks + chemMarks
		self.marksCalculated.setText(str(self.total))

		self.examTotal = self.getTotalMarks()
		
		self.percentage = (self.total / float(self.examTotal)) * 100
		self.perCalculated.setText(str(self.percentage) + '%')



	def getTotalMarks(self):
		if self.examType.upper() == 'k-cet'.upper():
			return 180
		elif self.examType.upper() == 'jee-mains'.upper():
			return 360
		else:
			return 80

		



def main():

	app = QtGui.QApplication(sys.argv)
	oz = Oz()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

		