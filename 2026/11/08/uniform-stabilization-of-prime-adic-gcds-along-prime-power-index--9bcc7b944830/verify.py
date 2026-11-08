#!/usr/bin/env python3
"""Independent finite checks for the prime-power binomial-gcd stabilization theorem.
No finite search establishes the infinite theorem; see RESULT.md for its proof.
"""
from math import comb, gcd


def vp(x, p):
    count = 0
    while x % p == 0:
        count += 1
        x //= p
    return count


def digit_sum(n, p):
    total = 0
    while n:
        total += n % p
        n //= p
    return total


def legendre(n, p):
    count = 0
    while n:
        n //= p
        count += n
    return count


def min_valuation(m, p, a):
    n = p ** a
    t = m * n
    t_factorial = legendre(t, p)
    return min(t_factorial - legendre(m * k, p) - legendre(t-m*k, p)
               for k in range(1, n))


def cutoff(m, p):
    u = m
    while u % p == 0:
        u //= p
    c = digit_sum((p-1)*u, p) // (p-1)
    return max(1, c - 1)


def checks():
    direct = 0
    for p in (2, 3, 5):
        for m in range(1, 30):
            for a in range(1, 5):
                n = p ** a
                if n > 81 or m*n > 1100:
                    continue
                # Independent direct gcd of full binomial integers.
                g = 0
                for k in range(1, n):
                    g = gcd(g, comb(m*n, m*k))
                x = vp(g, p)
                assert x == min_valuation(m, p, a), (p,m,a,'direct')
                direct += 1
    print('DIRECT_BINOMIAL_GCD_OK', direct)

    wide = 0
    for p, mlimit, alimit in ((2, 320, 9), (3, 150, 6), (5, 100, 5), (7, 55, 4)):
        for m in range(1, mlimit + 1):
            r = cutoff(m, p)
            if p ** alimit > 1100:
                lim = 4
            else:
                lim = alimit
            ref = min_valuation(m, p, min(lim, r))
            for a in range(1, lim + 1):
                observed = min_valuation(m, p, a)
                expected = min_valuation(m, p, min(a, r))
                assert observed == expected, (p, m, a, r, observed, expected)
                assert observed >= 1
                wide += 1
            if r <= lim:
                assert min_valuation(m,p,lim)==ref
    print('VALUATION_STABILIZATION_OK', wide)

    # Independent Kummer carry count against factorial arithmetic.
    carries = 0
    for p in (2,3,5,7):
        for m in range(1,36):
            for a in (1,2,3):
                n=m*p**a
                for k in range(1,p**a):
                    x=m*k
                    y=n-x
                    s=0; carry=0
                    while x or y or carry:
                        x,r=divmod(x,p)
                        y,t=divmod(y,p)
                        carry=(r+t+carry)//p
                        s+=carry
                    assert s==legendre(n,p)-legendre(m*k,p)-legendre(m*(p**a-k),p)
                    carries += 1
    print('KUMMER_CARRY_REPLAY_OK', carries)

    assert [min_valuation(11,2,a) for a in range(1,6)] == [3,2,2,2,2]
    assert [min_valuation(39,2,a) for a in range(1,6)] == [4,4,3,3,3]
    print('NONTRIVIAL_LATE_DROP_OK', 'm=11', 'm=39')
    print('VERIFY_OK finite_checks_only=True independent_audit=False')

if __name__=='__main__':
    checks()
