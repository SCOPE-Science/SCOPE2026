"""Exact arithmetic checks for the square-pyramidal residue fiber theorem.

Run: python3 verify.py
This program checks finite cases; the unrestricted result uses the accompanying proof.
"""
from collections import Counter
from math import gcd


def S(n):
    return n * (n + 1) * (2 * n + 1) // 6


def primes_upto(bound):
    return [p for p in range(2, bound + 1) if p > 1 and all(p % q for q in range(2, int(p ** 0.5) + 1))]


def legendre(a, p):
    t = pow(a % p, (p - 1) // 2, p)
    return -1 if t == p - 1 else t


def expected_local(p, k):
    if p in (2, 3):
        return Counter({p: p ** k})
    eta = legendre(-3, p)
    c = 1 + legendre(3, p)
    triples = (p - eta - 3 * c) // 6
    singles = p - 3 * triples - 2 * c
    assert (p - eta - 3 * c) % 6 == 0
    h = Counter()
    h[3] = triples * p ** (k - 1)
    h[1] = singles * p ** (k - 1)
    branch = sum(((p - 1) // 2) * p ** (k - 2 * j - 1)
                 for j in range(1, (k - 1) // 2 + 1))
    h[1] += c * (p ** (k - 1) - 1 - branch)
    for j in range(1, (k - 1) // 2 + 1):
        h[1 + 2 * p ** j] += c * (p - 1) // 2 * p ** (k - 2 * j - 1)
    h[1 + p ** (k // 2)] += c
    return +h


def actual_local(p, k):
    m = p ** k
    period = m * (p if p in (2, 3) else 1)
    bins = Counter(S(n) % m for n in range(period))
    return Counter(bins.values()), bins


def expected_image_cardinality(mod):
    n = mod
    answer = mod
    for p in primes_upto(int(mod ** 0.5) + 1):
        if n % p:
            continue
        while n % p == 0:
            n //= p
        if p >= 5:
            answer = answer * (2 * p + legendre(-3, p)) // (3 * p)
    if n > 1:
        p = n
        if p >= 5:
            answer = answer * (2 * p + legendre(-3, p)) // (3 * p)
    return answer


def check():
    local_tests = 0
    local_targets = 0
    for p in primes_upto(43):
        k = 1
        while p ** k <= 60000:
            hist, bins = actual_local(p, k)
            predicted = expected_local(p, k)
            assert hist == predicted, (p, k, hist, predicted)
            assert sum(f * count for f, count in hist.items()) == p ** k * (p if p in (2, 3) else 1)
            assert len(bins) == (p ** k if p in (2, 3) else p ** (k - 1) * (2*p + legendre(-3,p))//3)
            local_tests += 1
            local_targets += p ** k
            k += 1
    total_mod = 0
    total_indices = 0
    for m in range(1, 301):
        period = m * gcd(m, 6)
        vals = [S(n) % m for n in range(2 * period)]
        assert vals[:period] == vals[period:]
        # Confirm no proper divisor is a period.
        for d in range(1, period):
            if period % d == 0:
                assert any(vals[n] != vals[n+d] for n in range(period))
        bins = Counter(vals[:period])
        assert len(bins) == expected_image_cardinality(m), (m, len(bins), expected_image_cardinality(m))
        total_mod += 1
        total_indices += period
    print('VERIFY_OK')
    print(f'local_tests={local_tests} local_domain_elements={local_targets}')
    print(f'global_moduli={total_mod} global_residue_indices={total_indices}')
    print('all_exact_integer_arithmetic=True')

if __name__ == '__main__':
    check()
