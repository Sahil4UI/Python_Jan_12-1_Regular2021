Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Data Collection
>>> x=5
>>> #list - Python's Data Collection
>>> x = [1,2,3,4,5]
>>> x
[1, 2, 3, 4, 5]
>>> x = [1.'hi',True,5.4]
SyntaxError: invalid syntax
>>> x = [1,'hi',True,5.4]
>>> x
[1, 'hi', True, 5.4]
>>> type(x)
<class 'list'>
>>> x
[1, 'hi', True, 5.4]
>>> x[0]
1
>>> x[-1]
5.4
>>> x
[1, 'hi', True, 5.4]
>>> x = [1,2,3,4,[5,6,7,[8,9,10]]]
>>> x[-1][-1][1]
9
>>> x[-1][-1][-2]
9
>>> x[-1]
[5, 6, 7, [8, 9, 10]]
>>> x=[1,2,3,4,5]
>>> x[1:4]
[2, 3, 4]
>>> #functions
>>> x=[]
>>> x.append(10)
>>> x
[10]
>>> x.append(11)
>>> x
[10, 11]
>>> x.append(12)
>>> x
[10, 11, 12]
>>> x.insert(0,78)
>>> x
[78, 10, 11, 12]
>>> x.insert(0,144)
>>> x
[144, 78, 10, 11, 12]
>>> x.insert(100,87)
>>> x
[144, 78, 10, 11, 12, 87]
>>> x[100]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x[100]
IndexError: list index out of range
>>> x
[144, 78, 10, 11, 12, 87]
>>> x.pop()
87
>>> x
[144, 78, 10, 11, 12]
>>> x.pop(3)
11
>>> x
[144, 78, 10, 12]
>>> x.remove(144)
>>> x
[78, 10, 12]
>>> del x[1]
>>> x
[78, 12]
>>> x.clear()
>>> x
[]
>>> x
[]
>>> x=[8,6,9]
>>> x[0] = 2345
>>> x
[2345, 6, 9]
>>> x = [1,2,43,5,6,67]
>>> for i in range(len(x)):
	print(x[i])

1
2
43
5
6
67
>>> x
[1, 2, 43, 5, 6, 67]
>>> largest = x[1]
>>> largest = x[0]
>>> for i in range(1,len(x)):
	if x[i] > largest:
		largest=x[i]

>>> largest
67
>>> max(x)
67
>>> x
[1, 2, 43, 5, 6, 67]
>>> largest = x[0]
>>> secondLargest = x[1]
>>> for i in range(2,len(x)):
	if x[i]>largest:
		secondLargest = largest
		largest = x[i]
	elif x[i] > secondLargest:
		secondLargest = x[i]

>>> largest
67
>>> secondLargest
43
>>> 
