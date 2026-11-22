"""Finite reproducibility checks for a base-3/2 binary-word discrepancy theorem.

This script supplies exact comparisons; the infinite assertions are proved separately.
"""
from functools import lru_cache


@lru_cache(maxsize=None)
def digit_parity(n):
    """Direct least-digit extraction: n=3q+r -> next state 2q, digit r."""
    if n == 0:
        return 0
    q, r = divmod(n, 3)
    return (digit_parity(2*q) + r) % 2


@lru_cache(maxsize=None)
def half_scaled(n):
    if n == 0:
        return 0
    q, r = divmod(n, 3)
    return half_scaled(2*q) if r < 2 else 1-half_scaled(2*q+1)


@lru_cache(maxsize=None)
def signed_sum(n):
    if n == 0:
        return 0
    q, r = divmod(n, 3)
    v = q - signed_sum(2*q)
    if r:
        v += 1
    if r == 2:
        v -= 1 - 2*(half_scaled(2*q) != half_scaled(2*q+1))
    return v


def defect(n):
    return 5*signed_sum(n)-n


def crt_start(k):
    modulus = 4**k
    residue = (-6 * pow(5, -1, modulus)) % modulus
    j = (-residue * pow(modulus, -1, 3)) % 3
    m = residue + modulus*j
    return m if m > 0 else m + 3*modulus


def run():
    # The digit algorithm and two different recursions generate the same word.
    for i in range(120000):
        assert digit_parity(i) == (
            half_scaled(i//3) if i%3 != 1 else 1-half_scaled(i//3)
        ), ('word', i)

    direct_signed = 0
    q01 = q10 = 0
    for i in range(30001):
        if i < 30000:
            direct_signed += 1 if half_scaled(i) == half_scaled(i+1) else -1
            q01 += int(digit_parity(i) == 0 and digit_parity(i+1) == 1)
            q10 += int(digit_parity(i) == 1 and digit_parity(i+1) == 0)
        if i < 30000:
            assert direct_signed == signed_sum(i+1), ('signed', i)
        if i < 30000 and (i+1)%3 == 0:
            n = (i+1)//3
            assert 20*q01 - 24*n == -defect(n)+10*(half_scaled(n)-half_scaled(0))
            assert 20*q10 - 24*n == -defect(n)-10*(half_scaled(n)-half_scaled(0))

    # The construction has exact drift 2 per two substitution steps.
    for k in range(1, 19):
        m0 = crt_start(k)
        assert 0 < m0 <= 3*4**k and m0%3 == 0
        assert (5*m0+6)%(4**k) == 0
        m = m0
        for j in range(k):
            assert m%3 == 0 and m%4 == 2
            assert half_scaled(2*m) == half_scaled(2*m+1)
            v = (3*m+2)//2
            assert v%2 == 0 and 2*v == 3*m+2
            m = 3*v//2
            assert 2*m == 3*v
            assert defect(2*m)-defect(2*m0) == 2*(j+1)
        assert 6*max(m, m0) <= 30*9**k

    print('PASS: 120000 independent rational-digit vs block comparisons')
    print('PASS: 30000 exact signed correlation checks')
    print('PASS: 10000 exact pair-count formula checks for each transition')
    print('PASS: 18 full CRT drift chains and interval bounds')


if __name__ == '__main__':
    run()
