"""Exhaustive small-alphabet checks for the rigidity of optimal
one-insertion covering codes of center length two.

Standard-library Python 3. The infinite-alphabet theorem relies on its
written proof, not on this finite test.
"""
from itertools import combinations, product
from math import comb


def is_transitive_triangle_free(q, arcs):
    arc = set(arcs)
    for a, b, c in product(range(q), repeat=3):
        if len({a, b, c}) == 3 and (a, b) in arc and (a, c) in arc and (b, c) in arc:
            return False
    return True


def covered(q, centers):
    for x, y, z in product(range(q), repeat=3):
        if not ({(x, y), (x, z), (y, z)} & centers):
            return False
    return True


def expected_code(q, part):
    a = set(part)
    b = set(range(q)) - a
    return {(x, y) for x, y in product(range(q), repeat=2) if (x in a) == (y in a)}


def expected_optima(q):
    return {frozenset(expected_code(q, a)) for a in combinations(range(q), q // 2)}


def verify(q):
    arcs = [(x, y) for x in range(q) for y in range(q) if x != y]
    max_arcs = (q * q) // 2
    optima = set()
    for chosen in combinations(arcs, max_arcs):
        if not is_transitive_triangle_free(q, chosen):
            continue
        chosen = set(chosen)
        code = frozenset((x, y) for x in range(q) for y in range(q) if (x, y) not in chosen)
        assert covered(q, code), (q, code)
        optima.add(code)
    expected = expected_optima(q)
    assert optima == expected, (q, len(optima), len(expected), optima ^ expected)
    assert len(optima) == comb(q, q // 2) // (2 if q % 2 == 0 else 1)
    print(f'q={q}: optimum_size={q*q-max_arcs}, distinct_minimum_codes={len(optima)}, symmetry_types=1')


if __name__ == '__main__':
    for q in range(2, 6):
        verify(q)
    print('CHECKER_OK')
