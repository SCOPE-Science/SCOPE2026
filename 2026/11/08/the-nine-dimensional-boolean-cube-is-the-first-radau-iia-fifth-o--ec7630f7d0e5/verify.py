#!/usr/bin/env python3
"""Exact integer certificate for graph-heat endpoint positivity on Boolean cubes.
Usage: python verify.py [CERTIFICATE.json]
No external dependencies. The proof in RESULT.md explains why sign checks imply the assertion.
"""
import json
import math
import sys
from fractions import Fraction


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def binomial(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def shell_factor(d, k, j):
    return sum((-1)**r * binomial(k, r) * binomial(d-k, j-r)
               for r in range(k+1))


def numerator(d, k):
    assert d >= 1 and 0 <= k <= d
    D = [[60, 72*j, 36*j*j, 8*j*j*j] for j in range(1, d+1)]
    N = [[60, -48*j, 12*j*j] for j in range(1, d+1)]
    prod_all = [1]
    for factor in D:
        prod_all = multiply(prod_all, factor)
    total = [0]*len(prod_all)
    for j in range(d+1):
        weight = shell_factor(d, k, j)
        if weight == 0:
            continue
        if j == 0:
            term = prod_all
        else:
            term = [1]
            for index, factor in enumerate(D, start=1):
                if index != j:
                    term = multiply(term, factor)
            term = multiply(term, N[j-1])
        for a, x in enumerate(term):
            total[a] += weight*x
    assert len(total) == 3*d+1
    return total


def translate_one(p):
    # Coefficient array of P(1+t).
    return [sum(p[j]*binomial(j, k) for j in range(k, len(p)))
            for k in range(len(p))]


def compress_unit(p):
    # Coefficient array of (1+t)^m P(t/(1+t)), m=deg P.
    m = len(p)-1
    return [sum(p[j]*binomial(m-j, k-j) for j in range(k+1))
            for k in range(m+1)]


def rational_value(d, k, h):
    h = Fraction(h)
    p = numerator(d, k)
    val = sum(Fraction(c)*h**i for i, c in enumerate(p))
    den = 2**d
    for j in range(1, d+1):
        den *= (60 + 72*j*h + 36*j*j*h*h + 8*j*j*j*h*h*h)
    return val / den


def build():
    # First failing dimension: all shell-types in dimensions <= 8.
    certified = {}
    nchecked = 0
    for d in range(1,9):
        for k in range(d+1):
            p = numerator(d,k)
            certified[f'{d}:{k}'] = p
            assert any(x>0 for x in p)
            if (d,k) != (8,1):
                assert all(x>=0 for x in p), (d,k)
                assert p[k] > 0, (d,k,p[k])
                assert all(x==0 for x in p[:k]), (d,k)
                nchecked += len(p)
    p = certified['8:1']
    short = compress_unit(p)
    long = translate_one(p)
    assert all(x>=0 for x in short)
    assert all(x>=0 for x in long)
    assert any(x>0 for x in short[1:])
    assert long[0]>0
    nchecked += len(short)+len(long)
    # Explicit exact negative nearest-neighbor value on the nine-cube at h=1.
    witness = rational_value(9,1,Fraction(1))
    expected = Fraction(-223660628942821971, 826114405977278306944)
    assert witness == expected
    assert witness < 0
    nchecked += 2
    # Independent check: direct Walsh spectral sum using only fractions.
    direct = Fraction(0)
    for j in range(10):
        eig = Fraction(60-48*j+12*j*j, 60+72*j+36*j*j+8*j*j*j)
        direct += shell_factor(9,1,j)*eig
    assert direct / 2**9 == witness
    nchecked += 1
    return {'schema_version':1,
        'statement':'All entry types of the three-stage fifth-order Radau IIA completed graph-heat step on Q_d are strictly positive for h>0 when 1<=d<=8; Q_9 has a negative adjacent-vertex entry at h=1.',
        'positive_polynomial_coefficients':certified,
        'exceptional_eight_cube_adjacent_distance':{
            'first_interval_transform':short,
            'second_interval_transform':long,
            'first_interval':'h=t/(1+t), t>=0, covers 0<=h<1',
            'second_interval':'h=1+t, t>=0, covers h>=1'},
        'negative_nine_cube_adjacent_at_h_one':{'numerator':witness.numerator,'denominator':witness.denominator},
        'test_count':nchecked}


def main():
    cert=build()
    if len(sys.argv)>1:
        with open(sys.argv[1],encoding='utf-8') as f:
            saved=json.load(f)
        assert saved==cert, 'Embedded certificate differs from exact symbolic recomputation'
    print('VERIFY_OK',cert['test_count'],'exact integer/rational coefficients and identities')
    print('Q9 h=1, distance=1:',str(rational_value(9,1,1)))

if __name__=='__main__':main()
