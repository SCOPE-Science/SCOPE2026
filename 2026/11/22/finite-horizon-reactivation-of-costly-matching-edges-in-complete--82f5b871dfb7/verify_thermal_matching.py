"""Reproduce exact spectra and optimal budgets for priced perfect matching heat-trace design.
Requires Python 3, NumPy, SciPy and SymPy; verification is corroborative, not an infinite proof.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.linalg import expm
import sympy as sp

checks = 0

def check(condition, msg):
    global checks
    if not condition:
        raise AssertionError(msg)
    checks += 1

def weighted_laplacian(m,a,b, symbolic=False):
    n=2*m
    z=sp.zeros(n,n) if symbolic else np.zeros((n,n),dtype=float)
    for i in range(n):
        for j in range(i+1,n):
            w=b if i//2==j//2 else a
            z[i,i]+=w; z[j,j]+=w
            z[i,j]-=w; z[j,i]-=w
    return z

def optimum(m,B,r,t):
    n=2*m; c=B/m; d=n-2
    if r>=2.0:
        b=0.0
    else:
        threshold=d/(2*c)*math.log(r/(2-r))
        b=max(0.0,(c/d*2-math.log(r/(2-r))/t)/(2*(d+r)/d)) if t>threshold else 0.0
    a=(c-r*b)/d
    return a,b

def exact_spectrum_check(m, anum, bnum):
    n=2*m
    a=sp.Rational(anum,31);b=sp.Rational(bnum,37)
    L=weighted_laplacian(m,a,b,True)
    X=sp.Symbol('X')
    ch=sp.factor(L.charpoly(X).as_expr())
    expected=sp.expand(X*(X-((n-2)*a+2*b))**m*(X-n*a)**(m-1))
    check(sp.simplify(ch-expected)==0,f'characteristic polynomial n={n}')
    check(sp.trace(L)==m*((n-2)*a+2*b)+(m-1)*n*a,f'trace n={n}')

for m in range(2,8):
    for anum,bnum in [(1,0),(5,2),(1,1),(8,11),(0,9)]:
        exact_spectrum_check(m,anum,bnum)

for m in range(2,11):
    for B in [0.7,1.,3.]:
        for r in [1.01,1.2,1.5,1.9,1.999,2.,2.05,3.,8.]:
            n=2*m; c=B/m; d=n-2
            threshold=d/(2*c)*math.log(r/(2-r)) if r<2 else math.inf
            for t in [0.001,0.03,0.3,1.,3.,10.,100.,1000.]:
                a,b=optimum(m,B,r,t)
                check(a>=-1e-12 and b>=-1e-12 and abs(m*(d*a+r*b)-B)<1e-10,'feasible')
                if r>=2 or t<=threshold:
                    check(b==0.0,'deleted regime')
                else:
                    check(b>0 and b<a,'activated but discounted')
                lamA=d*a+2*b; lamS=n*a
                F=1+m*math.exp(-t*lamA)+(m-1)*math.exp(-t*lamS)
                if n<=12 and t<=100:
                    empirical=float(np.trace(expm(-t*weighted_laplacian(m,a,b))))
                    check(abs(empirical-F)<1e-9,'matrix exponential spectrum')
                # sample two-sided independent feasible pair-invariant perturbations
                for frac in (0.,0.15,0.35,0.65,0.9,1.):
                    trialb=frac*c/r
                    triala=(c-r*trialb)/d
                    trial=1+m*math.exp(-t*(d*triala+2*trialb))+(m-1)*math.exp(-t*n*triala)
                    check(F<=trial+1e-11,'symmetric global minimum numerical')

# Unrestricted nonsymmetric allocations: compare trace exp against the exact optimum.
rng=np.random.default_rng(12817)
for m in range(2,6):
  n=2*m
  edges=[(i,j) for i in range(n) for j in range(i+1,n)]
  for r in (1.1,1.5,1.99,2.,3.):
    for t in (0.2,2.,25.):
      B=1.; a,b=optimum(m,B,r,t)
      opt=1+m*np.exp(-t*((n-2)*a+2*b))+(m-1)*np.exp(-t*n*a)
      for _ in range(10):
        v=rng.dirichlet(np.ones(len(edges)))*B
        L=np.zeros((n,n))
        for k,(i,j) in enumerate(edges):
          w=v[k]/(r if i//2==j//2 else 1.)
          L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
        check(np.trace(expm(-t*L))>=opt-1e-10,'unrestricted sampled feasible')

# Scaling law for t=theta*n*n/B (r fixed, 1<r<2).
for r in (1.1,1.5,1.9):
  q=math.log(r/(2-r))
  for theta in (q/8,q/4,q/2,q,3*q):
    pred=max(0.,1.-q/(4.*theta))
    for m in (500,2000,10000):
      n=2*m; a,b=optimum(m,1.,r,theta*n*n)
      check(abs(b/a-pred)<0.006,'scaled limit')

print('PASS',checks,'finite checks')
