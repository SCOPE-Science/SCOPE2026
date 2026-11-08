"""Independent finite checks for the Fermat-quotient pair-image theorem.

Run with Python 3: python verify.py
Finite checks corroborate; the theorem's generality comes from the proof.
"""
from collections import Counter
from math import comb, gcd


def phi(n):
    return sum(gcd(t, n) == 1 for t in range(1, n + 1))


def cutoff(p):
    # An integer-only version of ceil(log_p(8**phi(p-1))).
    bound = 8 ** phi(p - 1)
    k, power = 0, 1
    while power < bound:
        k, power = k + 1, power * p
    return k


def fibers(p, k, h=1):
    mod, target_mod = p ** (k + 1), p ** k
    counts = Counter()
    for n in range(mod):
        if n % p == 0 or (n + h) % p == 0:
            continue
        a = ((pow(n, p - 1, mod) - 1) % mod) // p
        b = ((pow(n + h, p - 1, mod) - 1) % mod) // p
        assert 0 <= a < target_mod and 0 <= b < target_mod
        counts[a, b] += 1
    return counts


def pair_point(p, k, r, s):
    mod = p ** (k + 1)
    w = {j: pow(j, p ** k, mod) for j in (r, s, r + 1, s + 1)}
    eta = w[r + 1] * pow(w[s + 1], -1, mod) % mod
    d = (w[r] - eta * w[s]) % mod
    assert d % p != 0
    u = (eta - 1) * pow(d, -1, mod) % mod
    v = (w[r] * u + 1) * pow(w[r + 1], -1, mod) % mod
    assert u % p == 1 and v % p == 1
    assert (w[s] * u + 1 - w[s + 1] * v) % mod == 0
    return (((pow(u, p - 1, mod) - 1) % mod) // p,
            ((pow(v, p - 1, mod) - 1) % mod) // p)


def check_one(p, k, h=1):
    counts = fibers(p, k, h)
    total = (p - 2) * p ** k
    assert sum(t * amount for t, amount in Counter(counts.values()).items()) == total
    if h == 1:
        # Every two residue components have exactly one common target.
        points = [pair_point(p, k, r, s)
                  for r in range(1, p - 1) for s in range(r + 1, p - 1)]
        assert all(counts[point] >= 2 for point in points)
        assert len(points) == comb(p - 2, 2)
    if k >= cutoff(p) or (k >= 2 and p <= 31):
        expected = Counter({1: total - 2 * comb(p - 2, 2),
                            2: comb(p - 2, 2)})
        expected = Counter({z: c for z, c in expected.items() if c != 0})
        assert Counter(counts.values()) == expected, (p, k, Counter(counts.values()), expected)
        assert len(counts) == total - comb(p - 2, 2)
    return len(counts)


def run():
    cases = [(3, 2), (5, 3), (7, 3), (11, 4), (13, 4),
             (17, 2), (19, 2), (23, 2), (29, 2), (31, 2)]
    for p, k in cases:
        check_one(p, k)
    assert Counter(fibers(11, 1).values()) == Counter({1: 36, 2: 27, 3: 3})
    # Shift rescaling: the count is invariant when p does not divide the shift.
    for p, k, h in [(5, 2, 2), (7, 2, 3), (11, 2, -2)]:
        shifted = fibers(p, k, h)
        assert Counter(shifted.values()) == Counter(fibers(p, k).values())
    print('VERIFY_OK prime_power_cases=10 shift_cases=3 triple_at_level_one_p11=3')


if __name__ == '__main__':
    run()
