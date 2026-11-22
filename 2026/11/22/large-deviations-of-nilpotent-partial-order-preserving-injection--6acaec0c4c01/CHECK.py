#!/usr/bin/env python3
"""Independent finite verification of rank counts of nilpotent increasing partial injections."""
from itertools import combinations
from math import comb

def recurrence(nmax):
    F = [[comb(n,k)**2 for k in range(n+1)] for n in range(nmax+1)]
    R=[]
    for n in range(nmax+1):
        arr=F[n][:]
        for j in range(n):
            a,b=R[j],F[n-1-j]
            for p,x in enumerate(a):
                for q,y in enumerate(b):
                    arr[p+q+1]-=x*y
        R.append(arr)
    return R

def brute(n):
    out=[0]*(n+1)
    for k in range(n+1):
        ss=list(combinations(range(n),k))
        for ds in ss:
            for im in ss:
                # A monotone partial injection is nilpotent iff it has no fixed point.
                if all(a!=b for a,b in zip(ds,im)):
                    out[k]+=1
    return out

R=recurrence(10)
for n in range(0,11):
    b=brute(n)
    assert b==R[n],(n,b,R[n])
    if n<=8 or n==10:
        print(f'n={n}: ' + repr(b) + f'; total={sum(b)}')
assert [sum(R[n]) for n in range(11)]==[1,1,3,9,29,97,333,1165,4135,14845,53791]
print('PASS: independent two-subset enumeration equals polynomial convolution for n=0,...,10')
print('PASS: scalar totals agree with known nilpotent sequence for n=0,...,10')
