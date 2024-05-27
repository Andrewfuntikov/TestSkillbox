def my_function():
    """Привет это текст дукоментации


    А это продолжение)))"""
    print(123)


print(my_function.__doc__)


# распаковка параметров (аргументов)
def vector_module(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# распаковка позиционных параметров
some_list = [2, 3, 4]
res = vector_module(*some_list)
# x, y, z = some_list
# vector_module(2, 3, 4)
print(res)

# распаковка именованных параметров
some_dict = {'x': 2, 'y': 3, 'z': 4}
res = vector_module(**some_dict)
# vector_module(x=2, y=3, z=4)
print(res)

# # Произвольное число позиционных параметров
# def print_them_all_v1(*args):
#     print('print_them_all_v1')
#     print('тип args:', type(args))
#     print(args)
#     for i, arg in enumerate(args):
#         print('позиционный параметр:', i, arg)
#
#
# print_them_all_v1(2, 'привет', 5.6)
#
# # распаковка
# my_favorite_pets = ['lion', 'elephant', 'monkey', 'cat', 'horse']
# print_them_all_v1(my_favorite_pets)
# print_them_all_v1(*my_favorite_pets)

#
# # Произвольное число именованных параметров
# def print_them_all_v2(**kwargs):
#     print('print_them_all_v2')
#     print('тип kwargs:', type(kwargs))
#     print(kwargs)
#     for key, value in kwargs.items():
#         print('именованный аргумент:', key, '=', value)
#
#
# print_them_all_v2(name='Вася', address='Moscow')
#
# # распаковка
# my_friend = {'name': 'Вася', 'address': 'Moscow', 'age': 25}
# print_them_all_v2(**my_friend)


# Комбинация
def print_them_all_v3(*args, **kwargs):
    print('print_them_all_v3')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v3('Вася', 'Moscow', 25)
print_them_all_v3(name='Вася', address='Moscow')

print_them_all_v3(1000, 'рублей', name='Вася', address='Moscow')

my_friend = {'name': 'Вася', 'address': 'Moscow'}
print_them_all_v3(1000, 'рублей', **my_friend)
