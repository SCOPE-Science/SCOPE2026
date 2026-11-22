#!/usr/bin/env python3
"""Standalone numerical and rational checks for priced friendship-network spectral-moment design.

Uses only the Python standard library. These checks illustrate, rather than replace,
the all-size convexity and scalar derivative proof.
"""
import math
import random
from fractions import Fraction as F

CHECKS = 0

def check(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)

def optimum(m, gamma, p, budget=1.0):
    assert m >= 2 and gamma > 0 and budget > 0 and p >= 0
    u = m - 1 + (2*m+1)**(-p)
    v = max(0.0, m*(4*gamma-1)/u)
    s = max(1.0, v**(1/(p+1)))
    a = 2*budget/(m*(s+4*gamma-1))
    b = a*(s-1)/2
    return a,b,s

def spectrum(m,a,b):
    return [a]*(m-1)+[a+2*b]*m+[(2*m+1)*a]

def laplacian(m, spoke, pair):
    n=2*m+1
    L=[[0.0]*n for _ in range(n)]
    for k in range(m):
        u,v=2*k+1,2*k+2
        for x,y,w in ((0,u,spoke[2*k]),(0,v,spoke[2*k+1]),(u,v,pair[k])):
            L[x][x]+=w; L[y][y]+=w
            L[x][y]-=w; L[y][x]-=w
    return L

def eigenvalues(A):
    A=[row[:] for row in A]; n=len(A)
    for _ in range(100*n*n):
        k,l=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda x:abs(A[x[0]][x[1]]))
        if abs(A[k][l]) < 1e-12: break
        v=A[k][l]
        tau=(A[l][l]-A[k][k])/(2*v)
        t=math.copysign(1.0,tau)/(abs(tau)+math.hypot(1.0,tau))
        c=1/math.sqrt(1+t*t); s=t*c
        aa,bb=A[k][k],A[l][l]
        A[k][k]=aa-t*v; A[l][l]=bb+t*v
        A[k][l]=A[l][k]=0.0
        for i in range(n):
            if i not in (k,l):
                x,y=A[i][k],A[i][l]
                A[i][k]=A[k][i]=c*x-s*y
                A[i][l]=A[l][i]=s*x+c*y
    eig=sorted(A[i][i] for i in range(n))
    assert abs(eig[0])<1e-9
    assert eig[1]>0
    return eig[1:]

def objective(eig,p):
    return -sum(math.log(z) for z in eig) if p==0 else sum(z**(-p) for z in eig)

def rational_inverse(A):
    n=len(A)
    M=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if M[i][k])
        M[k],M[pivot]=M[pivot],M[k]
        v=M[k][k]; M[k]=[x/v for x in M[k]]
        for i in range(n):
            if i!=k:
                v=M[i][k]
                M[i]=[M[i][j]-v*M[k][j] for j in range(2*n)]
    return [row[n:] for row in M]

def rational_trace(m,a,b):
    n=2*m+1
    Q=[[F(0) for _ in range(2*m)] for _ in range(2*m)]
    for k in range(m):
        # Inverting the two-vertex grounded triangle block
        A=[[a+b,-b],[-b,a+b]]
        inv=rational_inverse(A)
        for i in range(2):
            for j in range(2): Q[2*k+i][2*k+j]=inv[i][j]
    return sum(Q[i][i] for i in range(2*m))-sum(map(sum,Q))/n

def main():
    for m in range(2,8):
        for a,b in ((F(2,3),F(3,5)),(F(1,2),F(0)),(F(4,5),F(1,3))):
            exact=F(m-1,1)/a+F(1,2*m+1)/a+F(m,1)/(a+2*b)
            check(rational_trace(m,a,b)==exact,f'exact pseudoinverse m={m}')
    rng=random.Random(20261117)
    for m in (2,3,4,6):
        for gamma in (0.20,0.39,0.4375,0.50,0.8,1.6):
            for p in (0.0,0.25,0.5,1.0,2.0,5.0):
                a,b,s=optimum(m,gamma,p)
                check(abs(m*(2*gamma*a+b)-1)<1e-10,'budget')
                check((b>1e-10)==(4*m*gamma>2*m-1+(2*m+1)**(-p)+1e-9),'support threshold')
                numeric=eigenvalues(laplacian(m,[a]*(2*m),[b]*m))
                expected=spectrum(m,a,b)
                check(max(abs(x-y) for x,y in zip(numeric,sorted(expected)))<1e-8,'spectrum')
                goal=objective(expected,p)
                check(abs(objective(numeric,p)-goal)<1e-7*max(1,abs(goal)),'spectral moment')
                for z in (0, 0.02, 0.1, 0.5, 2, 10):
                    asp=2/(m*(1+2*z+4*gamma-1))
                    bsp=z*asp
                    cand=objective(spectrum(m,asp,bsp),p)
                    check(cand+1e-7*max(1,abs(goal))>=goal,'scalar global optimum')
                for _ in range(5):
                    raw=[rng.expovariate(1) for k in range(3*m)]
                    tot=sum(gamma*x for x in raw[:2*m])+sum(raw[2*m:])
                    sp=[x/tot for x in raw[:2*m]]
                    pa=[x/tot for x in raw[2*m:]]
                    actual=objective(eigenvalues(laplacian(m,sp,pa)),p)
                    check(actual+1e-7*max(1,abs(goal))>=goal,'unrestricted feasible comparison')
    for m in range(2,25):
        at0=(2*m-1+1)/(4*m)
        at1=(2*m-1+(2*m+1)**(-1))/(4*m)
        at8=(2*m-1+(2*m+1)**(-8))/(4*m)
        check(at0>at1>at8>(2*m-1)/(4*m),'strict threshold hierarchy')
        check(abs(1/at1-(2+1/m))<1e-12,'first-moment published endpoint')
    gamma=7/16; m=2; pc=math.log(2)/math.log(5)
    for p in (pc-0.03,pc,pc+0.03,1.0,10.0):
        _,b,_=optimum(m,gamma,p)
        check((b>1e-12)==(p>pc+1e-12),'five-vertex critical exponent')
    for m in (2,3,5,9):
        for gamma in (0.45,0.6,1.0):
            if gamma>(2*m-1)/(4*m):
                p=200
                a,b,s=optimum(m,gamma,p)
                target=math.log(m*(4*gamma-1)/(m-1))/2
                check(abs(p*b/a-target)<0.012,'high-order asymptotic')
    print(f'VERIFY_OK {CHECKS}')

if __name__=='__main__':main()
