#!/usr/bin/env python3
"""Independent arithmetic diagnostics for the stated large-delay polynomial asymptotic.

Uses mpmath and sympy. Numerical computations are not a proof for all delays.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 60

e, a, b = sp.symbols("e a b", positive=True)
z1, z2 = sp.symbols("z1 z2")
z0 = sp.I * sp.pi
z = z0 + z1 * e + z2 * e**2
H = (z-z0) + sp.log(1 + (sp.exp(e*z)-1)/b)
coef1 = sp.series(H,e,0,3).removeO().expand().coeff(e,1)
coef2 = sp.series(H,e,0,3).removeO().expand().coeff(e,2)
assert sp.simplify(coef1.subs(z1,-sp.I*sp.pi/b)) == 0
coef2 = coef2.subs(z1,-sp.I*sp.pi/b)
assert sp.simplify(coef2.subs(z2,sp.I*sp.pi/b**2 - (1-b)*sp.pi**2/(2*b**2))) == 0

for h in (1, 2):
    h = mp.mpf(h)
    X = (h + mp.sqrt(h*h+4*h))/2
    bb = X-h
    aa = 1-bb
    assert abs(X*bb-h) < mp.mpf('1e-55')
    C = aa*mp.pi**2/(2*bb**2)
    errors = []
    for N in (100, 300, 1000):
        guess = 1j*mp.pi*(1-1/(bb*N))
        f = lambda zz: mp.exp(zz)*(mp.exp(zz/N)-aa)+bb
        zz = mp.findroot(f, (guess, guess+mp.mpf('0.0001')))
        lam = mp.exp(zz/N)
        residual = abs(lam**(N+1)-aa*lam**N+bb)
        assert residual < mp.mpf('1e-45'), (h,N,residual)
        assert abs(lam) < 1
        measured = -N**3 * mp.log(abs(lam))
        errors.append(abs(C-measured))
        print('h=',mp.nstr(h,2), 'N=',N, 'scaled gap=',mp.nstr(measured,12), 'limit=',mp.nstr(C,12), 'root residual=',mp.nstr(residual,3))
    assert errors[2] < errors[1] < errors[0]
print('symbolic and high-precision numerical diagnostics passed')
