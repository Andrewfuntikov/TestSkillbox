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
