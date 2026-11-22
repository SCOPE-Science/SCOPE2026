#!/usr/bin/env python3
"""Independent numerical and exact sanity checks for the ring-torus normal-pair law.

Requires Python 3, NumPy, SciPy and SymPy. These tests are corroborative;
proof of the limiting density and its endpoint constants is analytic.
"""
import math
import numpy as np
import sympy as sp
from scipy.special import eval_legendre, gammaln

def b(k):
    return math.comb(2*k, k) / 4**k


# Exact arcsine-Legendre integrals: E[Z^(2j)] = binom(2j,j)/4^j.
z = sp.Symbol('z')
for k in range(9):
    p = sp.Poly(sp.legendre(2*k, z), z)
    val = sum(coef * sp.Rational(math.comb(degree, degree//2), 4**(degree//2))
              for (degree,), coef in p.terms())
    expected = sp.Rational(math.comb(2*k,k)**2,16**k)
    assert val == expected, (k, val, expected)

# All points sampled exactly from area measure by rejection from the torus
# cross-sectional angle, with an independent uniform rotation angle.
rng=np.random.default_rng(20261119)
n=180_000
for ratio in (1.2,3.0,8.0):
    phases=[]
    count=0
    while count<2*n:
        u=rng.uniform(0,2*math.pi,size=n)
        good=rng.uniform(0,1,size=n)*(ratio+1) < ratio+np.cos(u)
        phases.append(u[good])
        count+=int(np.sum(good))
    u=np.concatenate(phases)[:2*n]
    phi=rng.uniform(0,2*math.pi,size=2*n)
    normals=np.column_stack((np.cos(phi)*np.cos(u),
                             np.sin(phi)*np.cos(u),np.sin(u)))
    t=np.einsum('ij,ij->i',normals[:n],normals[n:])
    m2=float(np.mean(t*t))
    l4=float(np.mean(eval_legendre(4,t)))
    assert abs(m2-3/8)<0.007, (ratio,m2)
    assert abs(l4-b(2)**4)<0.008, (ratio,l4)
    print(f'R/r={ratio:.1f}: E[T^2]={m2:.6f}, E[P4(T)]={l4:.6f}')

# Endpoint log coefficient of exact spectral sum, computed at two
# small positive angular separations (not used as a proof).
k=np.arange(1,3800)
logb=gammaln(2*k+1)-2*gammaln(k+1)-k*math.log(4)
c=(4*k+1)*np.exp(4*logb)/2
angles=(0.02,0.008)
values=[]
for angle in angles:
    f=float(0.5+np.dot(c,eval_legendre(2*k,math.cos(angle))))
    values.append(f)
    residual=f-2/math.pi**2*math.log(1/angle)
    print(f'angle={angle:.3f}: f(cos(angle))={f:.6f}; log residual={residual:.6f}')
assert abs((values[1]-values[0])-
           2/math.pi**2*math.log(angles[0]/angles[1]))<0.04
print('All exact finite and numerical diagnostics passed.')
