#!/usr/bin/env python3
"""Standalone supplementary numerical and exact-integer checks for a graph heat-sampling theorem.
Run with Python 3 and the standard library only. All infinite statements have analytic proofs.
"""
import math
import cmath
from itertools import permutations

COUNT = 0

def ck(test, msg):
    global COUNT
    COUNT += 1
    if not test:
        raise AssertionError(msg)

def spectrum(m):
    return [2 - 2*math.cos(math.pi*j/m) for j in range(m)]

def amp(m,site):
    return [1/math.sqrt(m)]+[math.sqrt(2/m)*math.cos(math.pi*j*(site+.5)/m) for j in range(1,m)]

def det(A):
    A = [list(map(complex,r)) for r in A]
    n = len(A); sign=1
    out=1+0j
    for i in range(n):
        p=max(range(i,n),key=lambda k:abs(A[k][i]))
        if abs(A[p][i])<1e-90:return 0j
        if p!=i: A[p],A[i]=A[i],A[p];sign=-sign
        x=A[i][i];out*=x
        for j in range(i+1,n):
            t=A[j][i]/x
            for k in range(i+1,n): A[j][k]-=t*A[i][k]
    return sign*out

def mat(m,d,t,theta,site=0):
    mu=spectrum(m); w=amp(m,site)
    lam=sum(2-2*math.cos(z) for z in theta)
    return [[w[j]*math.exp(-k*t*(lam+mu[j])) for j in range(m)] for k in range(m)]

def vandermonde_pred(m,d,t,theta,site=0):
    mu=spectrum(m); w=amp(m,site)
    lam=sum(2-2*math.cos(z) for z in theta)
    res=math.exp(-lam*t*m*(m-1)/2)*math.prod(w)
    for i in range(m):
        for j in range(i+1,m):
            res*=math.exp(-t*mu[j])-math.exp(-t*mu[i])
    return res

def Phi(t,m,d):
    mu=spectrum(m)
    return sum((mu[j]-mu[i])/math.expm1(t*(mu[j]-mu[i]))-mu[i] for i in range(m) for j in range(i+1,m))-2*d*m*(m-1)

def finite_opt(m,d):
    lo,hi=1.e-7,2.0
    ck(Phi(lo,m,d)>0 and Phi(hi,m,d)<0,('bracket',m,d))
    for z in range(60):
        mid=(lo+hi)/2
        if Phi(mid,m,d)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def integral(t,n=260):
    # smooth triangular midpoint quadrature, not a proof of limits
    s=0.;h=1/n
    for i in range(n):
        u=(i+.5)/n
        mu_u=2-2*math.cos(math.pi*u)
        for j in range(i+1,n):
            v=(j+.5)/n
            delta=2-2*math.cos(math.pi*v)-mu_u
            s+=delta/math.expm1(t*delta)
    # Cancel the first boundary/diagonal term of the triangular Riemann sum.
    return s/(n*n)+1/(2*t*n)

def limit(d,n=260):
    target=2*d+1-4/math.pi**2
    lo,hi=.002,.6
    for i in range(47):
        mid=(lo+hi)/2
        if integral(mid,n)>target:lo=mid
        else:hi=mid
    return (lo+hi)/2

# Direct combinatorial path eigenvector equations and modal orthogonality.
for m in range(2,19):
    mu=spectrum(m)
    for j in range(m):
        v=[1/math.sqrt(m) if j==0 else math.sqrt(2/m)*math.cos(math.pi*j*(a+.5)/m) for a in range(m)]
        for a in range(m):
            L=(v[a]-(v[a-1] if a else 0))+(v[a]-(v[a+1] if a<m-1 else 0))
            if a==0:L=v[0]-v[1]
            if a==m-1:L=v[m-1]-v[m-2]
            ck(abs(L-mu[j]*v[a])<5e-12,('eigen',m,j,a))
        for k in range(j+1,m):
            u=[1/math.sqrt(m) if k==0 else math.sqrt(2/m)*math.cos(math.pi*k*(a+.5)/m) for a in range(m)]
            ck(abs(sum(x*y for x,y in zip(u,v)))<4e-12,('orthogonality',m,j,k))
        ck(abs(sum(t*t for t in v)-1)<5e-12,('norm',m,j))

# Complete sensor arithmetic ranks from the pattern of invisible path modes.
for m in range(2,65):
    for site in range(m):
        g=math.gcd(2*site+1,m)
        invisible=sum(abs(z)<1.e-11 for z in amp(m,site))
        ck(invisible==(g-1)//2,('blind',m,site,g,invisible))

# Independent determinant via elimination agrees with Fourier/Vandermonde factorization.
for m in range(2,7):
    for d in (1,2,3):
        for t in (.11,.21,.38,.77):
            theta=tuple(0.5 + (k+1)*.33 for k in range(d))
            for site in (0,m-1):
                A=mat(m,d,t,theta,site)
                actual=det(A); predicted=vandermonde_pred(m,d,t,theta,site)
                scale=max(1e-35,abs(predicted))
                ck(abs(actual-predicted)/scale<4.e-5,('det',m,d,t,site,actual,predicted))

# Strict concavity and unique optimum; boundary signs checked separately.
for m in range(2,14):
    for d in (1,2,3,5):
        tm=finite_opt(m,d)
        ck(0<tm<.4,('root',m,d,tm))
        ck(Phi(.80*tm,m,d)>0 and Phi(1.20*tm,m,d)<0,('peak',m,d))
        ck(Phi(.75*tm,m,d)>Phi(tm,m,d)>Phi(1.25*tm,m,d),('mono',m,d))
        if m==2:
            ck(abs(tm-.5*math.log(1+1/(2*d)))<1e-10,('m2',d))

# Limiting constants and first-order width correction: convergence, not certification.
expected={1:.1682323819219938,2:.100335065455689,3:.071550369747704}
for d,v in expected.items():
    approx=limit(d,220)
    ck(abs(approx-v)<4e-5,('limit integral',d,approx,v))
    for m in (64,128,256):
        tm=finite_opt(m,d)
        ck(abs(tm-v)<.01,('convergence',d,m,tm))

print('VERIFY_OK',COUNT,'supplementary_assertions')
