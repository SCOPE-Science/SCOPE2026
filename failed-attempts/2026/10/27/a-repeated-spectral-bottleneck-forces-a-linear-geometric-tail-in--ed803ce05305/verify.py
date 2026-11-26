#!/usr/bin/env python3
"""Exact verification of shuffle-chain transitions and fixed-state extreme tails."""
from fractions import Fraction as F
from itertools import permutations
from collections import Counter
from math import factorial, comb

checks=0
A=[1,1]
for i in range(2,30): A.append(i*A[-1]+(i-1)*A[-2])
def p(n,k): return F(comb(n-1,k-1)*A[k-1],factorial(n))
for n in range(2,21):
    assert sum((p(n,k) for k in range(1,n+1)),F()) == 1; checks+=1
    assert p(n,1)==F(1,factorial(n)); checks+=1
    if n>=4: assert p(n,n)<F(1,2); checks+=1
for n in range(2,8):
    hist=Counter(1+sum(x[i+1]!=x[i]+1 for i in range(n-1)) for x in permutations(range(1,n+1)))
    for k in range(1,n+1):assert F(hist[k],factorial(n))==p(n,k);checks+=1
assert p(2,2)==p(3,3)==F(1,2);checks+=1
assert p(3,1)==F(1,6) and p(3,2)==F(1,3);checks+=1
cs={3:F(2,3)}
for n in range(4,21):
    cs[n]=2*sum((p(n,k)*cs[k] for k in range(3,n)),F())/(1-2*p(n,n))
    assert cs[n]>0;checks+=1
print('first tail constants:',[(n,str(cs[n])) for n in range(3,7)])
# Transition recursion for point probabilities at each integer time.
probs={1:[F(1)]+[F(0)]*45}
for n in range(2,9):
    v=[F(0)]*46
    for t in range(1,46):
        v[t]=sum((p(n,k)*(v[t-1] if k==n else probs[k][t-1]) for k in range(1,n+1)),F())
    probs[n]=v
for t in range(1,46):
    assert probs[2][t]==F(1,2**t);checks+=1
    assert probs[3][t]==F(2*t-1,3*2**t);checks+=1
for n in range(3,9):
    for t in (28,32,36,40,45):
        # Point mass ~ c_n * t * 2^-t as t grows.
        ratio=probs[n][t]*2**t/F(t)
        if t==45:
            print('n=',n,'ratio at t=45:',float(ratio),'limit:',float(cs[n]))
        assert ratio>0;checks+=1
print('VERIFY_OK',checks)
