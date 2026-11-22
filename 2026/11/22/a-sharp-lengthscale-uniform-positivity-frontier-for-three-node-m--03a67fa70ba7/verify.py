"""Reproducible checks for symmetric Matérn-3/2 kernel quadrature.

Run with Python 3, SymPy, and mpmath. Numerical checks are supplementary;
the accompanying analytic inequalities prove the all-parameter statements.
"""
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 90
z, b, q, E, t = sp.symbols('z b q E t', positive=True)

# Symbolic center-numerator factorization, using independent exponential placeholders.
k = (1+z)*q
j = (1+2*z)*q**2
m0t = 2-(2+t)*E
mat = 2-E*((2+t)*(q+1/q)/2-z*(1/q-q)/2)
N = (1+j)*m0t-2*k*mat
factored = (1-q)*(2*(1-(1+2*z)*q)+E*z*(1+q)*(1+t-z))
assert sp.simplify(sp.expand(N-factored)) == 0
assert sp.simplify(1+j-2*k*k-(1-(1+2*z+2*z*z)*q*q)) == 0

# Center flat limit and four leading sign coefficients.
a = sp.symbols('a', positive=True)
bcoeff = sp.symbols('B', real=True)
F = 2*(sp.exp(z)-1-2*z)+z*(1+sp.exp(-z))*(1+bcoeff*z)*sp.exp(-bcoeff*z)
assert sp.expand(sp.series(F,z,0,5).removeO()).coeff(z,3) == sp.Rational(5,6)-bcoeff**2
Dz = 1-(1+2*z+2*z*z)*sp.exp(-2*z)
assert sp.series(Dz,z,0,4).removeO().coeff(z,3) == sp.Rational(4,3)

# Positive Taylor coefficients for the universal comparison.
for n in range(4,100):
    Pn = 2+3*n+sp.Rational(5,12)*n*(n-1)*(n-2)
    An = 2**(n+1)-Pn
    assert An > 0
    assert 2*Pn-(2+3*(n+1)+sp.Rational(5,12)*(n+1)*n*(n-1)) > 0


def mpweight(alpha, tau):
    alpha=mp.mpf(alpha); tau=mp.mpf(tau)
    def kernel(x):
        v=tau*abs(x)
        return (1+v)*mp.exp(-v)
    def primitive(r):
        return (2-(2+tau*r)*mp.exp(-tau*r))/tau
    k1=kernel(alpha); k2=kernel(2*alpha)
    D=1+k2-2*k1*k1
    m0=primitive(1)
    ma=(primitive(1+alpha)+primitive(1-alpha))/2
    w_outer=(ma-k1*m0)/D
    w_middle=((1+k2)*m0-2*k1*ma)/D
    K=mp.matrix([[1,k1,k2],[k1,1,k1],[k2,k1,1]])
    vec=mp.lu_solve(K,mp.matrix([ma,m0,ma]))
    err=max(abs(vec[i]-v) for i,v in enumerate([w_outer,w_middle,w_outer]))
    assert err < mp.mpf('1e-65')
    return w_outer,w_middle,D

ast=6-mp.sqrt(30)
assert abs(ast-1/(1+mp.sqrt(mp.mpf(5)/6))) < mp.mpf('1e-65')
random.seed(2026)
checks=0
for _ in range(360):
    aa=mp.mpf(random.randint(5,1000))/1000
    tt=mp.mpf(random.randint(10,20000))/2000
    u,v,d=mpweight(aa,tt)
    assert u>0 and d>0
    if aa>=ast: assert v>0
    checks+=1

# Flat limiting weights, with both signs and boundary equality.
for aa in [mp.mpf('0.4'),mp.mpf('0.5'),ast,mp.mpf('0.6'),mp.mpf('0.9'),mp.mpf('1')]:
    for tt in ['0.01','0.001']:
        u,v,d=mpweight(aa,tt)
        theoretical=(-aa*aa+12*aa-6)/(8*aa)
        theoretical_outer=(aa*aa-4*aa+6)/(16*aa)
        assert abs(v-theoretical)<mp.mpf('0.014')
        assert abs(u-theoretical_outer)<mp.mpf('0.014')
        if aa>=ast: assert v>0
        if aa<ast: assert v<0
        checks+=1

# Show a genuine sign change when the spacing is subcritical.
assert mpweight(mp.mpf('.5'),mp.mpf('.03'))[1]<0
assert mpweight(mp.mpf('.5'),mp.mpf('30'))[1]>0
assert mpweight(ast,mp.mpf('.0001'))[1]>0
print('PASS: 4 symbolic identities/series, 96 positive series coefficients,',checks,
      'high-precision linear-system and limit checks; both subcritical signs.')
print('critical spacing:',mp.nstr(ast,40))
