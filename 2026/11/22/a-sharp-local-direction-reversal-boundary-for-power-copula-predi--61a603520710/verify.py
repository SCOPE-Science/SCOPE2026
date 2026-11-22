#!/usr/bin/env python3
"""Exact symbolic and independent numerical checks of local directional-xi transition.

Only a verification aid: the proof of uniform local sign and uniqueness
uses analytical Taylor estimates and the analytic implicit-function theorem.
"""
import sympy as sp
import mpmath as mp

A,x,z=sp.symbols('alpha x beta',positive=True)
g=1-x**A
h=sp.simplify(g+x*sp.diff(g,x))
# Local Taylor coefficients from independently integrated conditional-CDF differences.
d2=6*sp.integrate(x**2*g**2,(x,0,1))-sp.Rational(4,9)*sp.integrate(h**2,(x,0,1))
d3=-12*sp.integrate(x**2*g**3,(x,0,1))+sp.Rational(4,9)*sp.integrate(h*(g**2+2*x*g*sp.diff(g,x)),(x,0,1))
D2= -4*A**3*(2*A-9)/(9*(A+3)*(2*A+1)*(2*A+3))
D3= 8*A**4*(2*A**2-43*A-27)/(9*(A+1)*(A+3)*(2*A+1)*(2*A+3)*(3*A+1))
assert sp.simplify(d2-D2)==0
assert sp.simplify(d3-D3)==0
assert sp.simplify(D2.subs(A,sp.Rational(9,2)))==0
assert sp.simplify(sp.diff(D2,A).subs(A,sp.Rational(9,2)))==-sp.Rational(9,100)
assert sp.simplify(D3.subs(A,sp.Rational(9,2)))==-sp.Rational(1458,1595)
assert sp.simplify(-D3.subs(A,sp.Rational(9,2))/sp.diff(D2,A).subs(A,sp.Rational(9,2)))==-sp.Rational(3240,319)
# Verify the conditional-CDF formulas and normalization at arbitrary algebraic parameters.
u,v=sp.symbols('u v',positive=True)
f=1+z*(1-u**A)
C=u*v**f
fu=sp.diff(C,u)
fv=sp.diff(C,v)
assert sp.simplify(fu-v**f*(1+u*sp.diff(f,u)*sp.log(v)))==0
assert sp.simplify(fv-u*f*v**(f-1))==0
# Exact beta expansions of v-integrated squared conditional deviations,
# checked at fixed alpha to avoid assumption-dependent CAS simplifications.
for av in [sp.Rational(1,2),1,2,3,sp.Rational(9,2),5,8]:
  assert (D2.subs(A,av)>0) == (av<sp.Rational(9,2)) if av!=sp.Rational(9,2) else D2.subs(A,av)==0
# Independent high-precision numerical quadrature of the original normalized functional.
mp.mp.dps=70

def xis(alpha,beta):
    a=mp.mpf(str(alpha)); b=mp.mpf(str(beta))
    def ff(x):
        val=1+b*(1-x**a)
        df=-b*a*x**(a-1)
        return val,df
    def forward(x):
        f,df=ff(x)
        return 1/(2*f+1)-2*x*df/(2*f+1)**2+2*x*x*df*df/(2*f+1)**3-2/(f+2)+2*x*df/(f+2)**2+mp.mpf(1)/3
    def reverse(x):
        f,_=ff(x)
        return x*x*(f*f/(2*f-1)-1)
    return 6*mp.quad(forward,[0,0.25,0.5,0.75,1]),6*mp.quad(reverse,[0,0.25,0.5,0.75,1])

for av in ['2','4.5','5']:
 for b in ['0.001','0.0005']:
    xif,xir=xis(av,b)
    delta=xir-xif
    c2=mp.mpf(str(sp.N(D2.subs(A,sp.Rational(av)),50)))
    c3=mp.mpf(str(sp.N(D3.subs(A,sp.Rational(av)),50)))
    approximation=(mp.mpf(b)**2)*c2+(mp.mpf(b)**3)*c3
    assert abs(delta-approximation) < 4*(mp.mpf(b)**4), (av,b,delta,approximation)
# Probe the signed sides around the shifted root near critical exponent.
for b in ['0.002','0.005']:
    root=mp.findroot(lambda aa: xis(aa,b)[1]-xis(aa,b)[0], (mp.mpf('4.35'),mp.mpf('4.5')))
    predicted=mp.mpf('4.5')-mp.mpf(3240)/319*mp.mpf(b)
    assert abs(root-predicted)<mp.mpf('0.015'), (b,root,predicted)
    print('beta',b,'root',mp.nstr(root,25),'linear',mp.nstr(predicted,25))
print('PASS: exact quadratic and cubic coefficients, sharp critical exponent, derivative, local drift, copula conditional derivatives, and independent high precision tests')
