# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Python\GUI\ui_elements\delete_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteItem(object):
    def setupUi(self, DeleteItem):
        DeleteItem.setObjectName("DeleteItem")
        DeleteItem.resize(400, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeleteItem.sizePolicy().hasHeightForWidth())
        DeleteItem.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(DeleteItem)
        self.centralwidget.setObjectName("centralwidget")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(10, 160, 101, 21))
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(280, 160, 101, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel.sizePolicy().hasHeightForWidth())
        self.cancel.setSizePolicy(sizePolicy)
        self.cancel.setObjectName("cancel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 451, 51))
        self.label.setObjectName("label")
        DeleteItem.setCentralWidget(self.centralwidget)

        self.retranslateUi(DeleteItem)
        QtCore.QMetaObject.connectSlotsByName(DeleteItem)

    def retranslateUi(self, DeleteItem):
        _translate = QtCore.QCoreApplication.translate
        DeleteItem.setWindowTitle(_translate("DeleteItem", "MainWindow"))
        self.ok.setText(_translate("DeleteItem", "OK"))
        self.cancel.setText(_translate("DeleteItem", "Cancel"))
        self.label.setText(_translate("DeleteItem", "TextLabel"))
