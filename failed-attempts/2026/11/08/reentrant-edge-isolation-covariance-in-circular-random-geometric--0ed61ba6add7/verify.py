#!/usr/bin/env python3
"""Exact and finite-grid checks for edge--isolation dependence on a circle."""
from fractions import Fraction as F
from itertools import product
from math import comb

def circle_cov(n,r):
    r=F(r); assert n>=2 and 0<r<F(1,2)
    q=1-2*r
    h=1 if r>=F(1,3) else 1-((q-r)/q)**2
    return F(comb(n,2))*q**(n-1)*((n-2)*h-2*n*r)

def algebra_cov(n,r):
    r=F(r); q=1-2*r
    if r<F(1,3):
        f=-r*(8*n*r*r-(3*n+10)*r+4)/q**2
    else:
        f=(n-2)-2*n*r
    return comb(n,2)*q**(n-1)*f

def lattice_cov_formula(n,m,r):
    r=F(r); assert 0<r<F(1,2)
    is_neighbor=lambda a,b: min(abs(a-b),m-abs(a-b))*r.denominator<=r.numerator*m
    b=sum(is_neighbor(0,j) for j in range(m))
    good=[j for j in range(m) if not is_neighbor(0,j)]
    h=F(sum(is_neighbor(i,j) for i in good for j in good),len(good)**2)
    q=F(len(good),m)
    return F(comb(n,2))*q**(n-1)*((n-2)*h-n*F(b,m))

def brute_lattice(n,m,r):
    r=F(r)
    isum=esum=eisum=0
    for sample in product(range(m),repeat=n):
        ds=[]
        for a in range(n):
            for b in range(a+1,n):
                d=min(abs(sample[a]-sample[b]),m-abs(sample[a]-sample[b]))
                if F(d,m)<=r:ds.append((a,b))
        e=len(ds)
        deg=[0]*n
        for a,b in ds:deg[a]+=1;deg[b]+=1
        i=deg.count(0)
        isum+=i;esum+=e;eisum+=e*i
    den=m**n
    return F(eisum,den)-F(esum,den)*F(isum,den)

def checks():
    tests=0
    for n in range(2,65):
        for r in [F(1,100),F(1,20),F(1,10),F(1,4),F(3,10),F(1,3),F(7,20),F(2,5),F(49,100)]:
            assert circle_cov(n,r)==algebra_cov(n,r)
            tests+=1
    # Conclusive rational sign tests away from exact crossing, including n=6.
    for n,r,sgn in [(5,F(3,10),-1),(6,F(1,5),-1), (6,F(1,4),0),
                    (6,F(3,10),1),(6,F(1,3),0),(6,F(2,5),-1),
                    (7,F(1,5),-1),(7,F(3,10),1),(7,F(2,5),-1),
                    (10,F(1,5),1),(10,F(2,5),0),(10,F(9,20),-1)]:
        c=circle_cov(n,r)
        assert (c>0)-(c<0)==sgn, (n,r,c,sgn)
        tests+=1
    for n,m,r in [(3,5,F(1,4)),(3,7,F(1,3)),(4,5,F(1,4)),(4,7,F(2,5)),(5,5,F(1,4))]:
        x=brute_lattice(n,m,r)
        y=lattice_cov_formula(n,m,r)
        assert x==y,(n,m,r,x,y)
        tests+=1
    # Lattice approximation of continuum: finite grids are a different model.
    for n,r in [(5,F(1,5)),(6,F(3,10)),(7,F(7,20)),(9,F(1,5))]:
        t=circle_cov(n,r)
        e1=abs(lattice_cov_formula(n,501,r)-t)
        e2=abs(lattice_cov_formula(n,2001,r)-t)
        assert e2<e1 and e2<F(1,30), (n,r,e1,e2)
        tests+=1
    print('PASS',tests,'exact algebraic, sign, finite-grid and convergence assertions')
    print('n=6, r=3/10 exact covariance =',circle_cov(6,F(3,10)))
    print('n=6, r=2/5 exact covariance =',circle_cov(6,F(2,5)))

if __name__=='__main__':checks()
