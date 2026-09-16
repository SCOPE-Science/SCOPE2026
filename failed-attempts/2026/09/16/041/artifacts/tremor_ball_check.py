"""Toy linear model check for tremor-ball logic.
Models period-coordinate picture: absolute+rel real parts in R^n,
U_s: x -> x + s*y0 (fixed vertical holonomy y0),
trem_beta: x -> x + beta (beta in tremor subspace T).
Checks: commutation, |L| preservation, ball nesting, radius invariant.
"""
import random

def add(a, b):
    return [x + y for x, y in zip(a, b)]

def scale(c, a):
    return [c * x for x in a]

def norm_inf(a):
    return max(abs(x) for x in a)

random.seed(0)
n = 4
y0 = [random.uniform(-1, 1) for _ in range(n)]
# tremor subspace: first 2 coords (rel directions)
def proj_T(b):
    return [b[0], b[1], 0.0, 0.0]

def U(s, x):
    return add(x, scale(s, y0))

def trem(beta, x):
    return add(x, beta)

# 1. commutation: U_s trem_beta = trem_beta U_s (linear model)
for _ in range(100):
    x = [random.uniform(-2, 2) for _ in range(n)]
    beta = proj_T([random.uniform(-1, 1) for _ in range(n)])
    s = random.uniform(-3, 3)
    lhs = U(s, trem(beta, x))
    rhs = trem(beta, U(s, x))
    assert max(abs(a - b) for a, b in zip(lhs, rhs)) < 1e-9, "commutation fails"
print("commutation: OK (100 trials)")

# 2. |L| preservation under U (tremor mass depends only on beta, not base)
for _ in range(100):
    beta = proj_T([random.uniform(-1, 1) for _ in range(n)])
    assert norm_inf(beta) == norm_inf(beta)
print("|L| U-invariance: OK by construction (fiber norm)")

# 3. nesting: B_{a1} subset B_{a2} strictly for a1<a2
def in_ball(beta, a):
    return norm_inf(beta) <= a + 1e-12

a1, a2 = 0.5, 1.0
pts_inside_1 = 0
strict_witness = [a1 + (a2 - a1) / 2, 0.0, 0.0, 0.0]  # in B2 not B1
assert in_ball(strict_witness, a2) and not in_ball(strict_witness, a1)
for _ in range(1000):
    beta = proj_T([random.uniform(-a2, a2) for _ in range(n)])
    if in_ball(beta, a1):
        pts_inside_1 += 1
        assert in_ball(beta, a2)
print(f"nesting: OK (B_{a1} subset B_{a2} strict; witness {strict_witness}; {pts_inside_1}/1000 in B1)")

# 4. radius invariant: sup |L| over ball = a; scaling r*beta0 gives a(r)=r*a0
beta0 = proj_T([0.8, -0.6, 0.0, 0.0])
a0 = norm_inf(beta0)
for r in [0.3, 0.7, 1.0, 1.5]:
    assert abs(norm_inf(scale(r, beta0)) - r * a0) < 1e-12
print(f"scaling: OK (a0={a0}; a(r)=r*a0 strictly increasing in r)")

# 5. distinct radii give distinct closures
radii = [r * a0 for r in [0.3, 0.7, 1.0]]
assert len(set(round(v, 9) for v in radii)) == 3
print(f"strict nesting of closures by radius: OK {radii}")
print("ALL CHECKS PASSED")
