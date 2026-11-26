#!/usr/bin/env python3
"""Independent finite checks for the five-frequency cross fourth-moment theorem.

Requires Python 3.10+ standard library only. Universal validity is supplied by
an exact algebraic proof, not by this finite checker.
"""
import cmath
import math
import random
from collections import defaultdict
from fractions import Fraction

FREQUENCIES=((0,0),(1,0),(-1,0),(0,1),(0,-1))
K=Fraction(27,11)
checks=0

def require(b,message):
    global checks
    assert b,message
    checks+=1

def norm4_by_sums(coeff):
    conv=defaultdict(complex)
    for j,p in enumerate(FREQUENCIES):
        for k,q in enumerate(FREQUENCIES):
            conv[p[0]+q[0],p[1]+q[1]]+=coeff[j]*coeff[k]
    return sum(abs(v)**2 for v in conv.values())

def norm4_by_differences(coeff):
    d=dict(zip(FREQUENCIES,coeff))
    cov=defaultdict(complex)
    for j,p in enumerate(FREQUENCIES):
        for k,q in enumerate(FREQUENCIES):
            cov[p[0]-q[0],p[1]-q[1]]+=coeff[j]*coeff[k].conjugate()
    return sum(abs(v)**2 for v in cov.values())

def grid_moment(coeff,N,M):
    out=0.
    for j in range(N):
        z=cmath.exp(2j*math.pi*j/N)
        for k in range(M):
            w=cmath.exp(2j*math.pi*k/M)
            out+=abs(coeff[0]+coeff[1]*z+coeff[2]/z+coeff[3]*w+coeff[4]/w)**4
    return out/(N*M)

def defect(coeff):
    S=sum(abs(v)**2 for v in coeff)
    a,b,c,d,e=(v/math.sqrt(S) for v in coeff)
    x=abs(b)**2+abs(c)**2
    y=abs(d)**2+abs(e)**2
    s=x+y
    q=abs(b*c)
    t=abs(d*e)
    dh=x/2-q
    dv=y/2-t
    aligned=[abs(v) for v in (a,b,c,d,e)]
    pi=norm4_by_sums(aligned)-norm4_by_sums((a,b,c,d,e))
    terms=(11/4)*(s-8/11)**2+(3/4)*(x-y)**2
    terms+=2*(2*(1-s)*(dh+dv)+dh*(x/2+q)+dv*(y/2+t)+x*y-4*q*t)
    terms+=pi
    return terms,pi

def run():
    rng=random.Random(20261024)
    for _ in range(1500):
        c=[complex(rng.uniform(-2,2),rng.uniform(-2,2)) for j in range(5)]
        S=sum(abs(t)**2 for t in c)
        qa=norm4_by_sums(c)/S**2
        qb=norm4_by_differences(c)/S**2
        require(abs(qa-qb)<1e-11,'pair-sum versus autocorrelation')
        require(qa<=float(K)+1e-11,'sharp bound')
        rem,pi=defect(c)
        require(abs(float(K)-qa-rem)<2e-11,'exact normalized defect identity')
        require(pi>=-1e-11,'phase majorization')
    # Exact integer coefficient sums/correlations and rational sharp bound.
    for j in range(300):
        c=[complex(rng.randrange(-4,5),rng.randrange(-4,5)) for _ in range(5)]
        if not any(c):continue
        S=int(sum(abs(t)**2 for t in c))
        y=norm4_by_sums(c)
        require(int(y)*11<=27*S*S,'exact integer inequality')
    # Finite grids of both cyclic orders at least five are nonaliasing.
    for N,M in ((5,5),(5,6),(6,8),(7,5),(8,9),(9,11)):
        for j in range(30):
            c=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(5)]
            require(abs(norm4_by_sums(c)-grid_moment(c,N,M))<1e-9,
                    'finite-grid Fourier moment')
    for j in range(110):
        alpha=rng.uniform(-math.pi,math.pi)
        beta=rng.uniform(-math.pi,math.pi)
        lam=complex(rng.uniform(-2,2),rng.uniform(-2,2))
        z=cmath.exp(1j*alpha)
        w=cmath.exp(1j*beta)
        c=[lam*math.sqrt(3),lam*math.sqrt(2)*z,lam*math.sqrt(2)/z,
           lam*math.sqrt(2)*w,lam*math.sqrt(2)/w]
        S=sum(abs(t)**2 for t in c)
        require(abs(norm4_by_sums(c)/S**2-float(K))<2e-12,'rigid extremizer')
        rem,pi=defect(c)
        require(abs(rem)<2e-11 and abs(pi)<2e-11,'zero deficit at extremizer')
    print('PASS:',checks,'independent finite verification assertions')

if __name__=='__main__':run()
