"""Finite arithmetic cross-checks for the unary-binary tree offspring construction.

The infinite-dimensional theorem relies on analytical estimates, not finite enumeration.
"""
import math
from fractions import Fraction


def sequence(num, den, kmax):
    # kappa=num/den; integer ceilings via an exponential sample where exact.
    kappa = num / den
    cutoffs = set()
    j = 1
    while True:
        n = math.ceil(2.0 ** (j / (2.0 * kappa)) - 1e-12) + j
        if n > kmax:
            break
        cutoffs.add(n)
        j += 1
    bits = []
    for k in range(1, kmax + 1):
        bits.extend((2, 1))
        if k in cutoffs:
            bits.append(2)
    return bits, cutoffs


def test():
    checks = 0
    for num, den in ((1, 2), (1, 1), (2, 1)):
        bits, cuts = sequence(num, den, 256)
        pops = [1]
        for b in bits:
            assert b in (1, 2)
            pops.append(pops[-1] * b)
            checks += 1
        n = 0
        twos = 0
        for k in range(1, 257):
            n += 2
            twos += 1
            if k in cuts:
                n += 1
                twos += 1
            assert pops[n] == 2 ** twos
            assert n == 2 * k + sum(1 for v in cuts if v <= k)
            checks += 2
        for horizon in (1, 2, 3, 5, 13, 29):
            # Formula for the number of descendants, hence shift norm at p=2:
            ratios = [pops[a + horizon] // pops[a] for a in range(len(bits) - horizon + 1)]
            assert max(ratios) >= pops[horizon]
            assert all(r in (2**u for u in range(horizon + 1)) for r in ratios)
            checks += 2
        kappa = Fraction(num, den)
        rho = 1 + 1 / kappa
        for p in (Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3), Fraction(4), Fraction(5)):
            assert (kappa * (p - 1) > 1) == (p > rho)
            checks += 1
    print('TREE_PERIPHERAL_PHASE_FINITE_OK', checks)

if __name__ == '__main__':
    test()
