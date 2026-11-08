"""Analytic-identity and finite-orbit checks for the critical quotient iteration."""
from math import exp,sqrt
import sympy as sp

z,e=sp.symbols('z e')
L=sp.log(1+z)+(2/e)*sp.log(1-e*(1+z)**(1-e)*z)
coeffs=[sp.simplify(sp.limit(sp.diff(L,z,i).subs(z,0)/sp.factorial(i),e,0)) for i in (1,2,3)]
# Generic-epsilon coefficients by a direct Taylor expansion.
Lt=sp.series(L,z,0,4).removeO()
f=sp.series(sp.exp(Lt),z,0,4).removeO().expand()
a=sp.factor(f.coeff(z,2)); b=sp.factor(f.coeff(z,3))
assert sp.simplify(a-(e-2))==0
assert sp.simplify(b-(e**2/sp.Integer(3)-2*e+sp.Rational(8,3)))==0
kappa=sp.factor(2*(a*a+b))
assert sp.simplify(kappa-sp.Rational(4,3)*(2-e)*(5-2*e))==0
assert coeffs==[-1,sp.Rational(-5,2),sp.Rational(1,3)]

def step(u,n):
    if n is None:
        return u*exp(2*u*(1-u))
    return u*(1-(1/n)*u**(1-1/n)*(u-1))**(2*n)

for n in [1,2,3,7,None]:
    v=0.04; u=1+v
    c=float(1/sp.sqrt(kappa.subs(e, 0 if n is None else sp.Rational(1,n))))
    for i in range(200000):
        u=step(u,n)
    est=sqrt(200000)*abs(u-1)
    assert est>c*0.8 and est<c*1.1,(n,est,c)
    print('n=',n,'limit=',c,'finite_iter=',est,'ratio=',est/c)
print('VERIFY_OK exact_coefficients=3 cubic_return=1 finite_orbits=5')
