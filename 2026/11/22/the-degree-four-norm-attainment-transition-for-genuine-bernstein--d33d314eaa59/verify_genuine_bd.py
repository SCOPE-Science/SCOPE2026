"""Exact and numerical tests for the genuine Bernstein-Durrmeyer BV error law."""
from fractions import Fraction
from math import comb, sqrt, pi
from itertools import product
import sympy as sp
from scipy.special import betainc
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

s=sp.symbols('s'); q=sp.symbols('q')
def exact_abs_poly(n):
    v=0
    for i in range(n+2):
        for j in range(n):
            v+=abs(i+j-n)*comb(n+1,i)*comb(n-1,j)*s**(i+n-1-j)*(1-s)**(n+1-i+j)
    return sp.expand(v)

low={1:1-2*q,2:1-2*q+4*q*q,3:1-2*q+10*q*q-12*q**3}
for n in (1,2,3):
    expression=exact_abs_poly(n)
    assert sp.expand(expression-low[n].subs(q,s*(1-s)))==0
    assert sp.factor(low[n]-1).subs(q,sp.Rational(1,8))<0
print('EXACT_LOW_DEGREE_POLYNOMIALS_PASS')

for n in range(1,15):
    f=exact_abs_poly(n)
    assert sp.simplify(f.subs(s,sp.Rational(1,2))-sp.Rational(n*comb(2*n,n),4**n))==0
    assert f.subs(s,0)==1 and f.subs(s,1)==1
print('EXACT_CENTRAL_BINOMIAL_AND_ENDPOINT_IDENTITIES_PASS',14)

for n in range(1,17):
    for r in (0.03,0.1,0.23,0.4,0.5,0.77,0.93):
        qq= (lambda x: x**n+sum(comb(n,k)*x**k*(1-x)**(n-k)*(1-betainc(k,n-k,r)) for k in range(1,n)))
        direct=quad(qq,0,r,epsabs=2e-12)[0]+quad(lambda x:1-qq(x),r,1,epsabs=2e-12)[0]
        formula=float(exact_abs_poly(n).subs(s,sp.Rational(str(r))))/(n+1)
        assert abs(direct-formula)<5e-10,(n,r,direct,formula)
print('INDEPENDENT_STEP_RESPONSE_QUADRATURE_PASS',16*7)

for n in (2,3,4,5,8,16,32,64,128,256):
    center=n/(n+1)*comb(2*n,n)/4**n
    if n<=3: assert center<1/(n+1)
    else: assert center>1/(n+1)
    if n>=32: print('CLT_CENTRAL_SANITY',n,round(center*sqrt(n),9), 'target',round(1/sqrt(pi),9))
print('ALL_GENUINE_BD_CHECKS_PASS')
