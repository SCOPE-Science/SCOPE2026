#!/usr/bin/env python3
"""Finite exact checks and independent numerical stress tests for the two-zealot opinion chain."""
from fractions import Fraction as F
from math import exp, log, copysign, isclose, lgamma

checks = 0

def check(test, message='identity'):
    global checks
    if not test:
        raise AssertionError(message)
    checks += 1

def f_exact(x, a):
    # alpha 1 and 2: exact rational evaluation of the piecewise response
    assert a in (1, 2) and isinstance(x,F)
    t = 2*x-1
    if a == 1: return x
    return (1+t*t)/2 if t>=0 else (1-t*t)/2

def tr(m, k, a):
    # (up, down) one selected susceptible per step, with opposite zealots
    up = F(m-k, m)*f_exact(F(k+1, m+1), a) if k<m else F(0)
    down = F(k, m)*f_exact(F(m-k+1, m+1), a) if k>0 else F(0)
    return up,down

def solve(A,b):
    # independent Gauss-Jordan exact rational solve
    n=len(b)
    q=[list(map(F,row))+[F(bi)] for row,bi in zip(A,b)]
    for i in range(n):
        pivot=next(j for j in range(i,n) if q[j][i])
        q[i],q[pivot]=q[pivot],q[i]
        v=q[i][i]
        q[i]=[z/v for z in q[i]]
        for j in range(n):
            if j==i: continue
            v=q[j][i]
            q[j]=[x-v*y for x,y in zip(q[j],q[i])]
    return [z[-1] for z in q]

for m in range(2,12):
    for a in (1,2):
        p=[tr(m,k,a)[0] for k in range(m+1)]
        q=[tr(m,k,a)[1] for k in range(m+1)]
        w=[F(1)]
        for k in range(m): w.append(w[-1]*p[k]/q[k+1])
        check(all(w[k]==w[m-k] for k in range(m+1)),f'symmetry m={m},a={a}')
        z=sum(w)
        pi=[v/z for v in w]
        for k in range(m): check(pi[k]*p[k]==pi[k+1]*q[k+1])
        for k in range(m+1):
            entry=(pi[k-1]*p[k-1] if k else F(0))+(pi[k+1]*q[k+1] if k<m else F(0))+pi[k]*(1-p[k]-q[k])
            check(entry==pi[k],f'stationarity m={m}, a={a}, k={k}')
        if a==1:
            check(all(z==F(1,m+1) for z in pi))
        else:
            check(pi[0]<pi[1])
            check(pi[m//2]>=pi[0])
        # independent exact linear-system hitting times on states 0,...,m-1
        A=[]
        for k in range(m):
            row=[F(0)]*m
            row[k]=p[k]+q[k]
            if k: row[k-1]=-q[k]
            if k+1<m: row[k+1]=-p[k]
            A.append(row)
        hit=solve(A,[F(1)]*m)[0]
        formula=sum(sum(w[:k+1])/(w[k]*p[k]) for k in range(m))
        check(hit==formula, f'hitting-time m={m},a={a}')
        if a==1:
            H=sum((F(1,j) for j in range(1,m+1)),F(0))
            check(hit==m*(m+1)*H, f'critical clock m={m}')

def resp(x,a):
    if x==F(1,2): return .5
    t=2*x-1
    return (1+copysign(abs(t)**a,t))/2

def stationary(m,a):
    # log ratios; this implementation does NOT solve detailed balance equations
    logw=[0.]
    for j in range(1,m+1):
        x=j/(m+1)
        v=resp(x,a)
        logw.append(logw[-1]+log((m-j+1)/j)+log(v)-log(1-v))
    mx=max(logw); w=[exp(v-mx) for v in logw]; z=sum(w)
    return [v/z for v in w],logw

for m in (2,3,4,5,8,13,27,100):
    for a in (.25,.5,.9,1.0,1.1,1.5,2.,4.):
        ps,lw=stationary(m,a)
        check(isclose(sum(ps),1.,rel_tol=1e-12))
        for k in range(m+1):check(isclose(ps[k],ps[m-k],rel_tol=1e-10,abs_tol=1e-14))
        if a < 1:
            for k in range(1,(m+1)//2):check(ps[k]<ps[k-1])
        if a > 1:
            for k in range(1,(m+1)//2):check(ps[k]>ps[k-1])
        if a==1: check(all(isclose(p,1/(m+1),rel_tol=1e-12) for p in ps))

def g(x,a):
    if x==0: return log(a)
    if x==1: return -log(a)
    fx=resp(x,a)
    return log((1-x)/x)+log(fx)-log(1-fx)

def barrier(a):
    # midpoint quadrature independent of stationary recurrence
    n=20000; h=.5/n
    return abs(sum(g((j+.5)*h,a) for j in range(n))*h)

for a in (.3,.5,.8,1.3,1.7,2.,3.):
    delta=barrier(a)
    check(delta>0)
    # exact double-sum first-hit time in log space with logaddexp
    m=650
    ps,lw=stationary(m,a)
    p=[]
    for k in range(m):p.append((m-k)/m*resp((k+1)/(m+1),a))
    def la(x,y):
        if x < y: x,y=y,x
        return x+log(1+exp(y-x))
    cumul=lw[0]
    total=float('-inf')
    for k in range(m):
        if k: cumul=la(cumul,lw[k])
        total=la(total,cumul-lw[k]-log(p[k]))
    check(abs(total/m-delta)<.06, f'LD m={m},a={a}: {total/m} vs {delta}')

for a in (.3,.6,.85):
    p,lw=stationary(600,a)
    check(abs(p[0]-(1-a)/2)<.005)
    for j in range(5):check(abs(p[j]/p[0]-a**j)<.002)
for a in (1.4,2.,3.):
    m=1200
    ps,_=stationary(m,a)
    var=sum(((k-m/2)**2)*v for k,v in enumerate(ps))/m
    check(abs(var-.25)<(.28 if a<1.5 else .03),f'Gaussian variance {a}: {var}')

print('VERIFY_OK',checks,'exact and numerical checks')
