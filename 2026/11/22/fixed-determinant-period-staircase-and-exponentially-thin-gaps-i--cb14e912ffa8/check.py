#!/usr/bin/env python3
"""Finite high-precision diagnostics for a fixed-determinant max-plus staircase.
The analytic proof is in RESULT.md; numerical tests do not certify all n.
Requires mpmath. Run: python check.py
"""
import mpmath as mp
mp.mp.dps = 120

def threshold(r, n, u):
    theta_seed = mp.pi / (n + 1 - 1 / (r - 1))
    def f(theta):
        A = 1 + r*r - 2*r*mp.cos(theta)
        psi = mp.atan(mp.sin(theta) / (r - mp.cos(theta)))
        z = (1/A - u)*mp.sqrt(A)*mp.sin(theta)/r**(n+1)
        return (n+1)*theta - psi - mp.pi - mp.asin(z)
    theta = mp.findroot(f, (theta_seed*mp.mpf('0.99999'), theta_seed*mp.mpf('1.00001')))
    return 2*r*mp.cos(theta)

def test(r, n):
    D = r*r
    lower = threshold(r,n-1,1/D)
    a = threshold(r,n,0)
    b = threshold(r,n,1/D)
    assert 0 < lower < a < b < 2*r
    T = (lower+a)/2
    x,y = mp.mpf(1),mp.mpf(1)
    first_negative = None
    two_negative = False
    for j in range(n+2):
        if x<0 and first_negative is None:
            first_negative=j
            two_negative = y<0
        x,y = y+max(0,T*x),1-max(0,D*x)
    assert first_negative == n and two_negative
    assert mp.almosteq(x,1,abs_eps=mp.mpf('1e-80'))
    assert mp.almosteq(y,1,abs_eps=mp.mpf('1e-80'))
    gap = b-a
    width = a-lower
    gap_approx = 2*mp.pi**2*(r-1)*r**(-n)/(r**2*n**3)
    width_approx = 2*r*mp.pi**2/n**3
    q = (gap/width)/((r-1)*r**(-n)/r**3)
    print('r=',mp.nstr(r,8),'n=',n,'period=',n+2,
          'gap/coefficient=',mp.nstr(gap/gap_approx,9),
          'window/coefficient=',mp.nstr(width/width_approx,9),
          'ratio/coefficient=',mp.nstr(q,9))

if __name__ == '__main__':
    for rtext in ['1.1','1.414213562373095048801688724209698','2','3']:
        for n in [40,80,150]:
            test(mp.mpf(rtext),n)
    print('FINITE CHECKS PASSED')
