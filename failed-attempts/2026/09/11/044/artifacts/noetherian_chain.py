"""Artifact 1: Noetherian chain for (j, Dj, D2j) + sup bounds on F_trunc.
Verifies with sympy that the Ramanujan system in (E2,E4,E6,u=1/Delta)
has total degree <= 2 in each equation, and computes exact polynomial
expressions/degrees of j, Dj, D2j. Then derives rigorous uniform sup bounds
on F_trunc via majorant q-series (no grid needed).
D = (1/2pi i) d/dz; j' = d/dz j = 2pi i * Dj (fixed nonzero factor).
"""
import sympy as sp
from fractions import Fraction

E2, E4, E6, u = sp.symbols('E2 E4 E6 u')
DE2 = (E2**2 - E4) / 12
DE4 = (E2*E4 - E6) / 3
DE6 = (E2*E6 - E4**2) / 2
DU = -E2*u
for name, f in [("DE2", DE2), ("DE4", DE4), ("DE6", DE6), ("DU", DU)]:
    d = sp.Poly(f, E2, E4, E6, u).total_degree()
    print(f"chain {name}: total degree {d}")
    assert d <= 2

def D(f):
    return sp.expand(sp.diff(f, E2)*DE2 + sp.diff(f, E4)*DE4
                     + sp.diff(f, E6)*DE6 + sp.diff(f, u)*DU)

j = E4**3 * u
Dj = D(j)
D2j = D(Dj)
for name, f in [("j", j), ("Dj", Dj), ("D2j", D2j)]:
    P = sp.Poly(f, E2, E4, E6, u)
    print(f"{name} = {sp.expand(f)} | total degree {P.total_degree()} | terms {len(P.terms())}")
assert sp.Poly(j, E2, E4, E6, u).total_degree() == 4
assert sp.Poly(Dj, E2, E4, E6, u).total_degree() == 4
assert sp.Poly(D2j, E2, E4, E6, u).total_degree() == 5
# Dj closed form check: Dj = -E4^2 E6 u
assert sp.expand(Dj + E4**2*E6*u) == 0
print("closed form Dj = -E4^2*E6*u OK")

# ---- rigorous sup bounds on F_trunc ----
# y in [sqrt(3)/2, 2]; r = max|q| = exp(-pi*sqrt(3)); q0 = min|q| = exp(-4pi)
import math
y0 = math.sqrt(3)/2
r = math.exp(-2*math.pi*y0)          # <= 0.00434
q_lo = math.exp(-2*math.pi*2)        # min |q| on F_trunc (y<=2)
z3 = 1.202056903159594              # zeta(3) upper envelope 1.20206
z5 = 1.03692775514337               # zeta(5)
z2 = 1.64493406685                  # zeta(2)=pi^2/6
S = lambda k: sum((n**k)*(r**n) for n in range(1, 400))  # tail < 1e-300, negligible
S1, S2, S3, S5 = S(1), S(2), S(3), S(5)
B_E2 = 1 + 24*z2*S2  # sigma_1(n) <= zeta(2) n^2 envelope
B_E4 = 1 + 240*z3*S3
B_E6 = 1 + 504*z5*S5
# |Delta| >= |q| * prod(1-|q|^n)^24 >= q_lo * exp(-24 * sum r^n/(1-r^n))
tail = sum((r**n)/(1 - r**n) for n in range(1, 400))
Dmin = q_lo * math.exp(-24*tail/(1))  # crude: exp(-24*tail)
B_u = 1/Dmin
B_j = B_E4**3 * B_u
B_Dj = B_E4**2 * B_E6 * B_u
B_D2j = (B_E2*B_E4**2*B_E6/6 + B_E4**4/2 + 2*B_E4*B_E6**2/3) * B_u
print(f"r={r:.6f} q_lo={q_lo:.4e}")
print(f"sup|E2|<={B_E2:.4f} sup|E4|<={B_E4:.4f} sup|E6|<={B_E6:.4f}")
print(f"min|Delta|>={Dmin:.4e} sup|u|<={B_u:.4e}")
print(f"sup|j|<={B_j:.4e} sup|Dj|<={B_Dj:.4e} sup|D2j|<={B_D2j:.4e}")
assert Dmin > 0 and B_u < 1e6
print("CHAIN_CERTIFICATE_OK")
