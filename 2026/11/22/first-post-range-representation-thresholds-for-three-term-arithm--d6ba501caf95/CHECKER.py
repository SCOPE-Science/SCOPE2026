"""Standalone finite regression test for the first post-range arithmetic triple.

This is not a proof of the universal theorem. Run with Python 3:
    python3 CHECKER.py
"""
from math import gcd


def threshold(a, d, t):
    return a * (a + d + (t % 2 if a % 2 == 0 else 0)) + d * t


def verify_pair(a, d):
    assert a >= 3 and d >= 3 and gcd(a, d) == 1
    p = a // 2 + 1
    thresholds = [threshold(a, d, t) for t in range(a)]
    limit = max(thresholds) + a
    counts = [0] * (limit + 1)
    counts[0] = 1
    # Three independent unbounded-coin updates compute the exact denumerant.
    for coin in (a, a + d, a + 2 * d):
        for n in range(coin, limit + 1):
            counts[n] += counts[n - coin]
    assert len({v % a for v in thresholds}) == a
    assert all(counts[v] == p + 1 and counts[v - a] == p
               for v in thresholds)
    assert all(counts[n] > p for n in range(max(thresholds), limit + 1))
    observed_g = max(n for n, count in enumerate(counts) if count <= p)
    observed_genus = sum(count <= p for count in counts)
    g = (a * (a - 1) + (2 * a - 1) * d if a % 2
         else a * a + (2 * a - 1) * d)
    genus = a * (a + d) + (a - 1) * (d - 1) // 2
    if a % 2 == 0:
        genus += a // 2
    assert (observed_g, observed_genus) == (g, genus), (
        a, d, (observed_g, observed_genus), (g, genus))
    return len(thresholds)



def verify_pair_count_lemma():
    tests = 0
    for u in range(30):
        for v in range(-2, 2 * u + 3):
            direct = sum(1 for x in range(u + 1)
                         for y in range(u - x + 1)
                         if y + 2 * (u - x - y) == v)
            expected = (1 + min(v, 2 * u - v) // 2
                        if 0 <= v <= 2 * u else 0)
            assert direct == expected, (u, v, direct, expected)
            tests += 1
    return tests

def main():
    lemma_tests = verify_pair_count_lemma()
    cases = 0
    residues = 0
    for a in range(3, 122):
        for d in range(3, 20):
            if gcd(a, d) == 1:
                residues += verify_pair(a, d)
                cases += 1
    print("PASS: %d parameter pairs; %d threshold residues; "
          "all exact Frobenius and genus counts; %d pair-count lemma tests" % (cases, residues, lemma_tests))


if __name__ == "__main__":
    main()
