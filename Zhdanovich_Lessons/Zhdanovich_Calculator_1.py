


from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import sys

from PyQt5.Qt import *
from PyQt5 import QtGui


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = 0
        self.operand_1 = 0
        self.operand_2 = 0

    def initUI(self):
        self.setGeometry(300,300,300,320)
        self.setWindowTitle('Калькулятор')
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QtGui.QFont('Times',16))
        self.label.setStyleSheet('backgroun-color: grey')

        self.label.setText('0')
        self.label.resize(275, 100)
        self.move(50,50)

        self.num_1 = QPushButton('1', self)
        self.num_1.move(25,100)
        self.num_1.resize(50,50)

        self.num_2 = QPushButton('2', self)
        self.num_2.move(75, 100)
        self.num_2.resize(50, 50)

        self.num_3 = QPushButton('3', self)
        self.num_3.move(125, 100)
        self.num_3.resize(50, 50)

        self.num_4 = QPushButton('4', self)
        self.num_4.move(25, 150)
        self.num_4.resize(50, 50)

        self.num_5 = QPushButton('5', self)
        self.num_5.move(75, 150)
        self.num_5.resize(50, 50)

        self.num_6 = QPushButton('6', self)
        self.num_6.move(125, 150)
        self.num_6.resize(50, 50)

        self.num_7 = QPushButton('7', self)
        self.num_7.move(25, 200)
        self.num_7.resize(50, 50)

        self.num_8 = QPushButton('8', self)
        self.num_8.move(75, 200)
        self.num_8.resize(50, 50)

        self.num_9 = QPushButton('9', self)
        self.num_9.move(125, 200)
        self.num_9.resize(50, 50)

        self.num_0 = QPushButton('0', self)
        self.num_0.move(25, 250)
        self.num_0.resize(50, 50)

        self.num_stepen = QPushButton('x^y', self)
        self.num_stepen.move(175, 200)
        self.num_stepen.resize(50, 50)

        self.num_kvadrat = QPushButton('^2', self)
        self.num_kvadrat.move(225, 200)
        self.num_kvadrat.resize(50, 50)

        self.num_plus = QPushButton('+', self)
        self.num_plus.move(175, 100)
        self.num_plus.resize(50, 50)

        self.num_minus = QPushButton('-', self)
        self.num_minus.move(175, 150)
        self.num_minus.resize(50, 50)

        self.num_umnozh = QPushButton('*', self)
        self.num_umnozh.move(225, 100)
        self.num_umnozh.resize(50, 50)

        self.num_delenie = QPushButton('/', self)
        self.num_delenie.move(225, 150)
        self.num_delenie.resize(50, 50)

        self.num_clean = QPushButton('C', self)
        self.num_clean.move(75, 250)
        self.num_clean.resize(50, 50)

        self.num_ravno = QPushButton('=', self)
        self.num_ravno.move(125, 250)
        self.num_ravno.resize(100, 50)

        self.num_kvadrat = QPushButton('√', self)
        self.num_kvadrat.move(225, 250)
        self.num_kvadrat.resize(50, 50)

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.num_plus.clicked.connect(self.add)
        self.num_minus.clicked.connect(self.min)
        self.num_umnozh.clicked.connect(self.mult)
        self.num_delenie.clicked.connect(self.divis)
        self.num_stepen.clicked.connect(self.step1)
        self.num_kvadrat.clicked.connect(self.sqrt1)
        self.num_ravno.clicked.connect(self.ravno)
        self.num_clean.clicked.connect(self.Clear)


    def enter_value(self):
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enter_value()
    def two(self):
        self.my_input = '2'
        self.enter_value()
    def three(self):
        self.my_input = '3'
        self.enter_value()
    def four(self):
        self.my_input = '4'
        self.enter_value()
    def five(self):
        self.my_input = '5'
        self.enter_value()
    def six(self):
        self.my_input = '6'
        self.enter_value()
    def seven(self):
        self.my_input = '7'
        self.enter_value()
    def eight(self):
        self.my_input = '8'
        self.enter_value()
    def nine(self):
        self.my_input = '9'
        self.enter_value()
    def zero(self):
        self.my_input = '0'
        self.enter_value()

    def add(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def min(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def mult(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def divis(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def step1(self):
        self.operation = 'x^y'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def sqrt1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
    def kvadrat(self):
        self.operation = '^2'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def Clear(self):
        self.label.setText('')

    def ravno(self):
        if self.label.text():
            self.operand_2 = float(self.label.text())
        if self.operation == '+':
            self.label.setText(str(self.operand_1 + self.operand_2))
        elif self.operation == '-':
            self.label.setText(str(self.operand_1 - self.operand_2))
        elif self.operation == '*':
            self.label.setText(str(self.operand_1 * self.operand_2))
        elif self.operation == '/':
            if self.operand_2 == 0: self.label.setText('Ошибка! Деление на ноль.')
            else: self.label.setText(str(self.operand_1 / self.operand_2))
        elif self.operation == '^':
            self.label.setText(str(self.operand_1 ** self.operand_2))
        elif self.operation == '√':
            self.label.setText('')




app = QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec())
