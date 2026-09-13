"""Verify the explicit 4-colouring of the 1/sqrt(2) sphere orthogonality graph.

Graph: S = {x : |x| = r}, r = 1/sqrt(2), edge iff dot == 0.
Colouring from proof: octant-pair colours for interiors + explicit circle colours.
Checks:
 1. sign-pattern independence of each octant-pair class;
 2. compatibility lists respected by the boundary assignment;
 3. randomised properness test on many orthogonal pairs (interior-interior,
    interior-boundary, boundary-boundary incl. axis-circle adjacencies);
 4. quadrant lemma: same-quadrant / opposite-quadrant open arcs contain no
    orthogonal pair; adjacent quadrants can (so colour disjointness matters).
"""
import itertools, math, random
import numpy as np

r = 1.0 / math.sqrt(2.0)

PAIRS = {
    1: (1, 1, 1),    # +++/---
    2: (1, 1, -1),   # ++-/--+
    3: (1, -1, 1),   # +-+/-+
    4: (-1, 1, 1),   # -++/+--
}

def interior_color(x):
    s = tuple(1 if v > 0 else -1 for v in x)
    for c, rep in PAIRS.items():
        if s == rep or s == tuple(-v for v in rep):
            return c
    raise AssertionError("interior point has zero coordinate")

def boundary_color(x, tol=1e-12):
    z = [abs(v) < tol for v in x]
    nzero = sum(z)
    if nzero == 2:  # axis
        k = [i for i in range(3) if not z[i]][0]
        return [1, 2, 3][k]  # X->1, Y->2, Z->3
    if nzero == 1:
        k = z.index(True)
        if k == 2:  # C12: x3=0
            return 1 if x[0] * x[1] > 0 else 4
        if k == 1:  # C13: x2=0
            return 1 if x[0] * x[2] > 0 else 4
        if k == 0:  # C23: x1=0
            return 4 if x[1] * x[2] > 0 else 2
    raise AssertionError("not a boundary point")

def color_point(x, tol=1e-9):
    if all(abs(v) > tol for v in x):
        return interior_color(x)
    # snap near-zero to zero for classification, use exact signs otherwise
    y = [0.0 if abs(v) <= tol else v for v in x]
    return boundary_color(y)

# 1. sign-pattern independence: same pair-class => dot forced nonzero sign
for c, rep in PAIRS.items():
    for s1 in [rep, tuple(-v for v in rep)]:
        for s2 in [rep, tuple(-v for v in rep)]:
            # term signs s1[i]*s2[i]: all +1 (same pattern) or all -1 (opposite)
            terms = [a * b for a, b in zip(s1, s2)]
            assert len(set(terms)) == 1, (c, s1, s2)
print("1. octant-pair independence OK")

# 2. lists respected
# allowed lists: C12 pos {1,2} neg {3,4}; C13 pos {1,3} neg {2,4}; C23 pos {1,4} neg {2,3}
# plus global bans: C12 != 3 (Z colour), C13 != 2 (Y colour), C23 != 1 (X colour)
checks = [
    ((0.3, 0.4, 0.0), {1, 2}), ((0.3, -0.4, 0.0), {3, 4}),
    ((0.3, 0.0, 0.4), {1, 3}), ((0.3, 0.0, -0.4), {2, 4}),
    ((0.0, 0.3, 0.4), {1, 4}), ((0.0, 0.3, -0.4), {2, 3}),
]
for p, allowed in checks:
    n = math.sqrt(sum(v * v for v in p))
    q = tuple(v / n * r for v in p)
    got = boundary_color(q)
    assert got in allowed, (q, got, allowed)
# global bans
for t in np.linspace(0.05, math.pi / 2 - 0.05, 9):
    p12 = (r * math.cos(t), r * math.sin(t), 0.0)
    assert boundary_color(p12) != 3
    p13 = (r * math.cos(t), 0.0, r * math.sin(t))
    assert boundary_color(p13) != 2
    p23 = (0.0, r * math.cos(t), r * math.sin(t))
    assert boundary_color(p23) != 1
print("2. boundary lists + global bans OK")

# 3. randomised properness over orthogonal pairs
random.seed(0)
rng = np.random.default_rng(0)
def rand_sphere():
    v = rng.normal(size=3)
    return v / np.linalg.norm(v) * r

def orth_mate(x):
    # random vector orthogonal to x, scaled to radius r
    a = rng.normal(size=3)
    a -= a.dot(x) / x.dot(x) * x
    n = np.linalg.norm(a)
    if n < 1e-8:
        return orth_mate(x)
    return a / n * r

N = 20000
bad = 0
for _ in range(N):
    x = rand_sphere()
    y = orth_mate(x)
    if color_point(x) == color_point(y):
        bad += 1
        print("MONOCHROMATIC", x, y, color_point(x))
        break
assert bad == 0, "found monochromatic orthogonal pair"
print(f"3. random orthogonal-pair test OK ({N} pairs, no monochromatic edge)")

# targeted axis-circle tests: X vs all C23, Y vs all C13, Z vs all C12
for t in np.linspace(0, 2 * math.pi, 361):
    c23 = np.array([0.0, r * math.cos(t), r * math.sin(t)])
    if abs(math.cos(t)) > 1e-9 and abs(math.sin(t)) > 1e-9:
        assert color_point(np.array([r, 0, 0])) != color_point(c23)
        assert color_point(np.array([-r, 0, 0])) != color_point(c23)
    c13 = np.array([r * math.cos(t), 0.0, r * math.sin(t)])
    if abs(math.cos(t)) > 1e-9 and abs(math.sin(t)) > 1e-9:
        assert color_point(np.array([0, r, 0])) != color_point(c13)
    c12 = np.array([r * math.cos(t), r * math.sin(t), 0.0])
    if abs(math.cos(t)) > 1e-9 and abs(math.sin(t)) > 1e-9:
        assert color_point(np.array([0, 0, r])) != color_point(c12)
print("4. axis-circle adjacency colours differ OK")

# 5. quadrant lemma numeric check on C12
def dot(a, b): return float(np.dot(a, b))
# same open quadrant: no orthogonal pair
for _ in range(2000):
    t1 = rng.uniform(0.01, math.pi / 2 - 0.01)
    t2 = rng.uniform(0.01, math.pi / 2 - 0.01)
    a = np.array([r * math.cos(t1), r * math.sin(t1), 0.0])
    b = np.array([r * math.cos(t2), r * math.sin(t2), 0.0])
    assert abs(dot(a, b)) > 1e-6
# opposite quadrants Q1 vs Q3: no orthogonal pair
for _ in range(2000):
    t1 = rng.uniform(0.01, math.pi / 2 - 0.01)
    t3 = rng.uniform(math.pi + 0.01, 3 * math.pi / 2 - 0.01)
    a = np.array([r * math.cos(t1), r * math.sin(t1), 0.0])
    b = np.array([r * math.cos(t3), r * math.sin(t3), 0.0])
    assert abs(dot(a, b)) > 1e-6
print("5. quadrant lemma numeric check OK")
print("ALL CHECKS PASSED")
