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
# TODO добавь это в интересные факты