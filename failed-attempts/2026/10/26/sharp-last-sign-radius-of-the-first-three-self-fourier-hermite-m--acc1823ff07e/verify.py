#!/usr/bin/env python3
"""Exact symbolic checks for a degree-eight, Fourier-self-dual sign threshold."""
import sympy as s

u,z,a=s.symbols('u z a',real=True)
p=u**3-14*u**2+s.Rational(105,2)*u-s.Rational(105,2)
W=2*z**3-23*z**2+84*z-105
eta=14-2*z
alpha=-3*z**2+28*z-s.Rational(105,2)
q=lambda param: p+param*(u-3)
assert s.expand(s.hermite(4,s.sqrt(u))-(16*u*(u-3)+12))==0
assert s.expand(s.hermite(8,s.sqrt(u))-(256*u*p+1680))==0
assert s.rem(s.Poly(s.expand(q(alpha)-(u-eta)*(u-z)**2),z),s.Poly(W,z)).is_zero
assert s.rem(s.Poly(s.expand(q(alpha).subs(u,eta)),z),s.Poly(W,z)).is_zero
assert s.rem(s.Poly(s.expand(q(alpha).subs(u,z)),z),s.Poly(W,z)).is_zero
assert s.rem(s.Poly(s.expand(s.diff(q(alpha),u).subs(u,z)),z),s.Poly(W,z)).is_zero
assert s.expand(q(a).subs(u,eta)-q(alpha).subs(u,eta)-(eta-3)*(a-alpha))==0
assert s.expand(q(a).subs(u,z)-q(alpha).subs(u,z)-(z-3)*(a-alpha))==0
assert s.discriminant(W,z)==-6888
assert W.subs(z,s.Rational(11,2))==-6
assert W.subs(z,6)==3
assert s.expand(s.diff(W,z)-2*(z-3)*(3*z-14))==0
roots=s.nroots(W,n=60,maxsteps=100)
realroots=[r for r in roots if abs(s.im(r))<s.Float('1e-45')]
assert len(realroots)==1
r=s.re(realroots[0]); E=14-2*r; AA=alpha.subs(z,r)
assert s.Rational(11,2)<r<6 and 2<E<3 and AA>0
RR=s.sqrt(E/(2*s.pi))
assert abs(RR-s.Float('0.60096438785483901355'))<s.Float('1e-15')
print('EXACT_CERTIFICATE_OK')
print('Hermite polynomial bases, symbolic factorization modulo W, two contact equations, discriminant, and separation signs verified.')
print('W(z) =', W)
print('discriminant =',s.discriminant(W,z))
print('z =',s.N(r,35))
print('eta =',s.N(E,35))
print('alpha =',s.N(AA,35))
print('optimal radius =',s.N(RR,35))
print('Boundary node negative for every a>alpha; interior contact negative for every a<alpha.')
