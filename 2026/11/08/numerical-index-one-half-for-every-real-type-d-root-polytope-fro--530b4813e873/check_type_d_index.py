"""Exact finite checks of the signed-pair vertex/norming-functional identities.

Python 3 standard library only. Finite tests corroborate but do not prove the
all-dimensional theorem.
"""
from itertools import combinations, product


def vertices(d):
    for i, j in combinations(range(d), 2):
        for a, b in product((-1, 1), repeat=2):
            x = [0] * d
            x[i], x[j] = a, b
            yield tuple(x)


def generators(d):
    for k in range(d):
        for a in (-1, 1):
            f = [0] * d
            f[k] = 2 * a
            yield tuple(f)
    yield from product((-1, 1), repeat=d)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm_times_two(x):
    return max(2 * max(abs(t) for t in x), sum(abs(t) for t in x))


def check(d):
    vs = list(vertices(d))
    fs = list(generators(d))
    roots = set(vs)
    assert len(roots) == 2 * d * (d - 1)
    counter = 0
    for x in vs:
        assert norm_times_two(x) == 2
        for f in fs:
            assert abs(dot(f, x)) <= 2
            if abs(dot(f, x)) < 2:
                witnesses = [(y, tuple(a - b for a, b in zip(x, y))) for y in vs]
                assert any(z in roots and abs(dot(f, y)) == 2 and abs(dot(f, z)) == 2
                           for y, z in witnesses)
            counter += 1
    # The operator S(x) = (x_1+x_2)e_3; dual f is scaled by two.
    nrm2 = max(abs(x[0] + x[1]) for x in vs)
    num2 = max(abs((x[0] + x[1]) * f[2])
               for x in vs for f in fs if dot(f, x) == 2)
    assert (nrm2, num2) == (2, 2)
    # num2 == 2 means the unscaled numerical radius is 1.
    return counter


if __name__ == '__main__':
    total = sum(check(d) for d in (4, 5, 6, 7))
    print('TYPE_D_NUMERICAL_INDEX_EXACT_OK', total)
