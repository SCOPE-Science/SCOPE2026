"""Independent exact checks for the projective boundary and marked smooth point.

All formulas are integral, so checking the polynomial equalities proves them
in every characteristic. No external data are used.
"""
from sympy import symbols, expand, diff
u, v, t = symbols('u v t')
f_a=u**3*v**3 + u**3 + v**3 + u + v
f_b=f_a+u**2+v**2
for tag, f, target in (
    ('A', f_a, v**3+1+t**2+t**3*(v**3+v)),
    ('B', f_b, v**3+1+t+t**2+t**3*(v**3+v**2+v)),
):
    # t^3 f(1/t,v) as a polynomial, without division
    poly=expand(f.subs(u,1/t)*t**3)
    assert expand(poly-target)==0, (tag, poly)
    assert expand(f - f.xreplace({u:v,v:u}))==0
    assert poly.subs(t,0)==v**3+1
    assert expand(diff(poly,t).subs(t,0) - (0 if tag=='A' else 1))==0
    assert f.subs({u:0,v:0})==0
    assert diff(f,u).subs({u:0,v:0})==1
    assert diff(f,v).subs({u:0,v:0})==1
    # coefficient of u^3 v^3 is 1: (infinity,infinity) lies outside curve.
    assert f.coeff(u,3).coeff(v,3)==1
print('PASS: boundary charts, factor-exchange symmetry, marked smooth point')
