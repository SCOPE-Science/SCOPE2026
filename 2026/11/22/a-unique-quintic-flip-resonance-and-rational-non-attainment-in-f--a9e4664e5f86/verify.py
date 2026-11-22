#!/usr/bin/env python3
"""Check exact local return coefficients for a power-law grazing map.

Requires sympy and mpmath. Numerical checks supplement, not replace, proof.
"""
import sympy as S
import mpmath as MP

a, u = S.symbols('a u', positive=True)
w = a*(1-u)/(1+a+(1-a)*u)
# Taylor coefficients of P(z_*+h)-z_* at a derivative-minus-one point.
b2 = (1+u)*(a-1)/(2*w)
b3 = -(1+u)*(a-1)*(a-2)/(6*w**2)
b4 = (1+u)*(a-1)*(a-2)*(a-3)/(24*w**3)
b5 = -(1+u)*(a-1)*(a-2)*(a-3)*(a-4)/(120*w**4)
A = S.factor(-2*(b2**2+b3))
B = S.factor(b2*(b2**2+b3))
C = S.factor(-b2**2*b3-6*b2*b4+3*b3**2-2*b5)
A_expected = (1-a)*(1+u)*(1+a-3*(1-a)*u)/(6*w**2)
assert S.factor(A - A_expected) == 0
assert S.factor(B+b2*A/2) == 0
u_critical=(1+a)/(3*(1-a))
kappa=16*(2-a)**2*(1-a)**4*(1+a)**5/(405*a**4*(1-2*a)**3)
assert S.factor((C+kappa).subs(u,u_critical)) == 0
for M,aval,sign in [(2,S.Rational(1,4),-1),(3,S.Rational(1,4),1),
                    (2,S.Rational(1,3),1),(2,S.Rational(1,5),-1),
                    (4,S.Rational(1,5),1)]:
    uv=(1+aval)**(-M)
    Av=S.factor(A.subs({a:aval,u:uv}))
    assert S.sign(Av)==sign, (M,aval,Av)
    nv=1/(1+aval)
    zv=(1+uv)/(1+aval+(1-aval)*uv)
    assert zv>nv and zv<1

MP.mp.dps=75
for M in (2,4,8):
    root=MP.findroot(lambda x:3*(1-x)-(1+x)**(M+1),(.05,.45))
    nu=1/(1+root); uv=nu**M
    zs=(1+uv)/(1+root+(1-root)*uv)
    K=(1+uv)*(1-zs)**(1-root)/root
    p=lambda z:uv*z+K*(1-z)**root
    kv=16*(2-root)**2*(1-root)**4*(1+root)**5/(405*root**4*(1-2*root)**3)
    assert abs(p(zs)-zs)<MP.mpf('1e-65')
    h=MP.mpf('0.000002')
    estimate=(p(p(zs+h))-zs-h)/h**5
    assert abs(estimate+kv)/kv < MP.mpf('.0001'),(M,estimate,kv)

# Exact physical itinerary: one nonlinear step and M-1 strictly linear steps.
for M,aval in ((2,MP.mpf('.25')),(3,MP.mpf('.25')),(5,MP.mpf('.18'))):
    nu=1/(1+aval);uv=nu**M;zs=(1+uv)/(1+aval+(1-aval)*uv)
    K=(1+uv)*(1-zs)**(1-aval)/aval
    mu=(nu**(M-1)/K)**(1/(1-aval))
    x=mu*zs
    for j in range(1,M+1):
        if j==1:assert x<mu
        if j>1:assert x>mu
        x=nu*x+(mu-x)**aval if x<mu else nu*x
    assert abs(x-mu*zs)<MP.mpf('1e-55')
print('GRAZING_FLIP_PHASE_CHECK_OK')
