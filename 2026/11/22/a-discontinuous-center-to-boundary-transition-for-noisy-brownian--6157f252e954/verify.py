"""Reproducibility checks for fixed-width Brownian-bridge averaging designs.

Requires Python 3, SymPy and mpmath. These are finite computational checks;
the accompanying mathematical proof establishes the global claims.
"""
from fractions import Fraction
from random import Random
import sympy as s
import mpmath as mp

h,t,x,eta,z=s.symbols('h t x eta z', real=True)
k=lambda a,b: s.Min(a,b)-a*b
# Integrate the covariance in the three geometric regions rather than
# assuming the closed formulas for the posterior-risk numerator.
c_left=x*(1-t-h/s.Integer(2))
c_right=(t+h/s.Integer(2))*(1-x)
c_inside=s.factor(((1-x)*(x*x-t*t)/2 + x*((t+h)-x-((t+h)**2-x*x)/2))/h)
I_raw=s.integrate(c_left**2,(x,0,t))+s.integrate(c_inside**2,(x,t,t+h))+s.integrate(c_right**2,(x,t+h,1))
V_raw=s.integrate(c_inside,(x,t,t+h))/h
center=(1-h)/2
I0=(5-5*h*h+2*h**3)/240
B=(h*h-2)/12
V0=(3-2*h)/12
Z=(1-h)**2/4
assert s.simplify(I_raw - (I0+B*(t-center)**2+(t-center)**4/3))==0
assert s.simplify(V_raw-(V0-(t-center)**2))==0
assert s.simplify(s.integrate(c_left,(x,0,t))+s.integrate(c_inside,(x,t,t+h))+s.integrate(c_right,(x,t+h,1)) - ((t+h/2)*(1-t-h/2)-h*h/12)/2)==0
M=eta+V0
J=I0+B*z+z*z/3
H=s.factor(s.diff(J,z)*(M-z)+J)
assert s.simplify(s.diff(H,z)-s.Rational(2,3)*(M-z))==0
D=s.factor(J.subs(z,Z)*M - J.subs(z,0)*(M-Z))
D_target=(1-h)**2*(h*(35*h-14*h*h-20)-60*eta*(1+2*h-2*h*h))/2880
assert s.simplify(D-D_target)==0
hc=(35-s.sqrt(105))/28
assert s.simplify(14*hc**2-35*hc+20)==0
assert 0.88<float(hc)<0.89
eta_crit=s.factor(h*(35*h-14*h*h-20)/(60*(1+2*h-2*h*h)))
assert s.factor(D.subs(eta,eta_crit))==0
hh=s.Rational(19,20); zz=Z.subs(h,hh); vv=V0.subs(h,hh); aa=I0.subs(h,hh); bb=B.subs(h,hh)
assert eta_crit.subs(h,hh)==s.Rational(779,87600)
for noise,expected in [(s.Rational(1,200),s.Rational(1023,42780800)),(s.Rational(1,50),-s.Rational(2919,57137600))]:
    gap=(aa+bb*zz+zz**2/3)/(noise+vv-zz)-aa/(noise+vv)
    assert s.factor(gap-expected)==0

# Numerical quadrature with a separately assembled kernel; avoid SymPy's
# polynomial antiderivative in these checks.
mp.mp.dps=55
rng=Random(913701)
def K(a,b):
    return min(a,b)-a*b
def cov_direct(y,left,width):
    right=left+width
    cuts=sorted(set([left,right]+([y] if left<y<right else [])))
    return sum(mp.quad(lambda u:K(y,u),[a,b]) for a,b in zip(cuts[:-1],cuts[1:]))/width
for _ in range(8):
    width=mp.mpf(rng.randint(1,19))/20
    left=(1-width)*mp.mpf(rng.randint(0,100))/100
    noise=mp.mpf(rng.randint(1,20))/100
    cuts=[mp.mpf('0'),left,left+width,mp.mpf('1')]
    Icheck=sum(mp.quad(lambda ss:cov_direct(ss,left,width)**2,[a,b]) for a,b in zip(cuts[:-1],cuts[1:]) if b>a)
    Vcheck=mp.quad(lambda u:cov_direct(u,left,width),[left,left+width])/width
    ctr=(1-width)/2
    q=(left-ctr)**2
    Iformula=(5-5*width**2+2*width**3)/240+(width**2-2)*q/12+q**2/3
    Vformula=(3-2*width)/12-q
    assert abs(Icheck-Iformula)<mp.mpf('1e-45'), (width,left,Icheck,Iformula)
    assert abs(Vcheck-Vformula)<mp.mpf('1e-45'), (width,left,Vcheck,Vformula)
    assert Vformula+noise>0
print('PASS: exact covariance identities, monotone derivative, phase comparator, two rational examples, and 16 independent numerical quadratures.')
