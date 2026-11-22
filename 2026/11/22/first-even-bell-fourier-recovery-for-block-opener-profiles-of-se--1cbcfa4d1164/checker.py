"""Exact integer certificate for the Fourier spectrum of partition block openers.

Usage: python3 checker.py certificate.json
Requires only Python's standard library. No external data or imports.
"""
import json
import sys
from fractions import Fraction


def opener_histogram_formula(n):
    result = []
    for mask in range(1 << (n-1)):
        blocks, count = 1, 1
        for pos in range(2, n+1):
            if mask & (1 << (pos-2)):
                blocks += 1
            else:
                count *= blocks
        result.append(count)
    return result


def opener_histogram_enumeration(n):
    hist = [0] * (1 << (n-1))
    def visit(pos, maximum, mask):
        if pos == n:
            hist[mask] += 1
            return
        for value in range(maximum+2):
            next_mask = mask | ((1 << (pos-1)) if value == maximum+1 else 0)
            visit(pos+1, max(maximum, value), next_mask)
    visit(1, 0, 0)
    return hist


def integer_walsh(values):
    out = values[:]
    h = 1
    while h < len(out):
        for base in range(0, len(out), 2*h):
            for j in range(base, base+h):
                a, b = out[j], out[j+h]
                out[j], out[j+h] = a+b, a-b
        h *= 2
    return out


def direct_walsh(hist, mask):
    return sum(count * (-1 if (index & mask).bit_count() % 2 else 1)
               for index, count in enumerate(hist))


def verify(cert):
    assertions = 0
    for n in range(1, 9):
        h_formula = opener_histogram_formula(n)
        h_enum = opener_histogram_enumeration(n)
        assert h_formula == h_enum
        assertions += len(h_formula)
        assert h_formula == cert['histograms'][str(n)]
        assertions += 1
        spec = integer_walsh(h_formula)
        assert spec == cert['spectra'][str(n)]
        assertions += 1
        for a in range(1 << (n-1)):
            assert spec[a] == direct_walsh(h_enum, a)
            assertions += 1
        # The first vertex is always a block opener, so both full-cube
        # Fourier values over the first coordinate are opposite signs.
        assert sum(h_formula) == cert['bell_numbers'][str(n)]
        assertions += 1
    for n in range(1, 9):
        vals = cert['spectra'][str(n)]
        zeros = [i for i, v in enumerate(vals) if not v]
        assert zeros == cert['zero_frequency_masks'][str(n)]
        assertions += 1
        gap = min(abs(v) for v in vals if v)
        assert gap == cert['least_nonzero_magnitude'][str(n)]
        assertions += 1
    assert cert['least_nonzero_magnitude']['8'] == 8
    assert [a for a, v in enumerate(cert['spectra']['8']) if abs(v) == 8] == [4,54,111,122]
    assert cert['zero_frequency_masks']['5'] == [7]
    assert cert['zero_frequency_masks']['2'] == [1]
    assert cert['bell_numbers']['8'] == 4140
    # Complete exact Fourier idempotent for the fifth-order range.
    zeros = [(7 << 1), (7 << 1) | 1]
    kernel = []
    for x in range(32):
        q = Fraction(int(x == 0), 1)
        q -= sum(Fraction((-1 if (a & x).bit_count() % 2 else 1), 32)
                 for a in zeros)
        kernel.append(q)
    assert sum(map(abs, kernel), Fraction(0)) == Fraction(15, 8)
    assert kernel[0] == Fraction(15, 16)
    assert sum(v != 0 for v in kernel) == 16
    assertions += 8
    print('PASS: %d exact tests, including independent restricted-growth enumeration, direct character sums and Walsh butterflies.' % assertions)

if __name__ == '__main__':
    with open(sys.argv[1] if len(sys.argv)>1 else 'certificate.json', encoding='utf-8') as fh:
        cert = json.load(fh)
    verify(cert)
