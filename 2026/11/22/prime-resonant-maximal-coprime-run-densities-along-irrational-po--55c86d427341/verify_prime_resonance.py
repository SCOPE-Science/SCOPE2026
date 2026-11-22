#!/usr/bin/env python3
"""Finite consistency checks for polynomial-floor coprimality runs.

All checks are finite: the infinite density theorem and prime-resonance
asymptotics require the mathematical proof and cited large-prime theorem.
"""
from fractions import Fraction
from math import gcd, isqrt, log, exp


def primes_below(bound):
    a = bytearray(b'\x01') * (bound + 1)
    a[0:2] = b'\x00\x00'
    for i in range(2, isqrt(bound) + 1):
        if a[i]:
            a[i * i:bound + 1:i] = b'\x00' * ((bound - i * i) // i + 1)
    return [i for i in range(2, bound + 1) if a[i]]


def block_local_prime(r, p):
    count = sum(
        all(gcd(u, v + j) % p != 0 for j in range(r))
        for u in range(p) for v in range(p)
    )
    assert count == (p * (p - 1) if p <= r else p * p - r)
    return Fraction(count, p * p)


def truncated_block(r, pp):
    out = Fraction(1, 1)
    for p in pp:
        out *= (Fraction(p - 1, p) if p <= r else Fraction(p * p - r, p * p))
    return out


def direct_crt(d, r):
    return sum(
        all(gcd(d, u, v + j) == 1 for j in range(r))
        for u in range(d) for v in range(d)
    )


def exact_run_crt(d, r):
    return sum(
        gcd(d, u, v - 1) > 1
        and all(gcd(d, u, v + j) == 1 for j in range(r))
        and gcd(d, u, v + r) > 1
        for u in range(d) for v in range(d)
    )


def polynomial_sample(limit, r):
    count = 0
    for n in range(1, limit + 1):
        t = isqrt(2 * n**4)  # floor(sqrt(2)*n^2), exactly
        if (gcd(n, t - 1) > 1
            and all(gcd(n, t + j) == 1 for j in range(r))
            and gcd(n, t + r) > 1):
            count += 1
    return count


def truncated_float(r, ps):
    a = 1.
    for p in ps:
        if p <= r:
            a *= 1 - 1 / p
        else:
            a *= 1 - r / (p * p)
    return a


def main():
    small = primes_below(19)
    checks = 0
    for p in small:
        for r in range(1, 13):
            assert block_local_prime(r, p) == (Fraction(p - 1, p) if p <= r else Fraction(p*p-r,p*p))
            checks += 1
    for d in (6, 30, 210):
        local = [p for p in small if d % p == 0]
        for r in range(1, 8):
            B = [truncated_block(k, local) for k in (r,r+1,r+2)]
            assert Fraction(direct_crt(d, r), d*d) == B[0]
            assert Fraction(exact_run_crt(d, r), d*d) == B[0]-2*B[1]+B[2]
            checks += 2
    ps = primes_below(100000)
    for r in range(1, 25):
        C0,C1,C2=[truncated_float(k,ps) for k in (r,r+1,r+2)]
        assert C0-2*C1+C2>0
        checks += 1
    for r in (1,2,3,4):
        observed = polynomial_sample(100000, r) / 100000
        predicted = (truncated_float(r,ps)-2*truncated_float(r+1,ps)+truncated_float(r+2,ps))
        print(f'EXAMPLE r={r} empirical={observed:.6f} prime_product={predicted:.6f}')
        assert abs(observed - predicted) < .012
        checks += 1
    print(f'VERIFY_OK finite_checks={checks} prime_bound=100000 exact_CRT_moduli=6,30,210 polynomial_sample=100000')


if __name__ == '__main__':
    main()
