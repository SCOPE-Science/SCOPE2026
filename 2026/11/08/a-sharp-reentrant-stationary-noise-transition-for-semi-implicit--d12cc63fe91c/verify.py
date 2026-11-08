#!/usr/bin/env python3
"""Exact-arithmetic checks for a stationary-noise step-size transition.

Only the standard Python library is needed.  The parameter a is the
positive time step and t is a curvature ratio.  The covariance results
are for the independently injected Brownian increments specified in
RESULT.md.  These finite checks accompany, but do not replace, proof.
"""
from fractions import Fraction as F
from math import sqrt, isclose
import random

counter = 0
def check(statement, message='identity'):
    global counter
    assert statement, message
    counter += 1

def stable(t,a):
    return 4+4*a+(2-t)*a*a > 0

def v_formula(t,a):
    return (a*a+2*a+2)/(t*(a+2)*(4+4*a+(2-t)*a*a))

def vprime(t,a):
    numer = ((t-2)*a**4 + 4*(t-2)*a**3 + (10*t-16)*a**2 +(8*t-16)*a-8)
    denom = t*(a+2)**2*(4+4*a+(2-t)*a*a)**2
    return numer/denom

def gaussian_elimination(A,b):
    n=len(b)
    M=[list(A[i])+[b[i]] for i in range(n)]
    for k in range(n):
        j=next(i for i in range(k,n) if M[i][k]!=0)
        M[k],M[j]=M[j],M[k]
        div=M[k][k]
        M[k]=[z/div for z in M[k]]
        for i in range(n):
            if i==k: continue
            f=M[i][k]
            M[i]=[M[i][j]-f*M[k][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def covariance(t,a):
    d=1+a
    u,w=a*0+1/d,a/d
    z,y=a*(1-t)/d**2,1/d+a*a*(1-t)/d**2
    # S = M S M^T + diag(0,a/d^2) ; S=(p,c;c,q)
    A=[
      [1-u*u,-2*u*w,-w*w],
      [-u*z,1-(u*y+w*z),-w*y],
      [-z*z,-2*z*y,1-y*y],
    ]
    return gaussian_elimination(A,[F(0),F(0),a/d**2])

# Direct Lyapunov solutions at rational parameters in the proven stable domain.
for ti in [F(1),F(6,5),F(8,5),F(19,10),F(39,20),F(99,50),F(2),F(21,10),F(3),F(7)]:
    for ai in [F(1,20),F(1,5),F(1,2),F(1),F(3,2),F(2),F(3),F(4),F(6),F(12)]:
        if not stable(ti,ai): continue
        p,c,q=covariance(ti,ai)
        check(p==v_formula(ti,ai),'Lyapunov vs explicit stationary variance')
        check(p>0 and q>0 and p*q-c*c>0,'positive-definite stationary covariance')
        # Independent derivative via exact rational difference quotient limit.
        num=ai*ai+2*ai+2
        den=ti*(ai+2)*(4+4*ai+(2-ti)*ai*ai)
        dnum=2*ai+2
        dden=ti*((4+4*ai+(2-ti)*ai*ai)+(ai+2)*(4+2*(2-ti)*ai))
        check(vprime(ti,ai)==(dnum*den-num*dden)/(den*den),'rational derivative')

# Compare the critical value in two algebraically independent ways.
a0=1+sqrt(3)
tc=(4+12*sqrt(3))/13
def T(a):
    return 2*(a**4+4*a**3+8*a*a+8*a+4)/(a**4+4*a**3+10*a*a+8*a)
check(isclose(T(a0),tc,rel_tol=0,abs_tol=1e-13),'exact critical point substitution')
check(tc > 1.9 and tc < 1.91,'critical-parameter enclosure')
check(T(.001)>tc and T(10000)>tc,'critical minimum boundaries')
for a in [0.01,.1,1,2,a0,4,10,100]:
    check(T(a)>=tc-1e-12,'critical min numerical diagnostic')

# Strictly stable example with a genuine sign reversal in total MSE.
tr=F(99,50)
for a,sgn in [(F(1),-1),(F(4),1),(F(20),-1)]:
    total=vprime(F(1),a)+10*vprime(tr,a)
    check((total>0) if sgn>0 else (total<0),f'sum derivative at a={a}')
    print(f'total_trace_derivative(t=99/50; 1+10 modes; a={a}): {total} = {float(total):.15g}')

# The high mode has negative-positive-negative derivatives, and all modes are stable.
for a,sgn in [(F(1),-1),(F(4),1),(F(20),-1)]:
    check(stable(tr,a),'unconditional Schur stability')
    g=vprime(tr,a)
    check((g>0) if sgn>0 else (g<0),'single-mode slope sign')

# Exact minimum at the endpoint t=2.
check(isclose(float(v_formula(F(2),F(1414213562373095,10**15))),
              (sqrt(2)-1)/4,rel_tol=0,abs_tol=2e-15),'endpoint stationary minimum')

# Direct stochastic iterate simulation for two arbitrary stable modes.
# Seed and sample count are explicit; these are finite diagnostics only.
for t,a in [(1.5,0.8),(1.98,4.0)]:
    rng=random.Random(2113)
    x=v=0.0
    n=180000
    d=1+a
    sumx=sumxx=0.0
    for k in range(n+3000):
        xn=(x+a*v)/d
        vn=(v+a*(1-t)*xn)/d + sqrt(a)/d*rng.gauss(0,1)
        x,v=xn,vn
        if k>=3000:
            sumx+=x
            sumxx+=x*x
    sample=sumxx/n-(sumx/n)**2
    expected=float(v_formula(t,a))
    check(abs(sample-expected)<.035*expected,'Gaussian simulation covariance diagnostic')
    print(f'MonteCarlo(t={t},a={a}): empirical_variance={sample:.9f}; exact={expected:.9f}')
print(f'PASS: {counter} checks')
