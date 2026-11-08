#!/usr/bin/env python3
"""Exact verification of the cyclic-pair-probability digit-block spectrum."""
from fractions import Fraction
from itertools import product
from collections import defaultdict


def partitions(n, cap=None):
    if n == 0:
        yield ()
    else:
        for k in range(min(n, cap if cap is not None else n), 0, -1):
            for tail in partitions(n-k, k):
                yield (k,) + tail


def numerator_and_probability(lam, p):
    n = sum(lam)
    s_old = 0
    total = 1
    m = max(lam)
    for j in range(1, m + 1):
        s = sum(min(x, j) for x in lam)
        c = (p**s - p**s_old) // (p**j - p**(j-1))
        assert c * (p**j - p**(j-1)) == p**s - p**s_old
        total += c * (p**(2*j) - p**(2*j-2))
        s_old = s
    return total, Fraction(total, p**(2*n))


def decode_probability(q, p):
    """Recover the partition when the prime is known; None means outside spectrum."""
    den = q.denominator
    a = 0
    while den > 1 and den % p == 0:
        den //= p
        a += 1
    if den != 1 or a < 3 or a % 2 == 0:
        return None
    n = (a + 1) // 2
    N = q * p**(2*n)
    if N.denominator != 1 or (N.numerator-1) % (p+1):
        return None
    T = (N.numerator-1)//(p+1)
    if T <= 0:
        return None
    digits = []
    while T:
        digits.append(T % p)
        T //= p
    lengths = []
    i = 0
    while i < len(digits):
        j = i
        while j < len(digits) and digits[j] == p-1:
            j += 1
        if j == i:
            return None
        lengths.append(j-i)
        if j == len(digits):
            break
        if digits[j] != 0 or j+1 == len(digits):
            return None
        i = j+1
    if lengths[0] < 2 or sum(lengths) != n:
        return None
    if any(lengths[k] < lengths[k+1] for k in range(len(lengths)-1)):
        return None
    lam = tuple(sum(a >= t for a in lengths) for t in range(1,lengths[0]+1))
    if numerator_and_probability(lam,p)[1] != q:
        return None
    return lam


def direct_probability(lam, p):
    moduli = tuple(p**a for a in lam)
    elements = list(product(*(range(m) for m in moduli)))
    multiples = {}
    for a in elements:
        zero = tuple(0 for _ in moduli)
        z = zero
        orbit = set()
        while z not in orbit:
            orbit.add(z)
            z = tuple((z[i] + a[i]) % moduli[i] for i in range(len(moduli)))
        multiples[a] = orbit
    count = sum((b in multiples[a]) or (a in multiples[b]) for a in elements for b in elements)
    return Fraction(count,len(elements)**2)


def run():
    cases = 0
    distinct = 0
    for p, nmax in ((2,20),(3,14),(5,12)):
        for n in range(2,nmax+1):
            seen = {}
            for lam in partitions(n):
                N, q = numerator_and_probability(lam,p)
                if len(lam) == 1:
                    assert q == 1
                    continue
                r = [sum(a >= j for a in lam) for j in range(1,max(lam)+1)]
                s = 0
                T = 0
                for j, z in enumerate(r,1):
                    T += p**(j-1+s)*(p**z-1)
                    s += z
                assert 1+(p+1)*T == N
                assert N % (p*p) == (-p) % (p*p)
                assert q.denominator == p**(2*n-1)
                assert decode_probability(q,p) == lam
                assert q not in seen, (p,n,lam,seen[q])
                seen[q]=lam
                cases += 1
            distinct += len(seen)
    brute_cases = 0
    for p, nmax in ((2,6),(3,4)):
        for n in range(1,nmax+1):
            for lam in partitions(n):
                _, q = numerator_and_probability(lam,p)
                assert direct_probability(lam,p) == q, (p,lam)
                brute_cases += 1
    assert decode_probability(Fraction(5,8),2) == (1,1)
    assert decode_probability(Fraction(17,32),2) == (2,1)
    assert decode_probability(Fraction(1,2),2) is None
    assert decode_probability(Fraction(1,1),2) is None
    print('PARTITION_CASES',cases)
    print('DISTINCT_CASES',distinct)
    print('BRUTE_GROUP_CASES',brute_cases)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
