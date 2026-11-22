#!/usr/bin/env python3
"""Exact finite checks for Dickson prime-power image and fiber theorem.

Run: python3 check_dickson.py
Only Python's standard library is used. These checks do not replace the proof.
"""
from collections import Counter
from math import isqrt


def dickson_coefficients(n):
    earlier, previous = [2], [0, 1]
    if n == 0:
        return earlier
    if n == 1:
        return previous
    for _ in range(2, n+1):
        current = [0] * max(len(previous)+1, len(earlier))
        for j, a in enumerate(previous):
            current[j+1] += a
        for j, a in enumerate(earlier):
            current[j] -= a
        earlier, previous = previous, current
    return previous


def evaluate(coefficients, x, modulus):
    result = 0
    for c in reversed(coefficients):
        result = (result*x + c) % modulus
    return result


def iterate(coefficients, x, modulus, steps):
    for _ in range(steps):
        x = evaluate(coefficients, x, modulus)
    return x


def valuation(n, p):
    assert n != 0
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def test_images():
    checked = 0
    for p, upper_k, max_r in [(5,6,3),(7,5,3),(11,4,3),(13,3,2)]:
        coefficients = dickson_coefficients(p)
        for r in range(1,max_r+1):
            for k in range(1,upper_k+1):
                q = p**k
                freq = Counter(iterate(coefficients,x,q,r) for x in range(q))
                centers = {a:iterate(coefficients,a,q,r) for a in range(p)}
                expected = {}
                for a in range(p):
                    h = 2 if a in (2,p-2) else 1
                    radius = min(k, 1+r*h)
                    for t in range(p**(k-radius)):
                        y = (centers[a] + p**radius*t) % q
                        assert y not in expected
                        expected[y] = p**min(k-1,r*h)
                assert dict(freq) == expected, (p,r,k,len(freq),len(expected))
                want = (p-2)*p**max(k-r-1,0)+2*p**max(k-2*r-1,0)
                assert len(freq) == want
                if k > 1:
                    period = p**max(1,k-r)
                    assert all(iterate(coefficients,x,q,r)==iterate(coefficients,x+period,q,r) for x in range(min(period,100)))
                    if period > p:
                        assert iterate(coefficients,0,q,r)!=iterate(coefficients,period//p,q,r)
                checked += q
                print('image',p,r,k,len(freq),'OK')
    return checked


def test_metric():
    checked=0
    for p in (5,7,11,13):
        c=dickson_coefficients(p)
        r=3
        K=9
        mod=p**K
        for a in range(p):
            h=2 if a in (2,p-2) else 1
            # Distinct points with differences of prescribed valuation.
            for e in range(1, K-r*h):
                for t in range(1,31):
                    x=a+p*t
                    y=x+p**e*(1+p*(t%7))
                    delta=(iterate(c,x,mod,r)-iterate(c,y,mod,r))%mod
                    assert delta!=0
                    assert valuation(delta,p)==e+r*h,(p,a,e,t)
                    checked += 1
    print('distance checks',checked,'OK')
    return checked


if __name__ == '__main__':
    counts=test_images()
    metric=test_metric()
    print('PASS: exact tested input values',counts,'; metric assertions',metric)
