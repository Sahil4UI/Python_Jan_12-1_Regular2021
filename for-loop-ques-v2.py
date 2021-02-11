Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,11):
	print(f"{i}/{i+1}")

1/2
2/3
3/4
4/5
5/6
6/7
7/8
8/9
9/10
10/11
>>> res = ""
>>> for i in range(1,11):
	res+=f"{i}/{i+1} + "

>>> res
'1/2 + 2/3 + 3/4 + 4/5 + 5/6 + 6/7 + 7/8 + 8/9 + 9/10 + 10/11 + '
>>> #sum of digits
>>> res = 0
>>> num = int(input("Enter Number : "))
Enter Number : 1234
>>> for i in range(len(str(num))):
	rem =x%10
	res += rem
	x = x//10

Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    rem =x%10
NameError: name 'x' is not defined
>>> num
1234
>>> res
0
>>> for i in range(len(str(num))):
	rem =num%10
	res += rem
	num = num//10

>>> res
10
>>> #take a number as input and check wether its prime or not
>>> 
