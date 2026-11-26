#!/usr/bin/env python3
"""Independent exact parity count and Krawtchouk projection certification."""
from math import comb, isqrt
from fractions import Fraction
from itertools import combinations

def parity_coeff(S,n):
    ans=0
    for a in range(n):
        for b in range(a,n):
            ans += -1 if sum(k in S for k in range(a,b+1))%2 else 1
    return ans

def krawtchouk(j,t,n):
    return sum((-1)**r*comb(t,r)*comb(n-t,j-r) for r in range(max(0,j-(n-t)), min(j,t)+1))

def endpoint(s):
    n=s*s-1;J=s*(s-1)//2;H=s*(s+1)//2;N=1<<n
    Z=comb(n,J)+comb(n,H)
    weighted=sum(comb(n,t)*abs(krawtchouk(J,t,n)+krawtchouk(H,t,n)) for t in range(1,n+1))
    return Fraction(N-Z+weighted,N)

for n in range(1,11):
    size=1<<n
    cnt=0
    for Sbits in range(size):
        S={k for k in range(n) if Sbits & (1<<k)}
        pref=1;Q=1;neg=0
        for i in range(n):
            pref*=(-1 if i in S else 1)
            Q+=pref
            if pref==-1: neg+=1
        exact=parity_coeff(S,n)
        assert exact == (Q*Q-(n+1))//2
        cnt += exact==0
    s=isqrt(n+1)
    assert cnt==(comb(n+1,s*(s-1)//2) if s*s==n+1 else 0)
    print(f"n={n}, verified all {size} frequencies; zero={cnt}")
for s in range(2,5):
    print(f"projection norm n={s*s-1}: {endpoint(s)} = {float(endpoint(s)):.9f}")
print('PASS independent interval enumeration and exact Krawtchouk projection constants')
