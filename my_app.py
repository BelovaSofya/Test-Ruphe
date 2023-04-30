# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from final_win import *
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear () #как будет выглядеть окно
        self.initUI() #создаем графические элементы
        self.connects() #устанавливаем связь между элементами
        self.show() #сделать окно видимым

    def set_appear(self):
        self.setWindowTitle(txt_title) #установли заголовок
        self.resize(win_width,win_height) #Изменили размер окна
        self.move(win_x,win_y) #появление окна в указанной точке

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.line = QVBoxLayout()

        self.line.addWidget(self.hello_text, alignment = AlignCenter)
        self.line.addWidget(self.instruction, alignment = AlignCenter)
        self.line.addWidget(self.button, alignment = AlignCenter)
        
    def show(self):
        self.setLayout(self.line)
        self.show()

    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

mw = MainWin()
app = QApplication([])
app.exec_()




