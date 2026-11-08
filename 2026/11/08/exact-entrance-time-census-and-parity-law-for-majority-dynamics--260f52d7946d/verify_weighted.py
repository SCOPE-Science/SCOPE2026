#!/usr/bin/env python3
"""Independent quotient-state, binomially weighted verification to n=120.
Run: python verify_weighted.py
"""
from collections import Counter
from math import comb

def next_state(n, a, b, s):
    d=n+1
    def V(old,ones):
        if 2*ones>d:return 1
        if 2*ones<d:return 0
        return old
    return (V(a,b+s),V(b,a+s),n*a if a==b else s)

def predicted(n):
    c=comb(n,n//2)
    if n&1:
        return {(1,0):2,(2,0):2,(1,1):2**n+2*c+2,
                (2,1):2**n-2*c-2,(1,2):2**(n+1)-4}
    return {(1,0):2,(2,0):2+2*c,(1,1):2**n+c+2,
            (2,1):2**n-c-2,(1,2):2**(n+1)-2*c-4}

for n in range(2,121):
    counts=Counter()
    for a in (0,1):
      for b in (0,1):
        for s in range(n+1):
          initial=(a,b,s)
          seen={initial:0};q=initial
          for t in range(1,8):
            q=next_state(n,*q)
            if q in seen:
                pre=seen[q];period=t-pre
                assert pre<=2 and period in (1,2)
                counts[(period,pre)]+=comb(n,s)
                break
            seen[q]=t
          else:raise AssertionError((n,initial))
    assert dict(counts)=={k:v for k,v in predicted(n).items() if v}, (n,counts,predicted(n))
    assert sum(counts.values())==4*(2**n)
print('PASS: independent quotient-state weighted census for every n=2..120, including exact first-entry categories')
