# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'photoadded.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import educorpus_kr
from score_2_GUI import *

class Ui_MainWindow(object):

    def rankButtonClicked(self):
        #MainWindow.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Score()
        self.ui.setupUi(self.window)
        self.window.show()
        return
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 780, 550)) #사진파일이 표시되는 라벨박스(사진크기보다 약간 더 여유있게)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 175, 400, 500)) #말뭉치 글박스(좌표x축,y축,너비,높이)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.backgroundIMG = QPixmap() #label이용해 배경 사진 첨부
        self.backgroundIMG.load("images/상식Up.png") #사진파일 경로 
        self.backgroundIMG = self.backgroundIMG.scaled(770,530) #사진크기
        self.label.setPixmap(self.backgroundIMG)

        palette = QtGui.QPalette() #말뭉치 글박스 배경 투명도0%로 배경색 제거
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 16, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        self.textEdit.setPalette(palette)

        self.btn_krpsToRank = QtWidgets.QPushButton(self.centralwidget) #말뭉치에서 랭킹판으로 이동하는 버튼
        self.btn_krpsToRank.setGeometry(QtCore.QRect(330, 470, 161, 41)) #버튼은 중앙 하단에 위치
        font = QtGui.QFont()
        font.setFamily("맑은 고딕") #GUI에 등장하는 버튼마다 디자인 통일감
        font.setPointSize(15)
        font.setBold(True)
        self.btn_krpsToRank.setFont(font)
        #self.btn_krpsToRank.setStyleSheet('color:white;background:rgb(170, 170, 255);border: 5px solid rgb(170, 170, 255);border-style:outset')
        #self.btn_krpsToRank.setStyleSheet('color:white;background:rgb(85, 170, 0);border: 5px solid rgb(177, 177, 160);border-style:outset')
        #self.btn_krpsToRank.setStyleSheet('color:white;background:rgb(255, 208, 20);border: 5px solid rgb(177, 177, 160);border-style:outset')
        #self.btn_krpsToRank.setStyleSheet('color:white;background:rgb(59, 42, 127);border: 5px solid rgb(177, 177, 160);border-style:outset')
        self.btn_krpsToRank.setStyleSheet(
        '''
        QPushButton { color:white;background:rgb(59, 42, 127);border: 5px solid rgb(177, 177, 160);border-style:outset}
        QPushButton:hover{ color: rgb(255,208,20)}
        ''')
        self.btn_krpsToRank.setObjectName("btn_krpsToRank")
        # 이벤트 핸들러(점수판 확인)
        self.btn_krpsToRank.clicked.connect(self.rankButtonClicked)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        font = QFont("맑은 고딕", 15) #말뭉치 폰트 종류, 사이즈 지정 #헤드라인A #맑은 고딕
        #colorVar = QColor(Red, Green, Blue, 투명도) #글씨색깔 0~255로 조절
        color = QColor(30,30,30,255) #검정,투명도100%
        self.textEdit.setCurrentFont(font)
        self.textEdit.setTextColor(color)
        _translate = QtCore.QCoreApplication.translate
        krps = educorpus_kr.edukrps() #말뭉치.py의 리턴값 krps 
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ""))
        self.textEdit.setText(krps) #krps에 들어간 랜덤한 상식문장 한 개를 textEdit 박스에 넣어줌.
        self.btn_krpsToRank.setText(_translate("MainWindow", "랭킹판 확인"))

if __name__ == "__main__":
    import sys
    libpaths = QtWidgets.QApplication.libraryPaths() #추가
    libpaths.append("C:\\Users\사용자\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\PyQt5\Qt\plugins")
    QtWidgets.QApplication.setLibraryPaths(libpaths)
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
