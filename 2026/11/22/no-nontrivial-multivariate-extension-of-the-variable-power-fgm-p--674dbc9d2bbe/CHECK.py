#!/usr/bin/env python3
"""Symbolic support for the exact multivariate power-product copula theorem.

This verifies finite-dimensional algebra, not the infinite-dimensional proof.
Dependencies: Python 3 and SymPy. No network, data file, or random seed required.
"""
from itertools import combinations
import sympy as sp


def face_formula(xs, a, face):
    rem = [u for u in xs if u not in face]
    p = sp.prod(rem)
    q = sp.prod(1-u for u in rem)
    return sp.expand_mul(p * (1 + a * (-1)**len(face) * q * sp.log(p)))


def prove_symbolic_face_identities():
    a = sp.Symbol('a', real=True)
    checked = 0
    for n in range(3, 7):
        xs = sp.symbols(f'u0:{n}', positive=True)
        C = sp.prod(xs)**(1 + a*sp.prod(1-u for u in xs))
        for k in range(1, n):
            for face in combinations(xs, k):
                direct = sp.diff(C, *face).subs({u: 1 for u in face}, simultaneous=True)
                expected = face_formula(xs, a, face)
                assert sp.simplify(sp.expand_log(direct - expected, force=True)) == 0, (n, face)
                checked += 1
    return checked


def prove_remaining_derivative_identities():
    x, y, z, b = sp.symbols('x y z b', positive=True)
    k = z * (1+b*(1-z)*sp.log(z))
    expected_k = 1 + b*((1-2*z)*sp.log(z) + 1-z)
    assert sp.simplify(sp.diff(k,z)-expected_k) == 0
    f = lambda v: v*(1-v)
    h = x*y + b*f(x)*f(y)*sp.log(x*y)
    D = ((1-2*x)*(1-2*y)*sp.log(x*y)
         + (1-2*x)*(1-y)+(1-x)*(1-2*y))
    assert sp.simplify(sp.diff(h,x,y)-(1+b*D)) == 0
    d_quarter = ((1-2*x)*sp.log(x/sp.Integer(4))/2
                 + sp.Rational(3,4)*(1-2*x) + (1-x)/2)
    assert sp.simplify(D.subs(y,sp.Rational(1,4))-d_quarter) == 0
    assert sp.limit(expected_k.subs(b, 1),z,0,dir='+') == -sp.oo
    assert sp.limit(d_quarter,x,0,dir='+') == -sp.oo
    return 5


def certify_negative_rational_boundaries():
    # Rigorous log(2)>1/2, since integral_1^2 1/t dt > 1/2.
    x = sp.Rational(1, 256)
    z = x
    # For one-free-coordinate face and b1=1:
    # c1 = 2-z -8(1-2z) log(2), bounded from above by:
    upper1 = 2-z-4*(1-2*z)
    assert upper1 < 0
    # For two-free-coordinate face and b2=1, y=1/4:
    # c2=1+(1-2x)/2*log(x/4)+3/4*(1-2x)+(1-x)/2.
    # Since log(x/4)=-10log(2)<-5, the upper bound is rational.
    upper2 = 1-sp.Rational(5,2)*(1-2*x)+sp.Rational(3,4)*(1-2*x)+(1-x)/2
    assert upper2 < 0
    return upper1, upper2


if __name__ == '__main__':
    identities = prove_symbolic_face_identities()
    auxiliary = prove_remaining_derivative_identities()
    bounds = certify_negative_rational_boundaries()
    print('face identities (dimensions 3..6):', identities)
    print('derivative/limit identities:', auxiliary)
    print('certified negative upper bounds:', *(str(v) for v in bounds))
    print('PASS; the all-n theorem is proved in RESULT.md')
