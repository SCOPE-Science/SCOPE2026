#!/usr/bin/env python3
"""Exact symbolic checks for the boundary-distance Bergman curvature theorem."""
import sympy as S
s,t=S.symbols('s t', real=True)

# Reconstruct coefficient ratios from beta moments, for all real t>-1.
a=[S.prod(t+k for k in range(3,2*n+3))/S.factorial(2*n+1) for n in range(4)]
c1=a[1]
c2=S.factor(a[2]-a[1]**2/2)
c3=S.factor(a[3]-a[1]*a[2]+a[1]**3/3)
assert S.simplify(c2+(t+3)*(t+4)*(t**2+t-15)/180)==0
assert S.simplify(c3-(t+3)*(t+4)*(2*t**4+10*t**3-16*t**2-24*t+315)/5670)==0
k0=S.factor(-4*c2/c1**2)
assert S.factor(k0-4*(t*t+t-15)/(5*(t+3)*(t+4)))==0
T=(S.sqrt(61)-1)/2
assert S.simplify(k0.subs(t,T))==0
assert S.simplify(S.diff(k0,t).subs(t,T)-(32*S.sqrt(61)-244)/45)==0
assert S.simplify((-36*c3/c1**2).subs(t,T)+S.Rational(24,7))==0
coef=S.factor(-S.diff(k0,t).subs(t,T)/((-36*c3/c1**2).subs(t,T)))
assert S.simplify(coef-(56*S.sqrt(61)-427)/270)==0

# Exact rational curvature for nonnegative integer exponents, no discretization.
num_expected={
1:s**6-18*s**5-69*s**4-140*s**3-153*s**2-450*s-195,
2:-2*(15*s**6+150*s**5+225*s**4+244*s**3+225*s**2+150*s+15),
3:2*(51*s**12-324*s**11-10170*s**10-79220*s**9-245763*s**8-972936*s**7-2826924*s**6-4609800*s**5-3802275*s**4-2582580*s**3-1294650*s**2-346500*s-6125)
}
den_expected={1:3*(s**2+2*s+5)**3,2:(5*s**2+6*s+5)**3,3:5*(3*s**4+20*s**3+114*s**2+84*s+35)**3}
for m in range(5):
 Q=sum(S.binomial(m+2,2*j+1)*s**j for j in range((m+1)//2+1))
 f=-(m+2)*S.log(1-s)+S.log(Q)
 g=S.factor(S.diff(f,s)+s*S.diff(f,s,2))
 k=S.factor(-(g*S.diff(g,s)+s*g*S.diff(g,s,2)-s*S.diff(g,s)**2)/g**3)
 if m==0:
  assert S.factor(k+1)==0
 if m in num_expected:
  assert S.factor(k-num_expected[m]/den_expected[m])==0
 if m==4:
  g_ex=12*(7*s**4+28*s**3+58*s**2+28*s+7)/((1-s)**2*(s+3)**2*(3*s+1)**2)
  assert S.factor(g-g_ex)==0
  N=147*(s**12+1)-7308*(s**11+s)-55818*(s**10+s**2)-195804*(s**9+s**3)-455427*(s**8+s**4)-850584*(s**7+s**5)-1064716*s**6
  den=6*(7*s**4+28*s**3+58*s**2+28*s+7)**3
  assert S.factor(k-N/den)==0
  assert S.expand(s**12*N.subs(s,1/s)-N)==0
  assert N.subs(s,0)>0 and N.subs(s,1)<0
  assert S.Poly(N,s).count_roots(0,1)==1
  signs=[S.sign(x) for x in S.Poly(N,s).all_coeffs()]
  assert signs[0]==signs[-1]==1 and all(z==-1 for z in signs[1:-1])
  root=float(S.nroots(N,maxsteps=250)[0]) if False else 0.0175975033598718
  assert N.subs(s,S.Rational(1759750,10**8))>0
  assert N.subs(s,S.Rational(1759751,10**8))<0
print('PASS: exact moments, threshold and transversality, integer curvatures, unique four-weight circle')
