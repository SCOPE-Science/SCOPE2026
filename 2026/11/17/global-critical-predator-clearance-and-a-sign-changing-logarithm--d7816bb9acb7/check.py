#!/usr/bin/env python3
"""Reproducibility checks for the critical ratio-dependent predator-prey flow.
Requires sympy, scipy, and numpy. Analytic proofs are in RESULT.md.
"""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

v,a,alpha,d=sp.symbols('v a alpha d',positive=True)
# At criticality u=1-a*v+O(v**2). Expand reciprocal-predator drift.
u=1-a*v
D=d*(1-sp.exp(-alpha*v/u))/v
series=sp.series(D,v,0,2).removeO().expand()
assert sp.simplify(series-d*alpha-d*alpha*(a-alpha/2)*v)==0
# The ratio equation uses f(z)=(d+a z)exp(-alpha z),
# and f'(z)<=0 for all z>=0 when a<=alpha*d.
z=sp.symbols('z',nonnegative=True)
f=(d+a*z)*sp.exp(-alpha*z)
assert sp.simplify(sp.diff(f,z)-sp.exp(-alpha*z)*(a-alpha*d-alpha*a*z))==0
# Exact identity for E=(1-u)-a*v, with b=d and z=v/u.
u,v_sym=sp.symbols('u v',positive=True)
e=sp.exp(-alpha*v_sym/u)
fu=u*(1-u)-a*v_sym*e
fv=d*v_sym*(e-1)
E=1-u-a*v_sym
Eder=sp.diff(E,u)*fu+sp.diff(E,v_sym)*fv
assert sp.simplify(Eder-(-u*E+a*v_sym*((1-d)*e+d-u)))==0

records=[]
for av in (0.2,0.5,0.9):
    alpha_v,dv=1.,1.
    def rhs(t,y):
        u,v=y
        e=np.exp(-alpha_v*v/u)
        return (u*(1-u)-av*v*e, dv*v*(e-1))
    sol=solve_ivp(rhs,(0,100000),(0.7,0.4),method='DOP853',rtol=2e-9,atol=3e-12,
                  dense_output=True,max_step=2.0)
    assert sol.success,sol.message
    u1,v1=sol.sol(10000.)
    u2,v2=sol.sol(100000.)
    lead=100000.*v2
    prey=100000.*(1-u2)
    corrected=((1/v2-100000)-(1/v1-10000))/np.log(10.)
    records.append((av,float(lead),float(prey),float(corrected),av-0.5))
    assert abs(lead-1)<0.002
    assert abs(prey-av)<0.003
    assert abs(corrected-(av-0.5))<0.01
print('Symbolic Taylor and monotonicity checks: PASS')
print('a, t v, t(1-u), observed log slope, predicted log slope:')
for x in records: print(' '.join(f'{r:.8f}' for r in x))
print('Numerical diagnostics: PASS')
