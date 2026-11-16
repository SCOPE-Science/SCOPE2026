#!/usr/bin/env python3
"""Exact 4x4 alternating-sign-matrix Fourier/projection checker.

Uses only Python standard library; no floating point arithmetic. With --write,
produces the 512-row reduced Fourier certificate and 42-row support certificate.
"""
import csv
import itertools
import pathlib
import sys
from collections import Counter
from fractions import Fraction

N = 4
Q = 1 << 9


def alternating_rows():
    rows = []
    for row in itertools.product((-1, 0, 1), repeat=N):
        partial = 0
        good = True
        for z in row:
            partial += z
            if partial not in (0, 1):
                good = False
                break
        if good and partial == 1:
            rows.append(row)
    return rows


def all_matrices():
    """Direct exhaustive enumeration: 8^4 candidate row sequences."""
    ans = []
    for a in itertools.product(alternating_rows(), repeat=N):
        good = True
        for j in range(N):
            partial = 0
            for i in range(N):
                partial += a[i][j]
                if partial not in (0, 1):
                    good = False
                    break
            if not good or partial != 1:
                good = False
                break
        if good:
            ans.append(a)
    return ans


def masks(a):
    full = sum((1 << (N*i+j)) for i in range(N) for j in range(N)
               if a[i][j] != 0)
    reduced = sum((1 << (3*i+j)) for i in range(3) for j in range(3)
                  if a[i][j] != 0)
    return full, reduced


def fwht(v):
    v = list(v)
    step = 1
    while step < len(v):
        for base in range(0, len(v), 2*step):
            for k in range(base, base+step):
                p, q = v[k], v[k+step]
                v[k], v[k+step] = p+q, p-q
        step *= 2
    return v


def affine_rank(xs):
    pivots = {}
    for x in xs[1:]:
        z = x ^ xs[0]
        while z:
            b = z.bit_length() - 1
            if b in pivots:
                z ^= pivots[b]
            else:
                pivots[b] = z
                break
    return len(pivots)


def compute():
    matrices = all_matrices()
    assert len(alternating_rows()) == 8
    assert len(matrices) == 42
    assert Counter(sum(a[i][j] == -1 for i in range(4) for j in range(4))
                   for a in matrices) == {0: 24, 1: 16, 2: 2}
    pairs = sorted(masks(a) for a in matrices)
    full = [t[0] for t in pairs]
    small = [t[1] for t in pairs]
    assert len(set(full)) == len(set(small)) == 42
    assert affine_rank(small) == 9
    for f in full:
        for i in range(4):
            assert sum((f >> (4*i+j))&1 for j in range(4)) % 2 == 1
        for j in range(4):
            assert sum((f >> (4*i+j))&1 for i in range(4)) % 2 == 1
    inc = [int(k in set(small)) for k in range(Q)]
    spectrum = fwht(inc)
    # Independent direct evaluation (character definition, no FWHT).
    direct = [sum(1 if ((freq & x).bit_count() & 1)==0 else -1
                  for x in small) for freq in range(Q)]
    assert spectrum == direct
    abs_hist = Counter(map(abs, spectrum))
    expected = {0:120, 2:146, 4:80, 6:77, 8:40,
                10:7, 12:8, 14:22, 20:4, 22:2,
                26:1, 28:4, 42:1}
    assert dict(abs_hist) == expected
    assert sum(z*z for z in spectrum) == Q*42  # Parseval
    support = [int(t != 0) for t in spectrum]
    kernel_numerators = fwht(support)
    assert Counter(kernel_numerators) == {
        -40:1, -32:4, -20:8, -16:10, -8:46, -4:120,
        0:132, 4:120, 8:46, 16:10, 20:8, 32:4,
        40:1, 120:1, 392:1
    }
    kernel_abs_sum = sum(map(abs, kernel_numerators))
    assert kernel_abs_sum == 3184
    assert Fraction(kernel_abs_sum, Q) == Fraction(199,32)
    assert sum(support) == 392
    assert max(map(abs, spectrum)) == 42
    assert min(abs(t) for t in spectrum if t != 0) == 2
    # Independent 16-variable character sum for every ambient frequency.
    full_hist = Counter()
    for freq in range(1 << 16):
        w = sum(1 if ((freq & mask).bit_count() & 1) == 0 else -1
                for mask in full)
        full_hist[abs(w)] += 1
    assert full_hist == Counter({k:128*v for k,v in expected.items()})
    assert full_hist[0] == 15360
    assert (1<<16)-full_hist[0] == 50176
    return matrices, pairs, spectrum, kernel_numerators


def write_certificates(pairs, spectrum, kernel_numerators):
    root = pathlib.Path(__file__).parent
    with (root/'support_masks.csv').open('w', newline='', encoding='utf8') as f:
        wr = csv.writer(f, lineterminator="\n")
        wr.writerow(('full_mask_16', 'upper_left_mask_9'))
        wr.writerows(pairs)
    with (root/'frequency_spectrum.csv').open('w',newline='',encoding='utf8') as f:
        wr = csv.writer(f, lineterminator="\n")
        wr.writerow(('frequency_9', 'walsh_coefficient', 'fourier_projector_kernel_numerator'))
        for freq,(w,p) in enumerate(zip(spectrum,kernel_numerators)):
            wr.writerow((freq,w,p))


def check_certificates(pairs, spectrum, kernel_numerators):
    root = pathlib.Path(__file__).parent
    with (root/'support_masks.csv').open(newline='',encoding='utf8') as f:
        r = csv.DictReader(f)
        assert [(int(t['full_mask_16']),int(t['upper_left_mask_9'])) for t in r] == pairs
    with (root/'frequency_spectrum.csv').open(newline='',encoding='utf8') as f:
        r = csv.DictReader(f)
        actual = [(int(t['frequency_9']),int(t['walsh_coefficient']),int(t['fourier_projector_kernel_numerator'])) for t in r]
    assert actual == [(u,w,p) for u,(w,p) in enumerate(zip(spectrum,kernel_numerators))]


def main():
    matrices, pairs, spectrum, kernel = compute()
    if '--write' in sys.argv:
        write_certificates(pairs,spectrum,kernel)
    check_certificates(pairs,spectrum,kernel)
    print('ASM4_WALSH_PROJECTION_EXACT_PASS asms=42 quotient=512 zeros=120 rank=50176 lambda=199/32 ambient_checks=65536')

if __name__ == '__main__':
    main()
