#!/usr/bin/env python3
"""Finite checks of Dickson prime-index value-set formulas.

The unlimited-prime and unlimited-exponent theorem is proved separately;
finite tests are not a proof of its universal quantifiers.
"""
from collections import Counter
from sympy import Poly, symbols

X = symbols('X')


def dickson_poly(n, a=1):
    previous, current = Poly(2, X), Poly(X, X)
    if n == 0:
        return previous
    if n == 1:
        return current
    for _ in range(2, n + 1):
        previous, current = current, Poly(X, X) * current - a * previous
    return current


def dickson_mod(n, x, a, modulus):
    previous, current = 2, x % modulus
    for _ in range(2, n + 1):
        previous, current = current, (x * current - a * previous) % modulus
    return current


def is_square_unit(a, p):
    return pow(a % p, (p - 1) // 2, p) == 1


def check_symbolic(p):
    dp = dickson_poly(p)
    assert all(int(c) % p == 0 for c in dp.all_coeffs()[1:])
    assert (dp.diff().exquo_ground(p) - Poly((X * X - 4)**((p - 1)//2), X)).set_modulus(p).is_zero
    m = (p-1)//2
    P = Poly(1, X) + sum((dickson_poly(j) for j in range(1, m+1)), Poly(0, X))
    assert dp - Poly(2, X) == (Poly(X, X)-Poly(2, X)) * P * P
    assert int(P.eval(2)) == p
    assert int(P.diff().eval(2)) % p == 0
    assert (P - Poly((X-2)**m, X)).set_modulus(p).is_zero


def check_numeric(p, a, k):
    modulus = p**k
    hist = Counter(dickson_mod(p, x, a, modulus) for x in range(modulus))
    sq = is_square_unit(a, p)
    if k == 1:
        wanted = Counter({1: p})
    elif k == 2:
        wanted = Counter({p: p})
    elif sq:
        wanted = Counter({p: (p-2)*p**(k-2), p*p: 2*p**(k-3)})
    else:
        wanted = Counter({p: p**(k-1)})
    got = Counter(hist.values())
    assert got == wanted, (p, a, k, got, wanted)
    # Every output is in a different mod-p fiber from a different input residue.
    for residue in range(p):
        values = {
            dickson_mod(p, x, a, modulus)
            for x in range(residue, modulus, p)
        }
        assert all(y % p == residue for y in values)
    return (p, a, k, len(hist), dict(sorted(got.items())))


def main():
    for p in (5, 7, 11, 13, 17):
        check_symbolic(p)
        print(f'Symbolic polynomial checks passed: p={p}')
    cases = []
    for p in (5, 7, 11, 13):
        for a in range(1, p):
            for k in (1, 2, 3):
                cases.append(check_numeric(p, a, k))
    for p in (5, 7):
        for a in range(1, p):
            cases.append(check_numeric(p, a, 4))
    for a in (1, 2):
        cases.append(check_numeric(11, a, 4))
    print(f'Passed {len(cases)} finite parameter/exponent cases')
    for p, a, k in ((5,1,3),(5,2,3),(7,1,4),(7,3,4),(11,1,4),(11,2,4)):
        print('Representative', check_numeric(p,a,k))
    p, modulus = 3, 3**4
    values = {dickson_mod(p, x, 1, modulus) for x in range(modulus)}
    assert len(values) == 13  # contrast with the p>=5 rule, which would give 15
    print('Excluded boundary: p=3, k=4 has 13 image residues, not 15')


if __name__ == '__main__':
    main()
