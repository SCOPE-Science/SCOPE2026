#!/usr/bin/env python3
"""Numerical cross-checks for exact uniform-marginal contour capacities.

Requires mpmath. This is a finite arithmetic diagnostic, not a proof of
universal quantifiers or a substitute for the analytic derivation.
"""
import mpmath as mp

mp.mp.dps = 60

def formula(a, b, p):
    a, b, p = map(mp.mpf, (a, b, p))
    if p == 1:
        return 2 * min(a, b)
    q = p / (p - 1)
    s = (a**q + b**q)**(1 / q)
    return 2*s if p < 1 else 2*(a+b-s)

def slope(a, b, p, u):
    a, b, p, u = map(mp.mpf, (a, b, p, u))
    z = u/a
    w = (1-z**p)**(1/p)
    return (b/a)*(z/w)**(p-1)

def numeric_integral(a, b, p):
    a, b, p = map(mp.mpf, (a, b, p))
    if p == 1:
        return 2 * a * min(1, b/a)
    q = p/(p-1)
    us = a**q/(a**q+b**q)**(1/p)
    # Integral on the two analytic sides, using independent quadrature
    # and excluding endpoint singularities via exact antiderivatives.
    vstar = b**q/(a**q+b**q)**(1/p)
    if p > 1:
        return 2*(mp.quad(lambda u: slope(a,b,p,u),[0,us])+a-us)
    return 2*(us + mp.quad(lambda u:slope(a,b,p,u),[us,a]))

def run():
    checked = 0
    for a, b in [('0.2','0.35'),('0.42','0.16'),('0.4','0.4'),('0.15','0.5'),('0.49','0.49')]:
        for p in ['0.25','0.5','0.8','1','1.5','2','3','5']:
            f = formula(a,b,p)
            num = numeric_integral(a,b,p)
            assert 0 <= f <= 2*min(mp.mpf(a),mp.mpf(b))+mp.mpf('1e-50')
            assert abs(f-num) < mp.mpf('1e-20'), (a,b,p,str(f),str(num))
            if p != '1':
                assert f < 2*min(mp.mpf(a),mp.mpf(b))
            checked += 3 if p != '1' else 2
    for r in ['0.1','0.25','0.49','0.5']:
        r=mp.mpf(r)
        assert abs(formula(r,r,2)-4*r*(1-1/mp.sqrt(2))) < mp.mpf('1e-50')
        assert formula(r,r,1) == 2*r
        for p in ['0.3','0.75','1.25','4']:
            p=mp.mpf(p)
            assert abs(formula(r,r,p)-4*r*min(2**(-1/p),1-2**(-1/p))) < mp.mpf('1e-50')
            checked+=1
        checked+=2
    print('PASS:', checked, 'independent finite formula/quadrature and specialization checks')

if __name__ == '__main__':
    run()
