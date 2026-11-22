#!/usr/bin/env python3
"""Independent numerical and symbolic cross-checks of the two-layer OU transport theorem.

Requires Python, numpy, scipy, mpmath and sympy.  Numeric tests complement,
but do not replace, the analytic sign/uniqueness proof in RESULT.md.
"""
import math
from numpy import array, outer, dot, linspace, exp
from scipy.linalg import solve_continuous_lyapunov, expm
from scipy.optimize import brentq
import sympy as sp
import mpmath as mp

COUNT = 0

def check(cond, note):
    global COUNT
    if not cond:
        raise AssertionError(note)
    COUNT += 1

def close(a,b,atol=1e-9,rtol=2e-9):
    return abs(a-b) <= atol+rtol*max(abs(a),abs(b))

def terms(g1,g2,D1,D2):
    a = D1*g1**3/(g1*g1-g2*g2)
    b = g2*(D2-D1*g1*g1/(g1*g1-g2*g2))
    return a,b

def C(t,g1,g2,D1,D2):
    a,b=terms(g1,g2,D1,D2)
    return a*math.exp(-g1*t)+b*math.exp(-g2*t)

def J(t,g1,g2,D1,D2):
    a,b=terms(g1,g2,D1,D2)
    return a*(-math.expm1(-g1*t))/g1+b*(-math.expm1(-g2*t))/g2

def M(t,g1,g2,D1,D2):
    a,b=terms(g1,g2,D1,D2)
    return 2*(a*(t/g1+math.expm1(-g1*t)/g1**2)
              +b*(t/g2+math.expm1(-g2*t)/g2**2))

def H(t,g1,g2,D1,D2):
    a,b=terms(g1,g2,D1,D2)
    return 2*(a*(1-(1+g1*t)*math.exp(-g1*t))/g1**2
             +b*(1-(1+g2*t)*math.exp(-g2*t))/g2**2)

q,d=sp.symbols('q d',positive=True)
A=sp.simplify(d/(1-q*q))  # with gamma1=D2=1
B=sp.simplify(q*(1-d/(1-q*q)))
check(sp.simplify(A+B/q-1)==0,'Green-Kubo limit')
check(sp.simplify(A+B-(d/(1+q)+q))==0,'positive zero-lag variance')
check(sp.simplify(A+B/q**2-(1/q)*(1-d/(1+q)))==0,'first covariance moment')
check(sp.simplify(A/(-B)-d/(q*(d-1+q*q)))==0,'crossing time')
for g1,g2 in [(1.,0.1),(1.,0.5),(2.4,0.7),(1.001,1.),(3.,0.004)]:
    q=g2/g1
    for d in [0.3*(1-q*q), 1-q*q, (1-q*q+1+q)/2, 1., 1+q, 1+q+0.25, 3*(1+q)]:
        D1=d*1.3;D2=1.3
        a,b=terms(g1,g2,D1,D2)
        F=array([[-g1,0.],[-g1,-g2]])
        Q=array([[2*D1,0.],[0.,2*D2]])
        S=solve_continuous_lyapunov(F,-Q)
        v=array([g1,g2])
        check(close(v@S@v,a+b,atol=1e-7),'independent Lyapunov zero lag')
        for t in [0.01/g1,0.1/g1,0.6/g1,1/g2,3/g2]:
            c1=float(v@expm(F*t)@S@v)
            c2=C(t,g1,g2,D1,D2)
            check(close(c1,c2,atol=1e-7),'independent matrix covariance')
            if t>=0.1/g1:
                hh=H(t,g1,g2,D1,D2)
                mm=M(t,g1,g2,D1,D2)
                jj=J(t,g1,g2,D1,D2)
                check(mm>0 and jj>0,'positive MSD and finite-window diffusion')
                check(close(t*2*jj-mm,hh,atol=1e-7),'integral identity')
                check(close((H(t+1e-5/g1,g1,g2,D1,D2)-H(t-1e-5/g1,g1,g2,D1,D2))/(2e-5/g1), 2*t*c2,atol=1e-5,rtol=2e-4),'sign-function derivative')
        c_inf=D2/g2*(1-d/(1+q))
        check(close(a/g1**2+b/g2**2,c_inf,atol=1e-6),'sharp far-tail sign')
        if d>1-q*q+1e-10:
            tc=math.log(a/-b)/(g1-g2)
            check(tc>0 and abs(C(tc,g1,g2,D1,D2))<1e-7,'unique covariance crossing')
            check(J(tc,g1,g2,D1,D2)>D2,'diffusivity overshoot')
        for t in [0.2/g1,1/g1,4/g2,30/g2]:
            h=H(t,g1,g2,D1,D2)
            if d<=1+q+1e-10: check(h> -1e-10,'no subdiffusive local exponent')
        if d>1+q+1e-10:
            tc=math.log(a/-b)/(g1-g2)
            f=lambda x: H(x,g1,g2,D1,D2)
            root=brentq(f,tc,200/g2)
            check(root>tc,'subdiffusive phase begins after covariance crossover')
            check(f(root-0.005/g1)>0 and f(root+0.005/g1)<0,'unique exponent crossing')

# Exact critical asymptotic with high precision, guarding cancellation.
mp.mp.dps=65
for qr in ['0.1','0.3','0.5','0.8']:
    g1=mp.mpf(1);g2=mp.mpf(qr);D2=mp.mpf(1); D1=1+g2
    AA=D1/(1-g2*g2);BB=g2*(1-D1/(1-g2*g2))
    for t in [mp.mpf('50')/g2,mp.mpf('80')/g2]:
        Hh=2*(AA*(1-(1+g1*t)*mp.exp(-g1*t))/g1**2+BB*(1-(1+g2*t)*mp.exp(-g2*t))/g2**2)
        Mm=2*(AA*(t/g1+(mp.exp(-g1*t)-1)/g1**2)+BB*(t/g2+(mp.exp(-g2*t)-1)/g2**2))
        scaled=(Hh/Mm)/mp.exp(-g2*t)
        check(abs(scaled/(g2/(1-g2))-1)<mp.mpf('0.04'),'critical exponential prefactor')
print('PASS:',COUNT,'independent and algebraic checks')
