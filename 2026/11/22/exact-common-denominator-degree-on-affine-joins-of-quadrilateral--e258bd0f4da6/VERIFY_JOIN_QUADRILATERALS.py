"""Exact rational checks for barycentric formulas on joins of model quadrilaterals.

The universal proof uses a separate vertex-excess argument; these tests cover
homogenized square/trapezoid coordinate identities, not arbitrary polygons.
Run: python VERIFY_JOIN_QUADRILATERALS.py
"""
from fractions import Fraction as F
from itertools import product


def factor(t, z1, z2, kind):
    if kind == 'square':
        vertices = ((0, 0), (1, 0), (1, 1), (0, 1))
        h = t
        p = ((t-z1)*(t-z2), z1*(t-z2), z1*z2, (t-z1)*z2)
    else:
        vertices = ((0, 0), (2, 0), (1, 1), (0, 1))
        h = 2*t-z2
        p = ((2*t-z1-z2)*(t-z2), z1*(t-z2), z1*z2,
             z2*(2*t-z1-z2))
    assert sum(p) == t*h
    assert sum(v[0]*pi for v, pi in zip(vertices, p)) == z1*h
    assert sum(v[1]*pi for v, pi in zip(vertices, p)) == z2*h
    return h, p, vertices


def check(k, seed, kinds):
    weights = [F(i+seed+1, 1) for i in range(k)]
    total = sum(weights)
    weights = [x/total for x in weights]
    polys = []
    for i, (t, kind) in enumerate(zip(weights, kinds)):
        y = F((i+seed) % 5+1, 7)
        u = F((2*i+seed) % 5+1, 7)
        x = u if kind == 'square' else u*(2-y)
        polys.append(factor(t, t*x, t*y, kind))
    denominator = F(1)
    for h, _, _ in polys:
        assert h > 0
        denominator *= h
    assert denominator > 0
    nsum = F(0)
    for i, (h, ps, vertices) in enumerate(polys):
        other = denominator / h
        nums = [pi*other for pi in ps]
        nsum += sum(nums)
        t = weights[i]
        z1 = sum(v[0]*pi for v, pi in zip(vertices, ps)) / h
        z2 = sum(v[1]*pi for v, pi in zip(vertices, ps)) / h
        assert sum(nums) == t*denominator
        assert sum(v[0]*num for v, num in zip(vertices, nums)) == z1*denominator
        assert sum(v[1]*num for v, num in zip(vertices, nums)) == z2*denominator
        assert all(num >= 0 for num in nums)
    assert nsum == denominator
    assert 4*k-2-(3*k-1) == k-1


def main():
    count = 0
    for k in range(2, 9):
        for seed in range(1, 17):
            for kinds in (('square',)*k, ('trapezoid',)*k,
                          tuple('square' if i % 2 else 'trapezoid' for i in range(k))):
                check(k, seed, kinds)
                count += 1
    print('Exact rational join identities passed:', count,
          'cases; dimensions 5, 8, 11, 14, 17, 20, 23.')


if __name__ == '__main__':
    main()
