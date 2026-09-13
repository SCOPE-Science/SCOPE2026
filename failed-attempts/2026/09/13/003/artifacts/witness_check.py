"""Numerical check for lane-1447 witness (numpy only).
Verifies Var/D ratio growth for psi_R(t)=min(max(t,0)^beta,R^beta),
beta=(2nu+1)/4, under univariate t_nu, plus MC in marginal direction.
"""
import math
import numpy as np

def c1(nu):
    return math.gamma((nu + 1) / 2) / (math.sqrt(math.pi * nu) * math.gamma(nu / 2))

nu = 3.0
c = c1(nu)
beta = (2 * nu + 1) / 4
print(f"c1({nu})={c:.6f} beta={beta}")
print("quadrature (trapezoid) 1D t_3:")
xs = np.concatenate([np.linspace(0, 1, 4001), np.logspace(0, 6, 40001)])
p = c * (1 + xs * xs / nu) ** (-(nu + 1) / 2)
for R in [5, 20, 100, 1000]:
    f = np.minimum(np.maximum(xs, 0.0) ** beta, R ** beta)
    fp = np.where(xs < R, beta * np.maximum(xs, 0.0) ** (beta - 1), 0.0)
    m1 = np.trapz(f * p, xs)
    m2 = np.trapz(f * f * p, xs)
    den = np.trapz(fp * fp * p, xs)
    print(f"  R={R:5d} Var~{m2 - m1*m1:12.3f} Den~{den:.4f} ratio~{(m2-m1*m1)/den:10.1f}")
print("MC marginal-direction (n=5,nu=3):")
rng = np.random.default_rng(0)
N = 400000
nn = 5
G = rng.chisquare(nu, size=N)
Z = rng.normal(size=(N, nn))
X = Z / np.sqrt(G / nu)[:, None]
x1 = X[:, 0]
for R in [5, 20, 100]:
    f = np.minimum(np.maximum(x1, 0.0) ** beta, R ** beta)
    fp = np.where(x1 < R, beta * np.maximum(x1, 0.0) ** (beta - 1), 0.0)
    print(f"  R={R:4d} empVar={f.var():10.2f} empDen={np.mean(fp*fp):.4f} empRatio={f.var()/np.mean(fp*fp):9.1f}")
print("Hessian radial eigenvalue (n=5,nu=3), negative for r^2>nu => non-log-concave:")
n = 5
a = (n + nu) / 2
for r2 in [0.5, 2.9, 3.0, 3.1, 20.0]:
    s = r2 / nu
    ev = (2 * a / nu) * (1 - s) / (1 + s) ** 2
    print(f"  r2={r2:5.1f} radial_ev={ev:+.4f}")
