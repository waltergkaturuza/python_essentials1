import time
#%timeit
def myfunc(a,b):
    return a+b

funcs = [myfunc]
print(funcs[0](2,3))


def dispatch_if(operator, x,y):
    if operator=="add":
        return x + y
    elif operator == "sub":
        return x -y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    return None

    
print(dispatch_if('mul',4,5))

def dispatch_dict(operator, x , y):
    return {
        'add':lambda: x+ y,
        'sub':lambda:x-y,
        'mul':lambda:x*y,
        'div':lambda:x/y
    }.get(operator, lambda: None)()
    
print(dispatch_dict('mul', 4, 6))

func_dict={
        'add':[lambda:x+y],
        'sub':lambda:x-y,
        'mul':lambda:x*y,
        'div':lambda:x/y
    }
def dispatch_dict_var(operator, x , y):
    return func_dict.get(operator, lambda: None)()


dispatch_dict_var('div', 9,3)