#find the sum of first 10 numbers(1-10)
'''
res = 1
for i in range(1,11):
    res = res *i # res *= i
print("sum = ",res)
'''

#fibonacci series  0 1 1 2 3 5 8 13........
'''
first = 0
second = 1
print(first,'\n',second)

for i in range(0,100):
    third = first + second
    print(third)
    first = second
    second = third
    #first,second = second, third
'''
# 1/2+2/3+3/4+4/5-------------------------------
'''
res=0
for i in range(1,11):
    res+=i/(i+1)
print(res)
'''
#1/2! + 2/3! + 3/4! + 4/5!+-----
'''
import math
res=0
for i in range(1,11):
    res+=i/math.factorial(i+1)
print(res)
'''
#Pattern questions
'''
*
**
***
****
*****
'''
'''
for i in range(1,6):
    print("*"*i)
'''
"""
    *
   ***
  *****
 *******
*********
"""
for i in range(1,6):
    print(' '*(5-i)+"*"*(2*i-1))

'''
*****
****
***
**
*
'''
for i in reversed(range(1,6)):
    print("*"*i)

#homework :
#find the sum of digits of number - > 125 - >1+2+5 - > // ,%
#find the reverse of number -> 1234 - > 4321













