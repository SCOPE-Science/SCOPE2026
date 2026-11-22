#!/usr/bin/env python3
"""Independent exact finite-instance checks for proportional divisor-window moments.

This is a finite verifier; it does not prove the asymptotic theorem.
Run: python3 verify.py
"""
from fractions import Fraction
from math import gcd, log, pi


def euler_phi(n):
    phi = list(range(n + 1))
    for p in range(2, n + 1):
        if phi[p] == p:
            for j in range(p, n + 1, p):
                phi[j] -= phi[j] // p
    return phi


def exact_moments(y):
    top = 4 * y
    phi = euler_phi(top)
    H = [Fraction(0)]
    for k in range(1, top + 1):
        H.append(H[-1] + Fraction(1, k))
    means = [H[2*y] - H[y], H[4*y] - H[2*y]]
    pairs = [[Fraction(0), Fraction(0)] for _ in range(2)]
    for r in range(1, top + 1):
        v = [H[2*y//r] - H[y//r], H[4*y//r] - H[2*y//r]]
        w = Fraction(phi[r], r*r)
        for i in range(2):
            for j in range(2):
                pairs[i][j] += w * v[i] * v[j]
    return means, pairs


def exact_brute(y):
    top = 4*y
    period = 1
    for d in range(1, top + 1):
        period = period*d // gcd(period, d)
    totals = [0, 0]
    pairs = [[0, 0], [0, 0]]
    for n in range(1, period + 1):
        c = [sum(n % d == 0 for d in range(y + 1, 2*y + 1)),
             sum(n % d == 0 for d in range(2*y + 1, 4*y + 1))]
        for i in range(2):
            totals[i] += c[i]
            for j in range(2):
                pairs[i][j] += c[i]*c[j]
    return ([Fraction(v, period) for v in totals],
            [[Fraction(v, period) for v in row] for row in pairs], period)


def dyadic_contrast_variance(y):
    top = 4*y
    phi = euler_phi(top)
    H = [0.0]*(top+1)
    for d in range(1, top+1):
        H[d] = H[d-1] + 1/d
    total = 0.0
    for r in range(1, top+1):
        g = 2*H[2*y//r] - H[y//r] - H[4*y//r]
        total += phi[r]/(r*r)*g*g
    mean = 2*H[2*y]-H[y]-H[4*y]
    return total-mean*mean


def integral_truncation(N):
    # Step endpoints exactly follow t=1/k,2/k,4/k, t>=1/N.
    ends = {1/N, 4.0}
    for a in (1,2,4):
        for k in range(1,a*N+1):
            t = a/k
            if 1/N <= t <= 4:
                ends.add(t)
    ends = sorted(ends)
    H = [0.0]*(4*N+1)
    for k in range(1,len(H)):
        H[k] = H[k-1] + 1/k
    val = 0.0
    for lo,hi in zip(ends,ends[1:]):
        # Floor function changes only at a/k; midpoint selects constant branch.
        t=(lo+hi)/2
        g=2*H[int(2/t)]-H[int(1/t)]-H[int(4/t)]
        val += (g*g)*log(hi/lo)
    return (6/pi**2)*val


def main():
    for y in (1,2,3):
        x=exact_moments(y)
        means, second, period=exact_brute(y)
        assert x == (means,second), f"finite-period mismatch at y={y}"
        print(f"Exact period y={y}, L={period}: moments agree")
    values={y:dyadic_contrast_variance(y) for y in (100,1000,5000)}
    print('Finite contrast variances', values)
    assert 0.50 < values[100] < values[1000] < values[5000] < 0.51
    integral=integral_truncation(3000)
    print('Integral from t>=1/3000:', integral)
    assert 0.5081 < integral < 0.5083
    assert abs(values[5000]-integral)<0.0002
    print('PASS: exact finite-period identities and numeric consistency checks')


if __name__=='__main__':
    main()
