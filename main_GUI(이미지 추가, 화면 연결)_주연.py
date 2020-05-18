# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# 이주연
# 게임 로고 이미지 추가, 창 연결

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from login_GUI import *
from score_1_GUI import *

class Ui_MainWindow(object):

    def loginButtonClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window)
        self.window.show()

    def rankButtonClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Score()
        self.ui.setupUi(self.window)
        self.window.show()
    '''
    def methodButtonClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_
    '''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 889, 770))
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        
        # 로그인 버튼
        self.btn_login = QtWidgets.QPushButton(self.page)
        self.btn_login.setGeometry(QtCore.QRect(250, 570, 400, 70))
        self.btn_login.setObjectName("btn_login")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily('맑은 고딕')
        font.setBold(True)
        self.btn_login.setFont(font)
        #self.btn_login.setStyleSheet('color:white;background:rgb(170, 170, 255);border: 5px solid rgb(212, 214, 255);border-style:outset')
        #self.btn_login.setStyleSheet('color:white;background:rgb(85, 170, 0);border: 5px solid rgb(170, 255, 127);border-style:outset')
        #self.btn_login.setStyleSheet('color:white;background:rgb(255, 208, 20);border: 5px solid rgb(255, 227, 111);border-style:outset')
        #self.btn_login.setStyleSheet('color:white;background:rgb(59, 42, 127);border: 5px solid rgb(59,42,217);border-style:outset')
        self.btn_login.setStyleSheet(
        '''
        QPushButton { color: white; background: rgb(255,208,20); border: 5px solid rgb(255,227,111); border-style:outset}
        QPushButton:hover{ color: rgb(59,42,127)}
        ''')
        
        #self.btn_login.setStyleSheet('color:white;background:rgb(59, 42, 127);border: 5px solid rgb(59,42,217);border-style:outset')
      
        # 랭킹 확인 버튼
        self.btn_rank = QtWidgets.QPushButton(self.page)
        self.btn_rank.setGeometry(QtCore.QRect(250, 660, 400, 70))
        self.btn_rank.setObjectName("btn_rank")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily('맑은 고딕')
        font.setBold(True)
        self.btn_rank.setFont(font)
        #self.btn_rank.setStyleSheet('color:white;background:rgb(170, 170, 255);border: 5px solid rgb(170, 170, 255);border-style:outset')
        #self.btn_rank.setStyleSheet('color:white;background:rgb(85, 170, 0);border: 5px solid rgb(177, 177, 160);border-style:outset')
        #self.btn_rank.setStyleSheet('color:white;background:rgb(255, 208, 20);border: 5px solid rgb(177, 177, 160);border-style:outset')
        #self.btn_rank.setStyleSheet('color:white;background:rgb(59, 42, 127);border: 5px solid rgb(177, 177, 160);border-style:outset')
        self.btn_rank.setStyleSheet(
        '''
        QPushButton { color:white;background:rgb(59, 42, 127);border: 5px solid rgb(177, 177, 160);border-style:outset}
        QPushButton:hover{ color: rgb(255,208,20)}
        ''')
        
        # 이미지 삽입
        self.lbl_startPicture = QtWidgets.QLabel(self.page)
        self.lbl_startPicture.setGeometry(QtCore.QRect(100, 50, 680, 510))
        self.lbl_startPicture.setPixmap(QPixmap("images/game_logo.png"))
        self.lbl_startPicture.setScaledContents(True)
        self.lbl_startPicture.show()
        self.lbl_startPicture.setObjectName("lbl_startPicture")
        
        # stackedWidget 설정
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        #------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 로그인 버튼/랭킹 점수판 확인 버튼 클릭 시, 이벤트 설정
        self.btn_login.clicked.connect(self.loginButtonClicked)
        self.btn_rank.clicked.connect(self.rankButtonClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_login.setText(_translate("MainWindow", "카카오톡 계정으로 로그인"))
        self.btn_rank.setText(_translate("MainWindow", "현재 랭킹 확인하기"))
        
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
