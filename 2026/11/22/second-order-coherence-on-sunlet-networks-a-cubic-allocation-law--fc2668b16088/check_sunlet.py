"""Reproducibility checks for budget-optimal second-order sunlet coherence.

Requires numpy and scipy. All reported finite checks are diagnostic, not a
replacement for the all-size analytic proof in RESULT.md.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

checks = 0

def verify(test, label):
    global checks
    assert bool(test), label
    checks += 1

def coeffs(n):
    return (Fraction(4*n-3, 4), Fraction(n*n-1, 6),
            Fraction(n**4+10*n*n-11, 180))

def P(n,t):
    A,B,C = [float(v) for v in coeffs(n)]
    return 2*A*t**3+B*t*t-B*t-2*C

def t2(n):
    return brentq(lambda t:P(n,t), 1e-10, n*n+10,xtol=1e-12)

def t1(n):
    A,B,C= [float(v) for v in coeffs(n)]
    return math.sqrt(B/(n-0.5))

def fun(n,t):
    A,B,C=[float(v) for v in coeffs(n)]
    return n*n*(1+t)**2*(A+B/t+C/t**2)

def lap(n,a,b):
    N=2*n
    L=np.zeros((N,N))
    for i in range(n):
        for j,w in [((i+1)%n,a),(i+n,b)]:
            L[i,i]+=w; L[j,j]+=w
            L[i,j]-=w;L[j,i]-=w
    return L

def f2matrix(L):
    vals=np.linalg.eigvalsh(L)
    if vals[1]<=0: return math.inf
    return float(np.sum(vals[1:]**-2))

# Exact polynomial identities independent of numerical diagonalization.
for n in range(3,81):
    A,B,C=coeffs(n)
    verify(A == Fraction(n,1)-Fraction(3,4), 'A')
    verify(B==Fraction(n*n-1,6), 'B')
    verify(C==Fraction(n**4+10*n*n-11,180),'C')
    verify(P(n,t2(n)-1e-6)<0<P(n,t2(n)+1e-6),'sign/cubic')

# Characteristic spectral sums and full matrix comparisons.
for n in range(3,13):
    lam=[2-2*math.cos(2*math.pi*k/n) for k in range(1,n)]
    A1=sum(1/x for x in lam)
    A2=sum(1/x**2 for x in lam)
    verify(abs(A1-(n*n-1)/12)<1e-8,'cycle reciprocal sum')
    verify(abs(A2-(n**4+10*n*n-11)/720)<1e-7,'cycle reciprocal square sum')
    for t in [0.12,0.45,1.2,4.0]:
        a=t/(n*(1+t));b=1/(n*(1+t))
        direct=f2matrix(lap(n,a,b)); closed=fun(n,t)
        verify(abs(direct-closed)<2e-7*max(1,closed),'full matrix spectral formula')
    t=t2(n)
    opt=minimize_scalar(lambda v:fun(n,v),bounds=(0.01,4*n),method='bounded',options={'xatol':1e-12})
    verify(abs(opt.x-t)<1e-4*max(1,t),'scalar numerical optimizer')
    # Invariant optimum outperforms randomly heterogeneous independent weights.
    rng=np.random.default_rng(n)
    optval=fun(n,t)
    for k in range(12):
        w=rng.gamma(shape=2.0,scale=1.0,size=2*n)
        w=w/w.sum()
        L=np.zeros((2*n,2*n))
        edges=[(i,(i+1)%n) for i in range(n)]+[(i,n+i) for i in range(n)]
        for (i,j),wt in zip(edges,w):
            L[i,i]+=wt;L[j,j]+=wt;L[i,j]-=wt;L[j,i]-=wt
        verify(f2matrix(L)>=optval*(1-1e-10),'heterogeneous competitor')

# Sharp comparison of optimum for first and second spectral inverse moments.
for n in range(3,501):
    verify(t2(n)>t1(n), 'strict second-order cycle priority')

c=brentq(lambda x:180*x**3+15*x*x-1,0.01,1)
verify(abs(c-0.15324232)<1e-8,'cubic asymptotic constant')
for n in [1000,5000,20000]:
    t=t2(n)
    verify(abs(t/n-c)<2.0/n,'asymptotic optimal ratio')
    verify(abs(t1(n)/math.sqrt(n)-1/math.sqrt(6))<0.005,'first-order ratio')
    if n>1000:
        excess=(fun(n,t1(n))-fun(n,t))/(n**5.5)
        verify(abs(excess-math.sqrt(6)/90)<0.004,'cross-objective excess')

print(f'PASS: {checks} finite analytical/numerical assertions')
print(f'c={c:.12f}; m=3: (t2,t1)={t2(3):.10f},{t1(3):.10f}; m=4: {t2(4):.10f},{t1(4):.10f}')
