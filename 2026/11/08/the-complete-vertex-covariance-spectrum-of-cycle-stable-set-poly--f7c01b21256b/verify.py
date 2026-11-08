#!/usr/bin/env python3
"""Standalone finite checks for exact cycle stable-set vertex covariance.

Enumerate all stable-set indicator vertices; compare exact count and
covariance entries with Fibonacci expressions; compare the finite DFT
against a closed formula; check spectral order. These finite checks do
not constitute a proof for arbitrary n.
"""
from fractions import Fraction
from math import cos, pi, sqrt


def fibonacci_list(n):
    f = [0, 1]
    for _ in range(n):
        f.append(f[-1] + f[-2])
    return f


def cycle_masks(n):
    for x in range(1 << n):
        if x & ((x << 1) | (x >> (n - 1))):
            continue
        # also test the closing edge and all other edges directly
        if any((x >> i) & (x >> ((i + 1) % n)) & 1 for i in range(n)):
            continue
        yield x


def main():
    r = (sqrt(5) - 3) / 2
    checks = 0
    count = 0
    for n in range(3, 17):
        f = fibonacci_list(n + 2)
        L = f[n - 1] + f[n + 1]
        masks = list(cycle_masks(n))
        assert len(masks) == L, (n, len(masks), L)
        count += len(masks)
        p = Fraction(f[n - 1], L)
        qq = []
        for k in range(n):
            a = sum(((x & 1) != 0) and (((x >> k) & 1) != 0) for x in masks)
            q = Fraction(a, L)
            expected = p if k == 0 else Fraction(f[k - 1] * f[n - k - 1], L)
            assert q == expected, (n, k, q, expected)
            qq.append(q)
            checks += 1
        for j in range(n):
            direct = sum(float(qq[k]) * cos(2 * pi * j * k / n) for k in range(n))
            if j == 0:
                direct -= n * float(p)**2
                formula = ((1 - r**n) / (1 + r**n) / (5 * sqrt(5))
                           + n * r**n / (5 * (1 + r**n)**2))
            else:
                formula = ((1 - r*r) * (1 - r**n) /
                           (5*(1 + r**n)*(1 - 2*r*cos(2*pi*j/n) + r*r)))
            assert abs(direct - formula) < 1e-9, (n, j, direct, formula)
            checks += 1
        base = ((1 - r**n) / (1 + r**n) / (5 * sqrt(5))
                + n * r**n / (5 * (1 + r**n)**2))
        other = [((1-r*r)*(1-r**n)/(5*(1+r**n)*
                  (1-2*r*cos(2*pi*j/n)+r*r))) for j in range(1,n)]
        assert base < min(other)
        top = max(other)
        maximizing = [j for j in range(1,n) if abs(other[j-1]-top)<1e-10]
        assert maximizing == ([n//2] if n%2 == 0 else [n//2,(n+1)//2])
    for n in range(17, 251):
        w = r**n
        base = (1-w)/(1+w)/(5*sqrt(5)) + n*w/(5*(1+w)**2)
        first = ((1-r*r)*(1-w)/(5*(1+w)*
                  (1-2*r*cos(2*pi/n)+r*r)))
        assert base < first
    assert abs((1/sqrt(5)) / (1/(5*sqrt(5))) - 5) < 1e-12
    print('CYCLE_STABLE_VERTEX_COVARIANCE_CHECKS_PASSED',
          'dimensions=14', 'vertices='+str(count),
          'exact_and_DFT_checks='+str(checks), 'high_dimension_order_tests=234')

if __name__ == '__main__':
    main()
