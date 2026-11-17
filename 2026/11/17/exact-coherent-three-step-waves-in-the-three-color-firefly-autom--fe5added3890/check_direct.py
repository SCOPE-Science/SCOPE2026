#!/usr/bin/env python3
"""Independent direct ring dynamics and third-iterate shift-count checks."""
from itertools import product

def advance(x):
    n=len(x);out=[]
    for i in range(n):
        state=x[i]
        blocked=(state==2 and (x[(i-1)%n]==1 or x[(i+1)%n]==1))
        out.append(state if blocked else (state+1)%3)
    return tuple(out)

def wave_count(n):
    plus=minus=both=0
    for x in product(range(3), repeat=n):
        y=advance(advance(advance(x)))
        p=(y==x[1:]+x[:1]);m=(y==x[-1:]+x[:-1])
        plus+=p;minus+=m;both+=(p and m)
        if p or m:
            # Coherent waves are periodic without any transient.
            z=x
            for t in range(3*n):z=advance(z)
            assert z==x
    return plus,minus,both
vals=[3,3,3,7]
for n in range(5,13):vals.append(3*vals[-1]-3*vals[-2]+vals[-3]+vals[-4])
for n in range(3,11):
    p,m,b=wave_count(n)
    assert (p,m,b)==(vals[n-1],vals[n-1],3),(n,p,m,b,vals[n-1])
    print('n=%d signed=(%d,%d) intersection=%d union=%d'%(n,p,m,b,p+m-b))
# Alternating classes (length 2) cannot satisfy 3-step translation unless constant.
for a in range(3):
 for b in range(3):
    x=(a,b)*3
    y=advance(advance(advance(x)))
    assert ((y==x[1:]+x[:1]) and a!=b)==False
print('direct independent enumeration and overlap test: PASS')
