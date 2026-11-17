#!/usr/bin/env python3
"""Reproducible exact-map identities and finite diagnostics for the SISI edge theorem.

Requires Python 3 and SymPy. Finite iterations illustrate but do not prove limits.
"""
from fractions import Fraction
import sympy as sp


def exact_identities():
    x, u, y, v, b = sp.symbols('x u y v b')
    i = u + v
    X = x + b * (1 - x) - 2 * b * i * x
    U = (1 - 2 * b) * u + 2 * b * i * x
    Y = (1 - b) * y + b * u - 2 * b * i * y
    V = (1 - b) * v + 2 * b * i * y
    z = u + 2 * v
    q = y - i
    claims = [
        X + U + Y + V - 1,
        (U + 2 * V) - z - 2 * b * i * q,
        (Y - U - V) - (1 - b - 2 * b * i) * q + 2 * b * v,
        (Y - U - V) - q + b * q + 2 * b * i * q + 2 * b * v,
    ]
    for j, formula in enumerate(claims, 1):
        assert sp.factor(formula.subs(x, 1 - u - y - v)) == 0, j
    # The doubly neutral parameter equalities in the parent SISI map.
    alpha, beta1, beta2, k1, k2 = b, 2*b, 2*b, 1, 1
    assert sp.expand(beta1*k1 - (b+alpha)) == 0
    assert sp.expand(b*(b+alpha) - alpha*beta2*k2) == 0
    print('PASS: 4 symbolic update identities and 2 threshold identities')


def check_orbit(b, state, n=400_000):
    x, u, y, v = map(float, state)
    B = float(b)
    assert abs(x+u+y+v-1) < 1e-12
    for k in range(n):
        i = u+v
        x, u, y, v = (
            x+B*(1-x)-2*B*i*x,
            (1-2*B)*u+2*B*i*x,
            (1-B)*y+B*u-2*B*i*y,
            (1-B)*v+2*B*i*y,
        )
        if k % 50000 == 0:
            assert -1e-10 <= min(x,u,y,v)
            assert abs(x+u+y+v-1) < 2e-8
    z = u+2*v
    target = 1/(16*B)
    assert abs(n*z*z/target - 1) < 0.06, (b,state,n*z*z,target)
    assert abs(v/(z*z)-2) < 0.10, (b,state,v/z**2)
    assert abs((y-u-v)/(z*z)+4) < 0.20, (b,state,(y-u-v)/z**2)
    print(f'PASS: b={B:.6g}, initial={state}, n*z_n^2={n*z*z:.8g}, limit={target:.8g}')


def boundary_check():
    b=Fraction(1,4)
    x,u,y,v = Fraction(1,2), Fraction(0), Fraction(1,2), Fraction(0)
    for n in range(1,25):
        i=u+v
        x,u,y,v=(x+b*(1-x)-2*b*i*x,(1-2*b)*u+2*b*i*x,(1-b)*y+b*u-2*b*i*y,(1-b)*v+2*b*i*y)
        assert u==v==0 and y==Fraction(1,2)*(1-b)**n
    print('PASS: exact infection-free exceptional orbit')


if __name__ == '__main__':
    exact_identities()
    boundary_check()
    for B, P in [
        (Fraction(1,10),(Fraction(3,10),Fraction(1,5),Fraction(2,5),Fraction(1,10))),
        (Fraction(1,4),(Fraction(0),Fraction(1),Fraction(0),Fraction(0))),
        (Fraction(1,3),(Fraction(0),Fraction(0),Fraction(0),Fraction(1))),
        (Fraction(1,4),(Fraction(3,10),Fraction(1,5),Fraction(2,5),Fraction(1,10))),
    ]:
        check_orbit(B,P)
    print('ALL CHECKS PASSED; finite diagnostics are not a proof of the theorem')
