
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#from newlabel import Ui_NewLabel
#
# from newcircuit import Ui_NewCircuit
from form import Ui_Form

class Ui_MainWindow(object):
	def __init__(self,MainWindow, parent=None):
		#super(Ui_MainWindow, self).__init__(parent)
		object.__init__(parent)

		#self.setupUi()
		
	#def setupUi(self):
		#object.__init__(parent)
		#self.lineTable = lineTable
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(510, 507)
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
		self.verticalLayout.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout.setSpacing(6)
		self.verticalLayout.setObjectName("verticalLayout")
		self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
		self.tabWidget.setObjectName("tabWidget")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
		self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout_2.setSpacing(6)
		self.verticalLayout_2.setObjectName("verticalLayout_2")

		form = Ui_Form(self)
		#self.tabWidget.addTab(form, "Page 1")

		self.verticalLayout.addWidget(self.tabWidget)
		MainWindow.setCentralWidget(self.centralWidget)
		self.menuBar = QtWidgets.QMenuBar(MainWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 510, 22))
		self.menuBar.setObjectName("menuBar")
		MainWindow.setMenuBar(self.menuBar)
		#self.mainToolBar = QtWidgets.QToolBar(MainWindow)
		#self.mainToolBar.setObjectName("mainToolBar")
		#MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
		self.statusBar = QtWidgets.QStatusBar(MainWindow)
		self.statusBar.setObjectName("statusBar")
		MainWindow.setStatusBar(self.statusBar)

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		MainWindow.showEvent = self.showEvent
		MainWindow.closeEvent = self.closeEvent
		#self.tableWidget.mousePressEvent = self.mousePressEvent

		self.mylist = list()
		self.mylabel = list()

		self.columns = list()
		self.rows = list()
		
		self.tempCut = list()
		self.newCut = list()

		self.tmplist = list() 
		self.comp1 = list()
		self.comp2 = list()

		self.maxTabs = list()	#lista, se guarda valores de tabs 
		self.tempTabsList = list()
		self.tempTabsLabel =list()

		self.tempVal = list()
		self.tempColumns = list()
		self.tempRows = list()

		self.valCut = False
		self.i = 0
		self.flagLabel = False
		self.flagOverLabel = False
		self.flagOverList = False

		self.flagEmpty = False

		self.editDelete = False 
		self.secondEdit = False
		self.flagEdit = False

		self.flagSave = False
		self.flagExit = False

		self.newtb.triggered.connect(self.newPage)
		self.savetb.triggered.connect(self.saveLayout)
		self.deletetb.triggered.connect(self.deletePage)
		self.exittb.triggered.connect(self.exitLayout)

		#self.tabWidget.tabBarClicked.connect(self.prueba)
		self.MainWindow = MainWindow

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Layout Editor"))
		##MainWindow.setWindowIcon(QtGui.QIcon('opt/Ditsa/DitsaNetEditor/LayoutEditor.png'))
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

		self.newtb = QtWidgets.QAction(QtGui.QIcon('image/nuevo.png'),'New',MainWindow)
		self.savetb = QtWidgets.QAction(QtGui.QIcon('image/guardar.png'),'Save',MainWindow)
		self.deletetb = QtWidgets.QAction(QtGui.QIcon('image/borrar.png'),'Delete',MainWindow)
		self.exittb = QtWidgets.QAction(QtGui.QIcon('image/salir.png'),'Exit',MainWindow)

		self.toolB = MainWindow.addToolBar('ToolBar')
		
		self.rbCM = QtWidgets.QRadioButton('Circuit Mode')
		self.rbLM = QtWidgets.QRadioButton('Label Mode')
		self.rbCM.setChecked(True)
		self.rbLM.setChecked(False)

		self.toolB.addWidget(self.rbCM)
		self.toolB.addWidget(self.rbLM)
		self.toolB.addAction(self.newtb)
		self.toolB.addAction(self.savetb)
		self.toolB.addAction(self.deletetb)
		self.toolB.addAction(self.exittb)

		#self.popMenu = QtGui.QMenu(self) 
		#self.popMenu.addSeparator() 
		#self.popMenu.addAction(QtGui.QAction('test2', self)) 

	def showEvent(self,event):
		print("ShowEvent") #None aplica cuando no hay settings # [] indica que hay settings pero esa lista no tiene algun dato
		settings = QtCore.QSettings('Settings/archivo.ini', QtCore.QSettings.NativeFormat)
		if settings.value('Settings/archivo.ini')!='':
			self.settingsList = settings.value("mylist")
			self.settingsLabel = settings.value("mylabel")
			self.settingsColumns = settings.value("columns")
			self.settingsRows = settings.value("rows")

			if self.settingsColumns != None and len(self.settingsColumns) != 0:
				self.columns = self.settingsColumns[:]
			else:
				self.columns.append('1%')
				self.columns.append('6')

			if self.settingsRows != None and len(self.settingsRows) != 0:
				self.rows = self.settingsRows[:]
			else:
				self.rows.append('1%')
				self.rows.append('6')

			if self.settingsList != None:
				self.mylist = self.settingsList[:] #para que no se corresponden con el mismo objeto
	
			if self.settingsLabel != None:
				self.mylabel = self.settingsLabel[:] #para que no se corresponden con el mismo objeto

			if self.settingsList != None or self.settingsLabel != None:
				self.populateTabs()
		
			form = Ui_Form(self)
			self.tabWidget.addTab(form, "Page 1")
			#self.newPage()
			tabC = self.tabWidget.count()
			#print("tabC:",tabC)

			if (self.settingsList != None  and len(self.settingsList)!=0) or (self.settingsLabel != None and len(self.settingsLabel)!=0):
				for i in range(int(self.numTabT)-tabC):
					#print("i",i)
					self.newPage()

	def closeEvent(self,event): 
		print("CloseEvent")
		if (len(self.mylist) != 0 or len(self.mylabel) != 0) and self.flagSave != True: 
			if self.flagExit != True:
				if self.settingsList != self.mylist or self.settingsLabel != self.mylabel:
					print("se han hecho cambios y no se ha guardado")
					msgExit = QtWidgets.QMessageBox()
					returnExit = msgExit.warning(self.MainWindow,'Warning','Do you want to save changes?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel)
					if returnExit == msgExit.Yes:
						self.saveLayout()
						MainWindow.close()
					if returnExit == msgExit.No:
						MainWindow.close()
					if returnExit == msgExit.Cancel:
						event.ignore()
				else:
					MainWindow.close()
		else:
			MainWindow.close()

	def populateTabs(self):
		print("populateTabs")
		for i in range(0,len(self.settingsList),4):
			self.maxTabs.append(self.settingsList[i])

		for i in range(0,len(self.settingsLabel),3):
			self.maxTabs.append(self.settingsLabel[i])

		if len(self.maxTabs)!= 0:
			print("max")
			y = max(self.maxTabs)
			self.numTabT = y.replace('%','')
			#print(self.numTabT)
			self.maxTabs.clear()

	def newPage(self): 
		#print("newPage")
		form = Ui_Form(self)
		self.tabWidget.addTab(form,"Page "+str(self.tabWidget.count()+1))

	def saveLayout(self): ##verificar 
		if len(self.mylist) != None or len(self.mylabel) != None:
			self.flagSave = True
			print("Save")
			settings = QtCore.QSettings('Settings/archivo.ini', QtCore.QSettings.NativeFormat)
			settings.setValue("mylist",self.mylist)
			settings.setValue("mylabel",self.mylabel)
			settings.setValue("columns",self.columns)
			settings.setValue("rows",self.rows)
			print("S1:",self.columns)
			print("S2:",self.rows)

	flagDelete = False
	def deletePage(self): #borrar y actualizar valores de tabs
		print("DeletePage")
		y = self.tabWidget.count()
		print("C:",self.columns)
		print("R:",self.rows)
		#print("actual:",y)
		if y == 1:
			msgTab = QtWidgets.QMessageBox()
			msgTab.critical(self.MainWindow,'Error','You do not delete to current Tab')
		else:
			x = self.tabWidget.currentIndex()
			print("index:",x)

			dif = y - x
			#print("dif:",dif)
			for k in range(0,dif+1):
				#print("k:",k)
				j = k + 1
				#print("x+k",x+k)
				print("x+j:",x+j)
				self.tabWidget.setTabText(x+j,"Page "+str(x+j))

				for i in range(0,len(self.mylist)-1,4):
					#if self.mylist[i] == '0'+str(x+1)+'%':
					#	self.tempCut.append(self.mylist[i]+self.mylist[i+1]+'/'+self.mylist[i+2]+"\n"+self.mylist[i+3])
					if self.mylist[i] == str(x+j)+'%':
						#print("cambia valor tabList")
						self.flagDelete = True
						self.tempCut.append(self.mylist[i]+self.mylist[i+1]+'/'+self.mylist[i+2]+"\n"+self.mylist[i+3])
						if k != 0:
							self.tempTabsList.append(self.mylist[i])
							self.tempTabsList.append(self.mylist[i+1])
							self.tempTabsList.append(self.mylist[i+2])
							self.tempTabsList.append(self.mylist[i+3])

				for i in range(0,len(self.mylabel)-1,3):
					if self.mylabel[i] == str(x+j)+'%': #x+2
						self.flagDelete = True
						self.tempCut.append(self.mylabel[i]+self.mylabel[i+1]+'/'+self.mylabel[i+2])
						if k != 0:
							self.tempTabsLabel.append(self.mylabel[i])
							self.tempTabsLabel.append(self.mylabel[i+1])
							self.tempTabsLabel.append(self.mylabel[i+2])

				for i in range(0,len(self.columns),2):
					if self.columns[i] == str(x+j)+'%':
						if k!=0:
							self.tempColumns.append(self.columns[i])
							self.tempColumns.append(self.columns[i+1])


				for i in range(0,len(self.rows),2):
					if self.rows[i] == str(x+j)+'%':
						if k!=0:
							self.tempRows.append(self.rows[i])
							self.tempRows.append(self.rows[i+1])

			self.rows.clear()
			self.columns.clear()
			self.cleanMylist()
			self.tempCut.clear()

			if self.flagDelete != False:
				self.flagDelete = False
				#print("TempTabslist:",self.tempTabsList)
				#print("TempTabslabel:",self.tempTabsLabel)
				
				for k in range(0,dif):
					#print("k2:",k)
					j = k + 1
					df = x+j
					#print("2x+j:",x+j)
					
					for i in range(0,len(self.tempTabsList),4):
						if  self.tempTabsList[i] == str(x+j)+'%':
							self.mylist.append(str(df-1)+'%')
							self.mylist.append(self.tempTabsList[i+1])
							self.mylist.append(self.tempTabsList[i+2])
							self.mylist.append(self.tempTabsList[i+3])

					for i in range(0,len(self.tempTabsLabel),3):
						if  self.tempTabsLabel[i] == str(x+j)+'%':
							self.mylabel.append(str(df-1)+'%')
							self.mylabel.append(self.tempTabsLabel[i+1])
							self.mylabel.append(self.tempTabsLabel[i+2])

					for i in range(0,len(self.tempColumns),2):
						if self.tempColumns[i] == str(x+j)+'%':
							self.columns.append(str(df-1)+'%')
							self.columns.append(self.tempColumns[i+1])


					for i in range(0,len(self.tempRows),2):
						if self.tempRows[i] == str(x+j)+'%':
							self.rows.append(str(df-1)+'%')
							self.rows.append(self.tempRows[i+1])

			self.tempRows.clear()
			self.tempColumns.clear()
			self.tempTabsList.clear()
			self.tempTabsLabel.clear()
			self.tabWidget.removeTab(x)

			print("CCCC:",self.columns)
			print("xxx:",self.rows)
			#print("ListFinish:",self.mylist)
			#print("LabelFinish:",self.mylabel)

	def exitLayout(self):
		print("Exit") 
		if (len(self.mylist) != 0 or len(self.mylabel) != 0) and self.flagSave != True: 
			if self.settingsList != self.mylist or self.settingsLabel != self.mylabel:
				print("se han hecho cambios y no se ha guardado")
				msgExit = QtWidgets.QMessageBox()
				returnExit = msgExit.warning(self.MainWindow,'Warning','Do you want to save changes?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel)
				if returnExit == msgExit.Yes:
					self.saveLayout()
					MainWindow.close()
				if returnExit == msgExit.No:
					self.flagExit = True
					MainWindow.close()
			else:
				MainWindow.close()
		else:
			MainWindow.close()
		

	def cleanMylist(self): #clean mylist and mylabel
		print("CleanMylist")
		#print(self.tempCut)
		for i in range(len(self.tempCut)):
			value = self.tempCut[i].split("/")
			cmpValue = value[0].split("%")
			#print("cmpV:",cmpValue)
			#print("value:",value)
			for j in range(len(self.mylist)-1):
				if cmpValue[0]+'%' == self.mylist[j] and cmpValue[1] == self.mylist[j+1]:
					self.mylist.pop(j+3)
					self.mylist.pop(j+2)
					self.mylist.pop(j+1)
					self.mylist.pop(j) #se recorre un lugar a la izquierda
					break

			for k in range(len(self.mylabel)-1):
				if cmpValue[0]+'%' == self.mylabel[k] and cmpValue[1] == self.mylabel[k+1]:
					self.mylabel.pop(k+2)
					self.mylabel.pop(k+1)
					self.mylabel.pop(k) #se recorre un lugar a la izquierda
					break
		
		#print("ListClean:",self.mylist)
		#print("LabelClean:",self.mylabel)

	def cleanColumnRow(self):
		print("cleanColRow")
		for i in range(len(self.tempVal)):
			for j in range(len(self.columns)-1):
				if self.tempVal[i] == self.columns[j]:
					print("VV:",self.columns[j])
					self.columns.pop(j+1)
					self.columns.pop(j)
					break




if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	#ui = Ui_MainWindow()
	#ui.setupUi(MainWindow)
	#MainWindow.show()
	ui = Ui_MainWindow(MainWindow)
	#ui.__init__(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
