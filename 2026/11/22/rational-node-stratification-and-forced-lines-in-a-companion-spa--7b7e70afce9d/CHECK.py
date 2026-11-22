#!/usr/bin/env python3
"""Exact finite-prime consistency checks for a companion space-filling family.

The general prime-power statements require the accompanying symbolic proof.
This file verifies independent polynomial differentiation, projective-point
enumeration, the rational Hessian, and the exceptional contained lines.
"""
from itertools import product
import math


def monomial(*powers):
    assert len(powers) == 4
    return tuple(powers)


def polynomial_terms(p, b):
    # F = sum_i L_i (X_i^p X_{i+1} - X_i X_{i+1}^p), cyclically.
    pairs = [
        (1, monomial(p, 2, 0, 0)),
        (-1, monomial(1, p + 1, 0, 0)),
        (1, monomial(0, p, 2, 0)),
        (-1, monomial(0, 1, p + 1, 0)),
        (1, monomial(0, 0, p, 2)),
        (-1, monomial(0, 0, 1, p + 1)),
        (b, monomial(2, 0, 0, p)),
        (-b, monomial(p + 1, 0, 0, 1)),
        (1, monomial(1, 0, 0, p + 1)),
        (-1, monomial(p, 0, 0, 2)),
    ]
    return pairs


def derivative(terms, x, k, p, ell=None):
    total = 0
    for coeff, ee in terms:
        if not ee[k]:
            continue
        c = coeff * ee[k]
        ex = list(ee)
        ex[k] -= 1
        if ell is not None:
            if not ex[ell]:
                continue
            c *= ex[ell]
            ex[ell] -= 1
        val = c
        for xx, power in zip(x, ex):
            val *= pow(xx, power, p)
        total = (total + val) % p
    return total


def evaluate(terms, x, p):
    return sum(c * math.prod(pow(xx, e, p)
                    for xx, e in zip(x, exp)) for c, exp in terms) % p


def points(p):
    for i in range(4):
        for tail in product(range(p), repeat=3 - i):
            yield (0,) * i + (1,) + tail


def expected_points(p, b):
    out = set()
    for t in range(1, p):
        if (pow(t, 5, p) - pow(t, 3, p)) % p == b:
            raw = (pow(t, -3, p), t, pow(t, -1, p), 1)
            factor = pow(raw[0], -1, p)
            out.add(tuple(factor * xx % p for xx in raw))
    return out


def hessian_expected(t, b, p):
    ti = pow(t, -1, p)
    return [
        [2*b % p, -t % p, 0],
        [-t % p, 2*pow(t, -3, p) % p, -ti % p],
        [0, -ti % p, 2*t % p],
    ]


def test_prime(p):
    pts = list(points(p))
    n_sing = 0
    n_special = 0
    for b in range(1, p):
        terms = polynomial_terms(p, b)
        seen = set()
        for x in pts:
            grads = [derivative(terms, x, k, p) for k in range(4)]
            if grads == [0, 0, 0, 0]:
                assert evaluate(terms, x, p) == 0, ('Euler/fill', p, b, x)
                seen.add(x)
        predicted = expected_points(p, b)
        assert seen == predicted, ('singular locus', p, b, seen, predicted)
        n_sing += len(seen)
        for t in range(1, p):
            x = (pow(t, -3, p), t, pow(t, -1, p), 1)
            if (pow(t, 5, p) - pow(t, 3, p)) % p != b:
                continue
            h = [[derivative(terms, x, i, p, j) for j in range(3)]
                 for i in range(3)]
            assert h == hessian_expected(t, b, p), ('Hessian', p, b, t, h)
            det = ((h[0][0]*(h[1][1]*h[2][2]-h[1][2]*h[2][1])
                    -h[0][1]*(h[1][0]*h[2][2]-h[1][2]*h[2][0])) % p)
            assert det == (2*t*(2*t*t-3)) % p, ('det', p, b, t)
            if 2*t*t % p == 3 % p:
                n_special += 1
                k = (1, t*t % p, pow(2, -1, p), 0)
                for i in range(3):
                    assert sum(h[i][j]*k[j] for j in range(3)) % p == 0
                # Check every point of the alleged line, including infinity.
                for s in range(p):
                    y = tuple((x[i] + s*k[i]) % p for i in range(4))
                    assert evaluate(terms, y, p) == 0, ('line', p, b, t, s)
                assert evaluate(terms, k, p) == 0, ('line infinite', p,b,t)
    assert n_sing == p - 3, ('incidence total',p,n_sing)
    expected_special = sum(2*t*t % p == 3 % p for t in range(1,p))
    assert n_special == expected_special
    print(f'p={p}: {n_sing} singular parameter-point pairs, {n_special} corank-one cases')


if __name__ == '__main__':
    for p in (3, 5, 7, 11, 13, 19):
        test_prime(p)
    print('All exact finite-prime tests passed; proof covers all odd prime powers.')
