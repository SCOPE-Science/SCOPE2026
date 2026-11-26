"""Exact finite checks for five-entry bistochastic cube roots."""

from fractions import Fraction
from itertools import combinations, permutations, product


def mat(f):
    return tuple(tuple(f(i, j) for j in range(3)) for i in range(3))


def mul(a, b):
    return mat(lambda i, j: sum(a[i][k] * b[k][j] for k in range(3)))


def perm(s):
    return mat(lambda i, j: int(s[i] == j))


def support(a):
    return frozenset((i, j) for i, j in product(range(3), repeat=2) if a[i][j] > 0)


def relabel(a, s):
    return mat(lambda i, j: a[s[i]][s[j]])


def cube(a):
    return mul(mul(a, a), a)


def primitive(e):
    adjacency = mat(lambda i, j: int((i, j) in e))
    power = adjacency
    for _ in range(9):
        if len(support(power)) == 9:
            return True
        power = mul(power, adjacency)
    return False


def main():
    perms = list(permutations(range(3)))
    matchings = [support(perm(s)) for s in perms]
    assert min(len(e | f) for e, f in combinations(matchings, 2)) == 5
    feasible = {e | f for e, f in combinations(matchings, 2) if len(e | f) == 5}
    assert len(feasible) == 9 and all(sum(m <= e for m in matchings) == 2 for e in feasible)
    admissible = {e for e in feasible if primitive(e)}
    assert len(admissible) == 6
    weights = {Fraction(j, 20) for j in range(1, 20)}
    matrices = [(p, relabel(((0, 0, 1), (p, 1-p, 0), (1-p, p, 0)), s))
                for p in weights for s in perms]
    for p in weights:
        canonical = ((0, 0, 1), (p, 1-p, 0), (1-p, p, 0))
        assert {support(relabel(canonical, s)) for s in perms} == admissible
        b12, b13, b23 = [mat(lambda i, j: p * (i == j) + (1-p) * (s[i] == j))
                         for s in ((1, 0, 2), (2, 1, 0), (0, 2, 1))]
        assert cube(canonical) == mul(mul(b23, b13), b12)
        sweeps = {mul(mul(a, b), c) for a, b, c in permutations((b12, b13, b23))}
        assert len(sweeps) == 6
        for sw in sweeps:
            roots = [(q, x) for q, x in matrices if cube(x) == sw]
            assert len(roots) == 1 and roots[0][0] == p
    print('PASS: 9 feasible supports, 6 primitive supports, 114 labeled sweeps')


if __name__ == '__main__':
    main()
