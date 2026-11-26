"""Exact finite-field verification of quadratic-residue covering triples."""
from collections import Counter
from itertools import combinations, product

P = 5
F = [(a, b) for a, b in product(range(P), repeat=2)]
ZERO = (0, 0)
ONE = (1, 0)
U = (0, 1)

def add(v, w):
    return ((v[0] + w[0]) % P, (v[1] + w[1]) % P)

def neg(v):
    return (-v[0] % P, -v[1] % P)

def sub(v, w):
    return add(v, neg(w))

def mul(v, w):
    return ((v[0] * w[0] + 2 * v[1] * w[1]) % P,
            (v[0] * w[1] + v[1] * w[0]) % P)

def norm(v):
    return (v[0] * v[0] - 2 * v[1] * v[1]) % P

def in_square_with_zero(v):
    return v == ZERO or norm(v) in (1, 4)

# Independent square set, not using the norm criterion.
Q0 = {mul(x, x) for x in F}
assert len(Q0) == 13
assert all(in_square_with_zero(v) == (v in Q0) for v in F)

def missing(centers, predicate=in_square_with_zero):
    return tuple(x for x in F if not any(predicate(sub(x, c)) for c in centers))

census = {}
solutions = {}
for second in (ONE, U):
    stats = Counter()
    solutions[second] = []
    for third in F:
        if third == ZERO or third == second:
            continue
        gap = len(missing((ZERO, second, third)))
        stats[gap] += 1
        if not gap:
            solutions[second].append(third)
    census[second] = dict(sorted(stats.items()))
assert census[ONE] == {2: 11, 3: 10, 4: 2}
assert census[U] == {0: 2, 2: 13, 3: 8}
assert solutions[ONE] == []
assert solutions[U] == [(1, 3), (4, 3)]
assert len(missing((ZERO, ONE))) == 6
assert len(missing((ZERO, U))) == 5

# A distinct implementation using an explicit square set for all 2300 triples.
covering = [t for t in combinations(F, 3)
            if not missing(t, lambda v: v in Q0)]
assert len(covering) == 100
assert all(not in_square_with_zero(sub(x, y))
           for t in covering for x, y in combinations(t, 2))
assert all(missing(t, lambda v: v in Q0)
           for t in combinations(F, 2))

T0 = frozenset((ZERO, U, (1, 3)))
Q = Q0 - {ZERO}
orbit = {
    frozenset(add(mul(s, x), t) for x in T0)
    for s in Q for t in F
}
assert orbit == set(map(frozenset, covering))
assert len(orbit) == 100
assert len(Q) * len(F) == 300
s = (2, 3)
f = lambda x: add(mul(s, x), U)
assert norm(s) == 1
assert frozenset(map(f, T0)) == T0
assert f(ZERO) == U and f(U) == (1, 3) and f((1, 3)) == ZERO

nonadjacent_pairs = sum(
    not in_square_with_zero(sub(x, y)) for x, y in combinations(F, 2))
assert nonadjacent_pairs == 150
assert len(covering) == nonadjacent_pairs * 2 // 3
print('VERIFY_OK field=25 total_triples=2300 covers=100 minimum_size=3')
print('pair_census_adjacent=', census[ONE], 'pair_census_nonadjacent=', census[U])
print('extensions_per_nonadjacent_pair=2 unique_affine_square_orbit=PASS')
print('all_covering_triples_independent=PASS stabilizer_order=3 norm_square_crosscheck=PASS')
