# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(362, 450)
        Dialog.setMinimumSize(QtCore.QSize(362, 450))
        Dialog.setMaximumSize(QtCore.QSize(362, 450))
        Dialog.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.le_q = QtWidgets.QLineEdit(self.widget)
        self.le_q.setGeometry(QtCore.QRect(0, 10, 331, 50))
        self.le_q.setMinimumSize(QtCore.QSize(0, 50))
        self.le_q.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_q.setFrame(False)
        self.le_q.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_q.setReadOnly(True)
        self.le_q.setObjectName("le_q")
        self.le_a = QtWidgets.QLineEdit(self.widget)
        self.le_a.setGeometry(QtCore.QRect(-1, 65, 331, 51))
        self.le_a.setMinimumSize(QtCore.QSize(0, 50))
        self.le_a.setStyleSheet("font: 75 20pt \"Calibri\";\n"
"background-color: rgb(170, 255, 255);")
        self.le_a.setFrame(False)
        self.le_a.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_a.setReadOnly(True)
        self.le_a.setObjectName("le_a")
        self.pb_del = QtWidgets.QPushButton(self.widget)
        self.pb_del.setGeometry(QtCore.QRect(250, 120, 78, 41))
        self.pb_del.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 255);")
        self.pb_del.setObjectName("pb_del")
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pb_dot = QtWidgets.QPushButton(Dialog)
        self.pb_dot.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_dot.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(240, 240, 240);")
        self.pb_dot.setObjectName("pb_dot")
        self.gridLayout.addWidget(self.pb_dot, 4, 0, 1, 1)
        self.pb_num_7 = QtWidgets.QPushButton(Dialog)
        self.pb_num_7.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_num_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_num_7.setObjectName("pb_num_7")
        self.gridLayout.addWidget(self.pb_num_7, 3, 0, 1, 1)
        self.pb_num_6 = QtWidgets.QPushButton(Dialog)
        self.pb_num_6.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_num_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_num_6.setObjectName("pb_num_6")
        self.gridLayout.addWidget(self.pb_num_6, 2, 2, 1, 1)
        self.pb_num_4 = QtWidgets.QPushButton(Dialog)
        self.pb_num_4.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_num_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_num_4.setObjectName("pb_num_4")
        self.gridLayout.addWidget(self.pb_num_4, 2, 0, 1, 1)
        self.pb_sign_2 = QtWidgets.QPushButton(Dialog)
        self.pb_sign_2.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_sign_2.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(240, 240, 240);")
        self.pb_sign_2.setObjectName("pb_sign_2")
        self.gridLayout.addWidget(self.pb_sign_2, 1, 3, 1, 1)
        self.pb_sign_3 = QtWidgets.QPushButton(Dialog)
        self.pb_sign_3.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_sign_3.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(240, 240, 240);")
        self.pb_sign_3.setObjectName("pb_sign_3")
        self.gridLayout.addWidget(self.pb_sign_3, 2, 3, 1, 1)
        self.pb_num_5 = QtWidgets.QPushButton(Dialog)
        self.pb_num_5.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_num_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_num_5.setObjectName("pb_num_5")
        self.gridLayout.addWidget(self.pb_num_5, 2, 1, 1, 1)
        self.pb_num_2 = QtWidgets.QPushButton(Dialog)
        self.pb_num_2.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_num_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_num_2.setObjectName("pb_num_2")
        self.gridLayout.addWidget(self.pb_num_2, 1, 1, 1, 1)
        self.pb_num_3 = QtWidgets.QPushButton(Dialog)
        self.pb_num_3.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_num_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_num_3.setObjectName("pb_num_3")
        self.gridLayout.addWidget(self.pb_num_3, 1, 2, 1, 1)
        self.pb_num_0 = QtWidgets.QPushButton(Dialog)
        self.pb_num_0.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_num_0.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_num_0.setObjectName("pb_num_0")
        self.gridLayout.addWidget(self.pb_num_0, 4, 1, 1, 1)
        self.pb_result = QtWidgets.QPushButton(Dialog)
        self.pb_result.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_result.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 127);")
        self.pb_result.setObjectName("pb_result")
        self.gridLayout.addWidget(self.pb_result, 4, 2, 1, 2)
        self.pb_num_9 = QtWidgets.QPushButton(Dialog)
        self.pb_num_9.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_num_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_num_9.setObjectName("pb_num_9")
        self.gridLayout.addWidget(self.pb_num_9, 3, 2, 1, 1)
        self.pb_num_8 = QtWidgets.QPushButton(Dialog)
        self.pb_num_8.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_num_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_num_8.setObjectName("pb_num_8")
        self.gridLayout.addWidget(self.pb_num_8, 3, 1, 1, 1)
        self.pb_num_1 = QtWidgets.QPushButton(Dialog)
        self.pb_num_1.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_num_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_num_1.setObjectName("pb_num_1")
        self.gridLayout.addWidget(self.pb_num_1, 1, 0, 1, 1)
        self.pb_sign_1 = QtWidgets.QPushButton(Dialog)
        self.pb_sign_1.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_sign_1.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(240, 240, 240);")
        self.pb_sign_1.setObjectName("pb_sign_1")
        self.gridLayout.addWidget(self.pb_sign_1, 0, 3, 1, 1)
        self.pb_sign_4 = QtWidgets.QPushButton(Dialog)
        self.pb_sign_4.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_sign_4.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(240, 240, 240);")
        self.pb_sign_4.setObjectName("pb_sign_4")
        self.gridLayout.addWidget(self.pb_sign_4, 3, 3, 1, 1)
        self.pb_percent = QtWidgets.QPushButton(Dialog)
        self.pb_percent.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_percent.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(240, 240, 240);")
        self.pb_percent.setObjectName("pb_percent")
        self.gridLayout.addWidget(self.pb_percent, 0, 2, 1, 1)
        self.pb_reset = QtWidgets.QPushButton(Dialog)
        self.pb_reset.setMinimumSize(QtCore.QSize(0, 45))
        self.pb_reset.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pb_reset.setObjectName("pb_reset")
        self.gridLayout.addWidget(self.pb_reset, 0, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DP Calculator"))
        self.le_a.setText(_translate("Dialog", "0"))
        self.pb_del.setText(_translate("Dialog", "Del"))
        self.pb_dot.setText(_translate("Dialog", "."))
        self.pb_num_7.setText(_translate("Dialog", "7"))
        self.pb_num_6.setText(_translate("Dialog", "6"))
        self.pb_num_4.setText(_translate("Dialog", "4"))
        self.pb_sign_2.setText(_translate("Dialog", "*"))
        self.pb_sign_3.setText(_translate("Dialog", "-"))
        self.pb_num_5.setText(_translate("Dialog", "5"))
        self.pb_num_2.setText(_translate("Dialog", "2"))
        self.pb_num_3.setText(_translate("Dialog", "3"))
        self.pb_num_0.setText(_translate("Dialog", "0"))
        self.pb_result.setText(_translate("Dialog", "="))
        self.pb_num_9.setText(_translate("Dialog", "9"))
        self.pb_num_8.setText(_translate("Dialog", "8"))
        self.pb_num_1.setText(_translate("Dialog", "1"))
        self.pb_sign_1.setText(_translate("Dialog", "/"))
        self.pb_sign_4.setText(_translate("Dialog", "+"))
        self.pb_percent.setText(_translate("Dialog", "%"))
        self.pb_reset.setText(_translate("Dialog", "C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
