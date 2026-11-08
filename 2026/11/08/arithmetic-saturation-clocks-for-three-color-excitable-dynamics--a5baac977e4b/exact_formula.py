#!/usr/bin/env python3
"""Exact rational histogram of activity on connected cactus graphs.
Public reproducibility utility: no external dependencies.
"""
from collections import Counter
from math import comb, factorial


def trinomial(n):
    d={0:1}
    for _ in range(n):
        e={}
        for t,v in d.items():
            for dt in [-1,0,1]:
                e[t+dt]=e.get(t+dt,0)+v
        d=e
    return d


def cactus_counts(lengths, bridges=0):
    # Counts for CCA activity, represented as a rational Fraction.
    from fractions import Fraction
    c={Fraction(0):3**(bridges+1)}
    for n in lengths:
        e={}
        for t,a in trinomial(n).items():
            if t%3==0:
                e[Fraction(abs(t),n)]=e.get(Fraction(abs(t),n),0)+a
        b={}
        for v,x in c.items():
            for w,y in e.items():
                z=max(v,w)
                b[z]=b.get(z,0)+x*y
        c=b
    return c


def main():
    for lengths,bridges in [([3,3],0),([4,4],0),([5,5],0),([3,4],1),([3,3,3],0),([4,4,4],0)]:
        d=cactus_counts(lengths,bridges)
        N=3**(1+bridges+sum(n-1 for n in lengths))
        assert sum(d.values())==N
        print('CASE',lengths,bridges,'states',N,'CCA_hist',','.join(f'{k}:{v}' for k,v in sorted(d.items())))
    for n in [6,7,8,9,10,11,12,15,18,21]:
        s=n%3;m=n-s
        a=trinomial(n)
        p=2*a[m]
        q=2*a[m-3] if m-3 else a[m-3]
        den=3**(n-1)
        print('EXTREME',n,'residue',s,'max',m,'p_num',p,'second_num',q,'den',den,
              'asympt_constant',f'6/{factorial(s)}')

if __name__=='__main__': main()
