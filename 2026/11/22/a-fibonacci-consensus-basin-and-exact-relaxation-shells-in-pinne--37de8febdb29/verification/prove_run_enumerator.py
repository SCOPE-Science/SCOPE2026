#!/usr/bin/env python3
"""Exact coefficient checks for pinned Rule-232 run counting (standard library)."""
from functools import lru_cache

def G_coefficient(n,L,u):
    """Coefficient of S(z,u)/(1-z*S(z,u)) in Z[[z]]."""
    # Numerator S=sum_{j=0}^L (uz)^j; denominator 1-sum_{j=0}^L u^j z^{j+1}.
    f=[0]*(n+1)
    for k in range(n+1):
        s=u**k if k<=L else 0
        for j in range(min(k-1,L)+1):
            if k>=j+1: s+=u**j*f[k-j-1]
        f[k]=s
    return f[n]

def parity_even(n,L):
    a=G_coefficient(n,L,1)
    b=G_coefficient(n,L,-1)
    assert (a+b)%2==0
    return (a+b)//2

def explicit_parity_count(n,L):
    count=0
    for w in range(1<<n):
        if w.bit_count()%2:continue
        run=0
        for j in range(n):
            run=run+1 if (w>>j)&1 else 0
            if run>L:break
        else:count+=1
    return count

def fibonacci(n):
    a,b=0,1
    for i in range(n): a,b=b,a+b
    return a

def no_odd_ones_runs(n):
    count=0
    for w in range(1<<n):
        r=0
        for i in range(n):
            if (w>>i)&1:r+=1
            else:
                if r&1:break
                r=0
        else:
            if not r&1:count+=1
    return count

for n in range(3,17):
    for t in range(n//2+2):
        L=2*t+1
        assert parity_even(n,L)==explicit_parity_count(n,L),(n,t)
    assert no_odd_ones_runs(n)==fibonacci(n+1),(n,no_odd_ones_runs(n))
    assert parity_even(n,2*(n//2)+1)==2**(n-1)
    last=parity_even(n,2*(n//2)+1)-parity_even(n,2*(n//2)-1)
    assert last==(1 if n%2==0 else 2),(n,last)
    print(f'n={n}: equilibrium count {parity_even(n,1)}, last shell {last}, consensus basin {fibonacci(n+1)}')
print('ENUMERATOR_OK')
