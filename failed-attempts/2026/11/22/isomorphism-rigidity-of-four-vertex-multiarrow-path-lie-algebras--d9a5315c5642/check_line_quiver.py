"""Exact, dependency-free checks for four-vertex line-quiver path Lie algebras.

Usage: python check_line_quiver.py
The all-parameter theorem has a separate written proof; finite checks are supplementary.
"""
from itertools import product


def paths(r, s, t):
    layers = [range(r), range(s), range(t)]
    return [(a, tuple(p)) for a in range(3) for b in range(a+1, 4)
            for p in product(*layers[a:b])]


def bracket(x, y):
    a, p = x
    b, q = y
    if a+len(p) == b:
        return (a, p+q), 1
    if b+len(q) == a:
        return (b, q+p), -1
    return None, 0


def rank_mod(rows, ncols, prime):
    pivots = {}
    for raw in rows:
        row = [v % prime for v in raw]
        for j in sorted(pivots):
            if row[j]:
                factor = row[j]
                row = [(v-factor*w) % prime for v, w in zip(row, pivots[j])]
        if not any(row):
            continue
        j = next(k for k, v in enumerate(row) if v)
        inv = pow(row[j], -1, prime)
        pivots[j] = [(v*inv) % prime for v in row]
    return len(pivots)


def invariants(r, s, t, prime):
    basis = paths(r,s,t)
    positions = {x: i for i,x in enumerate(basis)}
    n = len(basis)
    # First and second lower-central terms have path-length >=2, >=3.
    second = [x for x in basis if len(x[1]) >= 2]
    third = [x for x in basis if len(x[1]) == 3]
    # Obtain derived spaces from actual bracket evaluations.
    commutators = []
    for x in basis:
        for y in basis:
            z, c = bracket(x,y)
            if c:
                row = [0]*n
                row[positions[z]] = c
                commutators.append(row)
    d2 = rank_mod(commutators, n, prime)
    triple = []
    for x in basis:
        for y in second:
            z,c = bracket(x,y)
            if c:
                row = [0]*n
                row[positions[z]] = c
                triple.append(row)
    d3 = rank_mod(triple, n, prime)
    # The linear map x -> ([x,y])_{y in [L,L]}.
    rows = []
    for y in second:
        for z in third:
            row = [0]*n
            for i,x in enumerate(basis):
                w,c = bracket(x,y)
                if w == z:
                    row[i] = c
            rows.append(row)
    centralizer_codim = rank_mod(rows, n, prime)
    return (n-d2, d2-d3, d3, n-centralizer_codim-d2)


def main():
    checked = 0
    for prime in (2,3,5):
        for r,s,t in product(range(1,4),repeat=3):
            found = invariants(r,s,t,prime)
            expected = (r+s+t, s*(r+t), r*s*t, s)
            assert found == expected, (r,s,t,prime,found,expected)
            assert found == invariants(t,s,r,prime)
            checked += 1
    # Equal lower-central quotients but different intrinsic centralizer.
    a=(2,6,6)
    b=(3,8,3)
    def formula(x):
        r,s,t=x
        return r+s+t, s*(r+t), r*s*t, s
    assert formula(a)[:3] == formula(b)[:3] == (14,48,72)
    assert formula(a)[3] == 6 and formula(b)[3] == 8
    print('FOUR_VERTEX_QUIVER_LIE_CLASSIFICATION_OK', checked, 'finite tests')


if __name__ == '__main__':
    main()
