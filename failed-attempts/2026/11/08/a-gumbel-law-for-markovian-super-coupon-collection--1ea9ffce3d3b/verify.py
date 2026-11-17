#!/usr/bin/env python3
"""Finite exact checks for the Johnson-walk shadow collection theorem.
Standard-library only. The infinite-limit argument is analytic, not certified here.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import random


def neighbor_states(state, n):
    current = set(state)
    return [tuple(sorted((current - {old}) | {new}))
            for old in state for new in range(n) if new not in current]


def test():
    assertions = 0
    for n in range(5, 10):
        for r in range(1, min(4, n - 2) + 1):
            states = list(combinations(range(n), r))
            m = len(states)
            denom = r * (n - r)
            neighbors = {a: neighbor_states(a, n) for a in states}
            for a in states:
                nb = neighbors[a]
                assert len(nb) == denom and len(set(nb)) == denom
                assertions += 1
                assert all(a in neighbors[b] for b in nb)
                assertions += 1
            # Every inclusion-coordinate function has the asserted triangular action.
            for j in range(r + 1):
                theta = F(1) - F(j * (n + 1 - j), r * (n - r))
                coeff = F(r - j + 1, r * (n - r))
                for B in combinations(range(n), j):
                    Bs = set(B)
                    for R in states:
                        Rs = set(R)
                        lhs = F(sum(Bs.issubset(Nb) for Nb in map(set, neighbors[R])), denom)
                        rhs = theta * int(Bs.issubset(Rs))
                        rhs += coeff * sum(int((Bs - {b}).issubset(Rs)) for b in B)
                        assert lhs == rhs, (n, r, B, R, lhs, rhs)
                        assertions += 1
            for s in range(1, r + 1):
                A = set(range(s))
                H = {R for R in states if A.issubset(R)}
                assert F(len(H), m) == F(comb(r, s), comb(n, s))
                assertions += 1
                exits = sum(sum(Nb not in H for Nb in neighbors[R]) for R in H)
                flux = F(exits, m * denom)
                target_rate = F(comb(r-1, s-1), comb(n, s))
                assert flux == target_rate, (n, r, s, flux, target_rate)
                assertions += 1
                if comb(n, s) > 1:
                    A2 = set(list(combinations(range(n), s))[1])
                    union = {R for R in states if A.issubset(R) or A2.issubset(R)}
                    union_exits = sum(sum(Nb not in union for Nb in neighbors[R]) for R in union)
                    union_flux = F(union_exits, m * denom)
                    assert 0 < union_flux <= 2 * target_rate
                    assertions += 1
                    # One-step entrance bound used in the principal-eigenvalue proof.
                    for R in states:
                        if R not in union:
                            enter = F(sum(Nb in union for Nb in neighbors[R]), denom)
                            assert enter <= F(2, n-r)
                            assertions += 1
    # Independent stochastic diagnostic. Not an asymptotic proof.
    rng = random.Random(73429)
    n, r, s = 45, 3, 2
    N = comb(n, s)
    samples = []
    for _ in range(70):
        R = rng.sample(range(n), r)
        seen = set(combinations(sorted(R), s))
        elapsed = 0
        while len(seen) != N:
            pos = rng.randrange(r)
            old = set(R)
            new = rng.randrange(n)
            while new in old:
                new = rng.randrange(n)
            R[pos] = new
            seen.update(combinations(sorted(R), s))
            elapsed += 1
            if elapsed > 150_000:
                raise AssertionError('unexpectedly long simulated run')
        samples.append(elapsed)
    from statistics import mean
    rate = F(comb(r-1, s-1), N)
    print('CHECK_OK', assertions, 'exact rational assertions')
    print('SIM_DIAGNOSTIC', n, r, s, 'runs', len(samples),
          'mean_scaled', round(float(rate) * mean(samples), 3),
          'theory_logN', round(__import__('math').log(N), 3))


if __name__ == '__main__':
    test()
