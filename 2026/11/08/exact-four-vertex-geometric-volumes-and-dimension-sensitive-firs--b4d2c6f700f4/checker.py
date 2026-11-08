"""Reproduce exact four-point L-infinity connection integrals.

Python 3.9+ standard library only. No numerical integration or external data.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations

V = tuple(range(4))
EDGES = tuple(combinations(V, 2))
PERMS = tuple(permutations(V))


def edgeset(*pairs):
    return frozenset(tuple(sorted(e)) for e in pairs)


TYPES = {
    'claw': edgeset((0, 1), (0, 2), (0, 3)),
    'path': edgeset((0, 1), (1, 2), (2, 3)),
    'paw': edgeset((0, 1), (1, 2), (0, 2), (2, 3)),
    'cycle': edgeset((0, 1), (1, 2), (2, 3), (0, 3)),
    'diamond': edgeset((0, 1), (0, 2), (0, 3), (1, 2), (1, 3)),
    'clique': frozenset(EDGES),
}


def connected(edges):
    have = {0}
    while True:
        extend = have | {v for u, v in edges if u in have} | {u for u, v in edges if v in have}
        if have == extend:
            return len(have) == 4
        have = extend


def canon(edges):
    return min(tuple(sorted(tuple(sorted((p[u], p[v]))) for u, v in edges)) for p in PERMS)


def j1(edges):
    """Exact real-line volume of *mandatory* edge constraints.

    For each coordinate ordering, let three successive gaps be nonnegative.
    They have Jacobian one; connectedness constrains them to [0,1].
    """
    assert connected(edges)
    ans = Fraction(0)
    for order in PERMS:
        pos = {v: i for i, v in enumerate(order)}
        spans = {tuple(sorted((pos[u], pos[v]))) for u, v in edges}
        if (0, 3) in spans:
            ans += Fraction(1, 6)
        elif (0, 2) in spans and (1, 3) in spans:
            ans += Fraction(1, 3)
        elif (0, 2) in spans or (1, 3) in spans:
            ans += Fraction(1, 2)
        else:
            ans += 1
    return ans


def gamma_coeff(edges):
    aut = sum(1 for p in PERMS if frozenset(tuple(sorted((p[u], p[v]))) for u, v in edges) == edges)
    orbit = 24 // aut
    missing = [e for e in EDGES if e not in edges]
    coeff = Counter()
    for mask in range(1 << len(missing)):
        sup = edges | {e for i, e in enumerate(missing) if (mask >> i) & 1}
        coeff[j1(sup)] += orbit * (-1) ** mask.bit_count()
    return {x: c for x, c in coeff.items() if c}


def val(coeff, dimension):
    return sum((c * power ** dimension for power, c in coeff.items()), Fraction(0))


EXPECTED = {
    'claw': {Fraction(8): 4, Fraction(6): -12, Fraction(14, 3): 12, Fraction(4): -4},
    'path': {Fraction(8): 12, Fraction(6): -24, Fraction(16, 3): -12, Fraction(14, 3): 36, Fraction(4): -12},
    'paw': {Fraction(6): 12, Fraction(14, 3): -24, Fraction(4): 12},
    'cycle': {Fraction(16, 3): 3, Fraction(14, 3): -6, Fraction(4): 3},
    'diamond': {Fraction(14, 3): 6, Fraction(4): -6},
    'clique': {Fraction(4): 1},
}

EXPECTED_1 = {'claw': 0, 'path': 8, 'paw': 8, 'cycle': 0, 'diamond': 4, 'clique': 4}
EXPECTED_2 = {'claw': Fraction(64, 3), 'path': Fraction(464, 3),
              'paw': Fraction(304, 3), 'cycle': Fraction(8, 3),
              'diamond': Fraction(104, 3), 'clique': 16}


def test():
    assert len({canon(es) for es in TYPES.values()}) == 6
    allconn = set()
    for mask in range(64):
        e = frozenset(p for i, p in enumerate(EDGES) if (mask >> i) & 1)
        if connected(e):
            allconn.add(canon(e))
    assert len(allconn) == 6 == len({canon(e) for e in TYPES.values()})
    assert set(canon(e) for e in TYPES.values()) == allconn
    assert {k: j1(e) for k, e in TYPES.items()} == {
        'claw': 8, 'path': 8, 'paw': 6,
        'cycle': Fraction(16, 3), 'diamond': Fraction(14, 3), 'clique': 4}
    for k, edges in TYPES.items():
        got = gamma_coeff(edges)
        assert got == EXPECTED[k], (k, got)
        assert val(got, 1) == EXPECTED_1[k], k
        assert val(got, 2) == EXPECTED_2[k], k
    assert sum(EXPECTED_1.values()) == 24
    assert sum(EXPECTED_2.values()) == Fraction(992, 3)
    # Direct strict witnesses for C4 and claw in the plane.
    witness = {
        'cycle': [(0, 0), (.7, .7), (1.4, 0), (.7, -.7)],
        'claw': [(0, 0), (.9, .9), (-.9, .9), (0, -.9)],
    }
    for label, points in witness.items():
        edges = frozenset((i, j) for i, j in EDGES if
                          max(abs(points[i][d] - points[j][d]) for d in (0, 1)) < 1)
        assert canon(edges) == canon(TYPES[label]), (label, edges)
        # No forbidden distance equals threshold 1.
        assert all(abs(max(abs(points[i][d] - points[j][d]) for d in (0, 1))-1) > 0.01
                   for i,j in EDGES)
    for d in range(2, 20):
        assert all(val(EXPECTED[k], d) > 0 for k in TYPES)
    print('FOUR_COMPONENT_ALL_CHECKS_OK: exact inclusion-exclusion, D=1,2, six graph types, strict witnesses')


if __name__ == '__main__':
    test()
