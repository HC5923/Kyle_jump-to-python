'''
print("hi TSS2 Team")
'''

'''
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
'''

'''
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")
'''

'''
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
'''

'''
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
'''

'''
# 다양한 조건을 판단하는 elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")
'''

# Q1 조건문의 참과 거짓
"""
A1 shirt
* 3,4 가 참인데 3번이 우선이라 3번에서 컷
"""
"""
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
"""

"""
# Q2 3의 배수의 합 구하기
# while 문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자. (166833 출력)
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수가 3의 배수.
        result += i # result에 현재 i의 값을 더함. 즉, 3의 배수인 i 값을 result에 누적해서 더함
    i += 1 # 그 다음으로 넘어가기 위함
print(result)
"""

"""
# Q3 별 표시하기
# while 문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해보자
# *
# **
# ***
# ****
# *****

i = 0
while True:
    i += 1
    if i > 5 : break
    print("*" * i) # 별을 i 의 값만큼 출력
"""

"""
# Q4 1부터 100까지 출력하기
# for 문을 사용해 1부터 100까지의 숫자를 출력해 보자.
# for문과 함께 자주 사용하는 range 함수 사용

for i in range(1,101): # 숫자들의 시퀀스로 나열할 필요가 있다면 파이썬 내장 함수인 range 를 사용하면 됨. 1부터 101 전까지의 숫자를 의미
    print(i)
"""

"""
# Q5 평균 점수 구하기
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100] for 문을 사용하여 A 학급의 평균 점수를 구해 보자.
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0 # 변수를 0으로 초기화 시켜주는 변수로써, 학생들의 점수를 모두 더한 총합을 저장하는 용도로 사용
for score in A: # A의 각 요소를 하나씩 반복하기 위함. 즉, score 는 70, 60 순서로 각 점수를 받음
    total += score # total에 현재 score 값을 더함. 첨은 0으로 해놨기 때문에 첫 점수를 더하면 70이 됨. 
average = total / len(A) # 객체의 길이(항목 수)를 돌려주는 내장 함수 'len' 을 사용해서 A의 항목수를 토탈과 나눠줌  = 10 나누기 토탈
print(average)

=> 79
"""

"""
# Q6 리스트 컴프리헨션 사용하기
# 다음 소스 코드는 리스트의 요소 중에서 홀수만 골라 2를 곱한 값을 result 리스트에 담는 예제이다.
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1: # 0으로 떨어지지 않는 1을 넣어, 홀수값만 구하는 방식
        result.append(n * 2)
print(result)
=> [2,6,10]
"""

"""
# 위 코드를 리스트 컴프리헨션을 사용하여 표현해보자. 리스트 안에 for 문을 포함하는 방식. if 조건문도 포함할 수 있음.
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)
=> [2,6,10]
"""