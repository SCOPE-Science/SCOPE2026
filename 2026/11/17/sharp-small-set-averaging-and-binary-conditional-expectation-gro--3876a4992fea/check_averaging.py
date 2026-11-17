#!/usr/bin/env python3
"""Finite numerical diagnostics for mixed-norm atom averages."""
from math import isclose, log, exp


def conjugate(p):
    return p / (p - 1.0)


def sharp_constant(p, q):
    if p == q:
        return 1.0
    if p < q:
        a, b = 1.0/q, 1.0/conjugate(p)
    else:
        a, b = 1.0/conjugate(q), 1.0/p
    return exp(a*log(a) + b*log(b) - (a+b)*log(a+b))


def c_star(p, q):
    if p < q:
        a, b = 1.0/q, 1.0/conjugate(p)
    else:
        a, b = 1.0/conjugate(q), 1.0/p
    return b/(a+b)


def two_height_norm(p, q, t, c):
    w = c*t
    h = t*(1.0-c)/(1.0-w)
    assert 0.0 < h < 1.0
    assert isclose(w+(1.0-w)*h, t, rel_tol=1e-12, abs_tol=1e-16)
    a, b = p/q, conjugate(p)/conjugate(q)
    ia = w+(1.0-w)*h**a
    ib = w+(1.0-w)*h**b
    return (ia**(1.0/p)) * (ib**(1.0/conjugate(p))) / t


def run():
    checks=0
    pairs = [(2.0,4.0),(4.0,2.0),(1.5,5.0),(5.0,1.5),(2.5,3.5),(3.5,2.5)]
    for p,q in pairs:
        c=c_star(p,q)
        C=sharp_constant(p,q)
        assert 0.0<c<1.0 and 0.0<C<1.0
        checks+=1
        errors=[]
        for t in [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]:
            k=two_height_norm(p,q,t,c)
            d=abs(1.0/p-1.0/q)
            scaled=k*t**d
            assert k >= 1.0-1e-10
            assert k <= t**(-d)*(1.0+1e-12)
            assert isclose(k,two_height_norm(conjugate(p),conjugate(q),t,c),rel_tol=1e-12)
            checks+=3
            errors.append(abs(scaled-C))
        assert errors[-1] < errors[0]
        checks+=1
        assert errors[-1] < 0.04
        checks+=1
    print('MIXED_ATOM_AVERAGING_DIAGNOSTICS_OK',checks)


if __name__=='__main__':
    run()
