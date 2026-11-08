#!/usr/bin/env python3
"""Reproducible finite tests of a proposed exact Lie-complexity theorem.

All factor sets in these tests are complete through the stated length bound:
all omitted later gaps exceed the tested length, and two full large gaps
have already appeared in the finite prefix.
"""
from itertools import product
from random import Random


def infinite_prefix(gaps, n):
    """Finite prefix preserving every length-n factor of the infinite completion."""
    top = max([n + 3] + gaps) + 3
    complete_gaps = gaps + [top, top + 1, top + 2, top + 3]
    return '1' + ''.join('0'*g + '1' for g in complete_gaps) + '0'*(top+4)


def cyclic_rotations(w):
    return {w[k:] + w[:k] for k in range(len(w))}


def actual_classes(gaps, n):
    text = infinite_prefix(gaps, n)
    factors = {text[i:i+n] for i in range(len(text)-n+1)}
    good = set()
    visited = set()
    for f in factors:
        rot = cyclic_rotations(f)
        key = min(rot)
        if key in visited:
            continue
        visited.add(key)
        if rot <= factors:
            good.add(key)
    return good


def expected_classes(gaps, n):
    classes = {'0'*n, '0'*(n-1) + '1'}
    counts = {a: gaps.count(a) for a in set(gaps)}
    for a, m in counts.items():
        if n % (a + 1) == 0:
            r = n // (a + 1)
            if r >= 2 and m >= r:
                w = ('1' + '0'*a)*r
                classes.add(min(cyclic_rotations(w)))
    return classes


def check(gaps, n):
    got = actual_classes(gaps, n)
    want = expected_classes(gaps, n)
    assert got == want, {'gaps':gaps, 'n':n,
                         'missing':sorted(want-got), 'extra':sorted(got-want)}


def main():
    exhaustive = randomized = 0
    # Every multiplicity pattern on gaps 1, 2, 3, 4, including absent values.
    for profile in product(range(4), repeat=4):
        gaps = [a for a, m in enumerate(profile,1) for _ in range(m)]
        for n in range(1,21):
            check(gaps, n)
            exhaustive += 1
    # Additional skipped values, long plateaus, and large factor lengths.
    rng = Random(20261104)
    for _ in range(125):
        profile = [rng.randrange(0,7) for a in range(1,11)]
        gaps = [a for a, m in enumerate(profile,1) for _ in range(m)]
        for n in range(1,29):
            check(gaps, n)
            randomized += 1
    # Two explicit natural families.
    for bound in (20, 28, 36):
        for multiplicities in (lambda a: 1, lambda a: a):
            gaps = [a for a in range(1,bound+1) for _ in range(multiplicities(a))]
            for n in range(1,bound+1):
                check(gaps,n)
                randomized += 1
    print('PASS exhaustive_cases=',exhaustive,
          'random_and_family_cases=',randomized,
          'total=',exhaustive+randomized)


if __name__=='__main__':
    main()
