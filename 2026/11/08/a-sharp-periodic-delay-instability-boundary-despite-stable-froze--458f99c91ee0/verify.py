"""Exact symbolic replay of a periodic-delay Floquet computation.

Requires Python 3.9+ and SymPy 1.10+; run: python verify.py
"""
from sympy import Matrix, Rational, Symbol, eye, expand, factor, simplify

u, x = Symbol('u', real=True), Symbol('x')
b, a = Rational(4, 5), Rational(5)
delays = (1, 2, 3)

def step(j, u):
    coefficients = [Rational(0)] * 5
    lag = lambda index: delays[index % 3]
    terms = (
        (1, (1-b)*(2+a)), (2, 2*b-1-a*b),
        (lag(j), a*u),
        (1+lag(j-1), -a*u*(1-b)),
        (2+lag(j-2), a*u*b),
    )
    for k, value in terms:
        coefficients[k-1] += value/(1+a)
    return Matrix([coefficients] + [
        [int(col == row-1) for col in range(5)]
        for row in range(1, 5)
    ])

W0,W1,W2 = [step(j, u) for j in range(3)]
P = W2 * W1 * W0
cubic = (27000*x**3 + (10367-28675*u)*x**2
         + (4913-7825*u)*x - 5780*u)
assert simplify(P.charpoly(x).as_expr()-x**2*cubic/27000)==0
assert simplify(cubic.subs(x,1)-42280*(1-u))==0
assert simplify(cubic.subs(x,-1)+(21546+26630*u))==0

A=(10367-28675*u)/27000
B=(4913-7825*u)/27000
C=-5780*u/27000
Eplus=(43082550-7567687*u-9957495*u*u)/36450000
Eminus=(29817450+7567687*u+6616655*u*u)/36450000
assert simplify(1-C*C+B-A*C-Eplus)==0
assert simplify(1-C*C-B+A*C-Eminus)==0
assert 43082550-7567687-9957495>0
assert 29817450-7567687>0

critical=Rational(-10773, 13315)
assert cubic.subs({u:critical,x:-1})==0
assert simplify(cubic.subs(u,critical) - 4*(x+1)*(17975250*x*x+4372369*x+3113397)/2663)==0
assert simplify(P.subs(u,Rational(-9,10)).det() + 0)==0
assert simplify(P.subs(u,Rational(-9,10)).charpoly(x).as_expr().subs(x,-1)-Rational(269,3000))==0
assert simplify(P.subs(u,Rational(-9,10)).charpoly(x).as_expr().subs(x,1)-Rational(20083,6750))==0
# Exact frozen polynomial for each lag: x**m*(rho+5*sigma)-5*u*sigma.
rho=x*x-Rational(2,5)*x-Rational(3,5)
sigma=x*x-Rational(1,5)*x+Rational(4,5)
assert expand(rho+5*sigma)==6*x*x-Rational(7,5)*x+Rational(17,5)
assert simplify(sigma.subs(x,1))!=0
assert simplify((rho*sigma.subs(x,1/x)+rho.subs(x,1/x)*sigma)/2 - (x-1)**4/(10*x*x))==0
for lag in (1,2,3):
    coeff=[Rational(0)]*5
    for k, value in ((1,(1-b)*(2+a)),(2,2*b-1-a*b),
                     (lag,a*u),(1+lag,-a*u*(1-b)),(2+lag,a*u*b)):
        coeff[k-1]+=value/(1+a)
    F=Matrix([coeff]+[[int(col==row-1) for col in range(5)] for row in range(1,5)])
    expected=x**(3-lag)*(x**lag*(rho+5*sigma)-5*u*sigma)/(6)
    assert simplify(F.charpoly(x).as_expr()-expected)==0

# Direct rational replay at three sample feedback strengths.
for strength in (Rational(-9,10), critical, Rational(0), Rational(9,10)):
    char = P.subs(u,strength).charpoly(x).as_expr()
    assert simplify(char-x**2*cubic.subs(u,strength)/27000)==0

print('CHECKS_OK: symbolic Floquet polynomial, Schur tests, critical threshold, and frozen recurrences')
