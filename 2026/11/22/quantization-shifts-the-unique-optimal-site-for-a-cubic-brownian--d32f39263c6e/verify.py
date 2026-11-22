"""Reproduce exact one-site Brownian cubic-integral quadrature identities.

Requires Python >=3.10 and SymPy >=1.11. The mathematical proof is independent
of the finite numerical checks in this program.
"""
import sympy as S

x, t, s = S.symbols('x t s', positive=True)
checks = 0

def eq(a, b):
    global checks
    assert S.simplify(a-b) == 0, (a,b)
    checks += 1

# Brownian covariance Cov(W_t,W_x)=min(t,x), and Wick's identity.
variance = 2*S.integrate(S.integrate(9*s*s*t+6*s**3,(s,0,t)),(t,0,1))
eq(variance,S.Rational(9,5))

# Gaussian conditional third moment E[W_t^3|W_x=v]=A_t v^3+B_t v.
A = S.integrate(t**3/x**3,(t,0,x))+S.integrate(1,(t,x,1))
B = 3*(S.integrate(t*t/x-t**3/x**2,(t,0,x)) +
        S.integrate(t-x,(t,x,1)))
A = S.simplify(A); B=S.simplify(B)
eq(A,1-3*x/4)
eq(B,(7*x*x-12*x+6)/4)

# For X~N(0,x), E[X^3 sgn(X)]=2*x*sqrt(2*x/pi).
explained_sign = S.factor((2*x/S.pi)*(2*A*x+B)**2)
eq(explained_sign,x*(x*x-4*x+6)**2/(8*S.pi))

x_sign = (6-S.sqrt(6))/5
stationary_sign = 5*x*x-12*x+6
eq(stationary_sign.subs(x,x_sign),0)
assert 0 < float(x_sign) < 1
checks += 1
assert stationary_sign.subs(x,S.Rational(1,2))>0 and stationary_sign.subs(x,1)<0
checks += 1

sign_gain = S.simplify(explained_sign.subs(x,x_sign))
eq(sign_gain,24*(138+7*S.sqrt(6))/(3125*S.pi))
eq(S.simplify(sign_gain/variance),8*(138+7*S.sqrt(6))/(1875*S.pi))

# Exact Gaussian moments: E[X^2]=x, E[X^4]=3x^2, E[X^6]=15x^3.
explained_full = S.factor(15*A*A*x**3+6*A*B*x*x+B*B*x)
eq(explained_full,x*(29*x**4-72*x**3+36*x*x+18)/8)
g = 145*x**4-288*x**3+108*x*x+18
eq(S.diff(explained_full,x),g/8)
eq(S.diff(g,x),4*x*(145*x*x-216*x+54))
eq(g.subs(x,x_sign),(1566-576*S.sqrt(6))/25)
eq(g.subs(x,S.Rational(3,4)),S.Rational(801,256))
eq(g.subs(x,S.Rational(4,5)),-S.Rational(118,125))

# The quartic g has exactly one zero on (0,1): g' has a single
# zero there, so g grows first then decreases from positive to negative.
critical=[r for r in S.solve(145*x*x-216*x+54,x) if 0<float(r)<1]
assert len(critical)==1 and g.subs(x,0)>0 and g.subs(x,1)<0
checks+=1
x_full = float(S.nroots(g,maxsteps=100)[1]) if False else float([r for r in S.nroots(g,maxsteps=100) if abs(float(S.im(r)))<1e-12 and 0<float(S.re(r))<1][0])
assert float(x_sign)<x_full and S.Rational(3,4)<x_full<S.Rational(4,5)
checks+=1

# A numerically independent Gaussian-regression check: quadrature over t
# at x values, not algebraic substitution of the final risk polynomial.
import mpmath as M
M.mp.dps=45
for xv in [M.mpf('0.2'),M.mpf('0.5'),M.mpf('0.71010205144336'),M.mpf('0.78860958133058'),M.mpf('1')]:
    a=M.quad(lambda z:(z/xv)**3,[0,xv])+(1-xv)
    b=3*(M.quad(lambda z:(z*z/xv-z**3/xv**2),[0,xv])+M.quad(lambda z:z-xv,[xv,1]))
    gain_bit=(2*xv/M.pi)*(2*a*xv+b)**2
    gain_all=15*a*a*xv**3+6*a*b*xv**2+b*b*xv
    exact_bit=xv*(xv*xv-4*xv+6)**2/(8*M.pi)
    exact_all=xv*(29*xv**4-72*xv**3+36*xv*xv+18)/8
    assert M.fabs(gain_bit-exact_bit)<M.mpf('1e-37')
    assert M.fabs(gain_all-exact_all)<M.mpf('1e-37')
    checks+=2

print('EXACT_QUADRATURE_CHECKS_OK',checks)
print('SIGN_SITE', S.N(x_sign,20))
print('FULL_SITE', format(x_full,'.16f'))
print('SIGN_EXPLAINED',S.N(sign_gain,18))
print('SIGN_EXPLAINED_FRACTION',S.N(sign_gain/variance,18))
print('FULL_EXPLAINED',S.N(explained_full.subs(x,x_full),18))
print('FULL_EXPLAINED_FRACTION',S.N(explained_full.subs(x,x_full)/variance,18))
