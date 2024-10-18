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
result = add_mul('add',1,2,3,4,5)
print(result)
result = add_mul('mul',1,2,3,4,5)
print(result)
"""

"""
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
"""

"""
def vartest(a):
    a = a+1
    
vartest(3)
print(a)
"""

"""
def vartest(a):
    a = a+1
    return a

a = vartest(3)
print(a)
"""

"""
for i in range(10):
    print(i, end =' ')
"""

"""
f = open("새파일.txt", 'w')
f.close()
"""

"""
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
"""

# Q1 홀수, 짝수 판별하기
"""
def is_odd(number):
    if number % 2 == 1:
        return print("True")
    else:
        return print("False")
is_odd(99999999)
is_odd(10000000000000)
is_odd(3)
is_odd(4)
is_odd(5)
is_odd(6)
"""

# Q2 모든 입력의 평균값 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)
avg_numbers(1, 2)
