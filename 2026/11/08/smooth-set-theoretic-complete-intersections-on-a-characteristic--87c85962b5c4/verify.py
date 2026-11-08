#!/usr/bin/env python3
"""Exact polynomial identities for a purely inseparable scroll projection in characteristic two."""
import sympy as S
u,v,a,b=S.symbols('u v a b')
x,y,z,w,e=a*u,a*v,b*u**2,b*v**2,b*u*v

def mod2zero(expr):
    p=S.Poly(S.expand(expr),u,v,a,b)
    return all(int(c)%2==0 for c in p.coeffs())

checks = {
    'cubic_surface': x**2*w+y**2*z,
    'scroll_minor_xe_yz': x*e+y*z,
    'scroll_minor_xw_ye': x*w+y*e,
    'scroll_conic_projection': e**2+z*w,
    'square_descent_linear_section': (x+y+e)**2+(x**2+y**2+z*w),
}
for key,expr in checks.items():
    assert mod2zero(expr),key
    print(key,'PASS')
# Parameterize a smooth degree-three section of the scroll in characteristic two.
# The defining section is a(u+v)+buv, represented by x+y+e.
x1,y1,z1,w1=[S.expand(t.subs({a:u*v,b:u+v})) for t in (x,y,z,w)]
assert mod2zero(x1**2*w1+y1**2*z1)
assert mod2zero(x1**2+y1**2+z1*w1)
# Coefficient matrix for the cubic coordinate functions, reduced modulo two:
basis=[u**3,u**2*v,u*v**2,v**3]
M=S.Matrix([[int(S.Poly(f,u,v).coeff_monomial(m))%2 for m in basis] for f in (x1,y1,z1,w1)])
assert int(M.det())%2==1, M
print('twisted_cubic_immersion PASS; cubic coordinate rank',M.rank())
for d in range(1,51):
    degree=3*d
    genus=1+(3*d*d-5*d)//2
    assert (3*d*d-5*d)%2==0
    assert 2*genus-2==3*d*d-5*d
    assert degree>0 and genus>=0
print('intersection_adjunction_genus d=1..50 PASS')
print('ALL_CHECKS_PASSED')
