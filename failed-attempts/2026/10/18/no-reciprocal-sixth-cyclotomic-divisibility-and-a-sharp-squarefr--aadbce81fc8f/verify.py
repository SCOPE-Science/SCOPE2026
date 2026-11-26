"""Finite checks for the Phi_6 mutual-divisibility theorem.

These checks supplement, but do not replace, the descent proof.
"""
from math import isqrt


def f(n):
    return n * n - n + 1


def divisors(n):
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            yield d
            if d * d != n:
                yield n // d


def prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def main():
    cases = 0
    for a in range(2, 5001):
        for b in divisors(f(a)):
            if b <= a:
                continue
            cases += 1
            z = f(a) // b
            assert 1 <= z < a
            assert (b * z) % a == 1 % a
            assert (z*z*f(b) - f(z)) % a == 0
            assert f(b) % a != 0, (a,b,z)
    triple = (349, 121453, 9710803)
    assert all(prime(p) for p in triple)
    for i in range(3):
        assert f(triple[i]) % triple[(i+1) % 3] == 0
    n = 1
    h = 1
    for p in triple:
        n *= p
        h *= f(p)
    assert n == 411612748708891
    assert h % n == 0 and h // n == 410433300314317
    phi3 = lambda x: x*x+x+1
    assert phi3(3) == 13 and phi3(13) % 3 == 0
    print('VERIFY_OK', 'quotient_divisor_cases', cases, 'three_cycle', triple, 'value', h // n)


if __name__ == '__main__':
    main()
