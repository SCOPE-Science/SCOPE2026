"""Exact symbolic diagnostics for five equal-width interval Fourier-intensity jets.

Requires Python 3 and SymPy. Proof of the universal theorem is in RESULT.md;
these assertions reproduce the polynomial identities and explicit sharpness witness.
"""
from itertools import combinations
from sympy import Rational, Symbol, Poly, binomial, expand, factor, sign, simplify

u = Symbol('u')
e2,e3,e4,e5 = symbols = [Symbol('e2'), Symbol('e3'), Symbol('e4'), Symbol('e5')]
e = {0:1,1:0,2:e2,3:e3,4:e4,5:e5}
p = {0:5,1:0}
for k in range(2,11):
    if k <= 5:
        p[k] = expand(sum((-1)**(j-1)*e[j]*p[k-j] for j in range(1,k)) + (-1)**(k-1)*k*e[k])
    else:
        p[k] = expand(sum((-1)**(j-1)*e[j]*p[k-j] for j in range(1,6)))

expected = {
    2: -10*e2,
    4: 2*(11*e2**2 - 10*e4),
    6: -5*(14*e2**3 - 30*e2*e4 + 15*e3**2),
    8: 2*(131*e2**4-468*e2**2*e4+316*e2*e3**2-400*e3*e5+290*e4**2),
    10: -5*(206*e2**5-994*e2**3*e4+723*e2**2*e3**2 - 1600*e2*e3*e5 + 1090*e2*e4**2 + 10*e3**2*e4 + 625*e5**2)
}
for order,expr in expected.items():
    calculated=expand(sum((-1)**j * binomial(order,j)*p[j]*p[order-j] for j in range(order+1))/2)
    assert simplify(calculated-expr) == 0, order

brackets = [('-31/10','-29/10'),('-6/5','-9/10'),('0','3/10'),('3/4','1'),('29/10','31/10')]
for c in (1,2):
    poly = u**5-10*u**3+9*u-c
    assert Poly(poly,u).degree() == 5
    for a,b in brackets:
        va = poly.subs(u,Rational(a))
        vb = poly.subs(u,Rational(b))
        assert va*vb < 0,(c,a,b,va,vb)
    vals=[expr.subs({e2:-10,e3:0,e4:9,e5:c}) for expr in expected.values()]
    assert vals[:4] == [100,2020,56500,1824580],vals
    assert vals[-1] == 62684500 - 3125*c*c,vals
# A width of 1/10 is shorter than each gap between the rational root brackets.
assert all(Rational(brackets[j+1][0])-Rational(brackets[j][1]) > Rational(1,10) for j in range(4))
print('PASS: five universal moment identities, two five-root certificates, eight-jet collision, ten-jet separation.')
