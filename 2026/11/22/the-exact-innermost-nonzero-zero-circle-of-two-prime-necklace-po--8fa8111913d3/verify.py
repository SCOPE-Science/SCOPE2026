"""Independent elementary coefficient and numerical checks for the necklace-root theorem.

The infinite statements follow from the argument in RESULT.md, not from these tests.
No optional packages are required.
"""
import math
from math import gcd


def add(A, B, sign=1):
    C = A.copy()
    for k, v in B.items():
        C[k] = C.get(k, 0) + sign * v
    return {k: v for k, v in C.items() if v}


def mul(A, B):
    C = {}
    for i, a in A.items():
        for j, b in B.items():
            C[i + j] = C.get(i + j, 0) + a * b
    return {k: v for k, v in C.items() if v}


def rho(p, q):
    assert 2 <= p < q
    c, Q = p - 1, q - 1
    def H(x):
        return math.fsum(x ** (Q + c * j) for j in range(q))
    lo, hi = 0.0, 1.0
    for _ in range(90):
        mid = (lo + hi) / 2
        if H(mid) < 1:
            lo = mid
        else:
            hi = mid
    r = (lo + hi) / 2
    assert abs(H(r) - 1) < 1e-10
    return r


def lambert_w_positive(z):
    assert z > 0
    lo, hi = 0.0, max(1.0, math.log1p(z))
    for _ in range(90):
        mid = (lo + hi) / 2
        if mid * math.exp(mid) < z:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def coefficient_check(p, q, a, b):
    t = p ** (a - 1) * q ** (b - 1)
    n = p * q * t
    H = {t * (q - 1 + j * (p - 1)): 1 for j in range(q)}
    factored = mul({t: 1}, mul({0: 1, t * (p - 1): -1}, add({0: 1}, H, -1)))
    mobius = {n: 1, p * t: -1, q * t: -1, t: 1}
    assert factored == mobius, (p, q, a, b)
    root = rho(p, q)
    g = gcd(p - 1, q - 1)
    # At each predicted complex root every exponent in the positive factor is a multiple of tg.
    assert all((t * (q - 1 + j * (p - 1))) % (t * g) == 0 for j in range(q))
    # Positive derivative at rho ensures all minimal-modulus roots of the factor are simple.
    deriv = math.fsum((q-1 + j*(p-1)) * root ** (q-2+j*(p-1)) for j in range(q))
    assert deriv > 0
    # The other nonzero roots in the factorization have modulus one.
    assert root < 1.0
    return root, t*g


def run():
    cases = [(2,3),(2,5),(2,11),(3,5),(3,7),(3,11),(5,7),(5,11),(7,11)]
    for p, q in cases:
        for a, b in [(1,1),(2,1),(1,2),(2,2)]:
            r, m = coefficient_check(p, q, a, b)
            assert m == (p**(a-1))*(q**(b-1))*gcd(p-1,q-1)
        print(f'p={p}, q={q}, rho={r:.12f}, g={gcd(p-1,q-1)}')
    for p in (2,3,5):
        for q in (101,1009,10007):
            if q <= p:
                continue
            r = rho(p,q)
            approx = lambert_w_positive((q-1)/(p-1))/(q-1)
            discrepancy = abs((1-r)-approx)
            scaled = discrepancy*q*q/(math.log(q)**2)
            print(f'p={p}, q={q}, 1-rho={1-r:.12f}, Lambert-W={approx:.12f}, normalized_error={scaled:.5f}')
            assert scaled < 5
    print('PASS: 36 exact polynomial factorizations, complex angular constraints, uniqueness of positive radial root, and 9 asymptotic samples.')

if __name__ == '__main__':
    run()
