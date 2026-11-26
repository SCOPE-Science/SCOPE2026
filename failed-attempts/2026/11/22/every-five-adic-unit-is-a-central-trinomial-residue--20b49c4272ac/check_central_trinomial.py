#!/usr/bin/env python3
"""Independent integer checks of finite instances of a 5-adic density proof.
These tests do not certify any infinite statement.
"""
from math import comb

def check():
    N = 650
    t = [1, 1]
    checks = 0
    for n in range(2, N):
        q, rem = divmod((2*n-1)*t[-1]+3*(n-1)*t[-2], n)
        assert rem == 0
        t.append(q)
        checks += 1
    for n in range(35):
        v = sum(comb(n,2*j)*comb(2*j,j) for j in range(n//2+1))
        assert v == t[n]
        checks += 1
    for n in range(N):
        v, m = n, 1
        while v:
            m = m*t[v%5] % 5
            v //= 5
        assert t[n]%5 == m and m != 0
        checks += 1
    for k in (1,2,3):
        q=5**k
        hits = {v%q for v in t}
        assert {v for v in range(q) if v%5} <= hits
        assert not any(v%5==0 for v in hits)
        checks += len(hits)
    for n in range(1,130):
        assert (t[5*n]-t[n])%(5**(2+2*next((s for s in range(10) if n%5**(s+1)),10)))==0
        checks += 1
    for k in range(1,5):
        q=5**k
        for r in range(k-1,4):
            bound=5**(r-k+1)
            for a in range(min(bound,12)):
                for b in range(1,4):
                    n=a+5**r*b
                    if n>=N:continue
                    assert (t[n]-t[a]*t[5**r*b])%q==0,(k,r,a,b)
                    checks += 1
    for k in range(1,6):
        q=5**k
        assert len({pow(3,j,q) for j in range(4*5**(k-1))})==4*5**(k-1)
        checks += 1
    print('PASS:', checks, 'exact assertions (finite corroboration)')
if __name__=='__main__':check()
