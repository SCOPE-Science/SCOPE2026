"""Exact finite-field checks for the Gold-graph Gabor tomography spectrum.

Run: python3 verify.py. Uses Python's standard library only. Finite tests
supplement, and do not replace, the all-degree mathematical argument.
"""
from collections import Counter
from math import gcd, isqrt

POLY = {2: 0x7, 3: 0xB, 4: 0x13, 5: 0x25, 6: 0x43}


def multiplication(x, y, q, modulus):
    value = 0
    while y:
        if y & 1:
            value ^= x
        y >>= 1
        x <<= 1
        if x & q:
            x ^= modulus
    return value


def predicted(m):
    q = 1 << m
    out = Counter()
    out[2] += (q - 1) * q**3 // 4
    out[q] += 1
    if m & 1:
        out[isqrt(2 * q)] += q * (q - 1) // 2
    else:
        out[isqrt(q)] += 2 * q * (q - 1) // 3
        out[2 * isqrt(q)] += q * (q - 1) // 12
    out[0] = q**4 - sum(out.values())
    return out


def verify(m, k, full):
    assert gcd(m, k) == 1 and 2 <= m <= 6
    q, modulus = 1 << m, POLY[m]
    mult = [[multiplication(x, y, q, modulus) for y in range(q)] for x in range(q)]

    def power(x, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = mult[result][x]
            x = mult[x][x]
            exponent >>= 1
        return result

    def tr(x):
        total = 0
        for _ in range(m):
            total ^= x
            x = mult[x][x]
        assert total in (0, 1)
        return total

    f = [power(x, (1 << k) + 1) for x in range(q)]
    signs = [[1 - 2 * tr(mult[u][x]) for x in range(q)] for u in range(q)]
    observed = Counter()
    if full:
        for a in range(q):
            for b in range(q):
                fiber = [x for x in range(q) if f[x] ^ f[x ^ a] == b]
                for u in range(q):
                    for v in range(q):
                        observed[abs(sum(signs[u][x] * signs[v][f[x]] for x in fiber))] += 1
    else:
        # Directly enumerate every zero-translation Walsh coefficient, and
        # separately verify every differential fiber has size zero or two.
        for a in range(1, q):
            frequencies = Counter(f[x] ^ f[x ^ a] for x in range(q))
            assert len(frequencies) == q // 2
            assert set(frequencies.values()) == {2}
        for u in range(q):
            for v in range(q):
                observed[abs(sum(signs[u][x] * signs[v][f[x]] for x in range(q)))] += 1
        observed[2] += (q - 1) * q**3 // 4
        observed[0] += q**4 - q**2 - (q - 1) * q**3 // 4
    assert observed == predicted(m), (m, k, observed, predicted(m))
    print(f'm={m} k={k} q={q} full={str(full).lower()}'
          f' nonzero_rank={q**4 - observed[0]} bands={dict(sorted(observed.items()))} PASS')


def main():
    for m in range(2, 7):
        test_k = [1] if m == 6 else [k for k in range(1, m) if gcd(k, m) == 1]
        for k in test_k:
            verify(m, k, full=(m <= 5))
    print('ALL CHECKS PASSED: exhaustive character sums for m=2..5;'
          ' full zero-translation spectrum and all derivative fibers for m=6.')


if __name__ == '__main__':
    main()
