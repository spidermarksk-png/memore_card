from random import randint, shuffle

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QGroupBox,
                             QHBoxLayout, QLabel, QMessageBox, QPushButton,
                             QRadioButton, QVBoxLayout, QWidget)

#создание приложения и главного окна

class Question():
    def __init__(self,question, right_answer, wrong1, wrong2, wrong3):
        self.question = question 
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2  
        self.wrong3 = wrong3

q1 = Question('Что такое траектория?','Линия, вдоль которой движется тело', 'Форма волны, распространяющейся в веществе или пространстве','температура или тепло, передающееся от одного тела к другому','Сила, действующая на движущееся тело, направленная к центру вращения')
q2 = Question('Что такое атом?', 'Мельчайшая единица химического элемента', 'Крупная частица, состоящая из множества молекул', 'Жидкое вещество, используемое в парфюмерии', 'Энергия, выделяемая при ядерных реакциях')
q3 = Question('Что такое Броуновское движение?', "Это хаотическое движение мельчайших частиц", " Это направленное движение электрически заряженных частиц в проводнике", "Это движение планет и других небесных тел по орбитам вокруг Солнца", "Это процесс перемещения молекул вещества из области высокой концентрации в область низкой концентрации до достижения равномерного распределения")
q4 = Question('Чему равно ускорение свободно падения на Земле?', "10 м/с в квадрате", "15 м/с в квадрате", "10 м/с", "7 м/с")
q5 = Question('Что такое вещество?', "То, из чего состоит физическое тело", "Это способность физического тела совершать работу", "То, из чего состоит химическое тело", "Признак движения объекта")
q6 = Question('Что такое свободное падение?', "Это движение тела, которое происходит только под действием силы тяжести", "Это движение тела по окружности с постоянной скоростью", "Это движение тела с постоянной скоростью по горизонтальной поверхности без трения", "Это движение тела, подброшенного вверх, в момент достижения им наивысшей точки траектории")
q7 = Question('Что такое диффузия?', "Это процесс перемещения молекул вещества из области высокой концентрации в область низкой концентрации до достижения равномерного распределения", "Это процесс передачи тепловой энергии внутри твердого тела от более нагретой части к менее нагретой", "Это процесс перехода вещества из жидкого состояния в газообразное", "Это способность жидкости сохранять свой объем, но не сохранять форму, принимая форму сосуда")
q8 = Question('Что такое путь?', "Длина траектории, по которой движется тело", "Это векторная величина, представляющая собой направленный отрезок прямой, соединяющий начальное и конечное положение тела", "Это способность тела сохранять свою скорость неизменной при отсутствии действия внешних сил", "Это скорость изменения положения тела в пространстве относительно выбранной системы отсчета")
q9 = Question('Что такое плотность?', "Физическая величина, равная отношению массы тела и его обьема", "Это способность вещества изменять свою форму или размер при нагревании", " Это сила, с которой жидкость выталкивает погруженное в нее тело", "Это отношение силы, действующей перпендикулярно поверхности, к площади этой поверхности")
quests = [q1, q2, q3, q4, q5, q6, q7, q8, q9]


app = QApplication([]) 
main = QWidget()
answer = QWidget()
main.setWindowTitle('Memory Card')
quest = QLabel()
main.resize(900,700)
answer.resize(1280,1040)

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton()
rbtn2 = QRadioButton()
rbtn3 = QRadioButton()
rbtn4 = QRadioButton()
ask_btn = QPushButton('Следующий вопрос')


answ = QLabel('Правильно/Неправильно')
rt_answ = QLabel('Правильный ответ')
AnswerGroupBox = QGroupBox('Результат теста')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_main = QVBoxLayout()
layout_main.setSpacing(40)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ask = QHBoxLayout()
layout_answ = QHBoxLayout()
layout_rt_answ = QVBoxLayout()
layout_next_quest = QHBoxLayout()


layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_ask.addStretch(1)
layout_ask.addWidget(ask_btn, stretch = 2)
layout_ask.addStretch(1)


layout_rt_answ.addWidget(answ, alignment = Qt.AlignLeft | Qt.AlignTop)
layout_rt_answ.addWidget(rt_answ, alignment = Qt.AlignCenter)
AnswerGroupBox.setLayout(layout_rt_answ)

RadioGroupBox.hide()
AnswerGroupBox.show()

layout_main.addWidget(quest, alignment = Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(AnswerGroupBox)
layout_main.addLayout(layout_ask)

main.question_col = -1
main.right_answers = 0
main.all_quest = 0

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    ask_btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_answer():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    ask_btn.setText('Следующий вопрос')

def start_test():
    if ask_btn.text() == 'Ответить':
        show_answer()
    else:
        show_question()

answers = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q: Question):
    shuffle(answers)
    quest.setText(q.question)
    answers[0].setText(q.right_answer)
    rt_answ.setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    show_question()

def check_answer():
    if answers[0].isChecked():
        answ.setText('Правильно!')
        main.right_answers += 1
        print('Статистика')
        print('-Всего вопросов:', main.all_quest)
        print('-Правильных ответов:', main.right_answers)
        print('Рейтинг:',(main.right_answers / main.all_quest) * 100)
    elif answers[1].isChecked() or answers[2].isChecked() or answers[2].isChecked():
        answ.setText('Неправильно!')
    
    show_answer()

def next_question():
    main.question_col = randint(0, len(quests) - 1)
    q = quests[main.question_col]
    main.all_quest += 1
    ask(q)

def click_OK():
    if ask_btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()


ask_btn.clicked.connect(click_OK)
next_question()
main.setLayout(layout_main)
main.show()
app.exec_()
