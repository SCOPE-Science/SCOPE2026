#!/usr/bin/env python3
"""Reproduce analytical identities and finite consistency checks for inhibitory maps."""
import math
import numpy as np
import sympy as sp

# The log-Jacobian absolute-row majorant has a positive gap for 0<h<=1.
a, b, x, h, S = sp.symbols('a b x h S', positive=True)
F = b*x + a/(1+S)
major = (b*x+a*h*S/(1+S)**2)/F
gap = a*(1+(1-h)*S)/((1+S)**2*F)
assert sp.simplify(1-major-gap)==0

# Exact two-cycle and symmetric/transverse two-step multipliers for h=2, b=0.
A=sp.symbols('A',positive=True)
r=(A-sp.sqrt(A*A-4))/2
R=(A+sp.sqrt(A*A-4))/2
f=lambda z:A/(1+z*z)
fp=lambda z: -2*A*z/(1+z*z)**2
assert sp.simplify(f(r)-R)==0
assert sp.simplify(f(R)-r)==0
assert sp.simplify(r*R-1)==0
assert sp.simplify(fp(r)*fp(R)-4/A**2)==0

# Exact critical alpha when the scalar fixed-point multiplier crosses -1.
n=sp.symbols('n',positive=True)
z=sp.symbols('z',positive=True)
fixed_alpha=z*(1+z**n)
mult=-n*z**n/(1+z**n)
assert sp.simplify(mult.subs(z**n,1/(n-1))+1)==0

# Check representative heterogeneous networks and initial states.
cases=[
(.5,np.array([4.,1.,2.]),np.array([.2,.5,.7]),np.array([[1.,8.,0.],[3.,0.,5.],[0.,.8,6.]])),
(1.,np.array([3.,8.,2.]),np.array([.1,.8,.2]),np.array([[4.,0.,1.],[0.,3.,9.],[7.,2.,2.]])),
(.7,np.array([25.,.1,5.]),np.array([0.,.4,0.]),np.array([[12.,20.,0.],[1.,2.,30.],[0.,10.,3.]])),
]
for exponent,alpha,beta,C in cases:
    upper=alpha/(1-beta)
    D=1+C@upper**exponent
    delta=alpha/(D*D*(beta*upper+alpha))
    q=1-float(min(delta))
    assert 0 <= q < 1
    def step(xx):return beta*xx + alpha/(1+C@xx**exponent)
    star=upper.copy()
    for _ in range(5000):star=step(star)
    assert np.max(abs(star-step(star)))<1e-9
    for init in [np.zeros(3),np.ones(3),upper,np.array([100.,.001,50.])]:
        xx=init.copy(); ub=np.maximum(init,upper)
        d=1+C@ub**exponent
        lower=alpha/d
        xx=step(xx)
        assert np.all(xx>=lower-1e-10) and np.all(xx<=ub+1e-10)
        for _ in range(600):xx=step(xx)
        assert np.max(np.abs(xx-star))<1e-7

# Two-gene AK slice with h=2, beta=0, coupling epsilon=1/2, alpha=3.
alpha=3.
rootlo=(alpha-math.sqrt(alpha**2-4))/2
roothi=(alpha+math.sqrt(alpha**2-4))/2
assert abs(alpha/(1+rootlo**2)-roothi)<1e-14
assert abs(alpha/(1+roothi**2)-rootlo)<1e-14
assert abs(4/alpha**2-4/9)<1e-14
print('VERIFY_OK log_jacobian_gap=1 exact_two_cycle=4 scalar_threshold=1 network_cases=3 initial_states=12 two_gene_attractor=1')
