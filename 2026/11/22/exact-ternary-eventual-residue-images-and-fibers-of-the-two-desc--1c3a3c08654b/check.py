#!/usr/bin/env python3
"""Finite reproducibility checks for an Eulerian-column 3-adic image theorem.

Uses only Python's standard library. Finite testing is not a substitute for the
analytic proof recorded separately.
"""
from collections import Counter


def v3(n):
    if n == 0:
        return None
    e = 0
    while n % 3 == 0:
        e += 1
        n //= 3
    return e


def padic_log4(K):
    """Compute log(1+3) mod 3**K from its exact rational series."""
    m = 3 ** K
    val = 0
    for j in range(1, 3*K + 20):
        a = v3(j)
        if j-a >= K:
            continue
        unit = j // (3 ** a)
        term = (3 ** (j-a) * pow(unit, -1, m)) % m
        val = (val + (term if j % 2 else -term)) % m
    return val


def branch(eps, t, modulus):
    p = pow(4, t, modulus)
    if eps == 0:
        return ((2*t+1)*(t-p)) % modulus
    return ((t+1)*(2*t+1-4*p)) % modulus


def odd_critical(K):
    """Hensel-lift the odd-branch critical point and its value modulo 3**K."""
    m = 3 ** K
    l = padic_log4(K)
    def derivative(t):
        return (4*t+3-4*pow(4,t,m)*(1+(t+1)*l)) % m
    beta = 1
    for r in range(1, K):
        choices = [beta + j*3**r for j in range(3)
                   if derivative(beta + j*3**r) % 3**(r+1) == 0]
        assert len(choices) == 1
        beta = choices[0]
    assert derivative(beta) == 0
    return beta, branch(1, beta, m)


def square_roots_count(w, j):
    """Number of z mod 3**j with z*z == w, including j=0."""
    if j == 0:
        return 1
    m = 3 ** j
    w %= m
    if w == 0:
        return 3 ** (j//2)
    e = v3(w)
    if e % 2:
        return 0
    return 2 * 3**(e//2) if (w // 3**e) % 3 == 1 else 0


def critical_count(y, center, k):
    """The 3-adic quadratic sheet A+18*Z_3**2, with input t == 1 mod 3."""
    if (y - center) % 9:
        return 0
    j = k-2
    if j == 0:
        return 3
    modulus = 3**j
    w = (((y-center)//9)*pow(2,-1,modulus)) % modulus
    return 3*square_roots_count(w,j)


def predicted(y,k,odd_center):
    if k == 1:
        return {0:3,1:1,2:2}[y]
    ans = 2 if y%3 in (0,2) else 0
    return ans + critical_count(y,0,k) + critical_count(y,odd_center,k)


def count_squares(j):
    return 1 + sum(3**(j-2*a-1) for a in range((j-1)//2+1))


def check_eulerian_closed_form():
    a = [[0]*4 for _ in range(90)]
    a[0][0] = 1
    for n in range(1,90):
        for k in range(4):
            a[n][k] = ((n-k)*a[n-1][k-1] if k>0 else 0) + (k+1)*a[n-1][k]
    for n in range(90):
        expected = 3**n - (n+1)*2**n + n*(n+1)//2
        assert a[n][2] == expected, (n,a[n][2],expected)


def main():
    check_eulerian_closed_form()
    total = 90
    for k in range(1,9):
        modulus = 3**k
        beta, A = odd_critical(k)
        actual = Counter()
        for t in range(modulus):
            actual[branch(0,t,modulus)] += 1
            actual[branch(1,t,modulus)] += 1
        for y in range(modulus):
            got = actual[y]
            expect = predicted(y,k,A)
            assert got == expect,(k,y,got,expect)
            total += 1
        # Verify actual finite Eulerian numbers throughout one complete tail period.
        for n in range(k,k+2*modulus):
            observed = (pow(3,n,modulus)-(n+1)*pow(2,n,modulus)+n*(n+1)//2) % modulus
            expect = branch(n%2,n//2,modulus)
            assert observed == expect,(k,n,observed,expect)
            total += 1
        nsupport = sum(v>0 for v in actual.values())
        expected_support = 3 if k == 1 else 2*3**(k-1)+count_squares(k-2)
        assert nsupport == expected_support
        assert actual[0] == 2+3**(k//2)
        assert sum(actual.values()) == 2*modulus
        total += 3
        print(f'k={k}: 3**k={modulus}; beta_odd={beta}; A_odd={A}; '
              f'distinct={nsupport}; zero_fiber={actual[0]}; min_nonzero_fiber={min(actual.values())}')
    print(f'PASS: {total} exact assertions, including exhaustive fiber checks for k=1..8')

if __name__ == '__main__':
    main()
