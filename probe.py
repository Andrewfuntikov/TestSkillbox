import sys
# компоненты интерфейса
from PyQt5.QtWidgets import QApplication, QWidget

# Каждое приложение должно создать объект QApplication
# sys.argv - список аргументов командной строки
application = QApplication(sys.argv)
# QWidget - базовый класс для всех объектов интерфейса пользователя
# если использовать для виджета конструктор без родителя,
# то такой виджет станет окном
widget = QWidget()
widget.resize(320, 240)  # изменить размеры виджета
widget.setWindowTitle("Всем привет!")  # установить заголовок
widget.show()  # отобразить окно на экране
sys.exit(application.exec_())  # запуск основного цикла приложения