# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.widget = QtWidgets.QWidget(parent=Widget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(600, 70))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text")
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("margin-bottom:10px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(105, 400))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueCyr")
        font.setPointSize(-1)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: red;\n"
"font-size: 151px;\n"
"padding:0;")
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(700, 400))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueCyr")
        font.setPointSize(-1)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color:white;\n"
"font-size: 70px;\n"
"padding: 58px 0 0 -10px;\n"
"")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("margin-bottom:10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("margin-bottom:10px;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        #self.pushButton_3.clicked.connect(list_func)
        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "YaDISK"))
        self.pushButton_3.setText(_translate("Widget", "Список всех файлов"))

        self.label_2.setText(_translate("Widget", "Y"))
        self.label.setText(_translate("Widget", "andex DISK "))
        self.pushButton_2.setText(_translate("Widget", "Загрузить файл на диск"))
        self.pushButton.setText(_translate("Widget", "Сохранить файл с диска"))
