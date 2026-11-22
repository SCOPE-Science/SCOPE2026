#!/usr/bin/env python3
"""Exact algebra and numerical checks for the polynomial uniformity-test examples.

Requires sympy >=1.10 and mpmath >=1.2. The general theorem's positivity
and U-statistic central-limit steps are proved in RESULT.md, not by finite checks.
"""
import math
from fractions import Fraction
import sympy as s
import mpmath as mp

x,y,a,b=s.symbols('x y a b',real=True)
P2=lambda z: 6*z*z-6*z+1
P4=lambda z: 70*z**4-140*z**3+90*z*z-20*z+1
f=1+a*P4(x)+b*P2(x)
assert s.integrate(f,(x,0,1))==1
assert s.integrate(x*f,(x,0,1))==s.Rational(1,2)
F=s.integrate(f.subs(x,y),(y,0,x))
max_expect=2*s.integrate(x*f*F,(x,0,1))
D=s.factor(max_expect-2*s.integrate(x*f,(x,0,1))+s.integrate(x*x*f,(x,0,1)))
formula=(462*b+11*a*b-33*b*b-5*a*a)/6930
assert s.simplify(D-formula)==0
bminus=(462+11*a-s.sqrt((462+11*a)**2-660*a*a))/66
bplus=(462+11*a+s.sqrt((462+11*a)**2-660*a*a))/66
assert s.simplify(formula.subs(b,bminus))==0
assert s.simplify(formula.subs(b,bplus))==0
q=s.integrate(F+x-1,(x,0,y))
qform=lambda z: z*(z-1)*(14*a*z**4-28*a*z**3+17*a*z*z-3*a*z+3*b*z*z-3*b*z+6)/6
assert s.factor(q-qform(y))==0
Eq=s.integrate(qform(x)*f,(x,0,1))
Eq2=s.integrate(qform(x)**2*f,(x,0,1))
variance=s.factor(4*(Eq2-Eq**2))
assert s.simplify(variance.subs({a:0,b:0})-s.Rational(1,45))==0
assert s.simplify(variance.subs(a,-1)-(s.Rational(3187127,212270058)+s.Rational(536,257985)*b-s.Rational(282713,56756700)*b*b+s.Rational(461,363825)*b**3-b**4/s.Integer(11025)))==0
assert (s.Rational(3187127,212270058)+s.Rational(536,257985*80)+s.Rational(461,363825*80**3)) < s.Rational(1,45)
assert s.factor((1-P4(x))-10*x*(1-x)*(7*x*x-7*x+2))==0

checks=10
for aa in range(-100,101):
    if aa == 0: continue
    av=aa/100
    bv=(462+11*av-math.sqrt((462+11*av)**2-660*av*av))/66
    assert bv>0 and bv<1/80
    checks+=1
    # Sample-grid checks supplement, but do not replace, analytic positivity.
    for j in range(41):
        xx=j/40
        assert 1+av*float(P4(xx))+bv*float(P2(xx))>0
        checks+=1
    assert abs(float(formula.subs({a:av,b:bv})))<1e-11
    checks+=1

# Independently evaluate the limiting variance with high-precision quadrature.
mp.mp.dps=55
am=mp.mpf(-1)
bm=10/(451+mp.sqrt(451**2-660))
fm=lambda z:1+am*P4(z)+bm*P2(z)
qm=lambda z:z*(z-1)*(14*am*z**4-28*am*z**3+17*am*z*z-3*am*z+3*bm*z*z-3*bm*z+6)/6
E=mp.quad(lambda z:qm(z)*fm(z),[0,mp.mpf('0.5'),1])
E2=mp.quad(lambda z:qm(z)**2*fm(z),[0,mp.mpf('0.5'),1])
vm=4*(E2-E**2)
assert abs(vm-mp.mpf('0.01503693250994238296993934023723884639'))<mp.mpf('1e-35')
assert abs(vm-mp.mpf(str(variance.subs({a:-1,b:s.N((451-s.sqrt(451**2-660))/66,60)}).evalf(50))))<mp.mpf('1e-44')
z=mp.sqrt(2)*mp.erfinv(mp.mpf('0.95'))
power=mp.erfc(z/mp.sqrt(90*vm))
assert abs(power-mp.mpf('0.01718802635086213621530441669'))<mp.mpf('1e-28')
checks+=3

# Kernel U-statistic agrees with exact order-statistic representation.
for sample in ([0.13,0.61],[0.02,0.32,0.71],[0.02,0.13,0.62,0.98], [0.12,0.18,0.25,0.42,0.65,0.91]):
    vals=[s.Rational(str(t)) for t in sample]
    n=len(vals)
    total=sum((max(vals[i],vals[j])-vals[i]-vals[j]+(vals[i]**2+vals[j]**2)/2) for i in range(n) for j in range(i+1,n))*2/(n*(n-1))
    order=sum((2*(i-n)+(n-1)*v)*v for i,v in enumerate(sorted(vals),1))/(n*(n-1))
    assert total==order
    checks+=1
print(f'PASS: {checks} algebraic, positive-density-grid, and numerical assertions')
print('b(-1)=',mp.nstr(bm,25))
print('asymptotic_variance=',mp.nstr(vm,25))
print('limiting_5pct_rejection_probability=',mp.nstr(power,25))
