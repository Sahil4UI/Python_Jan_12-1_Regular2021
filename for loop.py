Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(4):#01,2,3
	print(i)

0
1
2
3
>>> for i in range(1,4):#1,2,3
	print(i)

1
2
3
>>> for i in range(1,11,2):
	print(i)

1
3
5
7
9
>>> for i in range(10,0,-1):
	print(i)

10
9
8
7
6
5
4
3
2
1
>>> for i in reversed(range(1,11)):
	print(i)

10
9
8
7
6
5
4
3
2
1
>>> #find the sum of numbers b/w 1-10
>>> result =0
>>> for i in range(1,11):
	result +=i

>>> print(result)
55
>>> '''
'''
'\n'
>>> '''
2X1=2
2X2=4
2X3=6
2X4=8
.
.
.
.
2X10=20
'''
'\n2X1=2\n2X2=4\n2X3=6\n2X4=8\n.\n.\n.\n.\n2X10=20\n'
>>> 
>>> for i in range(1,11):
	print(f"2 X {i} = {2*i}")

2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
2 X 10 = 20
>>> res=0
>>> for i in range(1,11):
	res = res+ 1/(i*2)

>>> res
1.4644841269841269
>>> 