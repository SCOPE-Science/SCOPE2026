#!/usr/bin/env python3
"""Finite diagnostics of a deterministic two-coordinate exponential recurrence.

No finite numerical calculation is used in place of the analytical proof.
"""
import math


def sample(x0, y0, beta, s, n):
    x, y = float(x0), float(y0)
    data = [(x, y)]
    for _ in range(n):
        x, y = x * math.exp(-x - beta*y*y), (1-s)*y + s*x
        data.append((x, y))
    return data


def checks():
    x0, beta = 0.4, 1.2
    for s, y0 in [(0.35, -0.1), (1.6, 0.9)]:
        v = sample(x0, y0, beta, s, 20000)
        assert all(0 < x <= 1/(n + 1/x0) + 1e-11 for n, (x, y) in enumerate(v))
        n = len(v)-1
        x, y = v[-1]
        assert abs(n*x - 1) < 0.003
        assert abs(n*n*(y-x)-1/s) < 0.08
        assert abs((1/x-n-(beta+0.5)*math.log(n)) -
                   (1/v[10000][0]-10000-(beta+0.5)*math.log(10000))) < 0.03
    # Every finite trajectory satisfies an exact signed sum identity at s=2.
    for y0 in [0.0, 0.5, 0.8]:
        v=sample(x0, y0, beta, 2.0, 120)
        summation=0.0
        for n, (x,y) in enumerate(v):
            assert abs(((-1)**n)*y - (y0-2*summation)) < 1e-11
            if n < len(v)-1:
                summation += ((-1)**n)*x
                xn, yn=v[n+1]
                eta=x+beta*y*y
                assert abs(xn-x*math.exp(-eta)) < 1e-14
                if n+2 < len(v):
                    x2,y2=v[n+2]
                    p=y/x-1; p2=y2/x2-1
                    eta1=xn+beta*yn*yn
                    b=math.exp(eta1)*(2-math.exp(eta))-1
                    assert abs(p2-(x/x2*p+b)) < 1e-12*max(1.0, abs(p2))
    # An approximate endpoint bracket is only a finite numerical diagnostic.
    for y0, expected in [(0,-1), (2*x0,1)]:
        v=sample(x0,y0,beta,2.0,8000)
        n=len(v)-1
        Ahat=(-1)**n*v[-1][1]
        assert Ahat*expected>0
    print('Finite identity, endpoint sign, and asymptotic diagnostics: PASS')


if __name__=='__main__':
    checks()
