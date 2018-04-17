#!usr/bin/env python3
# -*- coding:utf-8 -*-

name = input('Who are you?\n')
age = input('And how old are you?\n')

print(name, age)

print('Hello, '+name+'. This', 'is', 'a'+' python'+' program. ')
print('100 + 200 =', 100+200)

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

if int(age) >= 18:
    print('You are an adult. ')
else:
    print('You are a children. ')

a='ABC'
b=a
a='XYZ'
print(b)

PI=3.1415926

ord('中')
ord('a')
chr(66)
chr(26472)
'\u6768'
'EricKY26'.encode('ascii')
'凌尘飞雪'.encode('utf-8')
'EKY凌尘飞雪'.encode('utf-8')
b'EKY\xe5\x87\x8c\xe5\xb0\x98\xe9\xa3\x9e\xe9\x9b\xaa'.decode('utf-8')

len('EricKY26')
len('凌尘飞雪')

len(b'EKY')
len(b'EKY\xe5\x87\x8c\xe5\xb0\x98\xe9\xa3\x9e\xe9\x9b\xaa')
len('EKY凌尘飞雪'.encode('utf-8'))
len('EKY'.encode('utf-8'))

print('%3d-%02d' % (000, 14))
print('%.2f' % 3.1415926)