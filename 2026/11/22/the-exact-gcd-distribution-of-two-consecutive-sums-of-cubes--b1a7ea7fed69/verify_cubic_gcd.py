#!/usr/bin/env python3
"""Reproducible finite tests for a local gcd law for shifted cubic sums.
No external packages or network are required. These tests do not replace the infinite proof.
"""
from math import gcd
from collections import Counter

def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))

def pair_zero(x,y,m):
    return ((pow(x,3,m)+pow(y,3,m))%m == 0 and
            (pow(x+1,3,m)+pow(y+1,3,m))%m == 0)

def count_direct(q):
    return sum(pair_zero(x,y,q) for x in range(q) for y in range(q))

def pred(p,k):
    if p == 2: return {1:2, 2:4, 3:8}.get(k,0)
    if p == 3 or p%3==2: return 0
    return 6

def main():
    tested=0
    for p in range(2,42):
        if not is_prime(p):continue
        k=1
        while p**k<=400:
            got=count_direct(p**k)
            expected=pred(p,k)
            assert got==expected,(p,k,got,expected)
            tested+=1
            k+=1
    # Test all dyadic depths through modulus 256 by lifting the actual solution set.
    sols=[(0,0)]
    modulus=1
    for k in range(1,9):
        q=modulus*2
        next_sols=[(x+a*modulus,y+b*modulus) for x,y in sols
                   for a in (0,1) for b in (0,1)
                   if pair_zero(x+a*modulus,y+b*modulus,q)]
        assert len(next_sols)==pred(2,k), (k,len(next_sols))
        sols,modulus=next_sols,q
        if not sols: break
    # Check simple roots and each root's one-and-only-one lifting.
    lifts=0
    for p in (7,13,19,31):
        sol=[(x,y) for x in range(p) for y in range(p) if pair_zero(x,y,p)]
        assert len(sol)==6
        for x,y in sol:
            det=(9*(x-y)*(2*x*y+x+y))%p
            assert det != 0,(p,x,y)
            count=sum(pair_zero(x+a*p,y+b*p,p*p)
                       for a in range(p) for b in range(p))
            assert count==1,(p,x,y,count)
            lifts+=1
    checked=0
    for x in range(1,151):
        for y in range(1,151):
            g=gcd(x**3+y**3,(x+1)**3+(y+1)**3)
            assert g%3!=0 and g%16!=0,(x,y,g)
            for p in range(5,500):
                if is_prime(p) and g%p==0:
                    assert p%3==1,(x,y,g,p)
            checked+=1
    print('PASS: %d exhaustive prime-power modulus tests' % tested)
    print('PASS: all dyadic lifting levels through the first empty one')
    print('PASS: %d smooth-root single-lift checks' % lifts)
    print('PASS: %d positive integer pairs satisfy the support restrictions' % checked)

if __name__ == '__main__':main()
