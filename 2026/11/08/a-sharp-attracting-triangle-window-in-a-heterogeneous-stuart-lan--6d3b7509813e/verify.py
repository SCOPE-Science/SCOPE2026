#!/usr/bin/env python3
"""Exact characteristic and Sturm checks for a three-oscillator mean-zero rotating state.
Requires SymPy >=1.12. Run `python verify.py`.
"""
import sympy as sp

q, lam = sp.symbols('q lam')
r2 = sp.sqrt(2)
a = [sp.Matrix([1, 0]), sp.Matrix([0, r2]), sp.Matrix([-1, -r2])]
assert sum(a, sp.zeros(2,1)) == sp.zeros(2,1)
assert [sp.expand((v.T*v)[0]) for v in a] == [1, 2, 3]
C = sp.Matrix([[q, -4*q], [4*q, q]])
J = sp.zeros(6)
for j, v in enumerate(a):
    J[2*j:2*j+2, 2*j:2*j+2] += -2*v*v.T
    for k in range(3):
        J[2*j:2*j+2, 2*k:2*k+2] += C

P3 = 459*q**3 - 486*q**2 + 404*q - 240
P5 = 70227*q**5 - 78489*q**4 + 51678*q**3 - 24584*q**2 + 6408*q - 1440
P6 = (14326308*q**6 - 16456527*q**5 + 10608102*q**4
      - 4917328*q**3 + 1178872*q**2 - 215616*q + 17280)
coeffs = [sp.Integer(1), 12-6*q, 44-60*q+153*q**2,
          48-176*q+1224*q**2, 2652*q**2-144*q, 1632*q**2]
p5 = sum(coeffs[k]*lam**(5-k) for k in range(6))
assert sp.expand(J.charpoly(lam).as_expr() - lam*p5) == 0
# Reflection conjugates the Jacobian to its transpose and preserves every eigenvalue.
R = sp.diag(1,-1,1,-1,1,-1)
mirror = sp.zeros(6)
for j,v in enumerate(a):
    mv = sp.diag(1,-1)*v
    mirror[2*j:2*j+2,2*j:2*j+2] += -2*mv*mv.T
    for k in range(3):
        mirror[2*j:2*j+2,2*k:2*k+2] += C
assert sp.simplify(mirror - R*J.T*R) == sp.zeros(6)

# Hurwitz matrix for degree five (the zero symmetry eigenvalue is factored out).
a1,a2,a3,a4,a5 = coeffs[1:]
H = sp.Matrix([[a1,a3,a5,0,0], [1,a2,a4,0,0],
               [0,a1,a3,a5,0], [0,1,a2,a4,0], [0,0,a1,a3,a5]])
expected = [a1, -2*P3, -16*P5, -192*q*P6, -313344*q**3*P6]
for n in range(1, 6):
    assert sp.factor(H[:n,:n].det() - expected[n-1]) == 0

# Rational Sturm certificates; counts are computed by exact rational arithmetic.
for poly, whole, windows in [
    (P3, 1, [(sp.Rational(78,100),sp.Rational(79,100),1)]),
    (P5, 1, [(sp.Rational(59,100),sp.Rational(60,100),1)]),
    (P6, 2, [(sp.Rational(14,100),sp.Rational(15,100),1),
             (sp.Rational(58,100),sp.Rational(59,100),1)]),
]:
    obj = sp.Poly(poly,q, domain='ZZ')
    assert obj.count_roots(0, 2) == whole
    for left,right,number in windows:
        assert obj.count_roots(left,right) == number
assert P3.subs(q,0)<0 and P5.subs(q,0)<0
assert P6.subs(q,0)>0 and P6.subs(q,sp.Rational(1,5))<0 and P6.subs(q,sp.Rational(3,5))>0
root_windows = ((sp.Rational(14,100),sp.Rational(15,100)),
                (sp.Rational(58,100),sp.Rational(59,100)))
assert all(sp.Poly(P6,q).count_roots(*br)==1 for br in root_windows)
# The roots are simple; the endpoints are thus transverse linear spectral transitions.
assert sp.gcd(sp.Poly(P6,q),sp.Poly(sp.diff(P6,q),q)).degree()==0
assert sp.factor(P6.subs(q,sp.Rational(1,5)))<0
# Direct Routh-Hurwitz sign check at a representative, strictly stable parameter.
assert all(sp.sign(x.subs(q,sp.Rational(1,5)))==1 for x in expected)
print('VERIFY_OK characteristic_degree=6 symmetry_zero=1 hurwitz_minors=5 sturm_polynomials=3 real_root_brackets=4 stable_witness_q=1/5')
print('spectral_thresholds=', [float(sp.nroots(P6)[i]) for i in range(2) if sp.im(sp.nroots(P6)[i])==0])
