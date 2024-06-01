#  tuple - кортеж ()
#  list  - список []
#  dict  - словарь {}
# *args - распоковка списка **kwargs - распоковка словаря
# Чтобы импортировать модуль нужно добавить папку/файл в sources root
# max() - максимальный элемент
# min() - минимальный элемент
# sorted() - отсортированный список
# sum() - сумма элементов списка
# zip() - попарная компоновка элементов двух списков
# all() - True если ВСЕ элементы списка/множества True
# any() - True если ХОТЯ БЫ ОДИН элемент списка True
# dir() - список всех аттрибутов обьекта
# help() - встроенная помощь по функции/обьекту
# id() - внутренний идентификатор обьекта
# hash() - значение хэша для обьекта. Что такое хэш-функции см https://goo.gl/gZLM4o
# isinstance() - является ли обьект обьектом данного класса
# type() - тип(КЛАСС) обьекта
# open() - открыть файл на файловой системе
# globals() - встроенная функция, которая возвращает словарь глобальных имен
# locals() - встроенная функция, которая возвращает словарь локального пространства имен
# _sorted_keys = None Подчерк перед переменной говорит о том внутреняя переменная которую использовать на прямую не надо
# hasattr() - проверяем если ли атрибут в обьекте
# setattr() - проверяем если ли атрибут в обьекте, но можно манипулировать обьектами как переменной
# Эмуляция операторов сравнения
#
# object.__eq__(self, other) - равенство двух объектов ==
# object.__ne__(self, other) - не равно !=
# object.__lt__(self, other) - строго меньше <
# object.__le__(self, other) - меньше или равно <=
# object.__gt__(self, other) - строго больше >
# object.__ge__(self, other) - больше или равно >=
#
# должны возвращать boolean - True/False

# Эмуляция математических операций
# 2 + 2
# my_car + truck
#
# object.__add__(self, other) - сложение +
# object.__sub__(self, other) - вычитание -
# object.__mul__(self, other) - умножение *
# object.__truediv__(self, other) - деление /
# object.__floordiv__(self, other) - целочисленное деление //
# object.__mod__(self, other) - остаток от деления %
# object.__pow__(self, other) - возведение в степень **
# object.__lshift__(self, other) - побитовый сдвиг влево <<
# object.__rshift__(self, other) - побитовый сдвиг вправо >>
# object.__and__(self, other) - побитовое И &
# object.__xor__(self, other) - побитовое исключающее ИЛИ ^
# object.__or__(self, other) - побитовое ИЛИ |

# для операций расширенного присвоения служат методы
# object.__iadd__(self, other) - +=
# object.__isub__(self, other) - -=
# object.__imul__(self, other) - *=
# object.__itruediv__(self, other) - /+
# object.__ifloordiv__(self, other) - //=
# object.__imod__(self, other) - %=
# object.__ipow__(self, other) - **=
# object.__ilshift__(self, other) - <<=
# object.__irshift__(self, other) - >>=
# object.__iand__(self, other) - &=
# object.__ixor__(self, other) - ^=
# object.__ior__(self, other) - |=
#
# они изменяют сам объект (по месту, inplace)
# self.__dict__ - словарь атрибутов