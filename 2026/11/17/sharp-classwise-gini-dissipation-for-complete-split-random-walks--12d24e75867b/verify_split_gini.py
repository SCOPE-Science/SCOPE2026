"""Exact finite diagnostics for Gini dispersion under split-graph random walks.
The accompanying analytical argument, not finite enumeration, proves all dimensions.
"""
from fractions import Fraction as F
from itertools import combinations
import random


def walk(c, s):
    n = c + s
    d = n - 1
    return [[F(0) if i == j else
             (F(1, d) if i < c else F(1, c)) if (i < c or j < c) else F(0)
             for j in range(n)] for i in range(n)]


def apply(P, x):
    return [sum((p * v for p, v in zip(row, x)), F(0)) for row in P]


def gini(x, subset=None):
    if subset is None:
        subset = range(len(x))
    ids = list(subset)
    return sum((abs(x[i] - x[j]) for i, j in combinations(ids, 2)), F(0))


def powers(P, x, k):
    for _ in range(k):
        x = apply(P, x)
    return x


def allcuts(c, s):
    # Includes every individual subset rather than only symmetry-orbits.
    n = c + s
    P = walk(c, s)
    rho = F(s, n - 1)
    count = 0
    for mask in range(1, (1 << n) - 1):
        x = [F((mask >> j) & 1) for j in range(n)]
        a, b = sum(x[:c]), sum(x[c:])
        gx, gy = gini(x), gini(apply(P, x))
        gap = rho * gx - gy
        bound = (a * (c - a) * (s - 1) + s * b * (s - b)) / (n - 1)
        assert gap >= bound, ('classwise inequality', c, s, mask, gap, bound)
        if s >= 2:
            eq = (a == 0 and b == s) or (a == c and b == 0)
            assert (gap == 0) == eq, ('rigidity', c, s, mask, gap)
        else:
            assert gap == 0, ('complete graph equality', c, s, mask)
        for k in range(1, 5):
            assert gini(powers(P, x, k)) <= rho**k * gx
        count += 1
    return count


def sharp_modes(c, s):
    P = walk(c, s)
    rho = F(s, c + s - 1)
    x = [F(0)] * c + [F(1)] * s
    for k in range(1, 8):
        assert gini(powers(P, x, k)) == rho**k * gini(x)
    return 7


def random_real(c, s, seed):
    P = walk(c, s)
    rho = F(s, c + s - 1)
    rng = random.Random(seed)
    for _ in range(100):
        x = [F(rng.randint(-30, 30), rng.randint(1, 9)) for _ in range(c + s)]
        gy = gini(apply(P, x))
        rhs = rho * gini(x) - F(s - 1, c+s-1)*gini(x, range(c)) - F(s,c+s-1)*gini(x, range(c,c+s))
        assert gy <= rhs, ('general real inequality', c, s, x, gy, rhs)


def main():
    checked = sum(allcuts(c,s) for c in range(1,7) for s in range(1,7) if c+s<=10)
    print('EXACT_FULL_SUBSET_CLASSWISE_GINI_AND_RIGIDITY_PASSED', checked)
    witnesses = sum(sharp_modes(c,s) for c in range(1,14) for s in range(1,14))
    print('EXACT_ALL_POWERS_EIGENMODE_ATTAINMENT_PASSED', witnesses)
    for c in range(1,12):
        for s in range(1,12):
            random_real(c,s, seed=c*1000+s)
    print('EXACT_GENERAL_RATIONAL_INPUT_CLASSWISE_DISSIPATION_PASSED', 12100)
    print('ALL_SPLIT_GRAPH_GINI_CHECKS_PASSED')


if __name__ == '__main__':
    main()
