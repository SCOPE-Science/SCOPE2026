"""Verification script for N_{-3/2}(sl3) target data.
Checks: central charges; absolute-coset Zhu polynomials Delta(mu), w(mu);
dot-Weyl invariance of w, swap-oddness; Jacobian generic full rank (dominant map);
ordinary table; standard Z_n^2 DFT S-model unitarity, S^2=C, Verlinde group law
(finite mechanism underlying the continuous log-Verlinde used in DRAFT);
Weyl-orbit sizes (exact, via Fraction).
"""
import cmath
import math
from fractions import Fraction as F
import numpy as np

print("=== 1. Central charges ===")
k = F(-3, 2)
hv = 3
dim = 8
cL = k * dim / (k + hv)
cH = 2
cN = cL - cH
print(f"k={float(k)} cL={cL} cH={cH} cN={cN}")
assert cL == -8 and cN == -10
print("PASS: cL=-8, cH=2, cN=-10")

print("\n=== 2. Absolute-coset Zhu polynomials ===")
# (mu,mu) = (2s^2+2t^2+2st)/3, (mu,rho) = s+t  =>  Delta = (4s^2+4t^2+4st+6s+6t)/9
def Delta_fr(s, t):
    return (4 * s * s + 4 * t * t + 4 * s * t + 6 * s + 6 * t) / 9
# raw cubic C3(a,b) = (2a+b)(a-b)(a+2b), a=s+1, b=t+1; normalized w = C3/20
def C3_raw(s, t):
    a = s + 1
    b = t + 1
    return (2 * a + b) * (a - b) * (a + 2 * b)
def w_fr(s, t):
    return C3_raw(s, t) / 20

assert Delta_fr(F(0), F(0)) == 0 and w_fr(F(0), F(0)) == 0
assert Delta_fr(F(1), F(0)) == F(10, 9) and w_fr(F(1), F(0)) == 1
assert Delta_fr(F(0), F(1)) == F(10, 9) and w_fr(F(0), F(1)) == -1
print("PASS ordinary points: O0=(0,0), O1=(10/9,+1), O2=(10/9,-1)")

# dot-Weyl invariance of w; swap-oddness of w
def ds1(s, t):
    return (-s - 2, s + t + 1)
def ds2(s, t):
    return (s + t + 1, -t - 2)
for pt in [(F(1), F(0)), (F(7, 10), F(3, 10)), (F(2), F(1)), (F(1, 3), F(-1, 2))]:
    s0, t0 = pt
    w0 = w_fr(s0, t0)
    for f, nm in ((ds1, 'ds1'), (ds2, 'ds2')):
        q = f(s0, t0)
        assert w_fr(*q) == w0, (pt, nm)
    assert w_fr(t0, s0) == -w0, (pt, 'swap')
print("PASS: w dot-Weyl invariant, swap-odd; vacuum w=0")
d = Delta_fr(F(1), F(0)) - Delta_fr(*ds1(F(1), F(0)))
print(f"INFO: Delta is absolute-coset (not dot-invariant): shift example d={d}")

print("\n=== 3. Jacobian generic rank (dominance) ===")
import sympy as sp
s, t = sp.symbols('s t')
Dl = (4 * s**2 + 4 * t**2 + 4 * s * t + 6 * s + 6 * t) / 9
a, b = s + 1, t + 1
Wn = (2 * a + b) * (a - b) * (a + 2 * b) / 20
J = sp.Matrix([[sp.diff(Dl, s), sp.diff(Dl, t)],
               [sp.diff(Wn, s), sp.diff(Wn, t)]])
detJ = sp.factor(J.det())
print('detJ =', detJ)
for pt in [(0, 0), (1, 0), (0, 1), (sp.Rational(7, 10), sp.Rational(3, 10)),
           (sp.Rational(-1, 2), sp.Rational(1, 4))]:
    v = complex(J.det().subs({s: pt[0], t: pt[1]}).evalf())
    print(f"  {pt}: detJ={v.real:.4f}")
    assert abs(v) > 1e-9
print("PASS: Jacobian generically nonzero => mu -> (Delta,w) dominant, generically finite")

print("\n=== 4. S-kernel mechanism: Z_n^2 DFT unitarity, S^2=C ===")
n = 5
N = n * n
S = np.zeros((N, N), dtype=complex)
def idx(a1, a2):
    return (a1 % n) * n + (a2 % n)
for a1 in range(n):
    for a2 in range(n):
        for b1 in range(n):
            for b2 in range(n):
                S[idx(a1, a2), idx(b1, b2)] = \
                    cmath.exp(-2j * math.pi * (a1 * b1 + a2 * b2) / n) / n
err = np.max(np.abs(S @ S.conj().T - np.eye(N)))
C = np.zeros((N, N), dtype=complex)
for a1 in range(n):
    for a2 in range(n):
        C[idx(a1, a2), idx((-a1) % n, (-a2) % n)] = 1.0
err2 = np.max(np.abs(S @ S - C))
print(f"  max|SS^d - I|={err:.2e}  max|S^2-C|={err2:.2e}")
assert err < 1e-10 and err2 < 1e-10
print("PASS S unitary, S^2=C")

print("\n=== 5. Verlinde group law (finite model) ===")
S0x = S[idx(0, 0), :]
def V(a, b, c):
    return complex(np.sum(S[a, :] * S[b, :] * np.conj(S[c, :]) / S0x))
rng = np.random.default_rng(1)
for _ in range(8):
    a1, a2, b1, b2 = [int(x) for x in rng.integers(0, n, 4)]
    a = idx(a1, a2)
    b = idx(b1, b2)
    c = idx((a1 + b1) % n, (a2 + b2) % n)
    assert abs(V(a, b, c) - 1) < 1e-8
    assert abs(V(a, b, idx((a1 + b1 + 1) % n, (a2 + b2) % n))) < 1e-8
print("PASS: N=1 on group sum, 0 off-peak (8 trials); simple-current shift holds")

print("\n=== 6. Weyl-orbit sizes (exact) ===")
def s1(p):
    return (-p[0], p[0] + p[1])
def s2(p):
    return (p[0] + p[1], -p[1])
def orbit(p):
    seen = set()
    st = [p]
    while st:
        q = st.pop()
        if q in seen:
            continue
        seen.add(q)
        for f in (s1, s2):
            r = f(q)
            if r not in seen:
                st.append(r)
    return seen
o1 = orbit((F(1), F(0)))
o2 = orbit((F(7), F(3)))
print(f"  minuscule orbit size {len(o1)} (expect 3); generic orbit size {len(o2)} (expect 6)")
assert len(o1) == 3 and len(o2) == 6
print("PASS orbit sizes")

print("\nALL CHECKS PASSED")
