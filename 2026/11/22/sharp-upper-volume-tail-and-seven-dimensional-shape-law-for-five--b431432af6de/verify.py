#!/usr/bin/env python3
"""Exact symbolic checks for the five-point spherical-polytope upper-volume law.

Requires SymPy. This is a finite symbolic check of the Hessian and prefactor;
the compactness/localization and limiting-measure arguments are in RESULT.md.
"""
import sympy as S

def main():
    u, v, z1, z2, z3, t2, t3 = x = S.symbols('u v z1 z2 z3 t2 t3', real=True)
    p1 = S.Matrix([0, 0, 1]); p2 = S.Matrix([u, v, -S.sqrt(1-u*u-v*v)])
    base = []
    for z, a in [(z1,0),(z2,2*S.pi/3+t2),(z3,4*S.pi/3+t3)]:
        base.append(S.Matrix([S.sqrt(1-z*z)*S.cos(a), S.sqrt(1-z*z)*S.sin(a), z]))
    vol = S.expand((p1-p2).dot((base[1]-base[0]).cross(base[2]-base[0]))/6)
    origin = {y:S.Integer(0) for y in x}
    star = S.simplify(vol.subs(origin))
    assert star == S.sqrt(3)/2, star
    grad = [S.simplify(S.diff(vol, y).subs(origin)) for y in x]
    assert grad == [0]*7, grad
    H = S.zeros(7)
    for i in range(7):
        for j in range(i+1):
            H[i,j] = H[j,i] = S.simplify(-S.diff(vol, x[i], x[j]).subs(origin)/star)
    expected = S.Matrix([
        [S.Rational(1,2),0,-S.Rational(1,3),S.Rational(1,6),S.Rational(1,6),0,0],
        [0,S.Rational(1,2),0,-S.sqrt(3)/6,S.sqrt(3)/6,0,0],
        [-S.Rational(1,3),0,S.Rational(2,3),0,0,0,0],
        [S.Rational(1,6),-S.sqrt(3)/6,0,S.Rational(2,3),0,0,0],
        [S.Rational(1,6),S.sqrt(3)/6,0,0,S.Rational(2,3),0,0],
        [0,0,0,0,0,S.Rational(2,3),-S.Rational(1,3)],
        [0,0,0,0,0,-S.Rational(1,3),S.Rational(2,3)]])
    assert H==expected
    assert S.factor(H.det())==S.Rational(1,162)
    assert H.eigenvals()=={S.Rational(1,6):2,S.Rational(1,3):1,S.Rational(2,3):1,S.Integer(1):3}
    kappa7=S.pi**S.Rational(7,2)/S.gamma(S.Rational(9,2))
    jac_density=2*S.pi/(4*S.pi)**4
    branches=2*S.binomial(5,2)
    coeff=S.simplify(branches*jac_density*kappa7*2**S.Rational(7,2)/S.sqrt(H.det()))
    assert coeff==S.Rational(24,7),coeff
    print('Maximum volume:',star)
    print('Hessian determinant:',S.factor(H.det()))
    print('Hessian spectrum:',H.eigenvals())
    print('Branch count:',branches)
    print('Sharp coefficient:',coeff)
    print('ALL_CHECKS_PASSED')

if __name__=='__main__': main()
