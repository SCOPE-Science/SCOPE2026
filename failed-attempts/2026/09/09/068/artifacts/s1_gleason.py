"""Step 1: recompute unique putative extremal Type-II [72,36,16] enumerator W72*
from the Gleason basis, in exact rational arithmetic.
f = W([8,4,4] Hamming) = x^8 + 14 x^4 y^4 + y^8
g = W([24,12,8] Golay)  = x^24 + 759 x^16 y^8 + 2576 x^12 y^12 + 759 x^8 y^16 + y^24
W72 = c0 f^9 + c1 f^6 g + c2 f^3 g^2 + c3 g^3, solved from A0=1, A4=A8=A12=0.
All polys tracked as dicts {weight w: coeff of x^{72-w} y^w}, exact Fractions.
Checks: integrality, nonnegativity, support in 4Z, symmetry A_w=A_{72-w},
MacWilliams self-duality invariance.
Writes w72.json.
"""
from fractions import Fraction
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def mul(a, b):
    c = {}
    for wa, ca in a.items():
        for wb, cb in b.items():
            w = wa + wb
            c[w] = c.get(w, Fraction(0)) + ca * cb
    return c


def pw(a, k):
    r = {0: Fraction(1)}
    for _ in range(k):
        r = mul(r, a)
    return r


f = {0: Fraction(1), 4: Fraction(14), 8: Fraction(1)}
g = {0: Fraction(1), 8: Fraction(759), 12: Fraction(2576),
     16: Fraction(759), 24: Fraction(1)}

basis = []
for i in range(4):
    k = 9 - 3 * i
    basis.append(mul(pw(f, k), pw(g, i)))

# Solve sum_j c_j B_j[w] = delta for w in [0,4,8,12]
rows = [0, 4, 8, 12]
n = 4
M = [[Fraction(basis[j].get(w, 0)) for j in range(n)] for w in rows]
rhs = [Fraction(1) if w == 0 else Fraction(0) for w in rows]
A = [M[i][:] + [rhs[i]] for i in range(n)]
for col in range(n):
    piv = next(r for r in range(col, n) if A[r][col] != 0)
    A[col], A[piv] = A[piv], A[col]
    d = A[col][col]
    A[col] = [v / d for v in A[col]]
    for r in range(n):
        if r != col and A[r][col] != 0:
            q = A[r][col]
            A[r] = [A[r][c] - q * A[col][c] for c in range(n + 1)]
sol = [A[i][n] for i in range(n)]
print("Gleason coeffs c0..c3 =", sol)

W = {}
for j in range(n):
    for w, c in basis[j].items():
        W[w] = W.get(w, Fraction(0)) + sol[j] * c

full = {w: W.get(w, Fraction(0)) for w in range(73)}
for w in range(73):
    assert full[w].denominator == 1, (w, full[w])
Aint = {w: int(full[w]) for w in range(73)}
print("W72* nonzero coefficients:")
for w in range(73):
    if Aint[w]:
        print(f"  A[{w}] = {Aint[w]}")

# --- checks ---
assert Aint[0] == 1 and Aint[4] == 0 and Aint[8] == 0 and Aint[12] == 0
assert all(Aint[w] >= 0 for w in range(73))
assert all(Aint[w] == 0 for w in range(73) if w % 4 != 0)
assert Aint[72] == 1, "all-ones word must be present (Type II, 8|72)"
sym = all(Aint[w] == Aint[72 - w] for w in range(73))
print("symmetry A_w=A_{72-w}:", sym)
assert sym

# MacWilliams self-duality: W == (1/2^36) * Krawtchouk transform of W
# B_j = 2^-36 sum_w A_w K_j(w), K_j(w) = sum_{t=0..72} (-1)^t C(w,t) C(72-w, j-t)
from math import comb

K = {}
for j in range(73):
    s = Fraction(0)
    for w in range(73):
        if Aint[w]:
            k = sum((Fraction(-1) ** t) * comb(w, t) * comb(72 - w, j - t)
                    for t in range(73) if 0 <= t <= w and 0 <= j - t <= 72 - w)
            s += Aint[w] * k
    K[j] = s / Fraction(2 ** 36)
mw_ok = all(K[j] == Aint[j] for j in range(73))
print("MacWilliams self-duality invariant:", mw_ok)
assert mw_ok

with open(os.path.join(HERE, "w72.json"), "w") as fh:
    json.dump({"A": [Aint[w] for w in range(73)],
               "gleason_coeffs": [str(c) for c in sol]}, fh, indent=1)
print("wrote w72.json")
print("A16 =", Aint[16], " A20 =", Aint[20], " total =", sum(Aint.values()))
assert sum(Aint.values()) == 2 ** 36
print("STEP1 PASS")
