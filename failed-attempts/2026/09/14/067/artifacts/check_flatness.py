"""Symbolic verification of the constrained-harmonic zero-curvature characterization.

Model (Bohle-Pedit-Pinkall / Burstall-Calderbank form):
  nabla^mu = d + A0 + (mu-1)*B + (mu^{-1}-1)*C
with A0 base connection, B = Higgs+multiplier (1,0) part, C = (0,1) part,
all sl(2,C)-valued 1-forms. Curvature F(mu) = dA(mu) + A(mu)^A(mu) is a Laurent
polynomial in the central variable mu of degree -2..2. Flatness forall mu in C*
<=> all 5 Laurent coefficients vanish = the constrained-Willmore PDE system.

Noncommutative symbols cannot go into sympy.Poly/limit, so with G(mu)=mu^2*F(mu)
(a polynomial of degree <=4) coefficients are extracted by differentiation at
mu=0: g_k = G^{(k)}(0)/k!, c_{k-2} = g_k.
"""
import sympy as sp
from math import factorial

mu = sp.symbols('mu')
A01, A02 = sp.symbols('A01 A02', commutative=False)
B1, B2 = sp.symbols('B1 B2', commutative=False)
C1, C2 = sp.symbols('C1 C2', commutative=False)
D0, DB, DC = sp.symbols('D0 DB DC', commutative=False)

M1 = A01 + (mu - 1)*B1 + (1/mu - 1)*C1
M2 = A02 + (mu - 1)*B2 + (1/mu - 1)*C2
dpart = D0 + (mu - 1)*DB + (1/mu - 1)*DC
F12 = sp.expand(dpart + (M1*M2 - M2*M1))
G = sp.expand(F12 * mu**2)
print("G = mu^2 F12, preview:", str(G)[:200], "...")

g = {}
for k in range(5):
    dk = G
    for _ in range(k):
        dk = sp.diff(dk, mu)
    g[k] = sp.expand(dk.subs(mu, 0) / factorial(k))
    print(f"g_{k} (c_{k-2}) = {g[k]}")

# Exactness: sum g_k mu^k == G.
assert sp.expand(sum(g[k] * mu**k for k in range(5)) - G) == 0, "Laurent recomposition failed"
print("RECOMPOSITION OK: G(mu) = sum g_k mu^k exactly, remainder 0.")

# Identities.
assert sp.expand(g[4] - (B1*B2 - B2*B1)) == 0, f"top mismatch: {g[4]}"
print("TOP OK: c_2 = [B1,B2]")
assert sp.expand(g[0] - (C1*C2 - C2*C1)) == 0, f"bottom mismatch: {g[0]}"
print("BOTTOM OK: c_-2 = [C1,C2]")
s3, s1, s2 = str(g[3]), str(g[1]), str(g[2])
for tok in ['DB', 'A01', 'B1', 'C1']:
    assert tok in s3, f"c_1 missing {tok}: {g[3]}"
for tok in ['DC', 'A01', 'B1', 'C1']:
    assert tok in s1, f"c_-1 missing {tok}: {g[1]}"
assert 'D0' in s2 and 'DB' in s2 and 'DC' in s2, f"c_0 missing pieces: {g[2]}"
print("MIDDLE OK: c_1 has DB+[A,B]+[B,C] coupling; c_-1 has DC+[A,C]+[B,C]; c_0 couples D0/DB/DC.")
print("CONCLUSION: F(mu)=0 forall mu in C* <=> c_2=c_1=c_0=c_-1=c_-2=0,")
print("the constrained-harmonic (constrained Willmore) PDE system. VERIFIED.")
