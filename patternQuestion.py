#nested for Loop
'''
for i in range(1,5):
    for j in range(1,5):
        print(i,j)
'''
'''
for i in range(1,4):
    for j in range(1,i):
        print(i,j)
'''

'''
*
**
***
****
*****
'''
'''
for i in range(1,6):
    for j in range(i):
        print("*",end = "")
    print()
'''
'''
    *
   **
  ***
 ****
*****
'''
'''
for i in range(1,6):
    print(" " *(5-i),end="")
    for j in range(i):
        print("*",end = "")
    print()
'''
'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
'''
for i in range(1,6):
    print(" " *(5-i),end="")
    for j in range(i):
        print("*",end = " ")
    print()
'''
'''
1
12
123
1234
12345
'''
'''
1
22
333
4444
55555
'''

'''
0
'''


'''
1
00
111
0000
11111
'''
'''
1
01
010
1010
10101
'''
x=1
for i in range(1,6):
    for j in range(i):
        if x%2==0:
            print(0,end = "")
        else:
            print(1,end='')
        x+=1
    print()
















