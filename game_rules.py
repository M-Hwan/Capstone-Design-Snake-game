# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_rules1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# 주연 (창 연결, 디자인 추가)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rules(object):

    def game_start_btn(self):
        #MainWindow.close()
        import snake
        #MainWindow.hide()
        print('뱀 게임 시작')
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1139, 806)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 이미지 label 설정
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(2, 0, 1135, 650))
        self.label.setPixmap(QtGui.QPixmap("images/game_rules.png"))
        self.label.setScaledContents(True)
        #self.label.setWordWrap(False)
        #self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")

        # 게임 시작 버튼 설정
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 670, 291, 71))
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily('맑은 고딕')
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
        '''
        QPushButton { color:white; background:rgb(255, 208, 20);
        border:5px solid rgb(255, 227, 111); border-style:outset}
        QPushButton:hover { color: rgb(59,42,127)}
        '''
        )

        #self.pushButton.raise_()
        #self.label.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1139, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        
        # 게임 시작 버튼 이벤트 핸들러
        self.pushButton.clicked.connect(self.game_start_btn)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "게임 시작하기"))
        self.menu.setTitle(_translate("MainWindow", "파일"))
        self.menu_2.setTitle(_translate("MainWindow", "보기"))
        self.menu_3.setTitle(_translate("MainWindow", "도움말"))
        self.action.setText(_translate("MainWindow", "다시하기"))



if __name__ == "__main__":
    import sys
    libpaths = QtWidgets.QApplication.libraryPaths() #추가
    libpaths.append("C:\\Users\사용자\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\PyQt5\Qt\plugins")
    QtWidgets.QApplication.setLibraryPaths(libpaths)
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Rules()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
