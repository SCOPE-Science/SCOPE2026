"""Exact, finite-state regression checks for the Ising unmasking theorem.

Run: python3 check.py
Only Python's standard library is required. Finite tests corroborate algebra; the
proof of the all-length result is in RESULT.md, not in numerical enumeration.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product


def conditional_mean(partial, i, lam):
    """Ideal zero-field Ising-chain single-site conditional mean."""
    L = len(partial)
    left = next((j for j in range(i - 1, -1, -1) if partial[j] is not None), None)
    right = next((j for j in range(i + 1, L) if partial[j] is not None), None)
    if left is None and right is None:
        return F(0)
    if left is None:
        return (lam ** (right - i)) * partial[right]
    if right is None:
        return (lam ** (i - left)) * partial[left]
    u, v = lam ** (i - left), lam ** (right - i)
    return (u * partial[left] + v * partial[right]) / (
        1 + u * v * partial[left] * partial[right]
    )


def exact_output(L, lam, labels):
    """Enumerate the entire parallel decoder law, conditional on fixed step labels."""
    dist = {(None,) * L: F(1)}
    for step in sorted(set(labels)):
        sites = [i for i in range(L) if labels[i] == step]
        new = defaultdict(F)
        for state, prob in dist.items():
            chances = [(1 + conditional_mean(state, i, lam)) / 2 for i in sites]
            for xs in product((-1, 1), repeat=len(sites)):
                q = prob
                for s, p in zip(xs, chances):
                    q *= p if s == 1 else 1 - p
                if not q:
                    continue
                state2 = list(state)
                for i, x in zip(sites, xs):
                    state2[i] = x
                new[tuple(state2)] += q
        dist = new
    assert sum(dist.values()) == 1
    return dist


def pair_expectation(dist, i, j):
    return sum((p * xs[i] * xs[j] for xs, p in dist.items()), F(0))


def source_prob(xs, lam):
    p = F(1, 2)
    for i in range(len(xs) - 1):
        p *= (1 + lam * xs[i] * xs[i + 1]) / 2
    return p


def verify():
    checked = 0
    simultaneous = 0
    sequential = 0
    for length, rounds, lam in (
        (2, 3, F(1, 5)), (3, 3, F(1, 2)),
        (4, 3, F(3, 4)), (4, 3, F(-1, 2)),
        (5, 3, F(2, 5)), (5, 2, F(-3, 4)),
    ):
        rho = abs(lam)
        local_min = rho * (1 - rho * rho) ** 2 / (1 + rho ** 3) ** 2
        for labels in product(range(rounds), repeat=length):
            dist = exact_output(length, lam, labels)
            for i in range(length):
                assert sum(p * xs[i] for xs, p in dist.items()) == 0
                for j in range(i + 1, length):
                    signed = (-1 if lam < 0 and (j - i) % 2 else 1)
                    c = signed * pair_expectation(dist, i, j)
                    assert F(0) <= c <= rho ** (j - i), (length, lam, labels, i, j, c)
                    checked += 1
                    if j == i + 1 and labels[i] == labels[j]:
                        assert rho - c >= local_min, (length, lam, labels, i, c)
                        simultaneous += 1
            if len(set(labels)) == length:
                assert all(dist.get(xs, F(0)) == source_prob(xs, lam)
                           for xs in product((-1, 1), repeat=length))
                sequential += 1
    # Exact weighted average over independently chosen reveal labels.
    length, lam = 4, F(3, 5)
    masses = (F(1, 6), F(1, 3), F(1, 2))
    aggregate = defaultdict(F)
    for labels in product(range(len(masses)), repeat=length):
        w = F(1)
        for n in labels:
            w *= masses[n]
        for xs, p in exact_output(length, lam, labels).items():
            aggregate[xs] += w * p
    assert sum(aggregate.values()) == 1
    rho = abs(lam)
    local_min = rho * (1 - rho * rho) ** 2 / (1 + rho ** 3) ** 2
    collision = sum((w * w for w in masses), F(0))
    for i in range(length - 1):
        assert rho - pair_expectation(aggregate, i, i + 1) >= local_min * collision
        assert rho - pair_expectation(aggregate, i, i + 1) >= local_min / len(masses)
    # The regression is exact rational arithmetic with no numerical tolerances.
    print(f'PASS: {checked} pair inequalities; {simultaneous} adjacent co-reveal bounds;')
    print(f'PASS: {sequential} all-singleton partitions; independent-schedule mixture;')
    print(f'PASS: exact fraction mass, zero means, both interaction signs;')
    print(f'example collision probability = {collision}; conditional constant = {local_min}')


if __name__ == '__main__':
    verify()
