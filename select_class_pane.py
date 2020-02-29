# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_class_pane.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(458, 455)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 420, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 50, 72, 15))
        self.label_2.setObjectName("label_2")
        self.select_class_btn = QtWidgets.QPushButton(Form)
        self.select_class_btn.setGeometry(QtCore.QRect(140, 350, 181, 51))
        self.select_class_btn.setObjectName("select_class_btn")
        self.kch = QtWidgets.QLineEdit(Form)
        self.kch.setGeometry(QtCore.QRect(90, 110, 281, 61))
        self.kch.setObjectName("kch")
        self.kxh = QtWidgets.QLineEdit(Form)
        self.kxh.setGeometry(QtCore.QRect(90, 190, 281, 61))
        self.kxh.setObjectName("kxh")
        self.kxh_2 = QtWidgets.QLineEdit(Form)
        self.kxh_2.setGeometry(QtCore.QRect(90, 270, 281, 61))
        self.kxh_2.setObjectName("kxh_2")

        self.retranslateUi(Form)
        self.select_class_btn.clicked.connect(Form.auto_select_class)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Designed by RJY"))
        self.label_2.setText(_translate("Form", "选课界面"))
        self.select_class_btn.setText(_translate("Form", "开始抢课"))
        self.kch.setPlaceholderText(_translate("Form", "请输入课程号"))
        self.kxh.setPlaceholderText(_translate("Form", "请输入课序号"))
        self.kxh_2.setPlaceholderText(_translate("Form", "请输入您的邮箱以便在抢课成功后通知您"))

