#!usr/bin/env python3
# -*- coding:utf-8 -*-

# name = input('What\'s your name?\n')
# age_s = input('And how old are you?\n')
# height_s = input('Please tell me your height. (In meters)\n')
# weight_s = input('And now please tell me your weight. (In Kilograms)\n')

# age = int(age_s)
# height = float(height_s)
# weight = float(weight_s)


# if 'adult':
#     print('True')

# print(name, age)

# print('Hello, '+name+'. This', 'is', 'a'+' python'+' program. ')
# print('100 + 200 =', 100+200)

# num_a=0x000a
# print(num_a)
# num_b=1.23e-5
# print(num_b*100000000)

# print('I\'m Eric. \nHe thinks I\'m \"Erick\". \n\'\\\' is a backslash. \n\t1\t2\t3 ')
# print(r'I\'m Eric. \nHe thinks I\'m \"Erick\". \n\'\\\' is a backslash. \n\t1\t2\t3 ')
# print(r'''That's
# a
# multi-line
# text
# with
# a lot
# '/\/\/\/\/\'
# slashes.''')

# True and True
# False and True
# False and False
# True or True
# True or False
# False or False
# not True
# not False
# 5>3 and 3>5
# 5>3 or 3>5
# not 1>2


# a='ABC'
# b=a
# a='XYZ'
# print(b)

# PI=3.1415926

# ord('中')
# ord('a')
# chr(66)
# chr(26472)
# '\u6768'
# 'EricKY26'.encode('ascii')
# '凌尘飞雪'.encode('utf-8')
# 'EKY凌尘飞雪'.encode('utf-8')
# b'EKY\xe5\x87\x8c\xe5\xb0\x98\xe9\xa3\x9e\xe9\x9b\xaa'.decode('utf-8')

# len('EricKY26')
# len('凌尘飞雪')

# len(b'EKY')
# len(b'EKY\xe5\x87\x8c\xe5\xb0\x98\xe9\xa3\x9e\xe9\x9b\xaa')
# len('EKY凌尘飞雪'.encode('utf-8'))
# len('EKY'.encode('utf-8'))

# print('%3d-%10d' % (56, 14))
# print('%.2f' % 3.1415926)
# print('{0}-{1:10d}'.format(56, 14))

# name_cn = input('请输入姓名： \n')
# score_last = int(input('请输入该学生去年的成绩： \n'))
# score_this = int(input('请输入该学生今年的成绩： \n'))

# rate = (score_this-score_last)/score_last*100

# print('%s的成绩提高了%.1f%%' % (name_cn, rate))
# print('{0}的成绩提高了{1:.1f}%'.format(name_cn, rate))

# team_members = ['Destiny', 'Eric', 'Kathy']

# team_members
# len(team_members)
# team_members[-3]
# team_members[-2]
# team_members[-1]
# team_members[0]
# team_members[1]
# team_members[2]

# team_members.count('Eric')
# team_members.append('Darcey')
# team_members.insert(2, 'Nancy')
# team_members[2] = 'Leo'

# list1 = ['name', 86, ['A', 95], True]
# list1[0]
# list1[1]
# list1[2]
# list1[3]
# list1[2][1]
# list1[2][0]
# list_in = ['B', 86]
# list1[1] = list_in

# team_member_t = ('Destiny', 'Eric', 'Kathy')
# tuple0 = ()
# tuple1 = (1,)
# tuple_l = ('A', 2, ['L1', 'L2', True])
# tuple_l[2][-1] = False

# # exercise for list
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# # 打印Apple:
# print('L[0][0] is '+L[0][0])
# # 打印Python:
# print('L[1][1] is '+L[1][1])
# # 打印Lisa:
# print('L[2][2] is '+L[2][2])

# mates = ['Colrn', 'Kael', 'Nove']

# for name in mates:
#     print('Hello, '+name+'!')

# sum = 0

# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum+x
#     print(sum)

# list_num10 = list(range(1, 101))

# for a in list_num10:
#     sum = sum+a
# print(sum)

# sum=0
# n=99

# while n>0:
#     sum=sum+n
#     n=n-2
# print('sum =',sum)

# n = 1
# while n <= 100:
#     print(n)
#     n = n+1
#     if n>10:
#         break
# print('END')

# n = 0

# while n < 10:
#     n = n+1
#     if n % 2 == 0:  # 如果n是偶数，执行continue语句
#         continue  # continue语句会直接继续下一轮循环，后续的print(n)不会执行
#     print(n)

dict1 = {'Colrn': 83, 'Kael': 85, 'Eric': 80, 'Jason': 69}
dict1['Colrn']
dict1['Eric'] = 81
'Pyra' in dict1
dict1.get('Kael')
dict1.get('Yonda', -1)
dict1.pop('Jason')

tuple1 = (1, 2, 3)
tuple2 = (1, [2, 3])
list_dict = [7, 8, 9]
dict1[list_dict] = 88  # dict不能添加可变对象, dict的key必须是不可变对象
#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# dict2={tuple1:'A',tuple2:'B'}  # dict不能添加可变对象
dict2 = {tuple1: 'A', 'next': 'B'}

set1 = set([4, 5, 6])
set2 = set([3, 4, 5])

list_set1 = [7, 8, 9]
# set2.add(list_set1)  # set不能添加可变对象

a = 'abc'
b = a.replace('a', 'A')
