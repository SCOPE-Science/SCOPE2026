"""Standalone deterministic checks for dual-channel reset-source tomography.
Run: python verify.py (standard library only). This is a finite checker,
not a replacement for the analytical proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import cosh, sinh, log, isclose

checks = 0

def check(ok, msg):
    global checks
    assert ok, msg
    checks += 1

def determinant(a):
    a = [[Q(z) for z in row] for row in a]
    n = len(a)
    sign = 1
    d = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j,n) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j],a[pivot] = a[pivot],a[j]
            sign *= -1
        p = a[j][j]
        d *= p
        for i in range(j+1,n):
            v = a[i][j] / p
            for k in range(j+1,n):
                a[i][k] -= v*a[j][k]
            a[i][j] = 0
    return d*sign

def solve(a,b):
    n = len(a)
    a = [[Q(z) for z in row] + [Q(b[i])] for i,row in enumerate(a)]
    for j in range(n):
        pivot = next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot] = a[pivot],a[j]
        p = a[j][j]
        a[j] = [x/p for x in a[j]]
        for i in range(n):
            if i == j: continue
            v = a[i][j]
            a[i] = [a[i][k]-v*a[j][k] for k in range(n+1)]
    return [row[-1] for row in a]

def moments(t,w,K):
    return [sum((wi*ti**j for ti,wi in zip(t,w)),Q(0)) for j in range(-K,K+1)]

def hankel(u,s):
    return [[u[i+j] for j in range(s)] for i in range(s)]

def prony(u,s):
    c = solve(hankel(u,s),[-u[i+s] for i in range(s)])
    return c

def poly(c,x):
    return x**len(c) + sum((c[i]*x**i for i in range(len(c))),Q(0))

pool = [Q(1,2),Q(3,5),Q(3,4),Q(1),Q(5,4),Q(3,2),Q(2)]
for K in range(1,5):
    for s in range(1,K+2):
        for ix in combinations(range(len(pool)),s):
            t = [pool[i] for i in ix]
            raw = [Q((i+1)*(i+2)) for i in range(s)]
            w = [z/sum(raw) for z in raw]
            mm = moments(t,w,K)
            check(mm[K] == 1, 'normalization')
            u = mm
            H = hankel(u,K+1)
            det = determinant(H)
            check((det==0)==(s<=K),'Hankel rank certificate')
            if s<=K:
                c = prony(u,s)
                for ti in t:
                    check(poly(c,ti)==0, 'annihilator root')
                # ν weights are w_i t_i^{-K}; moments are u_i
                v = solve([[ti**j for ti in t] for j in range(s)],u[:s])
                check(v==[wi*ti**(-K) for wi,ti in zip(w,t)],'weights')
                check([v[i]*t[i]**K for i in range(s)] == w,'weight recovery')
                # all upper moments satisfy recurrence
                for i in range(2*K-s+1):
                    check(sum((c[j]*u[i+j] for j in range(s)), Q(0))+u[i+s]==0,'recurrence')
            else:
                check(det>0,'strict positive Hankel')

# Forward physical response (M,Pleft) -> bilateral moments at K rates.
L=8.0; D=1.7; x0=2.3; kap=0.28
for K in range(1,6):
    for s in range(1,K+2):
        t=pool[:s]
        weights=[float(Q(i+1,s*(s+1)//2)) for i in range(s)]
        x=[L/2-log(float(ti))/kap for ti in t]
        check(all(0<xi<L for xi in x),'positions interior')
        for j in range(1,K+1):
            k=j*kap; r=D*k*k
            h0=lambda z: sinh(k*(L-z))/sinh(k*L)
            hL=lambda z: sinh(k*z)/sinh(k*L)
            f=lambda z: h0(z)+hL(z)
            F=sum(w*f(z) for w,z in zip(weights,x))
            HL=sum(w*h0(z) for w,z in zip(weights,x))
            M=(1-f(x0))/(r*F)
            P=h0(x0)+(1-f(x0))*HL/F
            F2=(1-f(x0))/(r*M)
            HL2=F2*(P-h0(x0))/(1-f(x0))
            C=cosh(k*L/2)*F2
            S=sinh(k*L/2)*(2*HL2-F2)
            for sign,meas in [(1,C+S),(-1,C-S)]:
                actual=sum(w*float(ti)**(sign*j) for w,ti in zip(weights,t))
                check(isclose(meas,actual,rel_tol=1e-9,abs_tol=1e-9),'bilateral transform')

print('PASS: %d deterministic exact-rational and physical-transform checks' % checks)
