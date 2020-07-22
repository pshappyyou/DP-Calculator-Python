import sys, ui

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from PyQt5 import uic
#
# MainUI = '../_uiFiles/calc.ui'

class MainDiaglog(QDialog, ui.Ui_Dialog):
#class MainDiaglog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        # uic.loadUi(MainUI, self)
        self.setupUi(self)

        self.pb_num_1.clicked.connect(lambda state, button = self.pb_num_1: self.NumClicked(state, button))
        self.pb_num_2.clicked.connect(lambda state, button = self.pb_num_2: self.NumClicked(state, button))
        self.pb_num_3.clicked.connect(lambda state, button = self.pb_num_3: self.NumClicked(state, button))
        self.pb_num_4.clicked.connect(lambda state, button = self.pb_num_4: self.NumClicked(state, button))
        self.pb_num_5.clicked.connect(lambda state, button = self.pb_num_5: self.NumClicked(state, button))
        self.pb_num_6.clicked.connect(lambda state, button = self.pb_num_6: self.NumClicked(state, button))
        self.pb_num_7.clicked.connect(lambda state, button = self.pb_num_7: self.NumClicked(state, button))
        self.pb_num_8.clicked.connect(lambda state, button = self.pb_num_8: self.NumClicked(state, button))
        self.pb_num_9.clicked.connect(lambda state, button = self.pb_num_9: self.NumClicked(state, button))
        self.pb_num_0.clicked.connect(lambda state, button = self.pb_num_0: self.NumClicked(state, button))

        self.pb_sign_1.clicked.connect(lambda state, button = self.pb_sign_1: self.NumClicked(state, button))
        self.pb_sign_2.clicked.connect(lambda state, button = self.pb_sign_2: self.NumClicked(state, button))
        self.pb_sign_3.clicked.connect(lambda state, button = self.pb_sign_3: self.NumClicked(state, button))
        self.pb_sign_4.clicked.connect(lambda state, button = self.pb_sign_4: self.NumClicked(state, button))

        # self.pb_paren_1.clicked.connect(lambda state, button = self.pb_paren_1: self.NumClicked(state, button))
        # self.pb_paren_2.clicked.connect(lambda state, button = self.pb_paren_2: self.NumClicked(state, button))
        self.pb_dot.clicked.connect(lambda state, button = self.pb_dot: self.NumClicked(state, button))
        self.pb_percent.clicked.connect(lambda state, button = self.pb_percent: self.NumClicked(state, button))

        self.pb_result.clicked.connect(self.MakeResult)
        self.pb_reset.clicked.connect(self.Reset)
        self.pb_del.clicked.connect(self.Del)


    def NumClicked(self, state, button):

        orig_txt = self.le_q.text()

        if len(orig_txt) == 0 and (button == self.pb_sign_1 or button == self.pb_sign_2 or button == self.pb_sign_3 or button == self.pb_sign_4 or button == self.pb_percent or button == self.pb_dot or button == self.pb_result):
            if (len(self.le_a.text())>0):
                orig_txt = self.le_a.text()
            else:
                return False

        if len(orig_txt) > 0:
            last_char = orig_txt[-1]
            if (last_char == '+' or last_char == '-' or last_char == '*' or last_char == '/') and (button == self.pb_sign_1 or button == self.pb_sign_2 or button == self.pb_sign_3 or button == self.pb_sign_4 or button == self.pb_percent or button == self.pb_dot or button == self.pb_result):
                return False

        # if button == self.pb_percent:
        #     new_txt = '*0.01'
        # else:

        new_txt = button.text()

        self.le_q.setText(orig_txt + new_txt)

#    def NumClicked2(self):
#      orig_txt = self.le_q.text()
#        new_txt = self.pb_num_2.text()
#        self.le_q.setText(orig_txt + new_txt)

    def MakeResult(self):
        try:
            result = eval(self.le_q.text())
            #print(type(result))
            self.le_a.setText(str(result))
            self.le_q.clear()
        except Exception as e:
            print(e)
            #pass

    def Reset(self):
        self.le_q.clear()
        self.le_a.setText('0')

    def Del(self):
        if len(self.le_q.text()) <= 0:
            return
        else:
            origtxt = self.le_q.text()
            self.le_q.setText(origtxt[:-1])


app=QApplication(sys.argv)
main_dialog = MainDiaglog()
main_dialog.show()
app.exec_()