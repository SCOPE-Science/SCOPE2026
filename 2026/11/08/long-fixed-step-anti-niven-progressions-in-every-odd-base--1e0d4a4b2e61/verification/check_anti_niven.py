#!/usr/bin/env python3
"""Exact finite checks for a fixed-step anti-Niven progression construction.

Checks are finite corroboration; the theorem's infinite parameter domain
is established by the accompanying mathematical proof.
"""
from math import gcd, lcm


def primes_le(n):
    ans = []
    for v in range(2, n + 1):
        if all(v % q for q in ans if q * q <= v):
            ans.append(v)
    return ans


def find_rough_pair(b):
    U = 1 + 2 * b * (b - 1)
    # P = 1 + b*(b-3 + t*(b-1)) ensures P == 1 (mod b)
    # and P == -1 (mod b-1).
    for t in range(1, 100000):
        P = 1 + b * (b - 3 + t * (b - 1))
        Q = P - (b - 1)
        if Q <= U or P <= U:
            continue
        if all(P % q != 0 and Q % q != 0 for q in primes_le(U)):
            return P, Q, U
    raise AssertionError('Search bound exceeded')


def digit_sum(n, b):
    s = 0
    while n:
        n, r = divmod(n, b)
        s += r
    return s


def check_base(b, full=False):
    P, Q, U = find_rough_pair(b)
    # Exact local feasibility of the CRT avoidance condition.
    for q in primes_le(U):
        if (b-1) % q == 0:
            permitted = {(-1) % q}
        elif b % q == 0:
            permitted = {1 % q}
        else:
            permitted = set(range(q)) - {0, (b-1) % q}
        assert permitted and all(r % q != 0 and (r-(b-1)) % q != 0 for r in permitted)

    K = P - b
    a = (P + b) // (b - 1)
    R = K - a
    assert (P+b) % (b-1) == 0 and R >= 0
    assert P % b == 1 and Q % b == 2
    assert gcd(b, P*Q) == 1 and gcd(P,Q) == 1
    assert R + a == K and R + a*b == 2*P

    L = [1 + j*(b-1) for j in range(2*b+1)]
    exception = {0, 1, b+1}
    for j, v in enumerate(L):
        d = digit_sum(v, b)
        assert d == (1 if j in exception else b)
        D = Q if j in exception else P
        assert gcd(2*P+v, D) == 1
        assert v <= U
        if j in exception:
            assert v + 2*(b-1) <= U
    assert len(L) == 2*b+1

    # Build the literal separated one-digits for two modest cases.
    if full:
        # Explicit order without factorization of P*Q: iterate powers.
        z = b % (P*Q)
        H = 1
        while z != 1:
            z = z*b % (P*Q)
            H += 1
            if H > P*Q:
                raise AssertionError('Order bound')
        assert pow(b, H, P*Q) == 1
        C = sum(pow(b, 2*H*i) for i in range(1,R+1))
        C += sum(pow(b, 2*H*i+1) for i in range(1,a+1))
        assert C % (P*Q) == (2*P) % (P*Q)
        assert digit_sum(C, b) == K
        m = max(H, 3)
        if m % H: m += H - m % H
        N = C * pow(b, m) + 1
        for j in range(2*b+1):
            V = N+j*(b-1)
            assert digit_sum(V,b) == K + digit_sum(L[j],b)
            assert gcd(V,digit_sum(V,b)) == 1
    print('BASE_OK',b,'U',U,'P',P,'Q',Q,'a',a,'R',R,
          'length',2*b+1,'full',full)


if __name__ == '__main__':
    for base in [3,5,7,9,11,15,21,25,27,33]:
        check_base(base, full=base in [3,5])
    print('VERIFY_OK bases=10 complete_literal_bases=2 modular_checks=10')
