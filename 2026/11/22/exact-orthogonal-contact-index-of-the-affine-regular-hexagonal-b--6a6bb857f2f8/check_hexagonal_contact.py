"""Supplementary finite checks for the exact hexagonal orthogonal-contact index.

The mathematical proof is in RESULT.md; finite sampling is not exhaustive.
This checker uses only the Python standard library.
"""
import math
import random

TAU = 2.0 - math.sqrt(3.0)
STAR = (3.0 - math.sqrt(3.0)) / math.sqrt(2.0)

def norm_hex(x, y):
    return max(abs(x), abs(y), abs(x + y))

def score(u, v):
    x, y = u
    a, b = v
    determinant = abs(x * b - y * a)
    largest = max(math.hypot(x, a), math.hypot(y, b), math.hypot(x + y, a + b))
    return determinant / largest

def turn(x, y):
    return -y, x + y

def reflect(x, y):
    return x, -x - y

def edge(kind, t):
    if kind == 0:
        return (1.0, -t)
    if kind == 1:
        return (t, 1.0 - t)
    if kind == 2:
        return (-t, 1.0)
    raise ValueError(kind)

assert math.isclose(TAU * TAU - 4.0 * TAU + 1.0, 0.0, abs_tol=1e-14)
assert math.isclose(1.0 + TAU**2, 2.0 * (1.0 - TAU)**2, abs_tol=1e-14)
assert math.isclose(STAR**2, 6.0 - 3.0 * math.sqrt(3.0), abs_tol=1e-14)
assert math.isclose(score(edge(0, TAU), edge(2, TAU)), STAR, abs_tol=1e-14)
assert STAR > 2.0 / math.sqrt(5.0)

count = 5
rng = random.Random(20260927)
for _ in range(24000):
    a, b = rng.uniform(-3.0, 3.0), rng.uniform(-3.0, 3.0)
    n = norm_hex(a, b)
    assert math.isclose(norm_hex(*turn(a, b)), n, rel_tol=1e-12, abs_tol=1e-12)
    assert math.isclose(norm_hex(*reflect(a, b)), n, rel_tol=1e-12, abs_tol=1e-12)
    count += 2
    s, t = rng.random(), rng.random()
    u = edge(0, s)
    v = edge(rng.randrange(3), t)
    observed = score(u, v)
    assert observed <= STAR + 1e-12
    count += 1
    if v == edge(1, t):
        w = reflect(*u)
        z = tuple(-c for c in reflect(*v))
        assert math.isclose(score(u, v), score(w, z), abs_tol=1e-12)
        count += 1

# Deterministic facet-grid check, supplementary rather than exhaustive.
for j in range(101):
    for k in range(101):
        s = j / 100.0
        t = k / 100.0
        q = (1.0 - s * t) / max(
            math.hypot(1.0, s),
            math.hypot(1.0, t),
            math.hypot(1.0 - s, 1.0 - t),
        )
        assert q <= STAR + 1e-12
        count += 1

print('HEXAGONAL_ORTHOGONAL_CONTACT_DIAGNOSTIC_OK', count)
