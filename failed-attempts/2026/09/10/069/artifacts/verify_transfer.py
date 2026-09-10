"""Verify the numerical fiber-product certificate for the TARGET transfer lemma.

Checks (all from displayed formulas alone):
 1. Residue fiber coefficient: 2 preparation cells x 2^2 sign patterns = 8.
 2. Value-group fiber coefficient: 3 concurrent lines -> 6 sectors (Euler).
 3. Combined coefficient: 8*6 = 48.
 4. Exponent bound: d_k + 2 <= 2*(d_k+1) for all d_k >= 0.
 5. Realizability: all 4 monomial sign patterns and all 6 sector sign
    patterns occur (so the bounds are tight witnesses, not vacuous).
 6. Brute-force region count of the Gamma arrangement by angle sweep.
"""
import itertools
import math

# ---- 1. Residue sign patterns ----
signs = list(itertools.product([-1, 1], repeat=2))
assert len(signs) == 4, len(signs)
n_prep_cells = 2
K_k = n_prep_cells * len(signs)
assert K_k == 8, K_k
print(f"residue: {n_prep_cells} prep cells x {len(signs)} sign patterns = {K_k}")

# ---- 2/6. Gamma arrangement: 3 concurrent lines in the plane ----
# Lines: L1=0, L2=0, L1-L2=0 with distinct slopes through one point.
# Sectors = 2*m for m=3 concurrent lines in general position = 6.
m = 3
sectors_euler = 2 * m  # V=1, E=2m rays, F=E=2m for concurrent pencil
assert sectors_euler == 6
print(f"gamma (Euler): 2*{m} = {sectors_euler} sectors")

# Realizable strict sign vectors of (L1, L2, L1-L2) excluding zeros:
# (s1,s2) in {+,-}^2, third sign = sign(s1*|..| - s2*|..|); enumerate with
# generic magnitudes to show all 6 realizable strict patterns exist.
realizable = set()
for s1, s2 in itertools.product([-1, 1], repeat=2):
    for a, b in [(2.0, 1.0), (1.0, 2.0), (1.0, 1.0)]:
        v1, v2 = s1 * a, s2 * b
        d = v1 - v2
        if abs(d) < 1e-12:
            continue  # non-strict, skip
        realizable.add((s1, s2, 1 if d > 0 else -1))
# The 8 combinatorial patterns minus the 2 diagonal ties (s1==s2,a==b) = 6.
assert len(realizable) == 6, realizable
print(f"gamma realizable strict sign triples: {len(realizable)} (expected 6)")

# Angle-sweep brute force: pencil of 3 lines with angles 0, pi/3, 2pi/3;
# count distinct sign vectors on a circle.
angles = [0.0, math.pi / 3, 2 * math.pi / 3]
seen = set()
N = 720
for i in range(N):
    t = 2 * math.pi * i / N
    px, py = math.cos(t), math.sin(t)
    vec = []
    for a in angles:
        nx, ny = -math.sin(a), math.cos(a)  # normal
        s = px * nx + py * ny
        if abs(s) < 1e-12:
            vec = None
            break
        vec.append(1 if s > 0 else -1)
    if vec is not None:
        seen.add(tuple(vec))
assert len(seen) == 6, len(seen)
print(f"gamma angle-sweep regions: {len(seen)} (expected 6)")

K_gamma = 6
t_gamma = 2

# ---- 3. Product ----
N_total = K_k * K_gamma
assert N_total == 48, N_total
print(f"total: {K_k}*{K_gamma} = {N_total}")

# ---- 4. Exponent inequality for all relevant d_k ----
for d_k in range(0, 11):
    assert d_k + t_gamma <= 2 * (d_k + 1), d_k
print("exponent: d_k+2 <= 2*(d_k+1) for d_k=0..10 OK")

print("VERIFY_OK: N=48, exponent<=2*(d_k+1)")
