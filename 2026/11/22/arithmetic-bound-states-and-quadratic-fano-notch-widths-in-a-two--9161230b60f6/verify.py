#!/usr/bin/env python3
"""Independent exact and numerical checks for the two-arm stub transmission theorem.
Requires Python 3, sympy, numpy and scipy. No external data or network.
"""
from math import gcd, sin, cos, pi
from fractions import Fraction
import numpy as np
from scipy.optimize import brentq
import sympy as sp

E=sp.Symbol('E')
def P(n):
    old,cur=sp.Integer(1),E
    if n==0:return old
    for j in range(2,n+1):old,cur=cur,sp.expand(E*cur-old)
    return cur

def path(n, detune=0):
    a=sp.zeros(n)
    for j in range(n):
        a[j,j]=detune
        if j+1<n: a[j,j+1]=a[j+1,j]=1
    return a

# Exact characteristic and boundary resolvent tests, independent of polynomial recurrence.
exact=0
for n in range(1,9):
    M=path(n)
    assert sp.expand((E*sp.eye(n)-M).det(method='berkowitz')-P(n))==0
    for x in [sp.Rational(1,7),sp.Rational(3,7),sp.Rational(13,11)]:
        A=x*sp.eye(n)-M
        if A.det()==0: continue
        g=A.inv()[0,0]
        assert sp.cancel(g-P(n-1).subs(E,x)/P(n).subs(E,x))==0
        exact+=1

# BIC eigenspaces: two arms share exactly gcd(m+1,n+1)-1 eigenvalues.
bic=0
for m,n in [(1,1),(2,2),(2,5),(3,5),(4,9),(5,8),(6,13),(5,5)]:
    A=sp.diag(path(m),path(n))
    f=sp.gcd(P(m),P(n))
    assert sp.degree(f)==gcd(m+1,n+1)-1
    for root in sp.polys.polytools.intervals(f,eps=sp.Rational(1,10**9)):
        assert root is not None
    bic+=1

def green(n,e):
    # Evaluated from independent matrix inverse rather than Chebyshev recurrence.
    A=np.diag(np.zeros(n))
    for j in range(n-1):A[j,j+1]=A[j+1,j]=1
    return np.linalg.solve(e*np.eye(n)-A,np.eye(n)[:,0])[0]

def h(m,n,e,delta):return e-green(m,e)-green(n,e-delta)

def scattering(m,n,e,delta):
    # Solve the original infinite-lead boundary matching at its central site.
    # Unknowns r,t,side-root, m arm amplitudes, n arm amplitudes.
    k=np.arccos(e/2)
    z=np.exp(1j*k)
    N=3+m+n
    M=np.zeros((N,N),dtype=complex); rhs=np.zeros(N,dtype=complex)
    M[0,0]=-1;M[0,1]=1;rhs[0]=1 # t-r=1
    M[1,0]=-z;M[1,1]=e-z;M[1,2]=-1;rhs[1]=1/z
    M[2,1]=-1;M[2,2]=e;M[2,3]=-1;M[2,3+m]=-1
    for i in range(m):
        row=3+i;M[row,row]=e
        if i==0:M[row,2]=-1
        if i>0:M[row,row-1]=-1
        if i+1<m:M[row,row+1]=-1
    for i in range(n):
        row=3+m+i;M[row,row]=e-delta
        if i==0:M[row,2]=-1
        if i>0:M[row,row-1]=-1
        if i+1<n:M[row,row+1]=-1
    r,t,*_=np.linalg.solve(M,rhs)
    return float(abs(t)**2),float(abs(r)**2)

full=0
for m,n in [(1,1),(1,2),(2,3),(2,5),(3,5),(4,4),(5,8)]:
    for en in [0.17,0.39,1.17,-0.81]:
        delta=0.113
        H=h(m,n,en,delta)
        T=(4-en*en)*H*H/(1+(4-en*en)*H*H)
        tf,rf=scattering(m,n,en,delta)
        assert abs(tf-T)<1e-9,(m,n,en,T,tf)
        assert abs(tf+rf-1)<1e-9
        full+=1

# Independently solve Fano notch and its half-height intersections.
width_checks=0
for m,n,s in [(1,1,1),(2,2,1),(2,2,2),(2,5,1),(2,5,2),(3,5,1),(5,8,1),(5,8,2)]:
    d=gcd(m+1,n+1);theta=pi*s/d;e0=2*cos(theta)
    target=(m+1)**2*(n+1)**2/(4*sin(theta)**3*(m+n+2)**3)
    target_shift=(n+1)/(m+n+2)
    for delta in (0.01,0.005):
        center=brentq(lambda x:h(m,n,x,delta),e0+1e-7*delta,e0+(1-1e-7)*delta,xtol=1e-14)
        assert abs((center-e0)/delta-target_shift)<0.008
        def transmission(x):
            H=h(m,n,x,delta)
            return (4-x*x)*H*H/(1+(4-x*x)*H*H)
        left=brentq(lambda x:transmission(x)-.5,center-10*target*delta**2,center,xtol=1e-14)
        right=brentq(lambda x:transmission(x)-.5,center,center+10*target*delta**2,xtol=1e-14)
        assert abs(((right-left)/2)/delta**2/target-1)<0.025
        width_checks+=1
print('ALL_CHECKS_PASSED exact_resolvents=%d gcd_bics=%d direct_scattering=%d width_asymptotics=%d'%(exact,bic,full,width_checks))
