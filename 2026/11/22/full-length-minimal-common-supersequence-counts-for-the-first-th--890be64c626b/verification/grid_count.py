#!/usr/bin/env python3
"""Exact uniqueness-constrained shuffle count by lattice-path dynamic programming."""
from collections import defaultdict

def count(q,k):
    a=tuple(range(q))*k
    b=tuple(range(1,q))+ (0,)
    b=b*k
    n=len(a)
    dp={(0,0):1}
    for _ in range(2*n):
        nxt=defaultdict(int)
        for (i,j),w in dp.items():
            if i<n and (j==0 or a[i]!=b[j-1]) and (j==n or a[i]!=b[j]):
                nxt[i+1,j]+=w
            if j<n and (i==0 or b[j]!=a[i-1]) and (i==n or b[j]!=a[i]):
                nxt[i,j+1]+=w
        dp=nxt
    return dp.get((n,n),0)

def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

for q in range(3,6):
    for k in range(1,16):
        actual=count(q,k)
        expect={3:lambda n:1,4:lambda n:2**(4*n-1),5:lambda n:fib(10*n-1)}[q](k)
        assert actual==expect,(q,k,actual,expect)
    print(f'q={q}: all k=1..15 match predicted formula; k=1,2,3:',[count(q,k) for k in (1,2,3)])
print('DP: PASS')
