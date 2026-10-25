#!/usr/bin/env python3
"""Exact pair-overlap counts and numerical idempotence checks for the hypermatching Fourier projection."""
import itertools
import math
from collections import Counter
from fractions import Fraction


def partitions(values, block_size):
    if not values:
        yield ()
        return
    first = values[0]
    for tail in itertools.combinations(values[1:], block_size - 1):
        block = (first,) + tail
        remainder = tuple(x for x in values[1:] if x not in tail)
        for other in partitions(remainder, block_size):
            yield (block,) + other


def pair_flags(partition, pairs):
    block_of = {x: j for j, block in enumerate(partition) for x in block}
    return tuple(int(block_of[a] == block_of[b]) for a, b in pairs)


def case(n, k):
    N = n*k
    pairs = list(itertools.combinations(range(N), 2))
    parts = list(partitions(tuple(range(N)), k))
    expected_count = math.factorial(N) // (math.factorial(k)**n*math.factorial(n))
    assert len(parts) == expected_count
    m = n*math.comb(k, 2)
    p = Fraction(k-1, N-1)
    mu = m*p
    d = N*(N-3)//2
    flags = [pair_flags(x, pairs) for x in parts]
    s_values = [sum(a*b for a,b in zip(flags[0], row)) for row in flags]
    frequency = Counter(s_values)
    assert sum(frequency.values()) == len(parts)
    assert sum(s*count for s,count in frequency.items()) == len(parts)*mu
    exact_norm = sum(abs(Fraction(s)-mu)*count for s,count in frequency.items())*Fraction(d, len(parts)*(m-mu))
    if len(parts) <= 280:
        try:
            import numpy as np
        except ImportError:
            raise RuntimeError('NumPy is required for the direct projector check')
        mat = np.asarray(flags, dtype=float)
        gram = mat @ mat.T
        projector = d/(m-float(mu))*(gram-float(mu))/len(parts)
        assert abs(np.trace(projector)-d) < 1e-9
        assert np.max(np.abs(projector @ projector-projector)) < 1e-9
        assert abs(np.max(np.sum(np.abs(projector),axis=1))-float(exact_norm)) < 1e-9
    return len(parts), exact_norm


def main():
    for n,k in ((2,3),(2,4),(3,3),(4,2),(4,3)):
        count, norm = case(n,k)
        print(f'n={n} k={k} partitions={count} endpoint_norm={norm} ({float(norm):.10f})')
    from math import exp, factorial, pi
    for k in (2,3,4,5,7,12,24,48):
        lam = (k-1)**2/2
        a = (k-1)*exp(-lam+math.floor(lam)*math.log(lam)-math.lgamma(math.floor(lam)+1))
        print(f'k={k} asymptotic_norm_divided_by_N={a:.10f}')
    print(f'iterated_k_limit={1/math.sqrt(pi):.10f}')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
