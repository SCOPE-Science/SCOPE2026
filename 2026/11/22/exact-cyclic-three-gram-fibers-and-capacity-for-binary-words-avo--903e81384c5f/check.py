#!/usr/bin/env python3
"""Verify small cyclic three-gram reconstruction fibers of the no-11 binary source."""
from collections import defaultdict
from itertools import product
from math import comb, gcd


def phi(d):
    return sum(gcd(j,d)==1 for j in range(1,d+1))


def fiber(n,r,t):
    if r==0: return 1
    if t==0: return int(n==2*r)
    if not (1<=t<=r and n>=2*r+t): return 0
    R=n-2*r-t
    g=gcd(gcd(r,t),R)
    return sum(phi(h)*comb(r//h,t//h)*comb(R//h+t//h-1,t//h-1)
               for h in range(1,g+1) if g%h==0)//r


def canonical(w):
    return min(w[i:]+w[:i] for i in range(len(w)))


def signature(w):
    n=len(w)
    return tuple(sum(tuple(w[(i+j)%n] for j in range(3))==p for i in range(n))
                 for p in product((0,1),repeat=3))


def capacity(n):
    return 1+int(n%2==0)+sum(min(r,n-2*r) for r in range(1,n//2+1))


def singleton(n):
    return (1+int(n%2==0)+(n-1)//2
            +int(n>=6 and n%3==0)
            +int(n>=7 and n%3==1)
            +int(n>=8 and n%3==2))


def main():
    for n in range(1,16):
        fibers=defaultdict(set)
        for tup in product((0,1),repeat=n):
            if any(tup[i] and tup[(i+1)%n] for i in range(n)):
                continue
            c=canonical(tup)
            fibers[signature(tup)].add(c)
        observed={(sum(next(iter(v))),sig[5]):len(v)
                  for sig,v in fibers.items()}
        expected={(0,0):1}
        for r in range(1,n//2+1):
            if 2*r==n: expected[(r,r)]=1
            for t in range(1,min(r,n-2*r)+1):
                expected[(r,r-t)]=fiber(n,r,t)
        assert observed==expected, (n,observed,expected)
        assert len(fibers)==capacity(n), n
        assert sum(len(v)==1 for v in fibers.values())==singleton(n), n
        if n<=7: assert all(len(v)==1 for v in fibers.values())
        if n==8: assert max(map(len,fibers.values()))==2
        print(f'n={n:2d} profiles={len(fibers):2d} singleton={singleton(n):2d} necklaces={sum(map(len,fibers.values())):3d}')
    print('PASS: all cyclic input words and whole profile fibers through n=15')

if __name__=='__main__': main()
