#!/usr/bin/env python3
"""Standalone exact-moment checks for a shifted-inverse write-noise model.
The infinite-dimensional-parameter theorem uses the analytic proof, not finite tests.
Requires only Python 3's standard library.
"""
from fractions import Fraction as Q
from itertools import product
from math import isclose

def exact_enumeration(thetas, shift, sigma, weight, copies, v):
    # Every programmed entry has independent symmetric +/- sigma write noise.
    n=len(thetas)
    mu=Q(1,1)/(weight*(min(thetas)+shift))
    target=[v[i]*shift/(thetas[i]+shift) for i in range(n)]
    vals=[]
    for signs in product((-1,1),repeat=n*n*copies):
        residual=target.copy()
        for d in range(copies):
            for i in range(n):
                for j in range(n):
                    residual[i] -= mu*sigma*signs[d*n*n+i*n+j]*thetas[j]*v[j]/copies
        vals.append(sum(z*z for z in residual))
    return sum(vals,Q(0))/len(vals)

def exact_formula(thetas, shift, sigma, weight, copies, v):
    n=len(thetas)
    a=min(thetas)
    c=Q(n)*sigma*sigma/(copies*weight*weight)
    return sum(v[i]*v[i]*(shift*shift/(thetas[i]+shift)**2+c*thetas[i]**2/(a+shift)**2) for i in range(n))

def f1(b,c): return (b*b+c)/(1+b)**2
def fk(b,k,c): return b*b/(k+b)**2+c*k*k/(1+b)**2
def H(b,k): return b*b*(k+1+2*b)/(k+b)**2
def R(b,k): return b*(1+b)**3/(k+b)**3
def P(b,k): return (k+1)*(1+b)**3-k*b*(k+b)*(k+1+2*b)

def increasing_root(func,target):
    lo,hi=0.,1.
    while func(hi)<target: hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if func(mid)<target:lo=mid
        else:hi=mid
    return (lo+hi)/2

checks=0
for n in (2,3):
    for shift in (Q(0),Q(1,3),Q(2)):
        for thetas in ([Q(1),Q(2)], [Q(2),Q(5)]) if n==2 else ([Q(1),Q(3),Q(4)],):
            for v in ([Q(1)]*n, [Q(i+1,3) for i in range(n)]):
                for sigma,weight in ((Q(1,4),Q(1)),(Q(1,7),Q(3,4))):
                    x=exact_enumeration(thetas,shift,sigma,weight,1,v)
                    y=exact_formula(thetas,shift,sigma,weight,1,v)
                    assert x==y, (n,thetas,shift,x,y)
                    checks+=1
# Multi-copy second moments: 2 matrices of 2x2 random +/- errors.
for shift in (Q(0),Q(1),Q(2)):
    for v in ([Q(1),Q(0)],[Q(1,2),Q(-2,3)]):
        a=exact_enumeration([Q(1),Q(2)],shift,Q(1,4),Q(1),2,v)
        b=exact_formula([Q(1),Q(2)],shift,Q(1,4),Q(1),2,v)
        assert a==b,(a,b)
        checks+=1

# Exact-rational anchor: the optimum is a crossing at b=2, k=2, c=7/12.
k=Q(2);c=Q(7,12);b=Q(2)
assert f1(b,c)==Q(55,108) ==fk(b,k,c);checks+=1
assert H(b,k)==c*(k+1);checks+=1
assert P(b,k)<0 and R(b,k)<c*k and b>c;checks+=1
assert c*((k+b)/(1+b))**2==Q(28,27)>1;checks+=1
assert c<1 and c*k*k==Q(7,3);checks+=1
assert f1(b,c)<c*k*k;checks+=1

# The worst risk is at the spectral endpoints for convex scalar mode risks.
for k in [1.1,1.25,1.5,2,3,10,100]:
    for c in [0.0001,0.001,0.01,0.05,0.1,0.3,0.7,2,10]:
        x=increasing_root(lambda z:H(z,k), c*(k+1))
        m=increasing_root(lambda z:R(z,k), c*k)
        opt=min(x,m)
        val=max(f1(opt,c),fk(opt,k,c))
        assert x>c-1e-9
        assert abs(f1(x,c)-fk(x,k,c))<1e-9
        # Error cannot improve via lower or higher shifts.
        for factor in [.001,.05,.4,.8,.999,1.001,1.1,2,5,20]:
            y=opt*factor
            assert max(f1(y,c),fk(y,k,c)) >= val-1e-11,(k,c,x,m,opt,y)
            checks+=1
        # The intermediate eigenvalues do not beat extrema.
        for t in [1,1+.01*(k-1),1+.2*(k-1),1+.5*(k-1),1+.8*(k-1),k]:
            z=opt*opt/(t+opt)**2+c*t*t/(1+opt)**2
            assert z<=val+1e-11
            checks+=1
print('VERIFY_OK',checks,'exact moment identities and numerical root/inequality checks')
