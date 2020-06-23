# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_rules1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# 주연 (창 연결, 디자인 추가)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor, QIcon, QColor

class Ui_Rules(object):

    def game_start_btn(self):
        #MainWindow.close()
        import snake
        #MainWindow.hide()
        print('뱀 게임 시작')

    def setupUi(self, MainWindow):
        # 윈도우 아이콘 설정
        MainWindow.setWindowIcon(QIcon('images\game_logo.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1137, 920)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setStyleSheet(
        '''
        background-image: url(images/back.png);
        background-repeat: no-repeat;
        '''
        )
        # 이미지 label 설정
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(2, 10, 1135, 732))
        self.label.setPixmap(QtGui.QPixmap("images/game_rules.png"))
        self.label.setScaledContents(True)
        self.label.setStyleSheet(
        '''
        background: white;
        '''
        )
        #self.label.setWordWrap(False)
        #self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")

        # 게임 시작 버튼 설정
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 750, 330, 80))
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily('맑은 고딕')
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
        '''
        QPushButton { color:white; background:rgb(255, 208, 20);
        border:5px solid rgb(255, 227, 111); border-style:outset;
        border-radius: 25px;}
        QPushButton:hover { color: rgb(59,42,127);}
        '''
        )
        # 마우스 포인터 변경
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        
        #self.pushButton.raise_()
        #self.label.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        # 게임 시작 버튼 이벤트 핸들러
        self.pushButton.clicked.connect(self.game_start_btn)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "게임 조작법"))
        self.pushButton.setText(_translate("MainWindow", "게임 시작하기"))

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
