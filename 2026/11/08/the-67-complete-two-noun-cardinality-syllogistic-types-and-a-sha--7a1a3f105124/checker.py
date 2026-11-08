#!/usr/bin/env python3
"""Exact two-noun syllogistic type census and independent direct-semantics checks.

Requires Python 3 standard library. Run: python checker.py
All objects are finite, and the infinite-family statement uses the mathematical proof.
"""
from collections import Counter, defaultdict
from itertools import product

NOUNS = ((0, 1), (2, 3), (0, 2), (1, 3))
# A cell index is a truth assignment for two unary predicates:
# 0: both, 1: first only, 2: second only, 3: neither.


def sg(t):
    return (t > 0) - (t < 0)


def signature(cells):
    a, b, c, d = cells
    u, v = a - d, b - c
    return (tuple(int(x != 0) for x in cells),
            tuple(map(sg, (u, v, u + v, u - v))))


def direct_atoms(cells):
    total = [sum(cells[i] for i in noun) for noun in NOUNS]
    ans = []
    for op in range(4):
        for i, x in enumerate(NOUNS):
            for j, y in enumerate(NOUNS):
                if op == 0:  # all x are y
                    ans.append(all(cells[t] == 0 for t in set(x) - set(y)))
                elif op == 1:  # some x are y
                    ans.append(any(cells[t] > 0 for t in set(x) & set(y)))
                elif op == 2:  # at least as many x as y
                    ans.append(total[i] >= total[j])
                else:  # more x than y
                    ans.append(total[i] > total[j])
    assert len(ans) == 64
    return tuple(ans)


def min_pair(status, diff):
    # status Z / F / S / B: neither, first only, second only, both.
    if status == 'Z':
        return (0, 0) if diff == 0 else None
    if status == 'F':
        return (diff, 0) if diff >= 1 else None
    if status == 'S':
        return (0, -diff) if diff <= -1 else None
    if status == 'B':
        return (1 + max(diff, 0), 1 + max(-diff, 0))
    raise ValueError(status)


def analytic_catalogue():
    # Every face of the central B2 arrangement u=0,v=0,u=v,u=-v
    # has an L1-minimum lattice representative in this small box.
    profiles = {}
    for s1, s2 in product('ZFSB', repeat=2):
        for u, v in product(range(-2, 3), repeat=2):
            ad = min_pair(s1, u)
            bc = min_pair(s2, v)
            if ad is None or bc is None:
                continue
            cells = (ad[0], bc[0], bc[1], ad[1])
            if sum(cells) == 0:
                continue
            sig = signature(cells)
            if sig not in profiles or sum(cells) < sum(profiles[sig]):
                profiles[sig] = cells
    return profiles


def independent_enumeration(max_size=12):
    profiles = defaultdict(set)
    truth_signatures = {}
    reverse = {}
    first = {}
    for n in range(1, max_size + 1):
        for a in range(n + 1):
            for b in range(n-a+1):
                for c in range(n-a-b+1):
                    cells = (a, b, c, n - a-b-c)
                    sig = signature(cells)
                    atoms = direct_atoms(cells)
                    if sig in truth_signatures:
                        assert truth_signatures[sig] == atoms
                    else:
                        truth_signatures[sig] = atoms
                    if atoms in reverse:
                        assert reverse[atoms] == sig
                    else:
                        reverse[atoms] = sig
                    profiles[sig].add(n)
                    first.setdefault(sig, cells)
    return profiles


def main():
    catalogue = analytic_catalogue()
    direct = independent_enumeration()
    assert set(catalogue) == set(direct)
    assert len(catalogue) == 67
    counts = Counter(sum(x) for x in catalogue.values())
    assert [counts[i] for i in range(1, 8)] == [4,6,16,9,20,4,8]
    by_spectrum = Counter()
    for sig, example in catalogue.items():
        minimum = sum(example)
        is_even = sig[1][2] == 0 or sig[1][3] == 0
        tag = ('E' if is_even else 'T', minimum)
        by_spectrum[tag] += 1
        expected = {n for n in range(1,13) if n >= minimum and
                    (not is_even or n % 2 == 0)}
        assert direct[sig] == expected, (tag,example,sorted(direct[sig]))
    assert by_spectrum == {('T',1):4,('T',3):16,('T',5):20,('T',7):8,
                           ('E',2):6,('E',4):9,('E',6):4}
    # Sharp threshold: all four Venn cells inhabited and |p|>|q|>|not q|.
    for n in range(1,7):
        for a in range(n+1):
            for b in range(n-a+1):
                for c in range(n-a-b+1):
                    d=n-a-b-c
                    assert not (min(a,b,c,d) >= 1 and a+b > a+c > b+d)
    assert (3,2,1,1) == catalogue[signature((3,2,1,1))]
    assert 3+2 > 3+1 > 2+1
    print('TWO_NOUN_CARDINALITY_TYPES_OK')
    print('types:',len(catalogue),'minimum distribution:',[counts[i] for i in range(1,8)])
    print('spectrum types:',dict(sorted(by_spectrum.items())))
    print('atomic checks: 64 sentences; direct models through 12 elements')


if __name__ == '__main__':
    main()
