#!/usr/bin/env python3
"""Independent finite checks of the exact quadratic-gap polynomial identity."""
from collections import Counter


def quadratic_partition_polynomial(k):
    """Return degree -> multiplicity for Q_k(z) by direct integer compositions."""
    assert k >= 1
    out = Counter()
    for t in range(2, k + 2):
        weights = [j * (t - j) for j in range(1, t)]

        def rec(j, remainder, number_of_ones):
            if j == len(weights):
                if remainder == 0:
                    out[t + number_of_ones] += 1
                return
            weight = weights[j]
            for count in range(remainder // weight + 1):
                rec(j + 1, remainder - count * weight, number_of_ones + count)

        rec(0, k, 0)
    return out


def predicted(n, poly):
    return sum(multiplicity * max(n - length + 1, 0)
               for length, multiplicity in poly.items())


def scan_subsequence_frequency(bits, n):
    """Count 010 directly, scanning the letters left-to-right."""
    zero_count = pair_count = triple_count = 0
    for index in range(n):
        if (bits >> index) & 1:
            pair_count += zero_count
        else:
            triple_count += pair_count
            zero_count += 1
    return triple_count


def test():
    polynomials = {k: quadratic_partition_polynomial(k) for k in range(1, 41)}
    for k, poly in polynomials.items():
        assert max(poly) == k + 2
        assert poly[k + 2] == (1 if k == 1 else 3)
        slope = sum(poly.values())
        derivative = sum(degree * count for degree, count in poly.items())
        assert slope >= 1
        n = k + 1
        assert predicted(n, poly) == (n + 1) * slope - derivative
        assert predicted(k, poly) - ((k + 1) * slope - derivative) == (1 if k == 1 else 3)
    for n in range(15):
        frequency = Counter(scan_subsequence_frequency(w, n) for w in range(1 << n))
        for k in range(1, 41):
            assert predicted(n, polynomials[k]) == frequency[k], (n, k)
        assert frequency[0] == 1 + n * (n + 1) // 2
    sample = [(k, sum(polynomials[k].values()),
               sum((length-1)*count for length,count in polynomials[k].items()))
              for k in range(1, 13)]
    assert sample == [
        (1, 1, 2), (2, 3, 9), (3, 3, 12), (4, 7, 31),
        (5, 3, 18), (6, 12, 66), (7, 5, 34), (8, 14, 92),
        (9, 8, 60), (10, 21, 152), (11, 5, 48), (12, 30, 236)]
    print('PASS: brute force at all binary lengths n=0,...,14, frequencies k=1,...,40')
    print('PASS: polynomial degrees, top multiplicities and sharp thresholds k=1,...,40')
    print('PASS: 12 leading slopes and intercepts')


if __name__ == '__main__':
    test()
