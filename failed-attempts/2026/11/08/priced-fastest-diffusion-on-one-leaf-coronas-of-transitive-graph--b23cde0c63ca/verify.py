"""Standalone reproducibility checks for priced one-leaf corona spectral-gap formulas.

Requires Python 3 and numpy; exact tests use sympy.  Finite checks supplement,
not replace, the proof for all graph orders and all nonnegative weights.
"""
import math
from fractions import Fraction
import random
import numpy as np
import sympy as sp

COUNT = 0

def check(cond, info):
    global COUNT
    if not cond:
        raise AssertionError(info)
    COUNT += 1

def lap(n, edges, w):
    L = np.zeros((n,n))
    for (i,j),t in zip(edges,w):
        L[i,i] += t; L[j,j] += t
        L[i,j] -= t; L[j,i] -= t
    return L

def cycle(m):
    return [(i,(i+1)%m) for i in range(m)]

def complete(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def bipartite(p,q):
    return [(i,p+j) for i in range(p) for j in range(q)]

def solve(edges,n,c,B):
    mu = sorted(np.linalg.eigvalsh(lap(n, edges, [1.0]*len(edges))))[1]
    e=len(edges); a=e/mu; b=n*c; z=B/(2*a+b+2*math.sqrt(a*b))
    x=z*(2+math.sqrt(b/a))/mu
    y=z*(1+math.sqrt(a/b))
    return mu,z,x,y

rng=random.Random(31659)
for n,edges in [(m,cycle(m)) for m in range(3,18)] + [(n,complete(n)) for n in range(3,10)] + [(2*p,bipartite(p,p)) for p in range(2,7)]:
    for c in (0.2,1.,2.7):
        B=7.0
        mu,z,x,y=solve(edges,n,c,B)
        ee=edges+[(i,i+n) for i in range(n)]
        L=lap(2*n,ee,[x]*len(edges)+[y]*n)
        vals=np.linalg.eigvalsh(L)
        check(abs(vals[1]-z) < 2e-8, ('spectral',n,c,vals[1],z))
        check(abs(len(edges)*x+n*c*y-B)<2e-8,('budget',n,c))
        check(all(v>=-1e-8 for v in vals),('PSD',n,c))
        for _ in range(12):
            w=[rng.random()+0.02 for _ in ee]
            total=sum(w[:len(edges)])+c*sum(w[len(edges):])
            w=[u*B/total for u in w]
            zrand=np.linalg.eigvalsh(lap(2*n,ee,w))[1]
            check(zrand<=z+2e-8,('random contender',n,c,zrand,z))

# Exact calculations on three cycle sizes with rational Laplacian spectra and prices.
for m,c in [(3,sp.Rational(3,1)),(4,sp.Rational(2,1)),(6,sp.Rational(1,1)),(3,sp.Rational(1,3)),(4,sp.Rational(1,2)),(6,sp.Rational(4,1))]:
    lam={3:sp.Rational(3),4:sp.Rational(2),6:sp.Rational(1)}[m]
    B=sp.Rational(60)
    alpha=sp.Rational(m)/lam; beta=m*c
    d=2*alpha+beta+2*sp.sqrt(alpha*beta)
    z=sp.simplify(B/d)
    x=sp.simplify(z*(2+sp.sqrt(beta/alpha))/lam)
    y=sp.simplify(z*(1+sp.sqrt(alpha/beta)))
    check(sp.simplify(m*x+m*c*y-B)==0,('exact budget',m,c))
    edges=cycle(m)+[(i,i+m) for i in range(m)]
    L=sp.zeros(2*m)
    for (i,j),t in zip(edges,[x]*m+[y]*m):
        L[i,i]+=t; L[j,j]+=t; L[i,j]-=t; L[j,i]-=t
    F=sp.eye(2*m)-sp.ones(2*m)/(2*m)
    eigs=(L-z*F).eigenvals()
    check(all(bool(sp.simplify(t)>=0) for t in eigs),('exact PSD',m,c,eigs))
    check(sp.simplify((L-z*F).det())==0,('exact zero eigen',m,c))

for m in [3,4,5,6,8,10,20,40,80,160]:
    c=3.;B=17.
    mu,z,x,y=solve(cycle(m),m,c,B)
    lamb=4*math.sin(math.pi/m)**2
    check(abs(mu-lamb)<5e-11,('cycle mu',m))
    ratio=y/x
    rpred=math.sqrt(lamb/c)*(1+math.sqrt(c*lamb))/(2+math.sqrt(c*lamb))
    check(abs(ratio-rpred)<1e-10,('ratio',m))
    frac=m*c*y/B
    fpred=math.sqrt(c*lamb)*(1+math.sqrt(c*lamb))/(2+2*math.sqrt(c*lamb)+c*lamb)
    check(abs(frac-fpred)<1e-10,('frac',m))

print('VERIFY_OK', COUNT)
