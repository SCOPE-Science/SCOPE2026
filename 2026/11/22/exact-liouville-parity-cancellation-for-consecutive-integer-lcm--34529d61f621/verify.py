#!/usr/bin/env python3
"""Exact finite spot checks for the Liouville-sign mean of consecutive LCM quotients.

These tests are supplementary to the general mathematical proof.
"""
from math import gcd, lcm


def prime_list(bound):
    return [p for p in range(2, bound + 1) if all(p % d for d in range(2, int(p**0.5) + 1))]


def omega(n):
    s = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            s += 1
        d += 1
    return s + (n > 1)


def local_sign_sum(k, p):
    powers = []
    v = p
    while v <= k:
        powers.append(v)
        v *= p
    if not powers:
        return 1, 1
    m = powers[-1]
    t = sum((-1)**sum((n + k)//d - (n - 1)//d - 1 for d in powers)
            for n in range(m))
    return t, m


def s_direct(e, r):
    m = 2**e
    signs = [(-1)**(e if t == 0 else min(e, (t & -t).bit_length()-1))
             for t in range(m)]
    return sum(__import__('math').prod(signs[(t+i) % m] for i in range(r))
               for t in range(m))


def s_rec(e):
    vals = [2, 0, -2]
    for j in range(2, e+1):
        m = 2**j
        old = vals
        new = [None]*(m+1)
        for r in range(m+1):
            if r % 2 == 0:
                new[r] = 2*(-1)**(r//2)*old[r//2]
            else:
                h = r//2
                new[r] = (-1)**h*(old[h]-old[h+1])
        vals = new
    return vals


def checks():
    brute_cases = 0
    for k in range(1, 12):
        period = lcm(*range(1, k+1))
        actual = 0
        for n in range(1, period+1):
            product = 1
            least = 1
            for j in range(k+1):
                product *= n+j
                least = lcm(least, n+j)
            quotient = product//least
            actual += (-1)**omega(quotient)
            brute_cases += 1
        numerator, denominator = 1, 1
        for p in prime_list(k):
            a,b = local_sign_sum(k,p)
            numerator *= a
            denominator *= b
        assert period % denominator == 0
        assert actual*denominator == numerator*period, (k,actual, numerator, denominator)
    recurrence_cases = 0
    for e in range(1,10):
        vals = s_rec(e)
        m = 2**e
        for r in range(m+1):
            assert vals[r] == s_direct(e,r), (e,r)
            if 0 < r < m:
                if r == m//2:
                    assert vals[r] == 0
                else:
                    value = abs(vals[r])
                    v2_val = (value & -value).bit_length()-1
                    v2_r = (r & -r).bit_length()-1
                    assert v2_val == v2_r+1, (e,r)
            recurrence_cases += 1
    local_cases = 0
    for k in range(2,161):
        primes = prime_list(k)
        zeros = [p for p in primes if local_sign_sum(k,p)[0] == 0]
        expected = [2] if (k+1) % 3 == 0 and (((k+1)//3) & (((k+1)//3)-1)) == 0 else []
        assert zeros == expected, (k, zeros, expected)
        local_cases += len(primes)
    print(f'PASS: {brute_cases} quotient residues; {recurrence_cases} truncated-valuation sums; '
          f'{local_cases} prime-local sign sums; k=1..160, e=1..9')


if __name__ == '__main__':
    checks()
