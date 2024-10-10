'''
# print("hi")

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

# Q4 1부터 100까지 출력하기
# for 문을 사용해 1부터 100까지의 숫자를 출력해 보자.
