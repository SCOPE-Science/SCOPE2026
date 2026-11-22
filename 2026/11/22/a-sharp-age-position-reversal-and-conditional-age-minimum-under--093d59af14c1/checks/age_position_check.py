"""Symbolic and direct-kernel checks of stationary threshold-reset age/position identities.
Uses the diffusion generator and killed reflection kernel.
"""
import sympy as sp
import scipy.integrate as si
from scipy.special import ndtr
from math import sqrt, exp, pi

x, v, D=sp.symbols('x v D', positive=True)
L=lambda f: sp.expand(D*sp.diff(f,x,2)-v*sp.diff(f,x))
# Expected integrated rewards of an excursion and first time-weighted rewards.
g1=x/v
gx=x**2/(2*v)+D*x/v**2
gx2=x**3/(3*v)+D*x**2/v**2+2*D**2*x/v**3
h1=x**2/(2*v**2)+D*x/v**3
hx=x**3/(6*v**2)+D*x**2/v**3+2*D**2*x/v**4
for f,tgt in ((g1,1),(gx,x),(gx2,x**2),(h1,g1),(hx,gx)):
    assert sp.simplify(L(f)+tgt)==0
    assert sp.limit(f,x,0)==0
Epos=sp.simplify(gx/g1)
Eage=sp.simplify(h1/g1)
Eap=sp.simplify(hx/g1)
varpos=sp.factor(gx2/g1-Epos**2)
cova=sp.factor(Eap-Eage*Epos)
covr=sp.factor(varpos/v)
assert sp.factor(cova-(D**2/v**3-x**2/(12*v)))==0
assert sp.factor(covr-(D**2/v**3+x**2/(12*v)))==0
assert sp.factor(covr-cova-x**2/(6*v))==0
print('symbolic generator/PDE covariance identities passed')

def projected_y(t,x0,dr,diff):
    # E[X_t ; hit time>t] integrated over final position y.
    if t==0:return x0
    sd=sqrt(2*diff*t)
    m1=x0-dr*t
    m2=-x0-dr*t
    def phi(z):return exp(-z*z/2)/sqrt(2*pi)
    def i(m):
        z=m/sd
        return m*ndtr(z)+sd*phi(z)
    return i(m1)-exp(dr*x0/diff)*i(m2)

for x0,dr,diff in [(1,1,1),(2,1,0.5),(5,2,0.7),(1.2,2,1.7)]:
    mu=x0/dr
    theorx=float(Epos.subs({x:x0,v:dr,D:diff}))
    theorax=float(Eap.subs({x:x0,v:dr,D:diff}))
    # Direct integration over killed transition density as a function of time.
    valx=si.quad(lambda t:projected_y(t,x0,dr,diff),0,2000,epsabs=2e-8,limit=500)[0]/mu
    valax=si.quad(lambda t:t*projected_y(t,x0,dr,diff),0,2000,epsabs=2e-8,limit=500)[0]/mu
    print('params',x0,dr,diff,'E[X] numerical/formula',round(valx,9),round(theorx,9),'E[AX]',round(valax,9),round(theorax,9))
    assert abs(valx-theorx)<1e-5 and abs(valax-theorax)<1e-5
print('killed-kernel quadratures passed')

def transition(y,t,x0,dr,diff):
    if t<=0:return 0.0
    m1=y-x0+dr*t
    m2=y+x0+dr*t
    return (exp(-(m1*m1)/(4*diff*t)) - exp(dr*x0/diff-(m2*m2)/(4*diff*t)))/sqrt(4*pi*diff*t)

def conditional_mean_formula(y,x0,dr,diff):
    m=min(y,x0)
    return 2*diff/dr**2+abs(y-x0)/dr-2*m/(dr*__import__('math').expm1(dr*m/diff))
for y in [0.1,0.5,1.0,2.0,4.0]:
    denom=si.quad(lambda t:transition(y,t,1.,1.,1.),0,150,epsabs=2e-9,limit=400)[0]
    numer=si.quad(lambda t:t*transition(y,t,1.,1.,1.),0,150,epsabs=2e-9,limit=400)[0]
    cond=numer/denom
    form=conditional_mean_formula(y,1.,1.,1.)
    print('y',y,'conditional EAge direct/formula',round(cond,9),round(form,9))
    assert abs(cond-form)<2e-6
print('conditional age shape kernel quadratures passed')
