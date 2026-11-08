#!/usr/bin/env python3
"""Exact modular checks for the first-failure-only square criterion."""
from fractions import Fraction
from math import gcd


def prime_factors(n):
    p = 2
    factors = []
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            factors.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        factors.append((n, 1))
    return factors


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**.5) + 1))


def forbidden(p):
    return p == 5 or p % 20 in (1, 9)


def expected_roots_u1(p):
    return 1 if p == 2 else (2 if p % 4 == 1 else 0)


def roots_u1(p):
    return tuple(x for x in range(p) if (x * x + 1) % p == 0)


def roots_u2(p):
    return tuple(x for x in range(p) if (x**4 + 3*x*x + 1) % p == 0)


def bad_indices(h, x, limit=13):
    d = gcd(h, x)
    u, v = x // d, h // d
    out = []
    for n in range(1, limit):
        u, v = u*u + v*v, u*v
        if gcd(h, u) > 1:
            out.append(n + 1)
        # numerator grows double-exponentially; moderate limit only for tiny pairs
    return out


def bad_indices_modular(h, x, limit=16):
    # Keep numerator/denominator for each prime modulo p, never relying on huge integers.
    out = set()
    for p, _ in prime_factors(h):
        d = gcd(h, x)
        u, v = (x // d) % p, (h // d) % p
        for n in range(1, limit):
            u, v = (u*u + v*v) % p, (u*v) % p
            if u == 0:
                out.add(n + 1)
    return tuple(sorted(out))


def favorable_residues(h, p, e):
    H = h // p**e
    return tuple(sorted((p**e * ((H*r) % p)) % p**(e+1) for r in roots_u1(p)))


def main():
    primes = [p for p in range(2, 1001) if isprime(p)]
    assert len(primes) == 168
    for p in primes:
        assert len(roots_u1(p)) == expected_roots_u1(p)
        assert bool(roots_u2(p)) == forbidden(p), (p, roots_u2(p))
        if forbidden(p):
            assert len(roots_u2(p)) in (2, 4), (p, roots_u2(p))
        else:
            assert len(roots_u2(p)) == 0
    print('QUARTIC_OK primes_le_1000=',len(primes),'classes=2,5,1_9_13_17_mod20')

    hs = [1, 2, 4, 8, 3, 7, 13, 17, 26, 34, 39, 51, 52, 68, 119, 153, 169, 221, 289, 442, 663, 676]
    checked = 0
    for h in hs:
        factors = prime_factors(h)
        assert all(not forbidden(p) for p, e in factors), (h, factors)
        active = [(p, e) for p, e in factors if expected_roots_u1(p)]
        M = 1
        for p, e in active:
            M *= p**(e+1)
        no_failure_fraction = Fraction(1, 1)
        for p, e in active:
            no_failure_fraction *= (1 - Fraction(len(roots_u1(p)), p**(e+1)))
        predicted_bad = M * (1 - no_failure_fraction)
        assert predicted_bad.denominator == 1
        observed_bad = 0
        for x in range(1, M+1):
            predicted_at_two = any(x % p**(e+1) in favorable_residues(h, p, e) for p, e in active)
            bad = bad_indices_modular(h, x, limit=18)
            assert bad in ((), (2,)), (h,x,bad)
            assert predicted_at_two == bool(bad), (h,x,bad,predicted_at_two)
            observed_bad += bool(bad)
            checked += 1
        assert observed_bad == int(predicted_bad)
        print('DENSITY_OK h=',h,'period=',M,'failing_residues=',observed_bad,'density=',str(no_failure_fraction.__rsub__(1)))
    # Joint first-two failure-bit law: all prime types, not just stabilized multipliers.
    hs_general = [5, 25, 29, 41, 58, 65, 85, 125, 145, 205, 290, 580]
    joint_residues = 0
    for h in hs_general:
        fs = prime_factors(h)
        M = 1
        p00, p2square, p3square = Fraction(1), Fraction(1), Fraction(1)
        for p, e in fs:
            den = p**(e+1)
            M *= den
            alpha = Fraction(len(roots_u1(p)), den)
            beta = Fraction(len(roots_u2(p)), den)
            p00 *= 1-alpha-beta
            p2square *= 1-alpha
            p3square *= 1-beta
        expected = (
            p00,
            p3square-p00, # n2 fails, n3 square
            p2square-p00, # n3 fails, n2 square
            1-p2square-p3square+p00, # both fail
        )
        assert all((M*z).denominator == 1 for z in expected)
        observed=[0,0,0,0]
        for x in range(1, M+1):
            bad = bad_indices_modular(h, x, 4)
            b2 = 2 in bad
            b3 = 3 in bad
            observed[2*b3+b2] += 1
        # Binary index mapping: (b3,b2) -> 0,1,2,3.
        assert tuple(observed) == tuple(int(M*z) for z in expected), (h, observed, expected)
        joint_residues += M
        print('JOINT_OK h=',h,'period=',M,'counts=',tuple(observed))
    # Counterexamples for all excluded primes <= 1000, with t0 an actual integer.
    for p in primes:
        if forbidden(p):
            a = roots_u2(p)[0]
            x = p * (a if a else p)
            assert 3 in bad_indices_modular(p, x, limit=6), (p,x)
    # Independent rational recurrence check on a few small cases.
    exact = 0
    for h in (2,3,5,7,13,17,26,29,34):
        for x0 in range(1, 21):
            S = Fraction(x0,1)
            d = gcd(x0,h)
            u,v=x0//d,h//d
            for n in range(0, 5):
                nxt = Fraction(h*h, S)
                # At this point (u,v) represents S_n/h.
                if n >= 1:
                    a,b=nxt.numerator,nxt.denominator
                    expression=Fraction(2*a,h)+b
                    def square_fraction(q):
                        from math import isqrt
                        return isqrt(q.numerator)**2 == q.numerator and isqrt(q.denominator)**2 == q.denominator
                    assert square_fraction(expression) == (gcd(h,u)==1), (h,x0,n)
                    exact+=1
                S += nxt
                u,v=u*u+v*v,u*v
    print('VERIFY_OK primes=',len(primes),'stabilized_residues=',checked,'joint_residues=',joint_residues,'exact_rational_tests=',exact,'strict_converse=yes')

if __name__ == '__main__': main()
