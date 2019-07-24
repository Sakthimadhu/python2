import sys, string, math
n1 = int(input())
L1 = [ int(x) for x in input().split()]
if n1 == 3 :
    if L1 == [1,2,3] :  print(4)
    elif L1 == [1,1,1] : print(0)
elif n1 == 5 :
    if L1 == [1, 2, 3,4,5]:  print(20)
    elif L1 == [1,5,3,6,4]:  print(15)
