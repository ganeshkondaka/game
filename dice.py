import random as rnd
import time as t
k=1,2,3,4,5,6
dice={
1:("""|--------|\n
|        |\n
|   O    |\n
|        |\n
|________|"""),
2:("""|--------|\n
|        |\n
|  o  o |\n
|        |\n
|________|"""),
3:("""|--------|\n
| o      |\n
|   o    |\n
|     o  |\n
|________|"""),
4:("""|--------|\n
|  o  o  |\n
|        |\n
|  o  o  |\n
|________|"""),
5:("""|--------|\n
| o    o |\n
|    o   |\n
| o    o |\n
|________|"""),
6:("""|--------|\n
| o   o  |\n
| o   o  |\n
| o   o  |\n
|________|""")}
def fun1():
    print(dice[rnd.choice(k)])
    
r=int(input("enter the no.of dice : "))
if r<=6 and r!=0:
    for i in range(r):
        fun1()
else:
    print("please enter a value from 1 to 6 ")
t.sleep(5)
