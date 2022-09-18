def my_function(*args, **kwargs):
    egal = 0
    if type(kwargs) == float:
        egal += args
    for x in args:
         if type(x) == int or type(x) == float:
             egal += x
    else:
        return egal



print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', args=2))

