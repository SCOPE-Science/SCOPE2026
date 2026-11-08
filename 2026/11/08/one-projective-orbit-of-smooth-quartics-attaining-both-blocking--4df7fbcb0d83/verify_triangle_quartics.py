#!/usr/bin/env python3
"""Exact projective-triangle quartic census over F_5 (Python 3 + SymPy)."""
from itertools import product, permutations
import sympy as sp

P = 5
monomials = [(i, j, 4 - i - j) for i in range(5) for j in range(5 - i)]
mon_index = {m: i for i, m in enumerate(monomials)}

def normalize_point(v):
    a = next(w for w in v if w % P)
    t = pow(a, -1, P)
    return tuple(t * w % P for w in v)

points = sorted({normalize_point((x, y, 1)) for x in range(5) for y in range(5)} |
                {normalize_point((x, 1, 0)) for x in range(5)} | {(1, 0, 0)})
assert len(points) == 31
triangle = {normalize_point(v) for s in (0, 1, 4)
            for v in ((0, 1, -s), (1, -s, 0), (-s, 0, 1))}
assert len(triangle) == 9 and triangle.issubset(points)

lines = [{p for p in points if sum(a*b for a, b in zip(line, p)) % P == 0}
         for line in points]
assert len({frozenset(l) for l in lines}) == 31
assert all(len(line) == 6 for line in lines)
assert all(1 <= len(triangle & line) <= 4 for line in lines)
assert sorted([len(triangle & line) for line in lines]).count(4) == 3

def eval_mon(m, v):
    return (pow(v[0], m[0], P)*pow(v[1], m[1], P)*pow(v[2], m[2], P)) % P

def kernel(matrix):
    a = [list(row) for row in matrix]
    m, n = len(a), len(a[0])
    pivots, r = [], 0
    for col in range(n):
        pivot = next((i for i in range(r, m) if a[i][col] % P), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        t = pow(a[r][col] % P, -1, P)
        a[r] = [t * c % P for c in a[r]]
        for i in range(m):
            if i != r and a[i][col]:
                t = a[i][col]
                a[i] = [(a[i][j] - t*a[r][j]) % P for j in range(n)]
        pivots.append(col)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for col in free:
        b = [0]*n
        b[col] = 1
        for r, pivot in enumerate(pivots):
            b[pivot] = -a[r][col] % P
        basis.append(tuple(b))
    return basis

rows = {p: tuple(eval_mon(m, p) for m in monomials) for p in points}
basis = kernel([rows[p] for p in sorted(triangle)])
assert len(basis) == 6

def primitive(v):
    a = next(c for c in v if c)
    t = pow(a, -1, P)
    return tuple(c*t % P for c in v)

# One representative for every one-dimensional subspace in the six-dimensional kernel.
parameters = (w for w in product(range(P), repeat=6)
              if any(w) and next(x for x in w if x) == 1)
all_quartics = 0
counts = {}
exact = set()
for w in parameters:
    coeff = tuple(sum(w[j]*basis[j][i] for j in range(6)) % P for i in range(15))
    zeros = {p for p, ev in rows.items() if sum(c*v for c, v in zip(coeff, ev)) % P == 0}
    assert triangle.issubset(zeros)
    all_quartics += 1
    counts[len(zeros)] = counts.get(len(zeros), 0) + 1
    if zeros == triangle:
        exact.add(primitive(coeff))
assert all_quartics == 3906
assert len(exact) == 24
assert counts == {9:24, 10:240, 11:564, 12:560, 13:750, 14:564,
                  15:665, 16:228, 17:180, 18:40, 19:82, 21:9}

def transform(c, permutation, diagonal):
    out = [0]*15
    for coeff, e in zip(c, monomials):
        e2 = [0,0,0]
        scalar = coeff
        for i in range(3):
            e2[permutation[i]] = e[i]
            scalar = scalar*pow(diagonal[i], e[i], P) % P
        out[mon_index[tuple(e2)]] = scalar
    return primitive(out)

group = [(p, (1, a, b)) for p in permutations(range(3)) for a,b in product((1,4),repeat=2)]
assert len(group) == 24
for perm, diag in group:
    image = {normalize_point(tuple(diag[i]*pt[perm[i]] for i in range(3)))
             for pt in triangle}
    assert image == triangle
representative = min(exact)
orbit = {transform(representative, perm, diag) for perm, diag in group}
assert orbit == exact and len(orbit) == 24

# Geometric smoothness on the algebraic closure: affine Jacobian ideals are (1)
# in all three standard charts. Group transitivity makes one such test sufficient.
x, y, z = sp.symbols('x y z')
vars_ = (x, y, z)
F = sp.expand(sum(c*x**i*y**j*z**k for c, (i,j,k) in zip(representative,monomials)))
for i in range(3):
    remaining = tuple(vars_[j] for j in range(3) if j != i)
    f = sp.expand(F.subs(vars_[i], 1))
    g = sp.groebner([f, sp.diff(f,remaining[0]), sp.diff(f,remaining[1])],
                    *remaining, modulus=5, order='lex')
    assert len(g.polys) == 1 and g.polys[0].is_one, (i, list(g))

# The distinct smooth quartic constructed in the published general existence theorem
# has eleven rational points, so its example does not cover the nine-point stratum.
prior_example = sp.expand(x*y*(x*x+y*y)+(x*z+y*z)*(x*x+z*z))
prior_example_count = sum(int(prior_example.subs({x:p[0], y:p[1], z:p[2]})) % P == 0
                          for p in points)
assert prior_example_count == 11

print('TRIANGLE_QUARTIC_REPLAY_PASS', len(points), len(lines), len(triangle),
      len(basis), all_quartics, len(exact), len(orbit))
print('REPRESENTATIVE', F)
print('RATIONAL_POINT_HISTOGRAM', sorted(counts.items()))
print('PUBLISHED_EXAMPLE_RATIONAL_COUNT', prior_example_count)
