#!/usr/bin/env python3
"""Independent finite-parameter checks for the stated tempered gamma-clock displacement asymptotics.
Requires Python 3, NumPy, SciPy and SymPy; it is not a proof of any asymptotic limit.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma, gammainc, kve, loggamma
import sympy as sp

u,w=sp.symbols('u w',positive=True)
phi=u+w+1/(u*w)
Hessian=sp.hessian(phi,(u,w)).subs({u:1,w:1})
assert Hessian==sp.Matrix([[2,1],[1,2]])
assert Hessian.det()==3
assert Hessian.inv()==sp.Matrix([[sp.Rational(2,3),-sp.Rational(1,3)],[-sp.Rational(1,3),sp.Rational(2,3)]])
assert sp.simplify(phi.subs({u:1,w:1}))==3


def model(H,tau,lam,beta,alpha,k):
    a=H*gamma(2*H)*tau**(2*H-1)
    c=(2*H-1)*tau
    def variance(s):
        z=s/tau
        if z < 1e-5:  # small-time limit; this branch is outside the saddle at checked q
            return 0.5*s**(2*H)
        v=H*(2*H-1)*tau**(2*H)*(z*gamma(2*H-1)*gammainc(2*H-1,z)-gamma(2*H)*gammainc(2*H,z))
        return max(v,0.)
    def exact_scaled(q):
        x=math.sqrt(4*a*beta/lam*q**3)
        log_c=k*math.log(lam)-loggamma(k)-0.5*math.log(math.pi)-loggamma(alpha)-0.5*math.log(beta)
        def integrand(w):
            s=q*w/lam
            V=variance(s)
            if V<=0: return 0.
            z=x/math.sqrt(beta*V)
            log_val=(log_c+(k-1)*math.log(s)-lam*s+
                     (alpha-.5)*math.log(x/(2*math.sqrt(beta*V)))-.5*math.log(V)-z+
                     math.log(kve(alpha-.5,z))+3*q+math.log(q/lam))
            return math.exp(log_val) if log_val>-740 else 0.
        return quad(integrand,0.04,4.,epsabs=1e-8,epsrel=1e-9,limit=350)[0]
    def prediction_scaled(q):
        return math.sqrt(math.pi*lam/(3*a*beta))*q**(alpha+k-2)*math.exp(-lam*c)/(gamma(alpha)*gamma(k))
    return a,c,variance,exact_scaled,prediction_scaled

for params in [(0.8,1.,2.,1.,1.7,3.),(0.65,0.7,1.3,0.9,2.3,1.4)]:
    a,c,variance,exact_scaled,predict=model(*params)
    for s in (1.,4.,10.,30.):
        assert 0.<variance(s)<a*s, (params,s,variance(s),a*s)
    ratios=[]
    for q in (20.,40.,80.):
        r=exact_scaled(q)/predict(q)
        ratios.append(r)
        print('params=',params,'q=',q,'exact/pred=',r)
        assert 0.92<r<1.6, (params,q,r)
    assert ratios[0]>ratios[1]>ratios[2], ratios
    assert abs(ratios[-1]-1)<.1, ratios
print('CHECKS_PASS; computational finite-q diagnostics do not certify the asymptotic theorem')
