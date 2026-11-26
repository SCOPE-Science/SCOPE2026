"""Exact finite cross-checks for the second phase of three-coin p-Frobenius numbers.
The all-parameter theorem follows from the written proof, not these checks.
"""
from math import gcd


def count_by_residue(N, a, d):
    """Independently evaluate the finite (s,t) lattice-point formula."""
    if N < 0:
        return 0
    s0 = (N * pow(d, -1, a)) % a
    m = (N - d * s0) // a
    total = 0
    for k in range(max(0, m // d + 1)):
        s, t = s0 + a * k, m - d * k
        total += max(0, s // 2 - max(0, s - t) + 1)
    return total


def count_by_dynamic_programming(limit, a, d):
    counts = [0] * (limit + 1)
    counts[0] = 1
    for coin in (a, a + d, a + 2 * d):
        for n in range(coin, limit + 1):
            counts[n] += counts[n - coin]
    return counts


def candidate(a, d, p):
    h = (a - 1) // 2
    return a * (a + d + p - h - 2) + d * (a - 1)


def main():
    parameter_cases = 0
    residue_comparisons = 0
    dp_comparisons = 0
    all_small = 0
    for a in range(3, 84, 2):
        h = (a - 1) // 2
        for d in range(1, h + 1):
            if gcd(a, d) != 1:
                continue
            for p in range(h + 1, a + d + 1):
                g = candidate(a, d, p)
                assert count_by_residue(g, a, d) == p, (a, d, p, g)
                for t in range(1, a + 1):
                    assert count_by_residue(g + t, a, d) >= p + 1, (a, d, p, t)
                    residue_comparisons += 1
                parameter_cases += 1
                if a <= 21:
                    counts = count_by_dynamic_programming(g + a, a, d)
                    assert counts[g] == p
                    assert all(counts[g + t] > p for t in range(1, a + 1))
                    for n in range(g + a + 1):
                        assert counts[n] == count_by_residue(n, a, d), (a, d, p, n)
                        dp_comparisons += 1
                    all_small += 1
    a, d, p = 5, 3, 8
    counts = count_by_dynamic_programming(100, a, d)
    actual = max(n for n, val in enumerate(counts) if val <= p)
    assert candidate(a, d, p) == 72 and actual == 74
    print('PASS: parameter triples:', parameter_cases)
    print('PASS: successor-residue inequalities:', residue_comparisons)
    print('PASS: independent dynamic-programming/lattice comparisons:', dp_comparisons)
    print('PASS: complete small-case parameter triples:', all_small)
    print('PASS: outside-domain boundary sample (5,3,p=8): predicted 72, actual 74')


if __name__ == '__main__':
    main()
