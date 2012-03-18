# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore

class AbstractTab(QtGui.QWidget):
    """klasa bazowa dla każdej z zakładek aplikacji"""
    def __init__(self,parent=None):
         QtGui.QWidget.__init__(self,parent)
         self.initUi()
    def initUi(self):
        
        
        self.horizontalLayout = QtGui.QHBoxLayout(self)
        """Każdą zakładkę dzielimy jak na razie na 3 obszary: opcje,
        listy , wykresy """
        
        """Ramka przechowujaca listy"""
        self.listsFrame = QtGui.QFrame(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
        QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listsFrame.sizePolicy().hasHeightForWidth())
        self.listsFrame.setSizePolicy(sizePolicy)
        # ustawimy maksymalna szerokosc kolumny na 350
        self.listsFrame.setMaximumSize(QtCore.QSize(350, 16777215))
        self.listsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.listsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.listsFrame.setLineWidth(3)
        self.horizontalLayout.addWidget(self.listsFrame)

        #ustawiamy zarządce rozkładu vertical
        self.listsLayout = QtGui.QVBoxLayout(self.listsFrame)
        
        # Tool Box przechowujący listy
        self.listsToolBox = QtGui.QToolBox(self.listsFrame)

        #Index
        self.indexPage = QtGui.QWidget(self.listsFrame)
        self.indexPageLayout = QtGui.QHBoxLayout(self.indexPage)
        self.listsToolBox.addItem(self.indexPage, "Index")
        self.indexListView = QtGui.QTableView(self.listsFrame)
        self.tableStyle(self.indexListView) #ustawiamy styl tabeli
        self.indexPageLayout.addWidget(self.indexListView)
        

        #Stock
        self.stockPage = QtGui.QWidget(self.listsFrame)
        self.stockPageLayout = QtGui.QHBoxLayout(self.stockPage)
        self.listsToolBox.addItem(self.stockPage , "Stock")
        self.stockListView = QtGui.QTableView(self.listsFrame)
        self.tableStyle(self.stockListView)#ustawiamy styl tabeli
        self.stockPageLayout.addWidget(self.stockListView)

        #forex
        self.forexPage = QtGui.QWidget(self.listsFrame)
        self.forexPageLayout = QtGui.QHBoxLayout(self.forexPage)
        self.listsToolBox.addItem(self.forexPage, "Forex")
        self.forexListView = QtGui.QTableView(self.listsFrame)
        self.tableStyle(self.forexListView)#ustawiamy styl tabeli
        self.forexPageLayout.addWidget(self.forexListView)

        #Bond
        self.bondPage = QtGui.QWidget(self.listsFrame)
        self.bondPageLayout = QtGui.QHBoxLayout(self.bondPage)
        self.listsToolBox.addItem(self.bondPage, "Bond")
        self.bondListView = QtGui.QTableView(self.listsFrame)
        self.tableStyle(self.bondListView)
        self.bondPageLayout.addWidget(self.bondListView)


        #Commodity
        self.commodityPage = QtGui.QWidget(self.listsFrame)
        self.commodityPageLayout = QtGui.QHBoxLayout(self.commodityPage)
        self.listsToolBox.addItem(self.commodityPage, "Commodity")
        self.commodityListView = QtGui.QTableView(self.listsFrame)
        self.tableStyle(self.commodityListView)
        self.commodityPageLayout.addWidget(self.commodityListView)

        #Futures contract
        self.futuresContractPage = QtGui.QWidget(self.listsFrame)
        self.futuresContractPageLayout = QtGui.QHBoxLayout(self.futuresContractPage)
        self.listsToolBox.addItem(self.futuresContractPage, "Futures Contract")
        self.futuresContractListView = QtGui.QTableView(self.listsFrame)
        self.tableStyle(self.futuresContractListView)
        self.futuresContractPageLayout.addWidget(self.futuresContractListView)
        
        self.listsLayout.addWidget(self.listsToolBox)
        # koniec Tool Box
        

        """Ramka przechowujaca opcje"""
        self.optionsFrame = QtGui.QFrame(self)
        sizePolicy2 = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
        QtGui.QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.optionsFrame.sizePolicy().hasHeightForWidth())
        self.optionsFrame.setSizePolicy(sizePolicy2)

        
        # ustawimy maksymalna szerokosc kolumny na 150
        self.optionsFrame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.optionsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.optionsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.optionsFrame.setLineWidth(3)
        self.horizontalLayout.addWidget(self.optionsFrame)

        #ustawiamy zarządce rozkładu vertical
        self.optionsLayout = QtGui.QVBoxLayout(self.optionsFrame)
        
        #pola do wprowadzania okresu
        self.label = QtGui.QLabel('Range:',self.optionsFrame) 
        self.optionsLayout.addWidget(self.label)
        self.startDateEdit = QtGui.QDateEdit(self.optionsFrame)
        self.optionsLayout.addWidget(self.startDateEdit)
        self.endDateEdit = QtGui.QDateEdit(self.optionsFrame)
        self.optionsLayout.addWidget(self.endDateEdit)
        #koniec pola do wprowadzania okresu
			
	                
        """Ramka przechowujaca wykresy"""
        self.chartsFrame = QtGui.QFrame(self)
        sizePolicy3 = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
        QtGui.QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.chartsFrame.sizePolicy().hasHeightForWidth())
        self.chartsFrame.setSizePolicy(sizePolicy3)
        self.chartsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.chartsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.chartsFrame.setLineWidth(3)
        self.horizontalLayout.addWidget(self.chartsFrame)
        #ustawiamy zarządce rozkładu vertical
        self.chartsLayout = QtGui.QVBoxLayout(self.chartsFrame)

    def addChartButton(self):
        # Step combo box
        self.stepLabel = QtGui.QLabel('Step',self.optionsFrame)#label Step
        self.optionsLayout.addWidget(self.stepLabel)
        self.stepComboBox = QtGui.QComboBox(self.optionsFrame)
        self.stepComboBox.addItem('daily')
        self.stepComboBox.addItem('weekly')
        self.stepComboBox.addItem('monthly')
        self.optionsLayout.addWidget(self.stepComboBox)
        # chartType comboBox
        self.chartTypeLabel = QtGui.QLabel('Chart Type',self.optionsFrame)#label Chart Type
        self.optionsLayout.addWidget(self.chartTypeLabel)
        self.chartTypeComboBox = QtGui.QComboBox(self.optionsFrame)
        self.chartTypeComboBox.addItem('line')
        self.chartTypeComboBox.addItem('point')
        self.chartTypeComboBox.addItem('candlestick')
        self.optionsLayout.addWidget(self.chartTypeComboBox)
        # Scale Type
        self.scaleTypeLabel = QtGui.QLabel('Scale',self.optionsFrame)
        self.optionsLayout.addWidget(self.scaleTypeLabel)
        self.linearRadioButton = QtGui.QRadioButton('linear',self.optionsFrame)
        self.optionsLayout.addWidget(self.linearRadioButton)
        self.logRadioButton = QtGui.QRadioButton('log',self.optionsFrame)
        self.optionsLayout.addWidget(self.logRadioButton)
        #wyłaczenie voluminu
        self.volumenCheckBox = QtGui.QCheckBox('Hide Volumen',self.optionsFrame)
        self.optionsLayout.addWidget(self.volumenCheckBox)
        #wlacznie możliwości rysowania na wykeresie
        self.paintCheckBox = QtGui.QCheckBox('Enable painting',self.optionsFrame)
        self.optionsLayout.addWidget(self.paintCheckBox)
        #przycisk rysowania wykresu
        self.chartButton = QtGui.QPushButton('Chart',self.optionsFrame)
        self.chartButton.resize(self.chartButton.sizeHint())
        self.optionsLayout.addWidget(self.chartButton)
	#Spacer
        self.spacer = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, 		QtGui.QSizePolicy.Expanding)
        self.optionsLayout.addItem(self.spacer)
       
    def tableStyle(self,table):
        # hide grid
        table.setShowGrid(False)
        # set the font
        font = QtGui.QFont("Courier New", 10)
        table.setFont(font)
        # hide vertical header
        vh = table.verticalHeader()
        vh.setVisible(False)
        # set column width to fit contents
        table.resizeColumnsToContents()
        # set horizontal header properties
        hh = table.horizontalHeader()
        hh.setStretchLastSection(True)
        
        # enable sorting
        table.setSortingEnabled(True)


        
                
        
        
         
    
