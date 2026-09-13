"""Lane 1667 bounded recovery census (supports CLEAN_EXIT, proves nothing asymptotic).

For primes p = 1 mod 4 up to 1e6: H = isqrt(p), S_p = sum_{n<=H} legendre(n,p)
via Euler's criterion. Reports max of |S_p|/p^{1/4} and record holders.
Run: python3 census.py  (needs only stdlib; ~minutes for full range)
"""
import math


def primes_1mod4(a, b):
    sieve = bytearray(b"\x01") * (b - a)
    for q in range(2, int(b ** 0.5) + 1):
        s = max(q * q, ((a + q - 1) // q) * q)
        for j in range(s, b, q):
            sieve[j - a] = 0
    return [i for i, v in enumerate(sieve, a) if v and i > 1 and i % 4 == 1]


def leg(n, p):
    return -1 if pow(n, (p - 1) // 2, p) == p - 1 else 1


def main(lo=10 ** 5, hi=10 ** 6):
    best = (0.0, None, None)
    worst_neg = (0.0, None)
    zeros = 0
    over4 = 0
    tot = 0
    for p in primes_1mod4(lo, hi):
        tot += 1
        H = math.isqrt(p)
        s = sum(leg(n, p) for n in range(1, H + 1))
        r = s / p ** 0.25
        if s == 0:
            zeros += 1
        if abs(r) > 4.0:
            over4 += 1
        if r > best[0]:
            best = (r, p, s)
        if r < worst_neg[0]:
            worst_neg = (r, p)
    print("primes:", tot, "zeros:", zeros, "frac(|S|/p^1/4>4):", over4 / tot)
    print("max ratio S/p^1/4:", best)
    print("min ratio:", worst_neg)


if __name__ == "__main__":
    main(500000, 1000000)
