#!/usr/bin/env python3
"""Finite checks for prime-radical Swinnerton-Dyer specialization splitting laws.

Requires Python 3.11+ and SymPy 1.12+. The algebraic proof is independent
of these finite experiments.
"""
import json
import warnings
from sympy import Poly, symbols, resultant, primerange, factor_list, gcd, n_order

warnings.filterwarnings('ignore', category=DeprecationWarning)
X, Y = symbols('X Y')


def radical_sum_polynomial(p, primes):
    f = Poly(X, X)
    for ell in primes:
        expr = resultant(Y**p - ell, f.as_expr().subs(X, X-Y), Y)
        raw = Poly(expr, X)
        assert raw.LC() in (-1, 1)
        f = Poly(raw.monic().as_expr(), X)
        assert all(c.q == 1 for c in f.all_coeffs())
    return f


def expected_degrees(p, n, q, primes):
    if q == p:
        return [1] * (p**n)
    if q % p == 1:
        if all(pow(ell, (q-1)//p, q) == 1 for ell in primes):
            return [1]*(p**n)
        return [p]*(p**(n-1))
    d = int(n_order(q % p, p))
    return [1] + [d]*((p**n-1)//d)


def main():
    cases = [(3,(2,5)),(3,(2,5,7)),(5,(2,3)),(7,(2,3)),(3,(2,))]
    good = 0
    bad = 0
    total = 0
    examples = {}
    for p, primes in cases:
        n = len(primes)
        f = radical_sum_polynomial(p, primes)
        assert f.degree() == p**n and f.LC() == 1
        assert Poly(f.as_expr().subs(X, X+1), X).degree() == p**n
        examples[f'{p}:{"-".join(map(str,primes))}'] = str(f.as_expr()) if f.degree() <= 9 else f'degree {f.degree()}'
        for q in primerange(2, 251):
            fq = Poly(f.as_expr(),X,modulus=int(q))
            fac = factor_list(fq, modulus=int(q))[1]
            degrees = sorted([int(g.degree()) for g,e in fac for _ in range(e)])
            assert sum(degrees) == p**n
            assert max(degrees) <= p, (p, primes, q, degrees)
            if q==p:
                expected = [1] * (p**n)
                assert degrees == expected, ('characteristic p', p, primes, q)
            if gcd(fq, fq.diff()).degree() == 0:
                expected = sorted(expected_degrees(p,n,int(q),primes))
                assert degrees == expected, ('good prime', p, primes, q, degrees, expected)
                good += 1
            else:
                bad += 1
            total += 1
    print(json.dumps({'status':'PASS','good_prime_factorization_checks':good,
                      'bad_prime_factor_degree_checks':bad,
                      'total_prime_factorization_checks':total,
                      'cases':len(cases),'prime_bound_exclusive':251,
                      'small_examples':examples},sort_keys=True))

if __name__ == '__main__':
    main()
