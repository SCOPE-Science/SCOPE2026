#!/usr/bin/env python3
"""Reproduce stationary mode and small-splitting calculations for a three-state harmonic active particle."""
import math
from fractions import Fraction
import mpmath as mp
import sympy as sp

mp.mp.dps = 55
checks = 0

def verify(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

# Derive the scalar stationary equation from the Gauss hypergeometric equation.
c, e, u = sp.symbols('c e u', real=True)
alpha = 2*c - 1
B = sp.factor(2*c - (c-e+1)*u - 2*alpha*(1-u))
C = sp.factor(alpha*(alpha+1)*(1-u)/u - alpha*(2*c-(c-e+1)*u)/u+e*c)
verify(sp.simplify(B-(2-2*c+(3*c+e-3)*u))==0,'ODE derivative coefficient')
verify(sp.simplify(C-(1-c)*(2*c+e-1))==0,'ODE density coefficient')

# Independent stationary-generator moment recurrence versus the beta-product moments.
R,T=sp.symbols('R T', positive=True)
for r in [sp.Rational(1,3),sp.Rational(4,5),sp.Rational(1),sp.Rational(6,5),sp.Rational(3,2),sp.Rational(19,10),sp.Rational(2),sp.Rational(3)]:
    for t in [sp.Rational(1,2),sp.Rational(1),sp.Rational(7,5),sp.Rational(2),sp.Rational(5,2),sp.Rational(7,2),sp.Rational(5)]:
        moments=[sp.S.One]
        for k in range(1,7):
            from_gen=moments[-1]*sp.Rational(2*k-1,1)*(2*k-2+t)/((2*k-1+r)*(2*k-2+r+t))
            from_beta=sp.rf(sp.Rational(1,2),k)*sp.rf(t/2,k)/(sp.rf((r+t)/2,k)*sp.rf((r+1)/2,k))
            verify(sp.simplify(from_gen-from_beta)==0,'moment mismatch')
            moments.append(from_beta)

# Hypergeometric density and its exact derivative with respect to u=1-x².
def f_and_du(x,r,t):
    r=mp.mpf(r);t=mp.mpf(t)
    z=mp.mpf(x)**2
    U=1-z;c=r/2;e=(t-r-1)/2;a=t/2
    F=mp.hyp2f1(-e,c,2*c,U)
    H=mp.hyp2f1(1-e,c+1,2*c+1,U)
    K=mp.beta(c,c)/(mp.beta(a,c)*mp.beta(mp.mpf('.5'),c))
    value=K*U**(r-1)*F
    derivative=K*U**(r-2)*((r-1)*F-e*U*H/2)
    return value,derivative

# Exact resonance laws and the special uniform-density point.
for r in [mp.mpf('0.3'),mp.mpf('0.7'),mp.mpf('1.0'),mp.mpf('1.4'),mp.mpf('1.9'),mp.mpf('2.0'),mp.mpf('3.0')]:
    t=r+1
    for x in ['0.01','0.19','0.47','0.83']:
        p,_=f_and_du(x,r,t)
        exact=mp.gamma(r+mp.mpf('.5'))/(mp.sqrt(mp.pi)*mp.gamma(r))*(1-mp.mpf(x)**2)**(r-1)
        verify(abs(p-exact)<mp.mpf('1e-45'),'resonance beta-density mismatch')

# Exact residual of the derived second-order scalar equation, with derivatives
# obtained by high-precision automatic differentiation rather than the ODE.
for r,t in [('0.6','0.5'),('0.7','2.2'),('1.0','4'),('1.4','2.1'),('1.4','3.3'),('1.8','5'),('2.5','3')]:
    R=mp.mpf(r);T=mp.mpf(t)
    def p_of_u(y):return f_and_du(mp.sqrt(1-y),R,T)[0]
    for U in [mp.mpf('.15'),mp.mpf('.55'),mp.mpf('.81')]:
        p=p_of_u(U);p1=mp.diff(p_of_u,U);p2=mp.diff(p_of_u,U,2)
        A=2-R+(2*R+T-7)*U/2
        D=(2-R)*(R+T-3)/4
        res=U*(1-U)*p2+A*p1+D*p
        verify(abs(res)<mp.mpf('1e-35'),'ODE numerical residual')

# In each nonmonotone region, the derivative changes sign exactly as asserted.
cases=[
 ('0.5','0.4','minimum'),('0.7','1.2','minimum'),
 ('1.25','2.5','maximum'),('1.45','3.5','maximum'),
 ('1.6','4.5','maximum')]
for r,t,typ in cases:
    def d(x):return f_and_du(x,r,t)[1]
    # Use strict-bracketing bisection in z, rather than a local optimization routine.
    left=mp.mpf('1e-14'); right=mp.mpf('0.999999999')
    a=d(left);b=d(right)
    verify(a*b<0,'expected root bracketing missing')
    for k in range(190):
        mid=(left+right)/2
        if a*d(mid)>0:left=mid;a=d(mid)
        else:right=mid
    x=(left+right)/2
    verify(abs(d(x))<mp.mpf('1e-28'),'stationary point residual')
    verify((a>0 if typ=='minimum' else a<0) or (typ=='minimum' and d(mp.mpf('0.999'))>0),'orientation diagnostic')
    print('critical point',r,t,typ,mp.nstr(x,17))

# Bifurcation exponent and coefficient at the exact resonance line.
for r,sgn in [('0.6',-1),('1.3',+1)]:
    R=mp.mpf(r);c=R/2
    for delta in ['.008','.002']:
        dlt=mp.mpf(delta);T=R+1+sgn*dlt
        predicted=(mp.pi*dlt/(2*abs(R-1)*mp.sin(mp.pi*c)*mp.beta(c,c)))**(1/(2-R))
        def derivative_at(x):return f_and_du(x,R,T)[1]
        left=predicted/10;right=predicted*4
        verify(derivative_at(left)*derivative_at(right)<0,'asymptotic bracket')
        for j in range(145):
            mid=(left+right)/2
            if derivative_at(left)*derivative_at(mid)>0:left=mid
            else:right=mid
        root=(left+right)/2
        ratio=root/predicted
        verify(abs(ratio-1)<mp.mpf('.19'),'leading bifurcation coefficient mismatch')
        print('opening',r,delta,'location',mp.nstr(root,16),'predicted',mp.nstr(predicted,16),'ratio',mp.nstr(ratio,10))
print('passed',checks,'checks')
