#!/usr/bin/env python3
"""Reproducible algebraic and numerical checks for a Gaussian Langevin information transition.

Run with Python 3, sympy and mpmath. This checks identities and examples;
the global root-count and asymptotic claims use the analytical proof in RESULT.md.
"""
import sympy as S
import mpmath as M

b, z, d = S.symbols('b z d', real=True)
C = S.Matrix([
    [(2+b*b*d)/(2*(1-b*b)), -b*(2+d)/(2*(1-b*b))],
    [-b*(2+d)/(2*(1-b*b)), (2+(2-b*b)*d)/(2*(1-b*b))],
])
K = S.Matrix([[1,b],[b,1]])
B = S.diag(1,1+d)
assert S.simplify(K*C+C*K-2*B) == S.zeros(2)
Cinv = C.inv()
Ibb = S.factor(S.trace(Cinv*C.diff(b)*Cinv*C.diff(b))/2)
Ibd = S.factor(S.trace(Cinv*C.diff(b)*Cinv*C.diff(d))/2)
Idd = S.factor(S.trace(Cinv*C.diff(d)*Cinv*C.diff(d))/2)
F = ((d+2)**2*(4*(1+d)*(1+z)+d*d*z*(3-z)) /
     ((1-z)**2*(4+4*d+d*d*z)**2))
assert S.cancel(Ibb-F.subs(z,b*b)) == 0
assert S.cancel(Ibd - b*(d+2)*(4+b*b*d*(4+d)) /
                 ((1-b*b)*(4+4*d+b*b*d*d)**2)) == 0
assert S.cancel(Idd - (4*(2-b*b)+b*b*d*(4+b*b*d)) /
                 ((4+4*d+b*b*d*d)**2)) == 0

P = (2*d**4*z**3-(9*d**4+12*d**3+12*d**2)*z**2
     +(3*d**4-16*d**3-32*d**2-32*d-16)*z
     -(4*d**3+52*d**2+96*d+48))
assert S.cancel(S.diff(F,z) - ((d+2)**2*P /
                                ((z-1)**3*(d*d*z+4*d+4)**3))) == 0
assert S.expand(P.subs(z,0)+4*(d+1)*(d*d+12*d+12)) == 0
assert S.factor(P.subs(z,1)) == -4*(d+2)**4
assert S.expand(S.diff(P,z,2)-(12*d**4*z-18*d**4-24*d**3-24*d**2)) == 0
A = 2*z**3-9*z**2+3*z
B1 = 12*z*z+16*z+4
B2 = 12*z*z+32*z+52
B3 = 32*z+96
B4 = 16*z+48
assert S.cancel(P/d**4-(A-B1/d-B2/d**2-B3/d**3-B4/d**4)) == 0

# Exact-rational derivatives on a grid, including both sides of the transition.
checks = 0
for dd in [S.Rational(0),S.Rational(1),S.Rational(5),S.Rational(30),
           S.Rational(33),S.Rational(34),S.Rational(40),S.Rational(100)]:
    for j in range(1,20):
        zz = S.Rational(j,20)
        derivative = S.diff(F,z).subs({z:zz,d:dd})
        exact_sign = S.sign(derivative)
        poly_sign = -S.sign(P.subs({z:zz,d:dd}))
        assert exact_sign == poly_sign
        checks += 1

M.mp.dps = 50
p = lambda x,y: 2*y**4*x**3-(9*y**4+12*y**3+12*y**2)*x**2 + (3*y**4-16*y**3-32*y**2-32*y-16)*x-(4*y**3+52*y**2+96*y+48)
pz = lambda x,y: 6*y**4*x**2-(18*y**4+24*y**3+24*y**2)*x + 3*y**4-16*y**3-32*y**2-32*y-16
zc, dc = M.findroot((p,pz), (M.mpf('0.139'),M.mpf('33.22')))
assert M.mpf('0.13893864044866') < zc < M.mpf('0.13893864044867')
assert M.mpf('33.21953733337') < dc < M.mpf('33.21953733339')
assert abs(p(zc,dc)) < M.mpf('1e-38')
assert abs(pz(zc,dc)) < M.mpf('1e-38')

for dd, expect in [(10,0),(30,0),(40,2),(50,2),(100,2),(1000,2)]:
    poly = S.Poly(P.subs(d,dd),z)
    roots = S.nroots(poly,maxsteps=200)
    interior = [float(S.re(x)) for x in roots if abs(float(S.im(x))) < 1e-10 and
                0 < float(S.re(x)) < 1]
    assert len(interior)==expect
    if expect == 2:
        assert interior[0] < interior[1]

print('Lyapunov, Gaussian Fisher matrix, derivative, endpoint and normalization identities: PASS')
print('Exact rational derivative sign cross-checks:', checks)
print('Bifurcation root and finite numerical checks: PASS')
print('d_critical =', M.nstr(dc,27))
print('z_critical =', M.nstr(zc,27))
print('b_critical =', M.nstr(M.sqrt(zc),24))
print('Numerical checks are not a substitute for the universal proof.')
