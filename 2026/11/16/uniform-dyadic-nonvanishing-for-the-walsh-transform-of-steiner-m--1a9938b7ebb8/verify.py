#!/usr/bin/env python3
"""Exact Walsh checks for complements of Steiner triple systems.

Only Python's standard library is required. No floating-point arithmetic.
"""
from collections import Counter
from itertools import combinations
from math import comb


def projective_blocks(d):
    n = (1 << d) - 1
    return n, sorted({tuple(sorted((a - 1, b - 1, (a ^ b) - 1)))
                      for a, b in combinations(range(1, n + 1), 2)})


def affine_nine_blocks():
    points = [(a, b) for a in range(3) for b in range(3)]
    directions = [(0, 1), (1, 0), (1, 1), (1, 2)]
    return 9, sorted({tuple(sorted(points.index(((x + k * dx) % 3, (y + k * dy) % 3))
                                    for k in range(3)))
                      for x, y in points for dx, dy in directions})


def bose_fifteen_blocks():
    # Bose construction: Q=Z/5Z, layer index modulo three, quasigroup (a+b)/2.
    blocks = [(3*a, 3*a+1, 3*a+2) for a in range(5)]
    for a, b in combinations(range(5), 2):
        c = ((a+b)*3) % 5  # 3 = 2^{-1} modulo five.
        for j in range(3):
            blocks.append((3*a+j, 3*b+j, 3*c+(j+1)%3))
    return 15, sorted(tuple(sorted(t)) for t in blocks)


def cyclic_thirteen_blocks():
    n = 13
    starters = [(0, 1, 4), (0, 2, 7)]
    blocks = {tuple(sorted((x + shift) % n for x in starter))
              for starter in starters for shift in range(n)}
    return n, sorted(blocks)


def fast_walsh(a):
    a = a[:]
    block = 1
    while block < len(a):
        for start in range(0, len(a), 2*block):
            for i in range(start, start+block):
                x, y = a[i], a[i+block]
                a[i], a[i+block] = x+y, x-y
        block *= 2
    return a


def verify(n, blocks, label):
    lines = set(tuple(sorted(t)) for t in blocks)
    assert len(lines) == n*(n-1)//6
    pair_occ = Counter(p for t in lines for p in combinations(t, 2))
    assert all(pair_occ[x, y] == 1 for x, y in combinations(range(n), 2))
    assert sum(pair_occ.values()) == 3 * len(lines)
    bases = [t for t in combinations(range(n), 3) if t not in lines]
    expected_total = n*(n-1)*(n-3)//6
    assert len(bases) == expected_total
    N = 1 << n
    indicator = [0] * N
    for t in bases:
        indicator[sum(1 << i for i in t)] = 1
    spectrum = fast_walsh(indicator)
    assert sum(w*w for w in spectrum) == N * len(bases)  # Parseval.
    line_masks = [sum(1 << i for i in t) for t in lines]
    degree = (n-1)*(n-3)//2
    codegree = n-3
    for frequency, w in enumerate(spectrum):
        size = frequency.bit_count()
        # Triple bases lying completely in S = C(|S|,3) - STS blocks in S.
        contained_lines = sum((frequency & m) == m for m in line_masks)
        contained_bases = comb(size, 3) - contained_lines if size >= 3 else 0
        exact_formula = (len(bases) - 2*size*degree
                         + 4*comb(size, 2)*codegree - 8*contained_bases)
        assert exact_formula == w, (label, frequency, w, exact_formula)
        if n % 8 in (5, 7):
            assert w % 8 == 4, (label, frequency, w)
            assert w != 0
    if n % 8 in (5, 7):
        assert sum(w == 0 for w in spectrum) == 0
        assert ((n*(n-1)*(n-3)//6) % 8) == 4
    counter = Counter(spectrum)
    positives = sorted((abs(k), v) for k, v in counter.items() if k != 0)
    abs_counter = Counter()
    for w, count in counter.items():
        abs_counter[abs(w)] += count
    print(label, 'n='+str(n), 'bases='+str(len(bases)),
          'rank='+str(sum(w != 0 for w in spectrum)),
          'zeros='+str(counter[0]), 'minimum_nonzero='+str(min(x for x,_ in positives)),
          'absolute_spectrum='+repr(sorted(abs_counter.items())))
    return spectrum


def main():
    v7 = verify(*projective_blocks(3), 'PG(2,2)')
    v9 = verify(*affine_nine_blocks(), 'AG(2,3)')
    v13 = verify(*cyclic_thirteen_blocks(), 'cyclic STS(13)')
    v15a = verify(*projective_blocks(4), 'PG(3,2)')
    v15b = verify(*bose_fifteen_blocks(), 'Bose(15)')
    assert Counter(v15a) != Counter(v15b)
    assert v9[3] == 0  # Two marked points: general formula vanishes at n=9.
    assert v7[0] == 28 and v13[0] == 260 and v15a[0] == v15b[0] == 420
    print('STS_COMPLEMENT_WALSH_MOD8_PASS')


if __name__ == '__main__':
    main()
