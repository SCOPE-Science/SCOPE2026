#!/usr/bin/env python3
"""Independent numerical and symbolic checks of the explicit spectral formulas."""
from __future__ import annotations
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from scipy.special import ive, jn_zeros, gammaln, gammainc
from scipy.linalg import eigh

checks = 0

def chk(test, msg):
    global checks
    checks += 1
    if not bool(test):
        raise AssertionError(msg)

def positive_eigenvalue(t, order=180):
    nodes, weights = leggauss(order)
    x = t * (nodes + 1) / 2
    w = t * weights / 2
    X = np.sqrt(x[:, None] * x[None, :])
    # e^(-u-v) I_1(2 sqrt(uv)) = e^{-(sqrt u-sqrt v)^2} ive(1,2 sqrt(uv)).
    k = np.exp(-(np.sqrt(x[:, None]) - np.sqrt(x[None, :])) ** 2) * ive(1, 2 * X)
    M = k * np.sqrt(w[:, None] * w[None, :])
    return float(eigh(M, subset_by_index=(order-1, order-1), check_finite=False)[0][0])

# Semigroup Laplace exponents obey u_{s+t}(theta)=u_s(u_t(theta)).
theta, s, t = sp.symbols('theta s t', positive=True)
u = lambda tim, x: x/(1+tim*x)
chk(sp.simplify(u(s,u(t,theta))-u(s+t,theta)) == 0, 'branching semigroup Laplace law')
for n in range(1, 21):
    chk(sp.simplify(u(n,theta) - theta/(1+n*theta)) == 0, 'n step semigroup')

# Verify modified-Bessel kernel against its positive Gram expansion.
for a in [0.03,0.12,0.4,1.0,3.5,10.0]:
    for b in [0.01,0.17,0.9,5.5]:
        lhs = np.exp(-(a+b)) * ive(1,2*np.sqrt(a*b)) * np.exp(2*np.sqrt(a*b))
        rhs = np.exp(-(a+b)) * sum((a*b)**(k+0.5)/(float(sp.factorial(k))*float(sp.factorial(k+1))) for k in range(50))
        chk(abs(lhs-rhs) < 1e-9 * max(1.0,lhs), 'Gram series')

# Relative quadrature errors and exact small-time law.
small = [0.006,0.012,0.025,0.04]
for tt in small:
    lam = positive_eigenvalue(tt, 80)
    trunc = tt**2/2 - 2*tt**3/3
    chk(abs(lam-trunc) < 0.65*tt**4, f'small time expansion {tt} {lam}')
    chk(lam > 0 and lam < tt**2/2, 'small time positive correction')

vals = [(tt, positive_eigenvalue(tt)) for tt in [0.25,0.7,2.0,8.0,25.0,75.0,200.0,500.0]]
for i,(tt,lam) in enumerate(vals):
    chk(0 < lam < 1, 'spectral radius in (0,1)')
    if i:
        chk(lam > vals[i-1][1], 'strict time monotonicity')

bessel_gap = float(jn_zeros(1,1)[0]**2/4)
times = [25,75,200,500]
gaps = [tt * (1-positive_eigenvalue(tt)) for tt in times]
for g in gaps:
    chk(g < bessel_gap, 'finite-time gap below Bessel limit')
for g1,g2 in zip(gaps,gaps[1:]):
    chk(g2 > g1, 'Bessel gap convergence from below')
chk(abs(gaps[-1]-bessel_gap)/bessel_gap < 0.05, 'large-time Bessel coefficient trend')

# Independent Gram-moment method: the Bessel kernel is a sum of rank-one
# functions e^{-x} x^{k+1/2}/sqrt(k!(k+1)!). Their inner products are
# incomplete-gamma integrals, not the Nyström quadrature above.
for tt in [0.05, 0.25, 1.0, 3.0, 8.0]:
    N = 50
    a = np.arange(N)[:, None]
    b = np.arange(N)[None, :]
    p = a+b+2
    logden = p*np.log(2)+0.5*(gammaln(a+1)+gammaln(a+2)+gammaln(b+1)+gammaln(b+2))
    gram = np.exp(gammaln(p)-logden)*gammainc(p,2*tt)
    gram_lam = eigh(gram, subset_by_index=(N-1,N-1), check_finite=False)[0][0]
    direct_lam = positive_eigenvalue(tt, 130)
    chk(abs(gram_lam-direct_lam)<2e-10, 'independent incomplete-gamma Gram spectrum')

# The leading pole is real and negative, and its magnitude approaches 1 at long time.
for tt,lam in vals:
    pole = -1/lam
    chk(pole < -1, 'analytic pole outside physical omega > -1')

print(f'PASS: {checks} deterministic checks; Bessel coefficient = {bessel_gap:.12f}')
print('large-time t*(1-lambda):',list(zip(times,gaps)))
