def func_2():
    def func_3():
        print('in func_3 x =', x)

    print('in func_2 x =', x)
    func_3()


x = 42
func_2()
print('x =', x)