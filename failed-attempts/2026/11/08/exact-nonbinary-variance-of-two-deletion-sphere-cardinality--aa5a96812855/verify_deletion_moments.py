#!/usr/bin/env python3
"""Independent exact checks for q-ary two-deletion sphere moments."""
from itertools import product,combinations
from fractions import Fraction

def expected_moments(q,n):
    m=n-1
    mean=Fraction((q-1)**2*m*m+(q*q-1)*m+2*q,2*q*q)
    var=Fraction((m-1)*(q-1)*(2*m*m*(q-1)**2+m*(-2*q*q+5*q-3)+2*q*q-4*q),2*q**4)
    return mean,var

def formula_size(w):
    runs=[]
    for v in w:
        if runs and runs[-1][0]==v: runs[-1][1]+=1
        else:runs.append([v,1])
    r=len(runs)
    h=sum(b>=2 for a,b in runs)
    t=sum(runs[i][1]==1 and runs[i-1][0]==runs[i+1][0] for i in range(1,r-1))
    return r*(r-1)//2+h-t

def oracle_size(w):
    n=len(w)
    return len({tuple(w[k] for k in range(n) if k!=i and k!=j)
                for i,j in combinations(range(n),2)})

def run(q,n):
    total=total_sq=0
    count=q**n
    for w in product(range(q),repeat=n):
        b=oracle_size(w)
        f=formula_size(w)
        if b!=f: raise AssertionError(('pointwise',q,n,w,b,f))
        total+=b;total_sq+=b*b
    mean=Fraction(total,count)
    var=Fraction(total_sq,count)-mean**2
    em,ev=expected_moments(q,n)
    if (mean,var)!=(em,ev):
        raise AssertionError(('moments',q,n,(mean,var),(em,ev)))
    print('OK',q,n,count,'mean',mean,'variance',var)

if __name__=='__main__':
    for q,nmax in [(2,11),(3,8),(4,7),(5,6)]:
        for n in range(2,nmax+1): run(q,n)
    print('VERIFY_OK')
