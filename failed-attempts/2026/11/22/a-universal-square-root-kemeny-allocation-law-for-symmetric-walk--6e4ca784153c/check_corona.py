#!/usr/bin/env python3
"""Standalone exact checks for Kemeny optimization on leaf coronas.

Requires Python 3 and SymPy.  All graph and inverse-trace checks use
rational arithmetic.  Floating-point calculations are asymptotic sanity tests,
not the proof of the universal optimization theorem.
"""
from fractions import Fraction
from math import sqrt
import sympy as sp

checks = 0

def require(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

def cycle_edges(n):
    return sorted({tuple(sorted((i, (i+1) % n))) for i in range(n)})

def clique_edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def cube_edges(d):
    return [(i, i^(1<<j)) for i in range(1<<d) for j in range(d) if i < (i^(1<<j))]

def laplacian(n, weighted_edges):
    L=sp.zeros(n)
    for i,j,w in weighted_edges:
        L[i,i]+=w;L[j,j]+=w
        L[i,j]-=w;L[j,i]-=w
    return L

def kemeny_from_L(L):
    n=L.rows
    return sp.trace((L+sp.ones(n)/n).inv())-1

def corona_L(n, E, r, a, b):
    return laplacian((r+1)*n,[(i,j,a) for i,j in E]+[(i,n+i*r+j,b) for i in range(n) for j in range(r)])

families = ([('cycle', n, cycle_edges(n), 2) for n in range(3,9)]
          + [('clique',n,clique_edges(n),n-1) for n in range(2,8)]
          + [('cube',2**d,cube_edges(d),d) for d in range(1,4)])

for family,n,E,d in families:
    require(len(E)*2==n*d, f'{family} regularity')
    L=laplacian(n,[(i,j,sp.Integer(1)) for i,j in E])
    C=kemeny_from_L(L)
    require(C>0, f'{family} nonzero inverse trace')
    # Distinct rational test weights and one, two, or three leaves per core.
    for r in (1,2,3) if n<=6 else (1,):
        for a,b in [(sp.Rational(1,3*(d+r)),sp.Rational(1,3*(d+r))),
                    (sp.Rational(1,2*(d+r)),sp.Rational(1,4*(d+r)))]:
            require(d*a+r*b<=1, 'stochastic row budget')
            full=kemeny_from_L(corona_L(n,E,r,a,b))
            A=sp.Rational(n*r,1)-sp.Rational(r,r+1)
            expected=A/b+(r+1)*C/a
            require(sp.factor(full-expected)==0,f'{family} n={n} r={r} spectral transfer')
    if family=='cycle':
        require(C==sp.Rational(n*n-1,12), 'exact cycle inverse trace')
    if family=='clique':
        require(C==sp.Rational(n-1,n), 'exact clique inverse trace')
    if family=='cube':
        require(C==sum(sp.Rational(sp.binomial(d,k),2*k) for k in range(1,d+1)), 'cube eigenvalues')

# Exact algebra of the generalized minimizer R/u+S/(1-u).
for n in range(2,31):
    for d,C in [(2,sp.Rational(n*n-1,12)),
                (n-1,sp.Rational(n-1,n))]:
        for r in (1,2,3):
            A=sp.Rational(n*r,1)-sp.Rational(r,r+1)
            R=r*A; S=(r+1)*d*C
            x,y=sp.sqrt(R),sp.sqrt(S)
            u=x/(x+y); b=u/r; a=(1-u)/d
            objective=sp.simplify(A/b+(r+1)*C/a)
            minimum=sp.simplify((x+y)**2)
            require(sp.simplify(objective-minimum)==0,'exact minimal value')
            require(sp.simplify(R/(u*u)-S/((1-u)**2))==0,'stationarity')
            require(float(b)>0 and float(a)>0 and abs(float(d*a+r*b)-1)<1e-12,'interior, saturation')

for n in [10000,100000,1000000]:
    A=n-.5
    Ccycle=(n*n-1)/12
    B=4*Ccycle
    b=sqrt(A)/(sqrt(A)+sqrt(B))
    opt=(sqrt(A)+sqrt(B))**2
    naive=3*(A+2*Ccycle)
    require(abs(b*sqrt(n/3)-1)<.05,'cycle square-root scale')
    require(abs((naive/opt)-1.5)<.06,'cycle penalty')
    Cclique=(n-1)/n; B=2*(n-1)*Cclique
    b=sqrt(A)/(sqrt(A)+sqrt(B))
    opt=(sqrt(A)+sqrt(B))**2
    naive=n*(A+2*Cclique)
    require(abs(b-1/(1+sqrt(2)))<.05,'clique half-pendant limit')
    require(abs((naive/opt)/(n/(3+2*sqrt(2)))-1)<.05,'clique linear penalty')

# Fixed pendant multiplicities: two distinct core-growth regimes.
for r in (1,2,3,5):
    for n in (10000000,100000000):
        A=r*(n-1/(r+1))
        R=r*A
        cyc_C=(n*n-1)/12
        S=(r+1)*2*cyc_C
        u=sqrt(R)/(sqrt(R)+sqrt(S)); b=u/r
        opt=(sqrt(R)+sqrt(S))**2
        ordinary=(r+2)*(A+(r+1)*cyc_C)
        require(abs(b*sqrt((r+1)*n/6)-1)<.07,'multi-leaf cycle pendant law')
        require(abs(opt/((r+1)*n*n/6)-1)<.08,'multi-leaf cycle optimal Kemeny')
        require(abs(ordinary/opt-(r+2)/2)<.1,'multi-leaf cycle cost penalty')
        cli_C=(n-1)/n
        S=(r+1)*(n-1)*cli_C
        u=sqrt(R)/(sqrt(R)+sqrt(S)); b=u/r
        opt=(sqrt(R)+sqrt(S))**2
        ordinary=(n-1+r)*(A+(r+1)*cli_C)
        lim=r+sqrt(r+1)
        require(abs(b-1/lim)<.025,'multi-leaf clique pendant law')
        require(abs(opt/(lim*lim*n)-1)<.03,'multi-leaf clique optimal Kemeny')
        require(abs((ordinary/opt)/n-r/(lim*lim))<.03,'multi-leaf clique penalty')

print(f'PASS: {checks} independent algebraic/matrix/asymptotic assertions')
