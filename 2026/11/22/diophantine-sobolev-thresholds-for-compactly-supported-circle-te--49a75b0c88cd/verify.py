#!/usr/bin/env python3
"""Standalone finite checks for a circular triangular-kernel spectrum.

Requires Python 3 standard library and optionally mpmath for quadrature.
These checks are not a proof of any infinite statement.
"""
import cmath, math

def a_formula(n,c):
    return c*c/(2*math.pi) if n==0 else (1-math.cos(n*c))/(math.pi*n*n)

def a_exact_rational(n,c):
    if n==0: return c*c/(2*math.pi)
    return 2*math.sin(n*c/2)**2/(math.pi*n*n)

for c in (math.pi/2,math.pi/3,math.pi,math.pi/math.sqrt(2)):
    for n in range(-13,14):
        assert abs(a_formula(n,c)-a_exact_rational(n,c)) < 2e-14

# Two rotation orbits at c=pi/2: support four-point orbits.
q=4
xs=[2*math.pi*j/q for j in range(q)] + [.137+2*math.pi*j/q for j in range(q)]
w=[1]*q+[-1]*q
energy=sum(w[i]*w[j]*max(math.pi/2-min(abs(xs[i]-xs[j]),2*math.pi-abs(xs[i]-xs[j])),0) for i in range(2*q) for j in range(2*q))
assert abs(energy)<1e-10,energy

# Finite spectral coboundary norm identity for irrational support.
c=math.pi/math.sqrt(2)
fs={-3:complex(.1,-.3),1:complex(.7,.2),2:complex(-.2,.4),5:complex(.5,0)}
rk=sum(abs(v)**2/a_exact_rational(n,c) for n,v in fs.items())
g={n:1j*n*v/(1-cmath.exp(1j*n*c)) for n,v in fs.items()}
assert abs(rk-2*math.pi*sum(abs(v)**2 for v in g.values()))<1e-10

# Classical convergents distinguish a badly approximable irrational.
phi=(math.sqrt(5)-1)/2
vals=[n*abs(n*phi-round(n*phi)) for n in range(1,5000)]
assert min(vals)>.3

try:
    import mpmath as mp
    mp.mp.dps=50
    for c,n in ((mp.pi/2,3),(mp.pi/3,11),(mp.pi/mp.sqrt(2),7)):
        z=(1/mp.pi)*mp.quad(lambda t:(c-t)*mp.cos(n*t),[0,c])
        b=(1-mp.cos(n*c))/(mp.pi*n*n)
        assert abs(z-b)<mp.mpf('1e-39')
except ImportError:
    print('Optional mpmath quadrature unavailable; elementary checks passed')
print('Spectral, orbit-nullity, and coboundary diagnostics passed')
