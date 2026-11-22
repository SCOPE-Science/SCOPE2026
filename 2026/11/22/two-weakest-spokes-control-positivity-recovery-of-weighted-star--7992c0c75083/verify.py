"""Supplementary checks for positivity of weighted-star biharmonic resolvents.

This checks finite examples only; the accompanying proof establishes all weights
and all step sizes.
"""
from fractions import Fraction as Q
from random import Random
from math import isclose

def star_laplacian(w):
    n = len(w) + 1
    a = [[Q(0) for _ in range(n)] for _ in range(n)]
    for k, v in enumerate(w, 1):
        a[0][0] += v
        a[0][k] = a[k][0] = -v
        a[k][k] = v
    return a

def multiply(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def invert(a):
    n = len(a)
    b = [[Q(v) for v in row] + [Q(i==j) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        pivot = next(r for r in range(k,n) if b[r][k])
        b[k],b[pivot] = b[pivot],b[k]
        v = b[k][k]
        b[k] = [x/v for x in b[k]]
        for i in range(n):
            if i != k:
                v = b[i][k]
                b[i] = [x-v*y for x,y in zip(b[i],b[k])]
    return [row[n:] for row in b]

def resolvent(w,h):
    l=star_laplacian(w)
    l2=multiply(l,l)
    return invert([[Q(i==j)+h*l2[i][j] for j in range(len(l))] for i in range(len(l))])

def scalar_F(h,w):
    a,b=w[:2]
    return Q(1)/h-(len(w)+1)*a*b+sum(
        ((z-a)*(z-b))/(1+h*z*z) for z in w[2:]
    )

def root(w):
    a,b=[float(t) for t in w[:2]]
    lo,hi=0.,(len(w)-1)/((len(w)+1)*a*b)
    fw=[float(x) for x in w]
    for _ in range(90):
        x=(lo+hi)/2
        y=1/x-(len(fw)+1)*a*b+sum((z-a)*(z-b)/(1+x*z*z) for z in fw[2:])
        if y>0:lo=x
        else:hi=x
    return (lo+hi)/2

def run():
    rng=Random(20261116)
    exact=0
    for m in range(2,7):
        for case in range(14):
            w=sorted(Q(rng.randint(1,17),rng.randint(1,9)) for _ in range(m))
            h=Q(rng.randint(1,40),rng.randint(1,30))
            r=resolvent(w,h)
            assert all(r[i][i]>0 for i in range(m+1))
            assert all(r[0][i]>0 for i in range(1,m+1))
            assert all(sum(row)==1 for row in r)
            f=scalar_F(h,w)
            assert (r[1][2]>0)==(f<0) and (r[1][2]<0)==(f>0) or (r[1][2]==0 and f==0)
            if r[1][2]>=0:
                assert all(r[i][j]>=0 for i in range(1,m+1) for j in range(i+1,m+1))
            exact+=1
    bounds=0
    for m in (2,3,4,7,12):
        for case in range(60):
            w=sorted(10**rng.uniform(-1.5,1.5) for _ in range(m))
            t=root(w)
            low=1/((m+1)*w[0]*w[1])
            high=(m-1)/((m+1)*w[0]*w[1])
            assert low*(1-1e-12)<=t<=high*(1+1e-12)
            bounds+=1
    # The equal-weight formula and asymptotic sharp upper ratio.
    for m in range(2,12):
        assert isclose(root([Q(1)]*m),1/(m+1),rel_tol=1e-12)
    for m in range(3,10):
        w=[1.,2.]+[1e9]*(m-2)
        assert isclose(root(w),(m-1)/(2*(m+1)),rel_tol=2e-7)
    print(f'PASS: {exact} exact-rational resolvent checks, {bounds} threshold-bound checks, 17 limiting/equal-weight cases')
if __name__=='__main__':run()
