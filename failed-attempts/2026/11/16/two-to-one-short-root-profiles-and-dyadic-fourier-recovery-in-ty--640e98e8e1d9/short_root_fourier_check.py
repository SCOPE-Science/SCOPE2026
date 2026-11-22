#!/usr/bin/env python3
"""Exact short-root profile Walsh transform for type-C positive-root downsets.

Run with Python 3.10+; no third-party dependencies. Every calculation uses integers.
Type-C simple roots are e_i-e_(i+1) (i<n), 2e_n.
Root vectors below are expressed in that basis.
"""
from collections import Counter
from math import comb


def positive_roots(n):
    roots = []
    for i in range(n):
        for j in range(i + 1, n):
            difference = tuple(int(i <= k < j) for k in range(n))
            summation = tuple((int(i <= k < j) if k < j else
                               (2 if j <= k < n - 1 else 1)) for k in range(n))
            roots.extend([(difference, 'short'), (summation, 'short')])
        twice = tuple((2 if i <= k < n - 1 else (1 if k == n - 1 else 0))
                      for k in range(n))
        roots.append((twice, 'long'))
    roots.sort(key=lambda z: (sum(z[0]), z[0]))
    assert len(roots) == n * n and len({p for p, _ in roots}) == n * n
    return roots


def short_projected_ideals(n):
    entries = positive_roots(n)
    roots = [r for r, _ in entries]
    short = [i for i, (_, kind) in enumerate(entries) if kind == 'short']
    down = [sum(1 << j for j, beta in enumerate(roots)
                if all(x <= y for x, y in zip(beta, alpha)))
            for alpha in roots]
    # First construction: add one admissible root to a downset.
    downsets = {0}
    frontier = [0]
    while frontier:
        mask = frontier.pop()
        for i in range(len(roots)):
            if (mask >> i) & 1 or (down[i] & mask) != (down[i] ^ (1 << i)):
                continue
            nextmask = mask | (1 << i)
            if nextmask not in downsets:
                downsets.add(nextmask)
                frontier.append(nextmask)
    assert len(downsets) == comb(2 * n, n)
    # Independent construction: choose an antichain, then take its downward closure.
    comparable = []
    for i, a in enumerate(roots):
        comparable.append(sum(1 << j for j, b in enumerate(roots)
                              if all(x <= y for x, y in zip(a, b))
                              or all(x >= y for x, y in zip(a, b))))
    reconstructed = set()
    def antichains(j, choice, union_down):
        if j == len(roots):
            reconstructed.add(union_down)
            return
        antichains(j + 1, choice, union_down)
        if not (choice & comparable[j]):
            antichains(j + 1, choice | (1 << j), union_down | down[j])
    antichains(0, 0, 0)
    assert reconstructed == downsets
    profiles = []
    for mask in sorted(downsets):
        profiles.append(sum(((mask >> i) & 1) << j for j, i in enumerate(short)))
    assert all(weight == 2 for weight in Counter(profiles).values())
    assert len(set(profiles)) * 2 == len(profiles)
    return entries, short, downsets, profiles


def fwht(values):
    n = len(values)
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            for j in range(i, i + width):
                a, b = values[j], values[j + width]
                values[j], values[j + width] = a + b, a - b
        width *= 2
    return values


def audit(n):
    entries, short, downsets, profiles = short_projected_ideals(n)
    m = len(short)
    freq = [0] * (1 << m)
    for p in profiles:
        freq[p] += 1
    values = fwht(freq)
    assert values[0] == len(profiles)
    assert sum(x*x for x in values) == (1 << m) * sum(v*v for v in Counter(profiles).values())
    zeros = sum(x == 0 for x in values)
    minimum = min(abs(x) for x in values if x)
    # Independent direct character evaluations at the critical frequencies.
    for k in {0, (1 << m) - 1, 4 if n == 3 else 0,
              33 if n == 4 else 0, 514 if n == 5 else 0}:
        if k < (1 << m):
            direct = sum(1 - 2 * ((k & p).bit_count() & 1) for p in profiles)
            assert direct == values[k]
    if n == 4:
        assert all(sum((mask >> j) & 1 for mask in profiles) % 2 == 0
                   for j in range(m))
        assert all(x % 4 == 2 for x in values)
        assert values[33] == 2
    if n == 3: assert values[4] == 0
    if n == 5: assert values[514] == 0
    return len(profiles),len(set(profiles)),zeros, len(values)-zeros,minimum

def audit_six():
    entries, short, downsets, profiles = short_projected_ideals(6)
    k = (1 << 0) | (1 << 8) | (1 << 19)
    positive = sum(((k & p).bit_count() & 1) == 0 for p in profiles)
    negative = len(profiles) - positive
    assert len(profiles) == 924 and len(set(profiles)) == 462
    assert positive == negative == 462
    return len(profiles), len(set(profiles)), k, positive, negative

if __name__ == '__main__':
    expected={2:(6,3,0,4,2),3:(20,10,18,46,4),
              4:(70,35,0,4096,2),5:(252,126,126056,922520,4)}
    for n in range(2,6):
        observed = audit(n)
        assert observed == expected[n], (n,observed,expected[n])
        print('C%d ideals=%d profiles=%d zeros=%d rank=%d min_nonzero=%d'
              % (n,*observed))
    n6 = audit_six()
    print('C6 ideals=%d profiles=%d zero_witness=%d positive=%d negative=%d' % n6)
    for n in (7,8):
        _, short, downsets, profiles = short_projected_ideals(n)
        print('C%d ideals=%d distinct_profiles=%d uniform_fiber=2' %
              (n, len(downsets), len(set(profiles))))
    print('SHORT_ROOT_C2_C8_FOURIER_PASS')
