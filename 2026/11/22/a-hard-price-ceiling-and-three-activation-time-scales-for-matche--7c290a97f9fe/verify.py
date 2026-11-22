#!/usr/bin/env python3
"""Independent finite checks for a priced-matching bipartite diffusion theorem.

Requires Python 3 and NumPy, SymPy. The infinite-family statements
are proved analytically in RESULT.md; these samples are consistency tests.
"""
import math
import numpy as np
import sympy as sp

checks = 0

def check(v, message='failed'):
    global checks
    assert v, message
    checks += 1

def eigenvalues_formula(m, p, q):
    return sorted([0.0, 2*(p+(m-1)*q)] + [m*q]*(m-1) + [2*p+(m-2)*q]*(m-1))

def laplacian(m, weights):
    L = np.zeros((2*m, 2*m))
    for i in range(m):
        for j in range(m):
            w = weights[i,j]
            L[i,i] += w
            L[m+j,m+j] += w
            L[i,m+j] -= w
            L[m+j,i] -= w
    return L

def h(m, p, q, t):
    return 1+math.exp(-2*(p+(m-1)*q)*t)+(m-1)*(math.exp(-m*q*t)+math.exp(-(2*p+(m-2)*q)*t))

def deriv_scaled(m, r, budget, t, p):
    q=(budget/m-r*p)/(m-1)
    A=2*(m-1)-(m-2)*r
    return m*r*math.exp(-m*q*t)-A*math.exp(-(2*p+(m-2)*q)*t)+2*(r-1)*math.exp(-2*(p+(m-1)*q)*t)

def optimum(m,r,budget,t):
    ub=budget/(m*r)
    dl=deriv_scaled(m,r,budget,t,0)
    du=deriv_scaled(m,r,budget,t,ub)
    if dl>=0: return 0., budget/(m*(m-1))
    if du<=0: return ub,0.
    lo,hi=0.,ub
    for _ in range(80):
        mid=(lo+hi)/2
        if deriv_scaled(m,r,budget,t,mid)<0:lo=mid
        else:hi=mid
    p=(lo+hi)/2
    return p,(budget/m-r*p)/(m-1)

# Exact block eigenvectors, for the entire 2m-dimensional space.
for m in range(3,9):
    for p,q in [(sp.Rational(0),sp.Rational(1,7)),(sp.Rational(1,5),sp.Rational(0)),(sp.Rational(2,11),sp.Rational(3,13)),(sp.Rational(1),sp.Rational(1))]:
        W=sp.Matrix(m,m,lambda i,j:p if i==j else q)
        d=p+(m-1)*q
        L=(sp.diag(*([d]*m))).row_join(-W).col_join((-W).row_join(sp.diag(*([d]*m))))
        u=sp.ones(m,1)
        v=u.col_join(u)
        check(L*v==sp.zeros(2*m,1),'constant mode')
        v=u.col_join(-u)
        check(L*v==2*d*v,'bipartition mode')
        for k in range(m-1):
            x=sp.zeros(m,1);x[k]=1;x[m-1]=-1
            v=x.col_join(x)
            check(L*v==(m*q)*v,'symmetric zero-sum mode')
            v=x.col_join(-x)
            check(L*v==(2*p+(m-2)*q)*v,'antisymmetric zero-sum mode')

