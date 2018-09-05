def print_max(x, y):
    '''compare two numbers and.

    two numbers should be integer'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
help(print_max)
