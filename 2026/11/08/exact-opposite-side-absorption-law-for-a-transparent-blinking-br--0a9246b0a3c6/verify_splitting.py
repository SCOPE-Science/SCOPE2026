#!/usr/bin/env python3
"""Reproducibility checks for two-sided gated Brownian absorption under resetting.

Requires Python, SymPy, NumPy and SciPy. Numerical checks are corroboration,
not substitutes for the uniqueness and monotonicity arguments in RESULT.md.
"""
import math
import numpy as np
import sympy as sp
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def formula(r, alpha, beta, D, x0):
    lam = alpha + beta
    k = math.sqrt(r / D)
    ell = math.sqrt((r + lam) / D)
    e = math.exp(-ell * x0)
    q = (1 - k / ell) / (2 * lam)
    pa = q * alpha * (1 - e)
    pi = q * (alpha + (r + beta) * e)
    pe = (beta * pa + alpha * pi) / lam
    a = ell / k
    h = 1 - 1 / a + math.exp(-a * k * x0) / (a * (a + 1))
    assert abs(pe - alpha / (2 * lam) * h) < 1e-12
    return pa, pi, pe


def symbolic_checks():
    alpha, beta, r, k, ell, E = sp.symbols('alpha beta r k ell E', positive=True)
    lam = alpha + beta
    B = (k/ell - 1) / 2
    C = (r / lam) * B * E
    U = -alpha * B * (1 + r * E / lam)
    delta = B * E * (1 + r / lam)
    expected_A = alpha * (-B) * (1 - E) / lam
    expected_I = (-B) * (alpha + (r + beta) * E) / lam
    checks = [
        U + alpha * (C + B),
        U + beta + alpha * (C + B + 1) - lam,
        beta - beta * ((B + 1) - B),
        beta * ell * B - beta * (k - ell * (B + 1)),
        U - (beta * expected_A + alpha * expected_I),
        delta - (expected_A - expected_I),
        (U + alpha * delta) / lam - expected_A,
        (U - beta * delta) / lam - expected_I,
        (r + lam) * C - r * delta,
    ]
    for i, item in enumerate(checks):
        assert sp.simplify(item) == 0, ('symbolic identity', i, item)
    a, s = sp.symbols('a s', positive=True)
    H = 1 - 1/a + sp.exp(-a*s)/(a*(a+1))
    dH_da = 1/a**2 - sp.exp(-a*s)*(s/(a*(a+1))+(2*a+1)/(a**2*(a+1)**2))
    assert sp.simplify(sp.diff(H, a) - dH_da) == 0
    assert sp.simplify(sp.diff(H, s) + sp.exp(-a*s)/(a+1)) == 0
    # Q(s)=exp(-as)[as/(a+1)+(2a+1)/(a+1)^2],
    # and Q'(s)<0 for all a>1 and s>=0.
    Q = sp.exp(-a*s)*(a*s/(a+1)+(2*a+1)/(a+1)**2)
    assert sp.simplify(sp.diff(Q,s) / sp.exp(-a*s) + a*a/(a+1)**2 + a*a*s/(a+1)) == 0
    print('symbolic: 12 exact identities verified')


def finite_difference(r, alpha, beta, D, x0, h=0.02, L=8):
    n = int(round(2*L/h))+1
    xs = np.linspace(-L,L,n)
    j0 = n//2
    jx = int(round((x0+L)/h))
    assert abs(xs[jx]-x0)<1e-10
    M=lil_matrix((2*n,2*n))
    rhs=np.zeros(2*n)
    for j in range(n):
        for state in (0,1): # 0=active, 1=inactive
            ix=state*n+j
            if state==0 and j==j0:
                M[ix,ix]=1
                continue
            if j==0 or j==n-1:
                M[ix,ix]=1
                M[ix,ix+(1 if j==0 else -1)]=-1
                continue
            switch=alpha if state==0 else beta
            M[ix,ix]=2*D/h**2+r+switch
            for neighbor in (j-1,j+1):
                if state==0 and neighbor==j0:
                    # A arrives at the absorbing point from the left or right.
                    rhs[ix]+=(D/h**2)*(1 if j<j0 else 0)
                else:
                    M[ix,state*n+neighbor]=-D/h**2
            M[ix,(1-state)*n+j]=-switch
            M[ix,state*n+jx]-=r
    values=spsolve(M.tocsr(),rhs)
    return float(values[jx]), float(values[n+jx])


def numerical_checks():
    tests=[(1,1,1,1,1),(1,.1,.1,1,1),(1,10,10,1,1),
           (1.2,.8,1.7,1,.5),(3,2,.5,1,1),(1.4,1.5,.8,1.3,1.0)]
    count=0
    for r,alpha,beta,D,x0 in tests:
        pa,pi,pe=formula(r,alpha,beta,D,x0)
        assert 0<pa<1 and 0<pi<1 and 0<pe<1
        count+=3
        # Refined finite-difference BVP checks are independently derived from
        # the local generator; first-order interface discretization is expected.
        h0=.05
        seq=[]
        for h in (h0,h0/2,h0/4):
            v=finite_difference(r,alpha,beta,D,x0,h=h,L=9)
            err=max(abs(v[0]-pa),abs(v[1]-pi))
            seq.append(err)
            count+=2
        assert seq[2] < seq[1] < seq[0], (r,alpha,beta,seq)
        assert seq[2] < 0.015,(r,alpha,beta,seq)
        count+=2
    for r in (.2,1,3):
      for D in (.7,2):
       for x0 in (.4,1,2):
        for pi_inactive in (.15,.5,.85):
         rates=(.05,.1,.3,1,5,20,100)
         values=[formula(r,pi_inactive*t,(1-pi_inactive)*t,D,x0)[2] for t in rates]
         assert all(b>a for a,b in zip(values,values[1:])), (r,D,x0,values)
         count+=6
         lam=2
         resets=(.05,.1,.3,1,5,20,100)
         values=[formula(rr,pi_inactive*lam,(1-pi_inactive)*lam,D,x0)[2] for rr in resets]
         assert all(b<a for a,b in zip(values,values[1:])), (r,D,x0,values)
         count+=6
    print(f'numerical: {count} finite-grid numerical comparisons, inequalities and monotonicity steps verified')


if __name__=='__main__':
    symbolic_checks()
    numerical_checks()
    print('All reproducibility checks passed; continuous assertions follow from proof.')
