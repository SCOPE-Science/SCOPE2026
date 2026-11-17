"""Reproducible symbolic checks and finite diagnostics for a normalized circle map."""
import cmath
import math
import sympy as sp

p, q, C = sp.symbols('p q C', positive=True)
Q = p*p + (3 - q - 4*C)*p + q
assert sp.factor(Q.subs(p, C) - (1-C)*(3*C+q)) == 0
C_from_Q = (p*p+(3-q)*p+q)/(4*p)
num = p*p + q*(4*C-2*p) + q*q - 4*p*p
assert sp.factor((num.subs(C,C_from_Q))/(4*p*p) - (q-p*p)*(q+3*p)/(4*p**3)) == 0
alpha = sp.Rational(4,5)
qq = 1-alpha**2
hh = (1-sp.sqrt(qq))/2
assert hh == sp.Rational(1,5)
fold_c2 = 1-hh**2
assert fold_c2 == sp.Rational(24,25)
assert sp.simplify((3-q-4*C)**2-4*q).subs({q:qq,C:fold_c2}) == 0
x = sp.symbols('x', real=True)
width = 2*sp.asin((1-sp.sqrt(1-x*x))/2)
assert sp.simplify(sp.series(width,x,0,6).removeO() - x*x/2 - x**4/8) == 0
assert sp.simplify(Q.subs({q:qq,C:fold_c2}) - (p-sp.Rational(3,5))**2) == 0
assert (1-alpha**2/2)**2 == sp.Rational(289,625)
assert 1/qq == sp.Rational(25,9)

def F(z, a, rho):
    v = rho*z+a
    return v/abs(v)

def test_cycles(a, deviation):
    rho = cmath.exp(1j*(math.pi+deviation))
    c = rho.real
    qv = 1-a*a
    B = 2+a*a-4*c*c
    discriminant = B*B-4*qv
    assert discriminant > 0
    for sign in (-1,1):
        P = (-B+sign*math.sqrt(discriminant))/2
        assert 0<P<c*c
        t = -c+math.sqrt(c*c-P)
        u = -c-math.sqrt(c*c-P)
        z = a*(t+rho)/(P-rho*rho)
        w = a*(u+rho)/(P-rho*rho)
        assert abs(abs(z)-1)<2e-12
        assert abs(abs(w)-1)<2e-12
        assert abs(F(z,a,rho)-w)<2e-12
        assert abs(F(w,a,rho)-z)<2e-12
        assert abs(z-w)>1e-8
        mu = (t*t+qv)*(u*u+qv)/(4*P*P)
        factor_mu = 1+(qv-P*P)*(qv+3*P)/(4*P**3)
        assert abs(mu-factor_mu)<2e-10
        assert (mu<1) == (sign==1)

for a in (.2,.5,.8):
    edge = math.asin((1-math.sqrt(1-a*a))/2)
    for fraction in (.2,.65):
        test_cycles(a,edge*fraction)
        test_cycles(a,-edge*fraction)

# Central half-turn exact witness.
a=4/5
rho=-1+0j
zp=a/2+1j*math.sqrt(1-a*a/4)
zm=zp.conjugate()
assert abs(F(zp,a,rho)-zm)<1e-14
assert abs(F(zm,a,rho)-zp)<1e-14
assert abs(F(1,a,rho)+1)<1e-14
assert abs(F(-1,a,rho)-1)<1e-14
print('PASS: symbolic factorization, double-root boundary, and 12 noncentral cycle diagnostics')
