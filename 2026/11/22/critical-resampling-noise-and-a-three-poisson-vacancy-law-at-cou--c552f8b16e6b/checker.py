"""Independent exact finite tests for noise-resampled coupon vacancies.
Standard library only. This file contains mathematical verification, not a certificate of asymptotic claims.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial


def falling(n,k):
    p=1
    for j in range(k):p*=n-j
    return p


def exact_factorial_moment(n,m,p,q,s,t,u):
    """Ordered s common, t first-only, u second-only vacant boxes."""
    if s+t+u>n:return Fraction(0)
    eps=Fraction(p,q)
    z=Fraction(0)
    for i in range(t+1):
        for j in range(u+1):
            A=s+t+j
            B=s+u+i
            both=s+i+j
            one=1-Fraction(A+B,n)+(1-eps)*Fraction(both,n)+eps*Fraction(A*B,n*n)
            z+=(-1)**(i+j)*comb(t,i)*comb(u,j)*one**m
    return falling(n,s+t+u)*z


def exhaustive_distribution(n,m,p,q):
    vals={}
    labels=range(n)
    total=(q**m)*(n**(2*m))
    for x in product(labels,repeat=m):
        absent_x=set(labels)-set(x)
        for y in product(labels,repeat=m):
            absent_y=set(labels)-set(y)
            c=len(absent_x&absent_y)
            l=len(absent_x-absent_y)
            r=len(absent_y-absent_x)
            weight=1
            for a,b in zip(x,y):
                weight*=n*(q-p)*(a==b)+p
            vals[c,l,r]=vals.get((c,l,r),0)+weight
    assert sum(vals.values())==total
    return vals,total


def verify(n,m,p,q):
    dist,total=exhaustive_distribution(n,m,p,q)
    count=0
    for s in range(4):
      for t in range(4-s):
       for u in range(4-s-t):
        empirical=Fraction(sum(w*falling(c,s)*falling(l,t)*falling(r,u) for (c,l,r),w in dist.items()),total)
        predicted=exact_factorial_moment(n,m,p,q,s,t,u)
        assert predicted==empirical,(n,m,p,q,s,t,u,predicted,empirical)
        count+=1
    eps=Fraction(p,q)
    a=(1-Fraction(1,n))**m
    b=(1-Fraction(1+eps,n)+eps/Fraction(n*n))**m
    d=(1-Fraction(2,n)+eps/Fraction(n*n))**m
    expected_cov=n*b+n*(n-1)*d-n*n*a*a
    ec=Fraction(sum(w*(l+c)*(r+c) for (c,l,r),w in dist.items()),total)
    ea=Fraction(sum(w*(l+c) for (c,l,r),w in dist.items()),total)
    eb=Fraction(sum(w*(r+c) for (c,l,r),w in dist.items()),total)
    assert ec-ea*eb==expected_cov
    return count+1,len(dist)


def main():
    cases=[(2,1,0,1),(2,3,1,2),(3,3,0,1),(3,3,1,2),(3,4,1,3),(3,5,2,3),(4,3,1,2),(4,4,1,3)]
    tests=0
    for n,m,p,q in cases:
        c,k=verify(n,m,p,q);tests+=c
        print(f'n={n}, m={m}, epsilon={p}/{q}: {c} rational identities, {k} states')
    print(f'PASS {tests} exact identities; proof of asymptotic limits is separate')
if __name__=='__main__':main()
