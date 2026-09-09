"""Step 4: Construction-A neighbor theta-series trace (exact integer arithmetic).
Even unimodular neighbor lattice route: for putative Type II [72,36,16] C,
L = A2(C) scaled Construction-A lattice is extremal even unimodular in dim 72
with minimal norm 8 (since d=16 -> norm d/2=8). Its theta series:
  Theta_L = E4^9 + a1 E4^6 D + a2 E4^3 D^2 + a3 D^3  (Siegel–Eisenstein basis),
  D = (E4^3 - E6^2)/1728 = Delta-like cusp weight 12,
solved from: constant term 1, vanishing of q^1..q^3 coeffs (min norm 8 means
no vectors of norm 2,4,6), i.e. coefficients of q^1,q^2,q^3 = 0.
E4 = 1+240q+2160q^2+6720q^3+17520q^4+...
E6 = 1-504q-16632q^2-122976q^3-...
Work in exact integers to O(q^8); solve 3x3 for (a1,a2,a3); report kissing
number (q^4 coeff) and next coeffs. Compare with the known extremal-theta
value: for extremal 72-dim lattice the kissing number is 6218175600
(Sloane's extremal theta series). Record match/mismatch honestly as the
'neighbor theta trace'. This does NOT by itself exclude anything; it localizes
the residual window: any putative neighbor lattice must reproduce this series.
Writes theta_trace.json.
"""
from fractions import Fraction
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
N = 9  # series to q^8

# Eisenstein series coeffs: E4 = 1 + 240 sum sigma3(n) q^n ; E6 = 1 - 504 sum sigma5(n) q^n
def sigma(k, n):
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)

E4 = [Fraction(1)] + [Fraction(240 * sigma(3, n)) for n in range(1, N)]
E6 = [Fraction(1)] + [Fraction(-504 * sigma(5, n)) for n in range(1, N)]


def mul(a, b):
    c = [Fraction(0)] * N
    for i in range(N):
        for j in range(N - i):
            c[i + j] += a[i] * b[j]
    return c


def pw(a, k):
    r = [Fraction(1)] + [Fraction(0)] * (N - 1)
    for _ in range(k):
        r = mul(r, a)
    return r


E43 = pw(E4, 3)
E62 = mul(E6, E6)
D = [(E43[n] - E62[n]) / 1728 for n in range(N)]
print("D = q + ... :", [float(x) for x in D[:6]])
assert D[0] == 0 and D[1] == 1  # D = q - 24q^2 + ...

B0 = pw(E4, 9)
B1 = mul(pw(E4, 6), D)
B2 = mul(pw(E4, 3), mul(D, D))
B3 = mul(mul(D, D), D)
for name, B in [("E4^9", B0), ("E4^6D", B1), ("E4^3D^2", B2), ("D^3", B3)]:
    print(name, [int(x) if x.denominator == 1 else x for x in B[:6]])

# Solve B0 + a1B1 + a2B2 + a3B3 has q^1=q^2=q^3=0.
M = [[B1[j], B2[j], B3[j]] for j in [1, 2, 3]]
rhs = [-B0[j] for j in [1, 2, 3]]
# 3x3 exact solve
A_ = [M[i][:] + [rhs[i]] for i in range(3)]
for col in range(3):
    p = next(i for i in range(col, 3) if A_[i][col] != 0)
    A_[col], A_[p] = A_[p], A_[col]
    d = A_[col][col]
    A_[col] = [v / d for v in A_[col]]
    for i in range(3):
        if i != col and A_[i][col] != 0:
            q = A_[i][col]
            A_[i] = [A_[i][k] - q * A_[col][k] for k in range(4)]
a = [A_[i][3] for i in range(3)]
print("theta coeffs (a1,a2,a3) =", a)
T = [B0[n] + a[0] * B1[n] + a[1] * B2[n] + a[2] * B3[n] for n in range(N)]
print("extremal theta series coeffs q^0..q^8:")
for n in range(N):
    print(f"  q^{2*n}: {T[n]} (int: {T[n].denominator == 1})")
assert all(x.denominator == 1 for x in T)
Tint = [int(x) for x in T]
print("kissing number (norm-8 vectors) =", Tint[4])
print("known extremal-72 kissing number 6218175600; match:", Tint[4] == 6218175600)
json.dump({"a": [str(x) for x in a], "theta": Tint}, open(os.path.join(HERE, "theta_trace.json"), "w"), indent=1)
print("wrote theta_trace.json")
