#!/usr/bin/env python3
"""Independent direct-DFT census of prime-power phase STFT support sizes.

No external packages. Normalizes each of f and g by its zeroth entry.
Usage: python verify.py
"""
from collections import Counter
from cmath import exp
from itertools import product
from math import pi


def census(p, q):
    phase = [exp(2j*pi*a/q) for a in range(q)]
    omega = [[exp(-2j*pi*k*t/p) for t in range(p)] for k in range(p)]
    sequences = [(0,) + a for a in product(range(q), repeat=p-1)]
    freq_counts = Counter()
    min_nonzero = float('inf')
    max_zero = 0.0
    for f in sequences:
        for g in sequences:
            support = 0
            for x in range(p):
                c = [phase[(f[t]-g[(t-x)%p])%q] for t in range(p)]
                for k in range(p):
                    amplitude = sum(c[t]*omega[k][t] for t in range(p))
                    absolute = abs(amplitude)
                    if absolute < 1e-8:
                        max_zero = max(max_zero, absolute)
                    else:
                        support += 1
                        min_nonzero = min(min_nonzero, absolute)
            freq_counts[support] += 1
    expected = Counter({
        p: 1,
        p*p-p+1: p*(q**(p-1)-1),
        p*p: q**(2*p-2)-1-p*(q**(p-1)-1)
    })
    assert freq_counts == expected, (p, q, freq_counts, expected)
    assert min_nonzero > 1e-5, (p, q, min_nonzero)
    assert max_zero < 1e-8, (p, q, max_zero)
    assert sum(freq_counts.values()) == q**(2*p-2)
    print(f'p={p}, q={q}: pairs={sum(freq_counts.values())}, '
          f'counts={dict(sorted(freq_counts.items()))}, '
          f'min_nonzero={min_nonzero:.8g}, max_zero={max_zero:.3g}')


if __name__ == '__main__':
    for parameters in [(2, 3), (3, 2), (3, 4), (5, 2), (5, 4)]:
        census(*parameters)
    print('PASS: all exhaustive direct-DFT checks.')
