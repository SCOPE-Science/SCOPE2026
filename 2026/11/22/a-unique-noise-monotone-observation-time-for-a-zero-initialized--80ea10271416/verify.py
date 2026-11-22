"""Verification of OU single-noisy-sensor observation-time identities.
Requires Python 3, sympy and scipy.  Run: python verify.py
"""
import math
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

a,t=sp.symbols('a t',positive=True)
z=sp.exp(-2*a)
q=(1-sp.exp(-2*a*t))/(2*a)
G=(2*(1+z)-(2+4*a*t+z)*sp.exp(-2*a*t)-sp.exp(-2*a*(1-t)))/(8*a**3)
F=1+4*a*t*sp.exp(2*a)-sp.exp(4*a*t)
Gp=sp.exp(-2*a*(t+1))*F/(4*a*a)
I1=sp.integrate(sp.exp(-2*a*(t-sp.Symbol('s',nonnegative=True)))*(1-sp.exp(-2*a*sp.Symbol('s',nonnegative=True)))**2/(4*a*a),(sp.Symbol('s',nonnegative=True),0,t))
I2=q*q*(1-sp.exp(-2*a*(1-t)))/(2*a)
for name,expr in [
  ('integrated covariance',I1+I2-G),
  ('derivative of gain',sp.diff(G,t)-Gp),
  ('derivative sign switch',sp.diff(Gp,t)+2*a*Gp-(sp.exp(-2*a*t)-sp.exp(-2*a*(1-t)))/a),
  ('derivative of F',sp.diff(F,t)-4*a*(sp.exp(2*a)-sp.exp(4*a*t))),
]:
    assert sp.simplify(sp.expand(expr))==0, name
    print('PASS:',name)

# Direct independently evaluated covariance integrations and first-order stationarity.
count=0
for aa in [0.07,0.2,0.8,1.5,4.0,15.0]:
    def qn(x):return -math.expm1(-2*aa*x)/(2*aa)
    def cov(s,x):return (math.exp(-aa*abs(s-x))-math.exp(-aa*(s+x)))/(2*aa)
    def gn(x):
        return (2*(1+math.exp(-2*aa))-(2+4*aa*x+math.exp(-2*aa))*math.exp(-2*aa*x)-math.exp(-2*aa*(1-x)))/(8*aa**3)
    def gpn(x):return math.exp(-2*aa*(x+1))*(1+4*aa*x*math.exp(2*aa)-math.exp(4*aa*x))/(4*aa*aa)
    for xx in [0.1,0.32,0.5,0.73,0.92]:
        direct = quad(lambda s:cov(s,xx)**2,0,xx,epsabs=1e-12)[0]+quad(lambda s:cov(s,xx)**2,xx,1,epsabs=1e-12)[0]
        assert abs(direct-gn(xx))<2e-10, (aa,xx,direct,gn(xx))
        count+=1
    def Ffun(x):
        return 1+4*aa*x*math.exp(2*aa)-math.exp(4*aa*x)
    tx=brentq(Ffun,0.5,1.0,xtol=1e-14)
    assert .5<tx<1
    for eta in [0,0.01,.3,10.0,1000.0]:
        def eqn(x):return gpn(x)*(qn(x)+eta)-gn(x)*math.exp(-2*aa*x)
        tm=brentq(eqn,.5,tx,xtol=1e-13)
        assert 0.5<tm<tx and abs(eqn(tm))<2e-9
        # endpoint and off-maximum comparison
        obj=lambda x:gn(x)/(qn(x)+eta) if x>0 or eta>0 else 0.
        for x in [.1,.5,tx,1.]:
            assert obj(tm)>=obj(x)-1e-10,(aa,eta,tm,x)
        count+=1
print('PASS:',count,'independent exact/numeric covariance and optimization instances')
