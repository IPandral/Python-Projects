#collection of instructions
#collection of code
def function2 (x):
    return 2*x
a = function2(3)
print (a)
b = function2 (4)
print(b)
c = function2 (5)
print(c)

def function3 (x, y):
    return x + y
e = function3 (1, 2)
print(e)

def function4(x):
    print(x)
    print("still in this function:")
    return 3*x
f = function4(4)
print(f)

def function5(some_argument):
    print(some_argument)
    print("weeeee")
function5(4)