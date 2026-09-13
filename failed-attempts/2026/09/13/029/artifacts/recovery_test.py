"""Bounded recovery test: naive structure-constant computation for BW GV-fail pair.
Goal: see whether dim HH^2 can be read off classically in-lane.
Result: BLOCKED (documents concrete obstructions).
"""
import itertools
import numpy as np

# --- Laufer algebra L = C<x,y>/(xy+yx, y^2-x^3), char 0 ---
# Normal words: x^i (0<=i<=5) and x^i y (0<=i<=2); total 9.
def mul_L(a, b):
    (i1, j1), (i2, j2) = a, b
    sign = -1 if (j1 == 1 and i2 % 2 == 1) else 1
    i, j = i1 + i2, j1 + j2
    if j == 2:
        i, j = i + 3, 0  # y^2 -> x^3
    if j == 0 and i >= 6:
        return None  # x^6 = 0
    if j == 1 and i >= 3:
        return None  # x^3 y = 0
    return (sign, (i, j))

basis = [(i, 0) for i in range(6)] + [(i, 1) for i in range(3)]
idx = {m: k for k, m in enumerate(basis)}
assert len(basis) == 9
# associativity spot-check on basis triples
nchk = 0
for a, b, c in itertools.product(basis, repeat=3):
    t1 = mul_L(a, b)
    # (ab)c
    left = {}
    if t1 is not None:
        s, m = t1
        t = mul_L(m, c)
        if t is not None:
            left[t[1]] = s * t[0]
    t2 = mul_L(b, c)
    right = {}
    if t2 is not None:
        s, m = t2
        t = mul_L(a, m)
        if t is not None:
            right[t[1]] = s * t[0]
    assert left == right, (a, b, c, left, right)
    nchk += 1
print(f"Laufer basis ok, dim=9, assoc triples checked={nchk}")

# relations hold?
# xy + yx
xy = mul_L((1, 0), (0, 1))
yx = mul_L((0, 1), (1, 0))
print("xy =", xy, " yx =", yx, " -> sum zero:", xy[1] == yx[1] and xy[0] == -yx[0])
yy = mul_L((0, 1), (0, 1))
print("y^2 =", yy, " (expect x^3 with +1)")

# center dimension (HH^0) by linear algebra
def struct_mats():
    n = 9
    Lm = [np.zeros((n, n), dtype=int) for _ in range(n)]
    Rm = [np.zeros((n, n), dtype=int) for _ in range(n)]
    for k, a in enumerate(basis):
        for j, b in enumerate(basis):
            t = mul_L(a, b)
            if t is not None:
                Lm[k][idx[t[1]], j] = t[0]
            t = mul_L(b, a)
            if t is not None:
                Rm[k][idx[t[1]], j] = t[0]
    return Lm, Rm

Lm, Rm = struct_mats()
M = np.vstack([Lm[k] - Rm[k] for k in range(9)])
u, s, vh = np.linalg.svd(M.astype(float))
rank = int((s > 1e-8).sum())
print(f"center: 9 - rank({rank}) = {9 - rank} => dim HH^0(Laufer) = {9 - rank}")

# Bar-complex size obstruction for HH^2 of the object/kernel
print("bar C^2 dim Hom(A^2,A) =", 9**2 * 9, "; C^3 dim =", 9**3 * 9,
      "-> naive cocycle linear system ~59k eqs; needs full bimodule resolution, not in lane.")
print("periodic tail: Booth H^*(A^der)=A_con[eta], |eta|=-2 => infinite-dim total cohomology; "
      "no finite pair of integers to compare without properness/support prescription.")

# --- Second (new BW) algebra: rewriting fails to close by hand ---
print("Gamma=<a,b>/(ab+ba, a^2-b^3-aba): eliminating aba via ab=-ba gives a^2(1+b)=b^3, "
      "i.e. a^2=b^3-b^4+b^5 (if b^6=0); monomial count b^i,a b^i gives 12, not 9; "
      "extra 3 relations (consequences of a^3=0/b^6=0) have no confluent order by hand; "
      "no Singular/Macaulay2/QPA engine in lane -> structure constants unavailable.")
print("CONCLUSION: explicit HH^2 dimensions uncomputable in-lane; target blocked.")
