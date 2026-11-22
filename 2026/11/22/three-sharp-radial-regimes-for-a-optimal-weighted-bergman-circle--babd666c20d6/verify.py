"""Finite diagnostics for a weighted analytic-kernel sampling theorem.
Pure Python 3 standard library; computations are checks, not infinite proofs.
"""
import cmath
import math


def coeffs(p, n):
    b = [1.0]
    for k in range(1, n + 1):
        b.append(b[-1] * k / (p + k - 1))
    return b


def moments(p, n, ell):
    b = coeffs(p, n)
    d = [b[k] * math.exp(ell * k / n) for k in range(n + 1)]
    s = sum(d)
    return s, sum(k * v for k, v in enumerate(d)) / s


def stationarity(p, n, ell):
    _, mean = moments(p, n, ell)
    return mean - p / math.expm1(ell / n)


def optimum(p, n):
    lo, hi = 1e-10, 1.0
    while stationarity(p, n, hi) < 0:
        hi *= 2
    for _ in range(65):
        m = (lo + hi) / 2
        if stationarity(p, n, m) < 0:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def inverse(mat):
    size = len(mat)
    a = [[complex(v) for v in row] + [complex(i == j) for j in range(size)]
         for i, row in enumerate(mat)]
    for i in range(size):
        v = max(range(i, size), key=lambda k: abs(a[k][i]))
        a[i], a[v] = a[v], a[i]
        pivot = a[i][i]
        assert abs(pivot) > 1e-12
        a[i] = [q / pivot for q in a[i]]
        for j in range(size):
            if j != i:
                fac = a[j][i]
                a[j] = [u - fac * v for u, v in zip(a[j], a[i])]
    return [row[size:] for row in a]


def gram(p, n, x, angles, weights):
    a = [1.0 / v for v in coeffs(p, n)]
    return [[(1-x)**p * math.sqrt(a[k] * a[l]) * x**((k+l)/2)
             * sum(w * cmath.exp(1j*(k-l)*t)
                   for w, t in zip(weights, angles))
             for l in range(n+1)] for k in range(n+1)]


def main():
    checks = 0
    for p in (1.25, 1.5, 2., 2.75, 3.5):
        for n in (1, 2, 3, 8, 25, 100):
            ell = optimum(p, n)
            assert ell > 0 and abs(stationarity(p, n, ell)) < 1e-6
            assert stationarity(p, n, ell * 0.9) < 0
            assert stationarity(p, n, ell * 1.1) > 0
            checks += 3
    assert abs(math.exp(-optimum(2., 1)) - .25) < 1e-12
    checks += 1
    for p in (1.4, 2., 3.):
        for n in (2, 3, 4):
            x = 0.42
            ang = [2*math.pi*j/(n+1) for j in range(n+1)]
            weights = [1./(n+1)] * (n+1)
            g = gram(p, n, x, ang, weights)
            d = [(1-x)**p / b * x**k for k,b in enumerate(coeffs(p,n))]
            for i in range(n+1):
                assert abs(g[i][i]-d[i]) < 2e-13
                for j in range(n+1):
                    if i != j:
                        assert abs(g[i][j]) < 2e-13
                    checks += 1
            inv = inverse(g)
            bound = sum(1/y for y in d)
            assert abs(sum(inv[k][k] for k in range(n+1)).real/bound-1)<1e-12
            checks += 1
            for e in (0.08, -0.08):
                ang2 = ang[:]
                ang2[0] += e
                mat = gram(p,n,x,ang2,weights)
                inv2 = inverse(mat)
                assert sum(inv2[k][k].real for k in range(n+1)) > bound + 1e-7
                checks += 1
    for p in (1.4, 1.8):
        v1,v2=optimum(p,1000),optimum(p,10000)
        assert abs(v2-v1)<0.1
        checks+=1
    for n in (1000,10000):
        lc=optimum(2.,n)
        assert math.log(math.log(n)) < lc < math.log(math.log(n))+2
        checks+=1
    for p in (2.5,3.,4.):
        for n in (1000,10000):
            ell=optimum(p,n)
            B=(p-1)/(p-2)
            target=(p-2)*math.log(n)+math.log(p*B/math.gamma(p))
            assert abs(ell-target)<1.2
            checks+=1
    print('PASS:',checks,'finite independent diagnostics')

if __name__ == '__main__':
    main()
