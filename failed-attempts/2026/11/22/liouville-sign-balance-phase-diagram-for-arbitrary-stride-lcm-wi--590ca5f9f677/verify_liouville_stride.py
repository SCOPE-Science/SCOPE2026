#!/usr/bin/env python3
"""Exact independent finite checks of a Liouville sign-balance theorem.

Only Python's standard library is needed. The proof of the theorem is separate.
"""
from fractions import Fraction
from math import gcd, lcm


def factor(n):
    ans = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            ans[p] = ans.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def valuation(n, p):
    t = 0
    while n % p == 0:
        n //= p
        t += 1
    return t


def liouville(n):
    return -1 if sum(factor(n).values()) % 2 else 1


def direct_sign(k, c, n):
    terms = [n + i*c for i in range(k + 1)]
    prod = 1
    least = 1
    for x in terms:
        prod *= x
        least = lcm(least, x)
    assert prod % least == 0
    return liouville(prod // least)


def local_sign(k, c, n, p):
    exponents = [valuation(n + i*c, p) for i in range(k + 1)]
    return -1 if (sum(exponents) - max(exponents)) % 2 else 1


def base_means(N):
    # m_t: mean for a window of t consecutive integers at prime 2.
    m = [Fraction(0), Fraction(1), Fraction(1)]
    for t in range(3, N + 1):
        if t % 2 == 0:
            u = t // 2
            m.append((-1) ** (u-1) * m[u])
        else:
            u = t // 2
            m.append(Fraction((-1)**u, 2) * (m[u+1]-m[u]))
    return m


def binary_mean(k, e, means):
    t = k + 1
    if e == 0:
        return means[t]
    if k % 2 == 0:
        return Fraction(1) - Fraction(1, 2**e) + means[t] / (2**e)
    return (Fraction(1, 3) * (1 - Fraction(-1, 2)**e)
            + Fraction(-1, 2)**e * means[t])


def predicts_balance(k, e):
    t = k + 1
    if e == 0:
        while t % 2 == 0:
            t //= 2
        return t == 3
    if e == 1:
        return t.bit_count() == 1 and (t.bit_length() - 1) % 2 == 1
    if e == 2:
        return t.bit_count() == 1 and (t.bit_length() - 1) % 2 == 0
    return False


def main():
    assertions = 0
    means = base_means(2000)
    for t in range(2, 2000):
        assert (abs(means[t]) == 1) == (t & (t - 1) == 0)
        if t >= 3:
            assert means[t] != means[t + 1]
        assertions += 1
    for k in range(1, 2000):
        for e in range(0, 8):
            z = binary_mean(k, e, means)
            assert (z == 0) == predicts_balance(k, e), (k,e,z)
            assertions += 1

    # Independent local enumeration, including odd units in the step.
    for k in range(1, 75):
        h = (k.bit_length() - 1)
        for e in range(5):
            q = 1 << (e+h)
            for odd in (1, 3, 5):
                c = (1 << e) * odd
                # Choose n in [q, 2q) to avoid any zero term.
                observed = Fraction(sum(local_sign(k,c,n,2)
                        for n in range(q,2*q)),q)
                target = binary_mean(k,e,means)
                assert observed == target, (k,c,q,observed,target)
                assertions += 1

    # Direct integer product/LCM and prime-factor sign, not merely parity counts.
    for k in range(1, 9):
        L = 1
        for j in range(1,k+1):
            L = lcm(L,j)
        for c in range(1, 13):
            period = c * L
            primes = list(factor(period))
            signs = []
            for n in range(1,period+1):
                sign = direct_sign(k,c,n)
                assert sign == __import__('math').prod(local_sign(k,c,n,p) for p in primes)
                signs.append(sign)
                assertions += 1
            local_means = []
            for p in primes:
                h = 0
                while p**(h+1) <= k:
                    h += 1
                q = p**(valuation(c,p)+h)
                s = sum(local_sign(k,c,n,p) for n in range(q,2*q))
                local_means.append(Fraction(s,q))
                if p != 2:
                    assert s % 2 != 0
                assertions += 1
            mean = Fraction(sum(signs),period)
            product_mean = __import__('math').prod(local_means)
            assert mean == product_mean, (k,c,mean,product_mean)
            assert (mean == 0) == predicts_balance(k,valuation(c,2))
            assertions += 2

    print('LIOUVILLE_STRIDE_BALANCE_EXACT_CHECK_OK',assertions)


if __name__ == '__main__':
    main()
