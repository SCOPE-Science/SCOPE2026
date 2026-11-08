"""Checks for the exact two-phase rank-one extragradient singular spectrum.

Run: python verify.py
Requires numpy and sympy. Analytic proof is in RESULT.md; finite tests are auxiliary.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

checks = 0

def require(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def step(h, v):
    v = np.asarray(v, dtype=float)
    outer = np.outer(v, v)
    out = np.eye(3)
    out[0, 0] = 1 - h*h
    out[0, 1:] = -h*v
    out[1:, 0] = h*v
    out[1:, 1:] -= h*h*outer
    return out

def claimed_singular_values(h, overlap):
    d = h*h*(1-h*h)
    k = 1-d
    c = abs(overlap)
    root = math.sqrt(4*k+d*d*c*c)
    return np.array([(root+d*c)/2, (root-d*c)/2, k])

# Symbolic polynomial identity in the coordinate chart
# u=(1,0), v=(c,s), with c^2+s^2=1.
h, c, s, L = sp.symbols('h c s L', real=True)
def sym_step(v):
    m = sp.eye(3)
    m[0,0] = 1-h*h
    for i in range(2):
        m[0,i+1] = -h*v[i]
        m[i+1,0] = h*v[i]
        for j in range(2):
            m[i+1,j+1] -= h*h*v[i]*v[j]
    return m
p = sym_step((c,s))*sym_step((1,0))
k = 1-h*h+h**4
d = h*h*(1-h*h)
poly = sp.expand(sp.det(L*sp.eye(3)-p.T*p))
expected = sp.expand((L-k*k)*(L*L-(2*k+d*d*c*c)*L+k*k))
remainder = sp.rem(sp.Poly(sp.expand(poly-expected),s),
                   sp.Poly(s*s+c*c-1,s)).as_expr()
require(sp.simplify(remainder)==0, 'symbolic characteristic identity')
require(sp.simplify(k+d-1)==0, 'contraction identity')
require(sp.simplify(sp.expand((2-d*c*c)**2-c*c*(4*(1-d)+d*d*c*c))-4*(1-c*c))==0,
        'strict monotonicity certificate')
require(sp.simplify((sp.sqrt(48+1)+1)/8-1)==0,
        'parallel endpoint')
require(sp.simplify(sp.sqrt(48)/8-sp.sqrt(3)/2)==0,
        'orthogonal endpoint')

for ih in range(1,60):
    hh=ih/60
    for ia in range(0,91):
        theta=math.pi*ia/180
        vv=(math.cos(theta),math.sin(theta))
        pp=step(hh,vv)@step(hh,(1,0))
        calculated=np.linalg.svd(pp,compute_uv=False)
        claimed=claimed_singular_values(hh,vv[0])
        require(np.max(np.abs(calculated-claimed))<3e-13,
                f'singular values h={hh} angle={theta}')
        optimized=(math.sqrt(48+vv[0]**2)+abs(vv[0]))/8
        require(claimed[0] >= optimized-2e-14,
                'global best one-cycle norm violated')
        require(claimed[0] < 1+2e-13,
                'contractivity bound violated')

# Sharp equal-step setting, for rational unit vectors and rational h^2.
for cc,ss in [(sp.Rational(0),sp.Rational(1)),
              (sp.Rational(3,5),sp.Rational(4,5)),
              (sp.Rational(5,13),sp.Rational(12,13)),
              (sp.Rational(1),sp.Rational(0))]:
    for hh in [sp.Rational(1,2), sp.sqrt(sp.Rational(1,2)), sp.Rational(4,5)]:
        mat=p.subs({h:hh,c:cc,s:ss})
        k0=sp.simplify(k.subs(h,hh)); d0=sp.simplify(d.subs(h,hh))
        polys=sp.factor((mat.T*mat).charpoly().as_expr())
        # charpoly uses its own lambda symbol.
        zz=list((mat.T*mat).charpoly().gens)[0]
        want=sp.expand((zz-k0**2)*(zz**2-(2*k0+d0**2*cc**2)*zz+k0**2))
        require(sp.simplify(sp.expand(polys-want))==0,'exact rational matrix certificate')

# Strict optimum away from parallelity in the entire allowed step region.
for cc in [0,0.125,0.25,0.5,0.8,0.99,0.9999]:
    factors=[claimed_singular_values(math.sqrt(z),cc)[0]
             for z in [0.01,0.1,0.2,0.3,0.4,0.49,0.5,0.51,0.6,0.8,0.99]]
    require(min(factors)==factors[6], 'sample optimum must be h^2=1/2')

print(f'PASS {checks} checks: exact characteristic polynomial, endpoints, '
      'monotonicity certificate, dense singular-value grid, and rational cases')
