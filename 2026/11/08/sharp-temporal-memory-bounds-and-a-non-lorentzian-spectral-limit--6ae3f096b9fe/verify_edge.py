"""Reproducible analytic-numeric checks for the stationary resetting-condensate edge.
Dependencies: Python 3.10+, NumPy and SciPy.
Run: python verify_edge.py
All dimensional tests use omega=1 and the edge-length unit x0=1.
"""
import math
from functools import lru_cache
from fractions import Fraction
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import roots_laguerre

X,W=roots_laguerre(58)
@lru_cache(maxsize=100000)
def lam(z):
    z=float(z)
    if z<0: raise ValueError('age must be nonnegative')
    if z==0: return 1.
    def inv(u):
        return (math.sqrt(u*(u-1))+math.asinh(math.sqrt(u-1)))/math.sqrt(2)
    return brentq(lambda u:inv(u)-z,1.,max(2.,1+3*z),xtol=2e-13)

def lam_vec(z):
    a=np.asarray(z,dtype=float)
    return np.array([lam(v) for v in a.flat]).reshape(a.shape)

def result(rate, s_values):
    # s = rate * lag; the sampled stationary age is X/rate.
    f=lam_vec(X/rate)
    mean=float(W@f)
    v=float(W@((f-mean)**2))
    assert v>0
    vals=[]
    for s in s_values:
        t=s/rate
        ft=lam_vec((X+s)/rate)
        cov=float(W@((f-mean)*(ft-(W@ft))))
        rho=math.exp(-s)*cov/v
        vals.append((s,rho,math.exp(s)*rho))
    # Integrated normalized correlation: exponential lag quadrature.
    conditional=lam_vec((X[:,None]+X[None,:])/rate)@W
    theta=float(W@((f-mean)*conditional)/v)
    amp=math.sqrt(2)*(W@((f-mean)*X))/(rate*v)
    return theta, float(amp), vals

# Independent check of scale factor, against the source's ODE.
sol=solve_ivp(lambda t,y:[y[1],1/y[0]**2],(0,8),[1.,0.],
              rtol=1e-12,atol=1e-13,dense_output=True)
for t in np.linspace(0,8,25):
    y=sol.sol(t)
    assert abs(float(y[0])-lam(t))<2e-9
    assert abs(float(y[1]**2)-2*(1-1/y[0]))<1e-9

# Exact moments underpinning the universal quadratic-age limit.
var_z2=math.factorial(4)-math.factorial(2)**2
cov_z2_z=math.factorial(3)-math.factorial(2)*math.factorial(1)
assert var_z2==20 and cov_z2_z==4
assert Fraction(var_z2+2*cov_z2_z,var_z2)==Fraction(7,5)

num=0
for r in [0.1,0.4,1.,3.,10.,40.]:
    theta,amp,vals=result(r,[0.05,0.2,0.7,1.,2.,4.])
    assert 1.<theta<2.,(r,theta)
    assert amp>1.,(r,amp)
    previous=1.
    for s,rho,k in vals:
        assert math.exp(-s)<rho<math.exp(-s/2),(r,s,rho)
        assert k>previous,(r,s,k,previous)
        previous=k
        num+=1
    print('rate=',r,' integrated_ratio=',round(theta,10),' tail_amplitude=',round(amp,10))

low=result(0.001,[0.5,1.,2.]); high=result(200.,[0.5,1.,2.])
assert abs(low[0]-1)<0.002,low
assert abs(high[0]-1.4)<0.001,high
for s,rho,_ in low[2]:
    assert abs(rho-math.exp(-s))<0.0005,(s,rho)
for s,rho,_ in high[2]:
    prediction=math.exp(-s)*(1+2*s/5)
    assert abs(rho-prediction)<0.0004,(s,rho,prediction)
print('PASS: ODE + energy, exact factorial coefficient,',num,
      'shape/bounds cases, two limiting profiles, integrated limits')
