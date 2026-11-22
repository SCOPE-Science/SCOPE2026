#!/usr/bin/env python3
"""Independent exhaustive direct dynamics on small labelled wheels."""
from itertools import product

def next_state(x):
    n=len(x)-1
    hub=x[0]
    y=[0]*(n+1)
    if hub!=0:
        y[0]=(hub+1)%4
    else:
        y[0]=1 if 1 in x[1:] else 0
    for i in range(n):
        v=x[1+i]
        if v: y[1+i]=(v+1)%4
        else:
            left=x[1+(i-1)%n]
            right=x[1+(i+1)%n]
            y[1+i]=int(hub==1 or left==1 or right==1)
    return tuple(y)

want={3:24,4:80,5:200,6:480,7:1232,8:3024}
for n,expected in want.items():
    period4=0
    fixed=0
    period2=0
    for x in product(range(4),repeat=n+1):
        y=next_state(x)
        z=next_state(y)
        w=next_state(next_state(z))
        if w!=x:continue
        if y==x:fixed+=1
        elif z==x:period2+=1
        else: period4+=1
    assert fixed==1 and period2==0 and period4==expected,(n,fixed,period2,period4)
    print(f"wheel_{n} configurations={4**(n+1)} fixed={fixed} primitive_two={period2} primitive_four={period4}")
print('PASS exhaustive 4-step evolution checks')
