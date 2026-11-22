#!/usr/bin/env python3
"""Checks explicit constrained interleaving witness families over a finite range."""
from math import isqrt

def is_prime(v):
    if v<2:return False
    return not any(v%d==0 for d in range(2,isqrt(v)+1))

def compose_sig(w):
    n=len(w)
    out=[]
    for k in range(1,n+1):
        c=[0]*(k+1)
        h=sum(x=='1' for x in w[:k]);c[h]+=1
        for i in range(k,n):
            h+=(w[i]=='1')-(w[i-k]=='1');c[h]+=1
        out.extend(c)
    return tuple(out)

def interleave(s,t):return s+''.join(ch+s for ch in t)

def admissible(w):return '11' not in w

def test(a,b):
    assert a>=5 and b>=3
    s='01'+'0'*(a-3)
    t='1'+'0'*(b-2)
    u,v=interleave(s,t),interleave(s,t[::-1])
    assert len(u)==a*b-1==len(v)
    assert admissible(u) and admissible(v)
    assert u!=v and u!=v[::-1]
    assert compose_sig(u)==compose_sig(v), (a,b)

if __name__=='__main__':
    tests=0
    for m in range(2,150):
        factors=[(a,m//a) for a in range(5,m+1) if m%a==0 and m//a>=3]
        expect=not (is_prime(m) or (m%2==0 and is_prime(m//2)) or m in (8,9,12,16))
        assert bool(factors)==expect,m
        if factors:
            a,b=factors[0]
            test(a,b);tests+=1
    print('CONSTRUCTION_OK',tests,'admissible non-reversal equicomposable witnesses for m<150')