# Matrix eigenvalues, budget and derivative stationarity across phase boundaries.
for m in [3,4,5,7,10]:
    for r in [0.2,0.5,0.9,1.,1.01,1.1,1.5,1.9,2.,2.1,2.5,3.,4.,7.]:
        for t in [0.02,0.3,1.,3.,10.,40.,200.]:
            p,q=optimum(m,r,1.,t)
            check(p >= -1e-11 and q >= -1e-11 and abs(m*r*p+m*(m-1)*q-1)<1e-10,'budget')
            if p > 1e-9 and q > 1e-9 and t<100:
                check(abs(deriv_scaled(m,r,1.,t,p))<2e-9,'stationarity')
            W=np.full((m,m),q);np.fill_diagonal(W,p)
            eig=np.linalg.eigvalsh(laplacian(m,W))
            check(np.allclose(eig,eigenvalues_formula(m,p,q),rtol=1e-9,atol=1e-9),'matrix spectrum')
            check(abs(np.exp(-t*eig).sum()-h(m,p,q,t))<2e-9,'heat trace')
            if t<10:
                for offset in [0.,.25,.5,.75,1.]:
                    pp=offset/(m*r);qq=(1/m-r*pp)/(m-1)
                    check(h(m,p,q,t)<h(m,pp,qq,t)+1e-10,'global scalar optimum')

# Test regime declarations and exact activation thresholds on both endpoints.
for m in [3,4,5,9,25,80]:
    for r in [0.2,0.6,0.9]:
        T=m*r/2*math.log((2-r)/r)
        for factor in [0.4,.8,1.,1.2,3.]:
            p,q=optimum(m,r,1.,T*factor)
            if factor<=1:check(q<1e-9,'ordinary-edge early deletion')
            else:check(q>1e-12,'ordinary-edge later activation')
    for r in [1.01,1.2,1.5,2.,2+1/(m-2)]:
        rcrit=2*(m-1)/(m-2)
        if r>=rcrit:continue
        A=2*(m-1)-(m-2)*r
        lo,hi=0.,100.
        for _ in range(100):
            x=(lo+hi)/2
            F=m*r*math.exp(-2*x)+2*(r-1)*math.exp(-m*x)-A
            if F>0:lo=x
            else:hi=x
        T=m*(m-1)*(lo+hi)/2
        for factor in [0.5,.9,1.,1.1,2.]:
            p,q=optimum(m,r,1.,T*factor)
            if factor<=1:check(p<1e-9,'matching-edge early deletion')
            else:check(p>1e-12,'matching-edge later activation')
    for r in [2*(m-1)/(m-2),2*(m-1)/(m-2)+.01,8.]:
        for t in [.1,1.,100.,1000.]:
            p,q=optimum(m,r,1.,t)
            check(p<1e-9,'permanent matching suppression')

# Verify unrestricted comparisons against asymmetric feasible conductances.
rng=np.random.default_rng(11519)
for m in [3,4,5,7]:
    for r in [.4, .9, 1., 1.2, 1.9, 2.5, 4.]:
        for t in [.2,2.,10.]:
            p,q=optimum(m,r,1.,t)
            target=h(m,p,q,t)
            for _ in range(20):
                raw=rng.gamma(1.5,1.,(m,m))
                costs=np.ones((m,m));np.fill_diagonal(costs,r)
                W=raw/(raw*costs).sum()
                trial=np.exp(-t*np.linalg.eigvalsh(laplacian(m,W))).sum()
                check(trial>target-1e-9,'unrestricted allocation beats claimed optimum')

# Growing-order activation scales: finite comparisons, not proofs.
for r in [1.2,1.5,1.8]:
    lim=.5*math.log(r/(2-r))
    for m in [100,400,1600]:
        A=2*(m-1)-(m-2)*r
        lo,hi=0.,10.
        for _ in range(80):
            x=(lo+hi)/2
            if m*r*math.exp(-2*x)+2*(r-1)*math.exp(-m*x)>A:lo=x
            else:hi=x
        check(abs((lo+hi)/2-lim)<5/m,'quadratic threshold limit')
for m in [100,400,1600]:
    lo,hi=0.,20.
    for _ in range(80):
        x=(lo+hi)/2
        if m*math.exp(-2*x)+math.exp(-m*x)>1:lo=x
        else:hi=x
    check(abs((lo+hi)/2-.5*math.log(m))<.01,'logarithmic threshold limit')
print('VERIFY_OK',checks,'exact mode, matrix spectrum, boundary, sample optimality, and asymptotic checks')
