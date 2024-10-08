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

# 다양한 조건을 판단하는 elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라"