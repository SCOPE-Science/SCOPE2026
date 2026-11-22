"""Supplementary reproducible checks for the SIS-logit equilibrium-fold theorem.

Run with Python 3.9 or later: python3 verify.py
All continuous claims follow from the analytic proof, not from this finite checker.
"""
import math


def logistic_pos(z):
    """exp(z)/(1+exp(z)), stably for nonnegative z."""
    return 1.0 / (1.0 + math.exp(-z))


def response(z):
    return 1.0 - logistic_pos(z)


def g(t, c, d):
    return (1.0 - t) * logistic_pos(c + d * t)


def dg(t, c, d):
    p = logistic_pos(c + d * t)
    return p * (-1.0 + (1.0 - t) * d * (1.0 - p))


def peak(c, d):
    assert d > 1 + math.exp(c)
    # Principal Lambert W: w + log(w) = c+d-1.
    h = c + d - 1.0
    lo, hi = 1e-15, max(1.0, h)
    for _ in range(150):
        mid = (lo + hi) / 2.0
        if mid + math.log(mid) < h:
            lo = mid
        else:
            hi = mid
    w = (lo + hi) / 2.0
    return 1.0 - (1.0 + w) / d, w / d


def root(f, a, b):
    fa, fb = f(a), f(b)
    assert fa * fb < 0, (a, b, fa, fb)
    for _ in range(100):
        m = (a + b) / 2
        if (f(m) > 0) == (fa > 0):
            a, fa = m, f(m)
        else:
            b = m
    return (a + b) / 2


def field(x, i, beta, gamma, c, d):
    return (response(c + d * i) - x,
            beta * (1.0 - x) * i * (1.0 - i) - gamma * i)


def jacobian(x, i, beta, gamma, c, d):
    p = logistic_pos(c + d * i)
    return ((-1.0, -d * p * (1.0 - p)),
            (-beta * i * (1.0 - i),
             beta * (1.0 - x) * (1.0 - 2.0 * i) - gamma))


def check(c, d, k):
    assert 0 < c < 5 and 1.0 + math.exp(c) < d < 35
    t, height = peak(c, d)
    assert 0 < t < 1
    assert abs(g(t, c, d) - height) < 1e-12
    assert abs(dg(t, c, d)) < 1e-11
    assert 1.0 / (1.0 - t) - d / (1.0 + math.exp(c + d * t)) < 1e-11
    assert g(0, c, d) < k < height
    a = root(lambda j:g(j, c, d)-k, 0.0, t)
    b = root(lambda j:g(j, c, d)-k, t, 1.0)
    assert 0 < a < t < b < 1
    for j,expected in ((a,-1),(b,+1)):
        x = response(c+d*j)
        f1, f2 = field(x,j,1.0,k,c,d)
        assert abs(f1)<1e-13 and abs(f2)<1e-13
        J=jacobian(x,j,1.0,k,c,d)
        trace=J[0][0]+J[1][1]
        determinant=J[0][0]*J[1][1]-J[0][1]*J[1][0]
        assert abs(determinant + j*dg(j,c,d)) < 1e-11
        assert trace < 0 and expected*determinant > 0
    assert response(c) > 0 and logistic_pos(c) < k
    return t,height,a,b


def main():
    checks=0
    for c in [0.15,0.5,1.0,1.5,2.0]:
        for d in [1.0+math.exp(c)+v for v in [0.2,1.0,3.0,10.0,18.0]]:
            t,h=peak(c,d)
            for r in [0.05,0.15,0.35,0.5,0.75,0.9,0.95]:
                k=(1.0-r)*logistic_pos(c)+r*h
                check(c,d,k)
                checks+=1
    assert math.e < 4 and math.e**3 > 8
    t,h,a,b=check(1,20,0.8)
    assert g(0.0,1,20)<0.8<g(0.1,1,20)
    assert abs(a-0.026390022711719644)<1e-10
    assert abs(b-0.1939116387789299)<1e-10
    assert abs(t-0.09212194768922244)<1e-10
    print('Supplementary checked parameter triples:',checks)
    print('Rational-witness peak location, peak height:',f'{t:.15f}',f'{h:.15f}')
    print('Rational-witness endemic prevalences:',f'{a:.15f}',f'{b:.15f}')
    print('Rational-witness endemic cooperation shares:',f'{response(1+20*a):.15f}',f'{response(1+20*b):.15f}')
    print('All supplementary checks PASS')


if __name__=='__main__':
    main()
