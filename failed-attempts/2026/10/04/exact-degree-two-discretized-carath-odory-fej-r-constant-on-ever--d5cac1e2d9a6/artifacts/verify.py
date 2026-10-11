#!/usr/bin/env python3
import math

TOL = 2e-9

def theorem_value(N):
    j = (3 * N) // 8
    u = math.cos(2 * math.pi * j / N)
    v = math.cos(2 * math.pi * (j + 1) / N)
    den = 1 + 2 * u * v
    a = -2 * (u + v) / den
    b = 1 / den
    return j, u, v, a, b

def constraints(N):
    # Symmetry lets us keep the distinct cosine samples on [0, pi].
    out = []
    for r in range(N // 2 + 1):
        x = math.cos(2 * math.pi * r / N)
        y = math.cos(4 * math.pi * r / N)
        out.append((x, y))
    return out

def feasible(N, a, b, tol=TOL):
    return all(1 + a*x + b*y >= -tol for x, y in constraints(N))

def independent_lp(N):
    cs = constraints(N)
    best = -1e100
    best_pair = None
    for i, (x1, y1) in enumerate(cs):
        for k in range(i + 1, len(cs)):
            x2, y2 = cs[k]
            det = x1*y2 - x2*y1
            if abs(det) < 1e-13:
                continue
            # Solve x_i*a + y_i*b = -1 for the two active rows.
            a = (-y2 + y1) / det
            b = (-x1 + x2) / det
            if a > best and feasible(N, a, b, 5e-9):
                best = a
                best_pair = (i, k)
    if best_pair is None:
        raise AssertionError(f"no feasible vertex found for N={N}")
    return best, best_pair

for N in range(5, 1001):
    j, u, v, a, b = theorem_value(N)
    if not (1 + 2*u*v > 0):
        raise AssertionError((N, 'denominator'))
    if not feasible(N, a, b, 2e-9):
        raise AssertionError((N, 'factorized extremizer not feasible'))
    # Check the factorization directly at every distinct sample.
    den = 1 + 2*u*v
    for x, y in constraints(N):
        lhs = 1 + a*x + b*y
        rhs = 2*(x-u)*(x-v)/den
        if abs(lhs-rhs) > 2e-9:
            raise AssertionError((N, 'factorization', lhs, rhs))
    eq = abs(a-math.sqrt(2)) < 2e-10
    if eq != (N % 8 == 0):
        raise AssertionError((N, 'sqrt2 criterion', a))

for N in range(5, 91):
    _, _, _, a, _ = theorem_value(N)
    lp, pair = independent_lp(N)
    if abs(lp-a) > 2e-8:
        raise AssertionError((N, 'LP mismatch', lp, a, pair))

print('formula_grid_checks=996 independent_lp_moduli=86')
print('VERIFY_OK')
