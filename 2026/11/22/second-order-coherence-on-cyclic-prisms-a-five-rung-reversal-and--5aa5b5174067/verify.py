"""Standalone checks for squared-inverse Laplacian optimal rung allocation.
Requires Python 3.9+, NumPy and SymPy. Runs with no private files or network.
Finite checks supplement, but do not replace, the analytic proof.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

CHECKS=0

def ck(condition,msg):
    global CHECKS
    if not condition:
        raise AssertionError(msg)
    CHECKS+=1


def cycle_modes(m):
    return 4*np.sin(np.pi*np.arange(m)/m)**2


def s(m,p):
    return (m*m-1)/12 if p==1 else (m**4+10*m*m-11)/720


def rhs(m,t,p):
    mu=cycle_modes(m)
    return float(np.sum((4-mu)/(mu+2*t)**(p+1)))


def ratio(m,p):
    lo,hi=1e-16,10.
    for _ in range(120):
        mid=(lo+hi)/2
        if rhs(m,mid,p)>s(m,p):lo=mid
        else:hi=mid
    return (lo+hi)/2


def tr_formula(m,a,b,p):
    mu=cycle_modes(m)
    return float(np.sum((a*mu[1:])**(-p))+np.sum((a*mu+2*b)**(-p)))


def tr_matrix(m,a,b,p):
    N=2*m
    L=np.zeros((N,N))
    for layer in [0,1]:
        for j in range(m):
            u=layer*m+j;v=layer*m+(j+1)%m
            L[u,u]+=a;L[v,v]+=a;L[u,v]-=a;L[v,u]-=a
    for j in range(m):
        u=j;v=m+j
        L[u,u]+=b;L[v,v]+=b;L[u,v]-=b;L[v,u]-=b
    ev=np.linalg.eigvalsh(L)
    ck(abs(ev[0])<1e-9 and ev[1]>1e-9,'connected spectrum')
    return sum(float(x**(-p)) for x in ev[1:])


def exact_formula(m,a,b,p):
    N=2*m
    L=sp.zeros(N)
    for layer in [0,1]:
        for j in range(m):
            u=layer*m+j;v=layer*m+(j+1)%m
            L[u,u]+=a;L[v,v]+=a;L[u,v]-=a;L[v,u]-=a
    for j in range(m):
        u=j;v=m+j
        L[u,u]+=b;L[v,v]+=b;L[u,v]-=b;L[v,u]-=b
    Q=L+sp.ones(N)/N
    inv=Q.inv()
    return (sp.trace(inv**p)-1).cancel()

# Exact cycle spectral-moment sums, tested through roots of unity for small sizes.
for m in range(3,7):
    mu=[2-2*sp.cos(2*sp.pi*k/m) for k in range(1,m)]
    for p in (1,2):
        ck(sp.simplify(sum(z**(-p) for z in mu)-sp.Rational(m*m-1,12) if p==1 else sum(z**(-p) for z in mu)-sp.Rational(m**4+10*m*m-11,720))==0, f'sum {m,p}')

# High-precision cycle moment identities on additional cycle lengths.
import mpmath as mp
mp.mp.dps=75
for m in range(7,35):
    mu=[4*mp.sin(mp.pi*k/m)**2 for k in range(1,m)]
    for p in (1,2):
        expected=mp.mpf(m*m-1)/12 if p==1 else mp.mpf(m**4+10*m*m-11)/720
        ck(abs(sum(z**(-p) for z in mu)-expected)<mp.mpf('1e-60'),f'mp cycle {m,p}')

# Exact finite reversal thresholds and two boundary checks.
for m in [5,6]:
    t0=sp.Rational(30,m*m+11)
    mu=[2-2*sp.cos(2*sp.pi*k/m) for k in range(m)]
    g=sp.simplify(sum((4-z)/(z+2*t0)**2 for z in mu)-sp.Rational(m*m-1,12))
    ck(g>0,f'strict m={m} comparison')
ck(sp.simplify(sp.Rational(1,sp.Rational(13,10)**2)+2/(3+2*sp.Rational(13,10))**2-sp.Rational(2,3))<0,'m3 first root below 13/10')
ck(sp.simplify(1/(2*sp.Rational(13,10)**3)+2/(3+2*sp.Rational(13,10))**3-sp.Rational(2,9))>0,'m3 second root above 13/10')
for p,goal in [(1,sp.Rational(5,4)),(2,sp.Rational(9,16))]:
    mu=[0,2,4,2]
    ck(sum((4-z)/sp.Integer(z+2)**(p+1) for z in mu)==goal,'m4 common root')

# Matrix vs Fourier formula; repeated with both objectives and multiple weights.
for m in range(3,12):
    for a,b in [(1/19,2/31),(3/41,1/29)]:
        for p in (1,2):
            v1=tr_matrix(m,a,b,p)
            v2=tr_formula(m,a,b,p)
            ck(abs(v1-v2)<2e-6*max(1,abs(v2)),f'matrix trace {m,a,b,p}')

# Exact rational matrix identity, without transcendental arithmetic.
for m in (3,4,5,6):
    for p in (1,2):
        a=sp.Rational(2,17);b=sp.Rational(3,23)
        direct=exact_formula(m,a,b,p)
        mu=[2-2*sp.cos(2*sp.pi*k/m) for k in range(m)]
        spectral=sp.simplify(sum((a*z)**(-p) for z in mu[1:])+sum((a*z+2*b)**(-p) for z in mu))
        ck(sp.simplify(direct-spectral)==0,f'exact matrix {m,p}')

# All-size analytic ordering checked against numerical roots for sample sizes.
for m in list(range(3,101))+[150,200,300,500,1000]:
    t1=ratio(m,1);t2=ratio(m,2)
    ck((t2>t1) if m==3 else (abs(t1-t2)<1e-10 if m==4 else (t2<t1)),f'ordering {m}')
    ck(abs(rhs(m,t2,2)-s(m,2))<2e-7*max(1,s(m,2)),f'root {m}')
    if m>=7:
        ck(t1>30/(m*m+11),f'comparison barrier {m}')

# Scaling of the two optima and the minimum/cross-objective regret.
c1=18**(1/3)
c2=540**(2/5)/2
for m in (1000,3000,10000,30000):
    t1=ratio(m,1);t2=ratio(m,2)
    ck(abs(t1*m**(2/3)/c1-1)<.05,f'p1 scale {m}')
    ck(abs(t2*m**(6/5)/c2-1)<.015,f'p2 scale {m}')
    a1=1/(m*(2+t1));b1=t1*a1
    a2=1/(m*(2+t2));b2=t2*a2
    F2=tr_formula(m,a2,b2,2)
    F_wrong=tr_formula(m,a1,b1,2)
    ck(F_wrong>F2,f'strict regret {m}')
    ck(abs(F2/(m**6/180)-1)<.1,f'leading min {m}')
    ck(abs((F_wrong-F2)/(c1*m**(16/3)/180)-1)<.11,f'regret {m}')
print('VERIFY_OK', CHECKS)
