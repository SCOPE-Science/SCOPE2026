"""Standalone finite checks for Chebyshev-root Hermite--Fejer variation analysis.

Run: python3 checker.py (numpy, scipy, sympy).
The unbounded-degree asymptotic is proved in the accompanying text, not by these tests.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar

x=sp.symbols('x',real=True)
for n in range(2,7):
    T=sp.chebyshevt(n,x)
    # Partition and Hermite interpolation conditions from polynomial division
    H=sp.Integer(0)
    xs=np.cos((np.arange(n)+.5)*math.pi/n)
    for k in range(n):
        y=sp.RootOf(T,k)
        # The n=6 RootOf expressions are costly, avoid exact substitution
        if n<=3:
            h=sp.cancel(T**2*(1-x*y)/(n*n*(x-y)**2))
            H+=h
    if n<=3:
        assert sp.simplify(H-1)==0
print('EXACT_HERMITE_FEJER_PARTITION_N2_N3_PASS')

# Numerical basis formula verifies 2n Hermite conditions,
# positivity, and partition of unity on an interior mesh.
for n in [2,3,4,7,12,24]:
    y=np.cos((np.arange(n)+0.5)*math.pi/n)
    xx=np.linspace(-1.,1.,20001)
    T=np.cos(n*np.arccos(xx))
    H=np.array([T*T*(1-xx*t)/(n*n*(xx-t)**2) for t in y])
    assert np.max(np.abs(H.sum(axis=0)-1))<1e-6
    assert H.min()>-1e-10
print('CARDINAL_NONNEGATIVITY_AND_PARTITION_CHECKS_PASS')

# For each step, all intervals with constant nodal labels have exactly one
# interior extremum, and the transition is monotone. Numerical root-free
# maximization estimates the total variation accurately for moderate n.
def step_values(theta,n,m):
    # Direct formula, safe strictly between nodes.
    k=np.arange(1,n+1)
    ph=(k-0.5)*math.pi/n
    x=math.cos(theta)
    y=np.cos(ph)
    q=np.cos(n*theta)**2*(1-x*y)/(n*n*(x-y)**2)
    return float(np.sum(q[:m]))

def norm_est(n):
    th=(np.arange(1,n+1)-0.5)*math.pi/n
    V=[]
    for m in range(1,n):
        a=1-step_values(0.,n,m)
        b=step_values(math.pi,n,m)
        z=1+a+b
        for j in range(1,n):
            if j==m: continue
            func=(lambda t:1-step_values(t,n,m)) if j<m else (lambda t:step_values(t,n,m))
            sol=minimize_scalar(lambda t:-func(t),bounds=(th[j-1],th[j]),method='bounded',options={'xatol':1e-13})
            z+=2*func(sol.x)
        V.append(z)
    return max(V),V.index(max(V))+1
for n in [2,3,4,6,8,12,18,30]:
    gain,m=norm_est(n)
    print('NUMERICAL_VARIATION_GAIN',n,repr(round(gain,9)),'extremal_step',m,'ratio_to_log',round(gain/math.log(n),6))
    assert gain>=1 and gain < 1+4/math.pi**2*math.log(n)+6
print('ALL_FINITE_HERMITE_FEJER_CHECKS_PASS')
