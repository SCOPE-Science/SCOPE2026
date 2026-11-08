#!/usr/bin/env python3
"""Standalone algebraic and numerical checks for a two-point noisy Anderson-mixing law."""
import math
import numpy as np
import sympy as S
from scipy.integrate import quad
from scipy.stats import norm
from numpy.polynomial.hermite import hermgauss

checks = 0
def verify(condition, label):
    global checks
    assert bool(condition), label
    checks += 1

# Check the actual ridge least-squares optimizer and exact error identity
r, theta, d, u, v, lam = S.symbols("r theta d u v lam", real=True)
x0 = theta-d/2
x1 = theta+d/2
y0 = r*x0+u-v/2
y1 = r*x1+u+v/2
res0, res1 = y0-x0, y1-x1
T = S.factor(res1-res0)
W = (1-r)*theta-u
gamma = -W*T/(T**2+lam)
Z = (S.Rational(1,2)+gamma)*y0+(S.Rational(1,2)-gamma)*y1
predicted = theta+W*(d*T-lam)/(T*T+lam)
verify(S.simplify(Z-predicted)==0, "exact algebraic output")
verify(S.simplify(T-(v-(1-r)*d))==0, "independent-noise difference")
verify(S.simplify((res0+res1)/2+W)==0, "residual center")
# derivative test of minimized (centered residual)^2 + ridge penalty
g=S.symbols("g", real=True)
obj=((res0+res1)/2-g*T)**2+lam*g*g
verify(S.simplify(S.diff(obj,g).subs(g,gamma))==0, "ridge stationarity")
verify(S.simplify(S.diff(obj,g,2)-2*(T*T+lam))==0, "ridge strict convexity")

# Algebraic local Taylor coefficients, from Gaussian heat-semigroup expansion.
R, TH, D, X, L = S.symbols("R TH D X L", positive=True)
a=(1-R)*TH
t0=-(1-R)*D
h=(D*X-L)/(X*X+L)
h0=S.factor(h.subs(L,0))
hL=S.diff(h,L).subs(L,0)
b=S.simplify(a*hL.subs(X,t0))  # deterministic regularization bias coefficient
c0=(2*TH*a*S.diff(h0,X,2)+a*a*S.diff(h0*h0,X,2)+S.Rational(1,2)*h0*h0).subs(X,t0)
c1=(2*TH*a*S.diff(hL,X,2)+a*a*S.diff(2*h0*hL,X,2)+h0*hL).subs(X,t0)
c2=(TH*a*S.diff(h0,X,4)+a*a/S.Integer(2)*S.diff(h0*h0,X,4)
    +S.Rational(1,2)*S.diff(h0*h0,X,2)).subs(X,t0)
verify(S.factor(b-R*TH/((1-R)**2*D**2))==0,"bias derivative")
verify(S.factor(c0-(D**2+4*TH**2)/(2*D**2*(1-R)**2))==0,"leading variance")
verify(S.factor(c1+(R*D**2+(12*R+4)*TH**2)/(D**4*(1-R)**4))==0,"linear ridge correction")
verify(S.factor(c2-3*(D**2+12*TH**2)/(D**4*(1-R)**4))==0,"fourth-order constant")
cstar=S.factor(-c1/(2*b*b))
verify(S.factor(cstar-(R*D**2+(12*R+4)*TH**2)/(2*R*R*TH*TH))==0,"sharp fourth-order ridge coefficient")
verify(S.factor(S.diff(b*b*L*L+c1*L+c2,L).subs(L,cstar))==0, "unique minimizer stationary")
verify(S.factor(S.diff(b*b*L*L+c1*L+c2,L,2)-2*b*b)==0, "strict convexity of coefficient")

def exact_risk(r,theta,d,sigma,lmbda):
    t0=-(1-r)*d
    sd=math.sqrt(2)*sigma
    mu=(1-r)*theta
    ew2=mu**2+sigma*sigma/2
    def integrand(t):
        h=(d*t-lmbda)/(t*t+lmbda)
        return (theta*theta+2*theta*mu*h+ew2*h*h)*norm.pdf(t,loc=t0,scale=sd)
    low,hi=t0-12*sd,t0+12*sd
    pts=[0.0] if low<0<hi else None
    return quad(integrand,low,hi,epsabs=2e-11,epsrel=4e-10,points=pts,limit=500)[0]

