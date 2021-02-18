Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x= [1,2,3,4,5,6,7,8,9,10]
>>> min(x)
1
>>> max(x)
10
>>> sum(x)
55
>>> x = [1,99,66,3434,112,-100]
>>> x
[1, 99, 66, 3434, 112, -100]
>>> x.sort()
>>> x
[-100, 1, 66, 99, 112, 3434]
>>> x.sort(reverse=True)
>>> x
[3434, 112, 99, 66, 1, -100]
>>> x
[3434, 112, 99, 66, 1, -100]
>>> x = [1,2,3,4]
>>> y = [5,6,7,8]
>>> x+y
[1, 2, 3, 4, 5, 6, 7, 8]
>>> x-y
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x-y
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> x*y
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x*y
TypeError: can't multiply sequence by non-int of type 'list'
>>> x/y
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x/y
TypeError: unsupported operand type(s) for /: 'list' and 'list'
>>> x
[1, 2, 3, 4]
>>> x*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> x
[1, 2, 3, 4]
>>> #shallow copy
>>> x
[1, 2, 3, 4]
>>> y = x.copy()
>>> x
[1, 2, 3, 4]
>>> y
[1, 2, 3, 4]
>>> id(x)
2777462758720
>>> id(y)
2777462757568
>>> x
[1, 2, 3, 4]
>>> x.pop()
4
>>> x
[1, 2, 3]
>>> y
[1, 2, 3, 4]
>>> x
[1, 2, 3]
>>> y=x
>>> id(x)
2777462758720
>>> id(y)
2777462758720
>>> x.pop()
3
>>> x
[1, 2]
>>> y
[1, 2]
>>> from copy import copy
>>> x=[1,2,3,4,5]
>>> y=copy(x)
>>> x
[1, 2, 3, 4, 5]
>>> y
[1, 2, 3, 4, 5]
>>> id(x)
2777431351872
>>> id(y)
2777462605056
>>> x=[1,2,[3,4,5]]
>>> id(x)
2777462166784
>>> y=copy(x)
>>> id(y)
2777462757568
>>> x
[1, 2, [3, 4, 5]]
>>> id(x[2])
2777462759872
>>> id(x[2])
2777462759872
>>> y = copy(x)
>>> id(y[2])
2777462759872
>>> #
>>> from copy import deepcopy
>>> x
[1, 2, [3, 4, 5]]
>>> y = deepcopy(x)
>>> id(x[2])
2777462759872
>>> id(y[2])
2777462758400
>>> 
