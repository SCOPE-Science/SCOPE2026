#!/usr/bin/env python3
"""Independent binomial-sum formula for powers of (1+z)^2+z^3."""
from math import comb

def choose(n,r):
    return comb(n,r) if 0<=r<=n else 0

def a(k,r):
    return sum(comb(k,j)*choose(2*(k-j),r-3*j) for j in range(k+1))

def p(k,r):
    v=a(k,r)+a(k,3*k-r)
    if r==0:v-=1
    if r==2:v+=2*k
    if r==3:v+=k
    return v

def unimodal(c):
    falling=False
    for x,y in zip(c,c[1:]):
        if y<x:falling=True
        if y>x and falling:return False
    return True

if __name__=='__main__':
    assert a(1,0)==1 and a(1,1)==2 and a(1,2)==1 and a(1,3)==1
    for k in range(1,104):
        c=[p(k,r) for r in range(3*k+1)]
        assert unimodal(c)==(k<103)
        if k==103:
            print('central_binomial_check',*(c[r] for r in [153,154,155,156]))
            print('middle_valley_positive',c[153]-c[154]>0)
    print('BINOMIAL_VERIFY_OK')
