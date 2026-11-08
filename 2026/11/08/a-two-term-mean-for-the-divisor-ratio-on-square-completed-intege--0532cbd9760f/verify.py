#!/usr/bin/env python3
"""Independent exact checks for square-completion divisor-ratio mean.

Run with Python 3: python verify.py
All identity checks use exact rational arithmetic. Euler-product truncations
and finite-range asymptotics are diagnostics, not a proof of the limit.
"""
from fractions import Fraction
from math import isqrt, gamma, sqrt, log, pi


def prime_factors(m):
    out = []
    p = 2
    while p * p <= m:
        if m % p == 0:
            k = 0
            while m % p == 0:
                m //= p
                k += 1
            out.append((p, k))
        p += 1
    if m > 1:
        out.append((m, 1))
    return out


def tau(n):
    val = 1
    for _, a in prime_factors(n):
        val *= a + 1
    return val


def omega(n):
    return len(prime_factors(n))


def f_factor(m):
    val = Fraction(1)
    for _, a in prime_factors(m):
        val *= Fraction(2*a+1, 2)
    return val


def f_valuation(m):
    # Separate route: factor m*m, and normalize by unitary divisor count.
    return Fraction(tau(m*m), 2**omega(m*m))


def test_factors():
    for m in range(1, 361):
        assert f_factor(m) == f_valuation(m), m
    return 360


def test_square_blocks():
    # Independent direct-square-completion and grouped-weight sums, including
    # square and nonsquare end points.  The nonfull final block is tested.
    direct = Fraction(0)
    full = Fraction(0)
    previous = 0
    tested = 0
    for X in range(1, 15001):
        m = isqrt(X)
        if m*m < X:
            m += 1
        direct += f_valuation(m)
        if (m-1)*(m-1) == X-1:
            full += (2*m-3)*f_factor(m-1) if m > 1 else 0
        grouped = full + (X - (m-1)*(m-1))*f_factor(m)
        assert direct == grouped, (X, direct, grouped)
        tested += 1
    return tested


def test_local_series():
    # Polynomial coefficient test: (1-z)^2 sum_{a>=0} f(p^a) z^a
    # agrees with 1-z/2+z^2/2 through degree 40.
    a = [Fraction(1)] + [Fraction(2*k+1,2) for k in range(1,41)]
    for k in range(41):
        c = a[k]-(2*a[k-1] if k>=1 else 0)+(a[k-2] if k>=2 else 0)
        expected = Fraction(1) if k==0 else (Fraction(-1,2) if k==1 else (Fraction(1,2) if k==2 else Fraction(0)))
        assert c==expected,(k,c,expected)
    return 41


def sieve_primes(bound):
    primes = bytearray(b'\x01')*(bound+1)
    primes[:2] = b'\x00\x00'
    for p in range(2,isqrt(bound)+1):
        if primes[p]:
            primes[p*p:bound+1:p] = b'\x00'*(((bound-p*p)//p)+1)
    return [p for p in range(2,bound+1) if primes[p]]


def constants(primes):
    H=1.0
    lg=0.0
    for p in primes:
        z=1.0/p
        num=1-z/2+z*z/2
        H *= num/sqrt(1-z)
        lg -= log(p)*z*((z-0.5)/num + 0.5/(1-z))
    gamma_e=0.5772156649015328606065120900824
    k0=sqrt(2/pi)*H
    k1=sqrt(2/pi)*H*(lg+(3*gamma_e-1)/2)
    return H, lg, k0, k1


def test_diagnostics():
    H,lg,k0,k1=constants(sieve_primes(20000))
    assert 1.42 < H < 1.45
    assert -0.85 < lg < -0.80
    assert 1.13 < k0 < 1.16
    assert -0.56 < k1 < -0.49
    checks=[]
    for M in (100,400,1200,4000):
        exact=sum(((2*m-1)*f_factor(m) for m in range(1,M+1)),Fraction(0))
        x=M*M
        leading=k0*x*sqrt(log(x))
        two=leading+k1*x/sqrt(log(x))
        checks.append((M,round(float(exact)/x,8),round(two/x,8)))
    return H,lg,k0,k1,checks


def main():
    n1=test_factors()
    n2=test_square_blocks()
    n3=test_local_series()
    H,lg,k0,k1,checks=test_diagnostics()
    print('LOCAL_EULER_COEFFICIENTS_OK',n3)
    print('INDEPENDENT_FACTORIZATIONS_OK',n1)
    print('DIRECT_VS_GROUPED_SQUARE_COMPLETION_OK',n2)
    print('EULER_PRODUCT_TRUNCATION', 'H=',round(H,9), 'Hprime_over_H=',round(lg,9))
    print('ASYMPTOTIC_COEFFICIENTS_TRUNCATION',round(k0,9),round(k1,9))
    print('FINITE_DIAGNOSTICS_M_observed_two_term',checks)
    print('VERIFY_OK exact_checks=yes finite_diagnostics_not_an_infinite_proof=yes')

if __name__=='__main__':
    main()
