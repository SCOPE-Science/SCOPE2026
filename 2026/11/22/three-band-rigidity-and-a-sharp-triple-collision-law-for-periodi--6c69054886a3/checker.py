"""Standard-library numerical diagnostics for three-interleaved Fourier interpolation.
Checks complete-matrix spectral moments and collision scalings, not an infinite proof.
"""
import cmath
import math


def predicted(n, eps):
    assert n % 3 == 0 and 0 <= eps < 1
    theta = 2*math.pi*(1-eps)/3
    a = (1 + 2*math.cos(theta))/3
    b = (1 + 2*math.cos(2*theta))/3
    delta = math.sqrt(b*b/4 + 2*a*a)
    return sorted([1+b/2-delta, 1-b, 1+b/2+delta] * (n//3))


def product(a,b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def direct_gram(n, eps):
    y = [j + (eps if j%3 == 0 else (-eps if j%3 == 2 else 0))
         for j in range(n)]
    f = [[cmath.exp(2j*math.pi*k*u/n)/math.sqrt(n) for k in range(n)]
         for u in y]
    return [[sum(f[i][k]*f[j][k].conjugate() for k in range(n))
             for j in range(n)] for i in range(n)]


def main():
    total = 0
    for n in (3, 6, 9, 12, 15, 18, 24, 36):
        for eps in (0, .002, .1, .24, .25, .26, .4, .5, .75, .9, .97):
            gram = direct_gram(n, eps)
            theory = predicted(n, eps)
            # The three first spectral power sums are independent full-matrix
            # invariants, evaluated without invoking a spectral solver.
            power = gram
            for p in (1,2,3):
                measured = sum(power[i][i] for i in range(n))
                expected = sum(x**p for x in theory)
                assert abs(measured - expected) < 5e-10, (n, eps, p, measured, expected)
                if p < 3:
                    power = product(power, gram)
            total += 1
    x = predicted(3,.25)
    assert max(abs(a-b) for a,b in zip(x,(1/3,4/3,4/3))) < 1e-13
    for t in (.03,.02,.01):
        x = predicted(3,1-t)
        assert abs(math.sqrt(x[0])/t**2/(4*math.pi**2/(27*math.sqrt(3)))-1)<.015
        assert abs(math.sqrt(x[-1]/x[0])*t*t/(81/(4*math.pi**2))-1)<.015
    print('PASS: %d full-matrix spectral-moment comparisons; quarter-threshold and near-collision checks' % total)


if __name__ == '__main__':
    main()
