"""Reproduce the radial ambiguity, exact critical-point, and minimax calculations."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar

s,w,T,a=sp.symbols('s w T a',real=True)
F=sp.exp(-s)*(1+w*(s*s-2*s))
assert sp.simplify(sp.diff(F,s)-sp.exp(-s)*(-1+w*(-s*s+4*s-2)))==0
D=4*a-a*a-2
assert sp.simplify(F.subs({s:a,w:1/D})-2*(a-1)*sp.exp(-a)/D)==0
assert sp.simplify(F.subs({s:T,w:1/D})-sp.exp(-T)*(D+T*(T-2))/D)==0
assert sp.simplify((D-1).subs(a,1))==0

# The conventional unit-norm Gaussian and first Hermite window.
def h0(t):return 2**.25*np.exp(-np.pi*t*t)
def h1(t):return 2*np.sqrt(np.pi)*t*h0(t)
def amb(num,x,y):
    h=[h0,h1][num]
    def real(t):return h(t+x/2)*h(t-x/2)*np.cos(2*np.pi*y*t)
    def imag(t):return -h(t+x/2)*h(t-x/2)*np.sin(2*np.pi*y*t)
    return quad(real,-9,9,epsabs=1e-11)[0]+1j*quad(imag,-9,9,epsabs=1e-11)[0]
for x,y in [(0,0),(.4,.7),(.7,0),(0,1/math.sqrt(math.pi)),(.2,-.9)]:
    z=math.pi*(x*x+y*y)
    assert abs(amb(0,x,y)-math.exp(-z/2))<4e-10
    assert abs(amb(1,x,y)-(1-z)*math.exp(-z/2))<4e-10

# Exact candidate minimum, including local interior minimum.
def value(T,w):
    svals=[0.,T]
    if w>0.5:
        q=math.sqrt(2-1/w)
        svals += [2-q,2+q]
    return min(math.exp(-ss)*(1+w*(ss*ss-2*ss)) for ss in svals if 0<=ss<=T)
def weight(T):
    if T<2:return 0.
    if T==2:return 0.5
    def eq(w):
        a=2-math.sqrt(2-1/w)
        return math.exp(-a)*(1+w*(a*a-2*a))-math.exp(-T)*(1+w*T*(T-2))
    return brentq(eq,0.5,1.,xtol=5e-15)

for radius in [.01,.25,1.,1.99,2.,2.0001,2.1,2.5,3.,4.,5.,8.,12.,18.]:
    optw=weight(radius)
    empirical=minimize_scalar(lambda v:-value(radius,v),bounds=[0.,1.],method='bounded',options={'xatol':1e-13})
    bound=value(radius,optw)
    assert bound>=-empirical.fun-4e-9,(radius,optw,bound,empirical.x,-empirical.fun)
    grid=np.linspace(0.,radius,2001)
    at_grid=np.min(np.exp(-grid)*(1+optw*(grid*grid-2*grid)))
    assert abs(at_grid-bound)<2e-5
    if radius>2:
        assert 0.5<optw<1.
        aa=2-math.sqrt(2-1/optw)
        assert 1<aa<2
        assert abs(2*(aa-1)*math.exp(radius-aa)-(4*aa-aa*aa-2+radius*(radius-2)))<2e-6
        assert bound>math.exp(-radius)
    if radius<2:assert optw==0.

# A concrete significant improvement at radius-squared 4.
opt4=weight(4.)
assert abs(opt4-0.6440631953262191)<1e-7
assert abs(value(4.,opt4)-0.11268707014568854)<1e-7

for R in [14.,18.,24.]:
    v=weight(R)
    ratio=(1-v)/((R-1)**2*math.exp(1-R))
    assert abs(ratio-1)<.03,(R,ratio)
print('ALL_SHARP_HERMITE_MINIMAX_CHECKS_PASSED')
