# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(506, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 50, 444, 194))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_One = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_One.setObjectName("btn_One")
        self.gridLayout.addWidget(self.btn_One, 4, 0, 1, 1)
        self.btn_Six = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Six.setObjectName("btn_Six")
        self.gridLayout.addWidget(self.btn_Six, 3, 2, 1, 1)
        self.btn_Seven = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Seven.setObjectName("btn_Seven")
        self.gridLayout.addWidget(self.btn_Seven, 2, 0, 1, 1)
        self.btn_Divide = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Divide.setObjectName("btn_Divide")
        self.gridLayout.addWidget(self.btn_Divide, 1, 3, 1, 1)
        self.btn_Five = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Five.setObjectName("btn_Five")
        self.gridLayout.addWidget(self.btn_Five, 3, 1, 1, 1)
        self.btn_Three = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Three.setObjectName("btn_Three")
        self.gridLayout.addWidget(self.btn_Three, 4, 2, 1, 1)
        self.btn_Nine = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Nine.setObjectName("btn_Nine")
        self.gridLayout.addWidget(self.btn_Nine, 2, 2, 1, 1)
        self.btn_Subtract = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Subtract.setObjectName("btn_Subtract")
        self.gridLayout.addWidget(self.btn_Subtract, 3, 3, 1, 1)
        self.btn_Percent = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Percent.setObjectName("btn_Percent")
        self.gridLayout.addWidget(self.btn_Percent, 1, 2, 1, 1)
        self.btn_Divide_2 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Divide_2.setObjectName("btn_Divide_2")
        self.gridLayout.addWidget(self.btn_Divide_2, 2, 3, 1, 1)
        self.btn_Add = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Add.setObjectName("btn_Add")
        self.gridLayout.addWidget(self.btn_Add, 4, 3, 1, 1)
        self.btn_Two = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Two.setObjectName("btn_Two")
        self.gridLayout.addWidget(self.btn_Two, 4, 1, 1, 1)
        self.btn_Four = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Four.setObjectName("btn_Four")
        self.gridLayout.addWidget(self.btn_Four, 3, 0, 1, 1)
        self.btn_PlusMinus = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_PlusMinus.setObjectName("btn_PlusMinus")
        self.gridLayout.addWidget(self.btn_PlusMinus, 1, 1, 1, 1)
        self.btn_Eight = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Eight.setObjectName("btn_Eight")
        self.gridLayout.addWidget(self.btn_Eight, 2, 1, 1, 1)
        self.le_WriteNum = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.le_WriteNum.setObjectName("le_WriteNum")
        self.gridLayout.addWidget(self.le_WriteNum, 0, 0, 1, 4)
        self.btn_Clear = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Clear.setObjectName("btn_Clear")
        self.gridLayout.addWidget(self.btn_Clear, 1, 0, 1, 1)
        self.btn_Equal = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Equal.setObjectName("btn_Equal")
        self.gridLayout.addWidget(self.btn_Equal, 5, 3, 1, 1)
        self.btn_Comma = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Comma.setObjectName("btn_Comma")
        self.gridLayout.addWidget(self.btn_Comma, 5, 2, 1, 1)
        self.btn_Zero = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_Zero.setObjectName("btn_Zero")
        self.gridLayout.addWidget(self.btn_Zero, 5, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_One.setText(_translate("Form", "1"))
        self.btn_Six.setText(_translate("Form", "6"))
        self.btn_Seven.setText(_translate("Form", "7"))
        self.btn_Divide.setText(_translate("Form", "/"))
        self.btn_Five.setText(_translate("Form", "5"))
        self.btn_Three.setText(_translate("Form", "3"))
        self.btn_Nine.setText(_translate("Form", "9"))
        self.btn_Subtract.setText(_translate("Form", "-"))
        self.btn_Percent.setText(_translate("Form", "%"))
        self.btn_Divide_2.setText(_translate("Form", "*"))
        self.btn_Add.setText(_translate("Form", "+"))
        self.btn_Two.setText(_translate("Form", "2"))
        self.btn_Four.setText(_translate("Form", "4"))
        self.btn_PlusMinus.setText(_translate("Form", "+/-"))
        self.btn_Eight.setText(_translate("Form", "8"))
        self.btn_Clear.setText(_translate("Form", "C"))
        self.btn_Equal.setText(_translate("Form", "="))
        self.btn_Comma.setText(_translate("Form", ","))
        self.btn_Zero.setText(_translate("Form", "0"))