nodes,weights=hermgauss(170)
def gh_risk(r,theta,d,sigma,lmbda):
    t0=-(1-r)*d
    T=t0+2*sigma*nodes
    mu=(1-r)*theta
    h=(d*T-lmbda)/(T*T+lmbda)
    return float(np.dot(weights,theta*theta+2*theta*mu*h+
                        (mu*mu+sigma*sigma/2)*h*h)/math.sqrt(math.pi))

for r0, th0, d0, sig0, lambda0 in [
    (0.5,1.,1.,0.12,.05),(0.3,.4,1.7,.3,.1),
    (.8,-1.5,.6,.04,.015),(.2,2.,3.,.07,.5)]:
    E=exact_risk(r0,th0,d0,sig0,lambda0)
    G=gh_risk(r0,th0,d0,sig0,lambda0)
    verify(abs(E-G) < 2e-8 * max(1,abs(E)), "independent quadratures")

# Compare the direct two-value, two-residual ridge update with the closed form,
# using independent point evaluations (no Gaussian assumption required here).
rng=np.random.default_rng(81371)
for _ in range(120):
    rv=rng.uniform(.05,.95); tv=rng.uniform(-2,2)
    dv=rng.uniform(.25,3); noise=rng.normal(0,.2,2)
    Lv=rng.uniform(.01,1)
    xx0=tv-dv/2; xx1=tv+dv/2
    yy0=rv*xx0+noise[0]; yy1=rv*xx1+noise[1]
    f0=yy0-xx0; f1=yy1-xx1
    gamma0=((f0+f1)/2)*(f1-f0)/((f1-f0)**2+Lv)
    direct=(.5+gamma0)*yy0+(.5-gamma0)*yy1
    UU=(noise[0]+noise[1])/2
    TT=(f1-f0)
    WW=(1-rv)*tv-UU
    formula=tv+WW*(dv*TT-Lv)/(TT*TT+Lv)
    verify(abs(direct-formula)<1e-12, "direct algorithm / formula")

# Numerical check of fourth-order expansion and the calibrated penalty.
def expansion(r,theta,d,sigma,c):
    c0v=(d*d+4*theta*theta)/(2*d*d*(1-r)**2)
    q=(r*r*theta*theta*c*c-(r*d*d+(12*r+4)*theta*theta)*c+
        3*(d*d+12*theta*theta))/(d**4*(1-r)**4)
    return sigma*sigma*c0v + sigma**4*q
for ss in [.008,.006,.004]:
    for c in [5.,21.,35.]:
        actual=exact_risk(.5,1.,1.,ss,c*ss*ss)
        asym=expansion(.5,1.,1.,ss,c)
        verify(abs(actual-asym) <= .1*ss**4*max(1,abs((asym-10*ss*ss)/ss**4)),"fourth-order asymptotic scale")
# In the asymptotic coefficient, c=21 uniquely beats nearby choices.
for c in [6,14,18,22,27,38]:
    verify(expansion(.5,1,1,.01,21)<expansion(.5,1,1,.01,c),
           "optimal fourth-order tuning")

# Independently integrate the tail conditional on W and check the exact tail coefficient.
def exact_tail(r,theta,d,sigma,z):
    t0=-(1-r)*d
    ws=(1-r)*theta+sigma*nodes/math.sqrt(1)
    # U~N(0,sigma²/2); Hermite nodes: sqrt(2)*sigma/sqrt(2)=sigma
    out=[]
    for ww in ws:
        v1=d*ww/(z-theta)
        v2=-d*ww/(z+theta)
        hi=max(v1,v2); lo=min(v1,v2)
        out.append(norm.cdf(hi,t0,math.sqrt(2)*sigma)-norm.cdf(lo,t0,math.sqrt(2)*sigma))
    return float(np.dot(weights,out)/math.sqrt(math.pi))
def folded_abs(mean,sd):
    return sd*math.sqrt(2/math.pi)*math.exp(-mean**2/(2*sd**2)) + mean*(2*norm.cdf(mean/sd)-1)
for sig in [.2,.3]:
    p0=norm.pdf(0,loc=-.5,scale=math.sqrt(2)*sig)
    coeff=2*p0*folded_abs(.5,sig/math.sqrt(2))
    for z in [3000,9000]:
        v=exact_tail(.5,1,1,sig,z)
        verify(abs(z*v/coeff-1)<.003, "Cauchy-tail coefficient")

print(f"PASS {checks} deterministic symbolic and numerical assertions")
print("Canonical r=1/2, theta=d=1: calibrated lambda/sigma²=21")
print("Canonical asymptotic risk: 10 sigma² -1140 sigma^4 + o(sigma^4)")
