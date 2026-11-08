#!/usr/bin/env python3
"""Exact finite corroboration of additive covering by dyadic norm-one pairs.
Run: python3 verify.py
All general statements are established mathematically in RESULT.md.
"""
from itertools import product


def points(k):
    m = 1 << k
    return {(a, b) for a in range(m) for b in range(m)
            if (a*a + b*b - 1) % m == 0}


def plus(a_set, b_set, m):
    return {((a+c) % m, (b+d) % m)
            for a, b in a_set for c, d in b_set}


def test_additive():
    for k in range(1, 8):
        m = 1 << k
        circle = points(k)
        odd = {(a,b) for a in range(m) for b in range(m) if (a+b)&1}
        even = {(a,b) for a in range(m) for b in range(m) if not ((a+b)&1)}
        oddodd = {(a,b) for a in range(1,m,2) for b in range(1,m,2)}
        twice = plus(circle, circle, m)
        thrice = plus(twice, circle, m)
        fourth = plus(thrice, circle, m)
        assert oddodd <= twice
        assert thrice == odd
        assert fourth == even
        assert (circle == odd) == (k <= 2)
        assert ((2%m,2%m) not in twice) if k>=3 else True
        print(f"k={k} circle={len(circle)} double={len(twice)} triple={len(thrice)} quadruple={len(fourth)}")


def test_square_certificate():
    cases = 0
    for k in range(1, 10):
        m = 1 << k
        aux = 1 << (k + 1)
        root = {pow(lam, 2, aux): lam for lam in range(1, aux, 2)}
        for u in range(1,m,2):
            for v in range(1,m,2):
                h=(u*u+v*v)//2
                assert h%4 == 1
                q=(2*pow(h,-1,aux)-1)%aux
                assert q%8==1 if aux>=8 else True
                lam=root[q]
                x=(u-lam*v)//2; y=(v+lam*u)//2
                xx=(u+lam*v)//2; yy=(v-lam*u)//2
                assert (x*x+y*y-1)%m == 0
                assert (xx*xx+yy*yy-1)%m == 0
                assert (x+xx-u)%m == 0 and (y+yy-v)%m == 0
                cases += 1
    print(f"constructive_oddodd_certificates={cases}")


if __name__ == '__main__':
    test_additive()
    test_square_certificate()
    print('VERIFY_OK')
