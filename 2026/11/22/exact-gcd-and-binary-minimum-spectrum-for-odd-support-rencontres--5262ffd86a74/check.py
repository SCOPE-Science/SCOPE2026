"""Exact diagnostic checks for the odd-moved rencontres-row theorem."""
from math import comb, gcd


def vp(x, p):
    if x == 0:
        raise ValueError('positive integers only')
    count = 0
    while x % p == 0:
        x //= p
        count += 1
    return count


def odd_prime_power(n):
    for p in range(3, n + 1, 2):
        if any(p % q == 0 for q in range(2, int(p ** .5) + 1)):
            continue
        t = n
        while t % p == 0:
            t //= p
        if t == 1:
            return p
    return 1


def expected(n):
    twopow = n * (n - 1) * (n - 2)
    while twopow % 2 == 0:
        twopow //= 2
    return n * (n - 1) * (n - 2) // twopow * odd_prime_power(n)


def digit_popcount(n):
    return n.bit_count()


def check():
    count = 0
    d = [1, 0]
    for n in range(2, 241):
        d.append(n * d[-1] + (-1) ** n)
    for m in range(3, 241, 2):
        assert vp(d[m], 2) == vp(m - 1, 2)
        count += 1
    for n in range(4, 241):
        g = 0
        targets = []
        N = n - 3
        common = vp(n * (n - 1) * (n - 2), 2)
        for m in range(3, n, 2):
            t = comb(n, m) * d[m]
            assert vp(t, 2) == common + vp(comb(n - 3, m - 3), 2), (n, m)
            g = gcd(g, t)
            if vp(t, 2) == common:
                targets.append(m)
            count += 1
        assert g == expected(n), (n, g, expected(n))
        count += 1
        ecount = (1 << (digit_popcount(N) - 1)) if n % 2 == 0 else (1 << digit_popcount(N)) - 1
        assert len(targets) == ecount, (n, targets, ecount)
        count += 1
    # Independently test congruence for all primes through 151 on every odd column.
    primes = [p for p in range(3, 152, 2) if all(p%q for q in range(2, int(p ** .5)+1))]
    for n in range(4, 152):
        for p in primes:
            if p > n:
                continue
            actual = all((comb(n, m) * d[m]) % p == 0 for m in range(3, n, 2))
            expected_flag = odd_prime_power(n) == p
            assert actual == expected_flag, (n, p, actual, expected_flag)
            count += 1
    print(f'PASS: {count} exact assertions; all rows n=4..240 and prime-support checks n<=151.')


if __name__ == '__main__':
    check()
