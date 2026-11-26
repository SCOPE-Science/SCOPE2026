#!/usr/bin/env python3
"""Exhaustive independent consistency check for two-deletion shadow moments.
No random samples or external data are used.
"""
from itertools import product,combinations
from fractions import Fraction
from math import comb

def formula_word(x):
    n=len(x); m=n-1
    t=[int(x[i]!=x[i+1]) for i in range(m)]
    a=sum(x[i]==x[i+1] and x[i+1]!=x[i+2] for i in range(n-2))
    b=sum(x[i]==x[i+2] and x[i]!=x[i+1] for i in range(n-2))
    z=sum(t)
    return 1+z*(z+1)//2-t[-1]+a-b

def distinct_subseq(x):
    return len({tuple(x[j] for j in range(len(x)) if j not in skip)
                for skip in combinations(range(len(x)),2)})

def moments(q,n):
    p=Fraction(q-1,q);h=1-p;m=n-1
    mean=1+(m-1)*p+comb(m,2)*p*p
    var=(m-1)*p*h*(-1+2*p+Fraction(m,2)*p+Fraction(m*(2*m-3),2)*p*p)
    return mean,var

if __name__=='__main__':
    nwords=0
    for q,nmax in [(2,12),(3,9),(4,7),(5,6)]:
        for n in range(2,nmax+1):
            total=0;total2=0;count=0
            for x in product(range(q),repeat=n):
                b=distinct_subseq(x)
                f=formula_word(x)
                assert b==f, (q,n,x,b,f)
                total+=b; total2+=b*b; count+=1
            em=Fraction(total,count)
            ev=Fraction(total2,count)-em*em
            assert (em,ev)==moments(q,n), (q,n,em,ev,moments(q,n))
            nwords+=count
            print(f'q={q:2d} n={n:2d} words={count:6d} mean={em} variance={ev}')
    print('PASS total source words',nwords)
