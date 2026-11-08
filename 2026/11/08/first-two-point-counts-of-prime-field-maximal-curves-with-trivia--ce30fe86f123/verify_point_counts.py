#!/usr/bin/env python3
"""Exact finite-field spot checks for two initial point counts of an Artin-Schreier quotient curve.

No external packages required.  The proof for all odd primes and all n>=2
is in RESULT.md, not in these finite checks.
"""

def count_over_prime(p, n):
    total = 2  # the finite ramified point at u=0 and the unique point at infinity
    for u in range(p):
        rhs = (-1 - 2 * sum(pow(u, ((p ** (2 * i) - 1) // (2 * (p - 1))), p)
                              for i in range(1, n + 1))) % p
        total += sum((u * pow(v, p, p) + v - rhs) % p == 0 for v in range(p))
    return total


def first_nonsquare(p):
    return next(a for a in range(2, p) if pow(a, (p - 1)//2, p) == p - 1)


def count_over_quadratic(p, n):
    d = first_nonsquare(p)

    def mul(a, b):
        return ((a[0] * b[0] + d * a[1] * b[1]) % p,
                (a[0] * b[1] + a[1] * b[0]) % p)

    def power(a, exponent):
        answer = (1, 0)
        while exponent:
            if exponent & 1:
                answer = mul(answer, a)
            a = mul(a, a)
            exponent >>= 1
        return answer

    els = [(i, j) for i in range(p) for j in range(p)]
    total = 2  # points on the smooth model not visible in the affine (u,v)-chart
    for u in els:
        rhs = (p - 1, 0)
        for i in range(1, n + 1):
            exponent = (p ** (2 * i) - 1) // (2 * (p - 1))
            a = power(u, exponent)
            rhs = ((rhs[0] - 2 * a[0]) % p, (rhs[1] - 2 * a[1]) % p)
        for v in els:
            t = mul(u, power(v, p))
            if ((t[0] + v[0]) % p, (t[1] + v[1]) % p) == rhs:
                total += 1
    return total


def predicted(p, n):
    delta = int((2 * n + 1) % p == 0)
    return (p + 1 + p * delta * int(p % 4 == 3),
            p * p + 1 + p * (p - 1) // 2 * delta)


def main():
    examples = [(3, 2), (3, 4), (3, 5), (5, 2), (5, 3),
                (7, 2), (7, 3), (11, 2), (11, 5)]
    for p, n in examples:
        observed = count_over_prime(p, n), count_over_quadratic(p, n)
        expected = predicted(p, n)
        assert observed == expected, (p, n, observed, expected)
        print(f"CHECK_OK p={p} n={n} N1={observed[0]} N2={observed[1]}")
    print("ALL_EXACT_FIELD_CHECKS_OK")

if __name__ == "__main__":
    main()
