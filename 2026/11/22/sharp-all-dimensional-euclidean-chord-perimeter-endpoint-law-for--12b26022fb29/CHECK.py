"""Reproducible symbolic and deterministic numerical diagnostics for the chord-perimeter law."""
import math
import numpy as np
import sympy as sp
from scipy.special import betainc, gammaln, roots_legendre

u, v, t = sp.symbols('u v t', real=True)
w = u*v - sp.sqrt((1-u*u)*(1-v*v))*sp.sqrt(1-t*t)
P = sp.sqrt(2-2*u) + sp.sqrt(2-2*v) + sp.sqrt(2-2*w)
H = sp.simplify(sp.hessian(3*sp.sqrt(3)-P, (u,v,t)).subs({u: -sp.Rational(1,2), v: -sp.Rational(1,2), t: 0}))
expected = sp.Matrix([[2*sp.sqrt(3)/3, sp.sqrt(3)/3, 0], [sp.sqrt(3)/3, 2*sp.sqrt(3)/3, 0], [0, 0, sp.sqrt(3)/4]])
assert H == expected
assert sp.simplify(H.det()-sp.sqrt(3)/4) == 0
assert all(float(z) > 0 for z in (H[0,0], H[:2,:2].det(), H.det()))

def constant(d):
    return math.exp((4-d/2)*math.log(2)+(3*d-10)/4*math.log(3)
                    + math.lgamma(d/2)-math.log(d)-0.5*math.log(math.pi)
                    -math.lgamma((d-1)/2))
assert abs(constant(3) - 2*math.sqrt(2)/(3*3**0.25)) < 1e-13
assert abs(constant(4) - 2*math.sqrt(3)/math.pi) < 1e-13

# Exact spherical conditional probability: for pairwise inner products u,v,
# s_1 has symmetric beta ((d-2)/2,(d-2)/2) law under x=(s_1+1)/2.
# The sublevel event necessarily has |u+1/2|,|v+1/2| < 4 sqrt(eps)
# for eps <= 0.01: by sum ell_ij^2 <= 9, Cauchy and
# sum(ell_ij-P/3)^2 <= 2 sqrt(3) eps, and ell_ij <= 2.
# Hence integrating on this entire square is not domain truncation.
def exact_event_quadrature(d, eps, N=320):
    assert 0 < eps <= 0.01
    a, wa = roots_legendre(N)
    L = 4*math.sqrt(eps)
    grid = -0.5 + L*a
    U, V = np.meshgrid(grid,grid,indexing='ij')
    weights = np.outer(wa,wa)*L**2
    assert min(grid)>-1 and max(grid)<1
    c=math.exp(math.lgamma(d/2)-0.5*math.log(math.pi)-math.lgamma((d-1)/2))
    fu = c*(1-U**2)**((d-3)/2)
    fv = c*(1-V**2)**((d-3)/2)
    needed = 3*math.sqrt(3)-eps-np.sqrt(2-2*U)-np.sqrt(2-2*V)
    assert np.min(needed)>0
    T=(1-needed**2/2-U*V)/np.sqrt((1-U**2)*(1-V**2))
    q = betainc((d-2)/2,(d-2)/2,np.clip((T+1)/2,0,1))
    return float(np.sum(fu*fv*q*weights))

for dim in (3,4,5,7):
    vals = []
    for eps in (0.01,0.002,0.0005):
        p = exact_event_quadrature(dim,eps)
        ratio = p/(constant(dim)*eps**(dim/2))
        assert math.isfinite(ratio) and 0.97 < ratio < 1.02, (dim,eps,ratio)
        vals.append(round(ratio,8))
    assert abs(vals[-1]-1) < abs(vals[0]-1)
    print(f'd={dim}: C={constant(dim):.12f}, ratios={vals}')
print('ALL_CHECKS_PASSED')
