# fibonacci series
"""
Created on Sat Dec 23 11:04:41 2023

@author: Tanaya
"""

n=int(input("enter a number"))
x=0
y=1
z=x+1
while z<=n:
    print(z)
    x=y
    y=z
    z=x+y
