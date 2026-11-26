#!/usr/bin/env python3
"""Reproduce finite modular checks for weighted ordered-partition polynomials."""
from math import comb, factorial


def vp(z, p):
    if z == 0:
        return 10**9
    count = 0
    while z % p == 0:
        z //= p
        count += 1
    return count


def is_prime(p):
    return p > 1 and all(p % d for d in range(2, int(p**0.5) + 1))


def has_full_order_two(p):
    if not is_prime(p):
        return False
    phi = p * (p - 1)
    return all(pow(2, phi // d, p * p) != 1 for d in range(2, phi + 1) if phi % d == 0 and is_prime(d))


def values_by_first_block(N, t, mod):
    out = [1]
    for n in range(1, N + 1):
        out.append(t * sum(comb(n, i) * out[n - i] for i in range(1, n + 1)) % mod)
    return out


def value_by_stirling(n, t):
    S = [1]
    for m in range(1, n + 1):
        nxt = [0] * (m + 1)
        for j in range(1, m + 1):
            nxt[j] = (j * S[j] if j < len(S) else 0) + S[j - 1]
        S = nxt
    return sum(factorial(j) * S[j] * t**j for j in range(len(S)))


def proper_divisors(q):
    return [d for d in range(1, q) if q % d == 0]


def main():
    primes = (3, 5, 11, 13)
    qs = (2, 4, 6, 8, 10, 12, 18, 20, 24, 30, 36, 40, 50, 60, 72, 90, 100, 110, 120)
    checks = 0
    comparisons = 0
    period_checks = 0
    expansion_checks = 0
    for p in primes:
        assert has_full_order_two(p)
        for t in (p - 1, 2*p - 1, p*p - 1):
            h = t + 1
            s = vp(h, p)
            mod = p**13
            seq = values_by_first_block(310, t, mod)
            for n in range(19):
                assert seq[n] == value_by_stirling(n, t) % mod
                comparisons += 1
            small_mod = p**7
            for n in (0, 1, 2, 3, 7, 11, 23, 31, 43):
                cutoff = 7 // s + 3
                expansion = sum((-1)**(n+b-1) * pow(h, b-1, small_mod)
                                * pow(1-h, -b, small_mod) * pow(b, n, small_mod)
                                for b in range(1, cutoff)) % small_mod
                assert expansion == seq[n] % small_mod, (p,t,n)
                expansion_checks += 1
            for q in qs:
                ell = vp(pow(2, q) - 1, p)
                for n in (s + ell + 1, s + ell + 2, 9, 17, 37, 72, 110):
                    if n < s + ell + 1 or n + q > 310:
                        continue
                    observed = vp((seq[n+q] - seq[n]) % mod, p)
                    assert observed == s + ell, (p,t,q,n,observed,s+ell)
                    checks += 1
            for a in range(1, 6):
                predicted = 2 if a <= s else (p-1)*p**(a-s-1)
                if predicted > 120:
                    continue
                start = max(12, a + 2)
                period_checks += 1
                smallmod = p**a
                assert all((seq[n+predicted] - seq[n]) % smallmod == 0 for n in range(start, 190))
                for d in proper_divisors(predicted):
                    assert any((seq[n+d]-seq[n]) % smallmod != 0 for n in range(start, 190)), (p,t,a,d)
    print(f'VERIFY_OK: {comparisons} independent Stirling/first-block comparisons; '
          f'{expansion_checks} p-adic moment expansion comparisons; '
          f'{checks} sharp valuations of even shifts; '
          f'{period_checks} prime-power period and proper-divisor tests')


if __name__ == '__main__':
    main()
