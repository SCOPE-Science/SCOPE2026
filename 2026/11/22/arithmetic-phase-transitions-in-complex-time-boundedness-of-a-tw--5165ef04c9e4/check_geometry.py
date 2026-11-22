"""Finite numerical diagnostics for two-rate Gaussian semigroup slice formulas.
The theorem is proved analytically; these numerical tests are not proof of equidistribution.
"""
import math
import numpy as np
k=math.sqrt(3.0)

def fraction(a,b,t):
    x=np.arange(0.5,1200000.5,1.)*(10000./1200000.)
    return np.mean((np.abs(np.sin(a*x))<=k*np.sinh(a*t)) & (np.abs(np.sin(b*x))<=k*np.sinh(b*t)))

def product(a,b,t):
    def f(c):
        return 2/math.pi*math.asin(min(1.0,k*math.sinh(c*t)))
    return f(a)*f(b)

for t in (0.06,0.12,0.2):
    observed=fraction(1, math.sqrt(2), t)
    expected=product(1, math.sqrt(2), t)
    print('irrational',t, 'observed',observed,'predicted',expected,'error',abs(observed-expected))
    assert abs(observed-expected)<0.0015
for m,n in ((2,3),(1,1),(3,5)):
    lam=0.5
    a,b=m*lam,n*lam
    for t in (0.005,0.01):
        delta=lambda v:math.asin(k*math.sinh(v*t))/v
        expected=2*lam/math.pi*min(delta(a),delta(b))
        x=np.arange(0.5,500000.5,1.)*(math.pi/lam/500000.)
        observed=np.mean((np.abs(np.sin(a*x))<=k*np.sinh(a*t)) & (np.abs(np.sin(b*x))<=k*np.sinh(b*t)))
        print('rational',m,n,t,observed,expected)
        assert abs(observed-expected)<1.0/500000+1e-6
print('GEOMETRY_DIAGNOSTICS_OK')
