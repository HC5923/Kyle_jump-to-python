"""
def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)
"""

"""
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
    
add(3, 4)
"""

"""
def sub(a, b):
    return a - b
result = sub(a=7, b=3)
print(result)
"""

"""
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1, 2, 3)
print(result)
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)
"""

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

