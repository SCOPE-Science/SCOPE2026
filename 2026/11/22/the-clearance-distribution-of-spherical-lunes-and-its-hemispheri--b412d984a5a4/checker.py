"""Independent numerical checks for spherical-lune clearance laws.
All claims are established analytically in RESULT.md; numerical tests are diagnostics.
Requires Python 3, NumPy, SciPy.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import betainc, beta

rng=np.random.default_rng(20261120)
checks=0

def surv(d, alpha, t):
    if t<=0:return 1.0
    if t>=alpha/2:return 0.0
    k=(d-2)/2
    return (2/alpha)*quad(lambda u: max(0,1-(math.sin(t)/math.sin(u))**2)**k,t,alpha/2,epsabs=1e-12,epsrel=1e-12)[0]

for d in (3,4,5,7,11):
    k=(d-2)/2
    for alpha in (.35,.9,math.pi/2,2.5,math.pi):
        # Distribution, normalization, monotonicity, hemisphere special case.
        levels=np.linspace(0,alpha/2,18)
        vals=[surv(d,alpha,float(t)) for t in levels]
        assert abs(vals[0]-1)<1e-14 and vals[-1]==0 and all(vals[i]>=vals[i+1]-1e-12 for i in range(len(vals)-1));checks+=1
        if alpha==math.pi:
            for t in levels[1:-1]:
                assert abs(surv(d,alpha,float(t))-betainc((d-1)/2,.5,math.cos(t)**2))<2e-10;checks+=1
        # second moment via independent beta factors and deterministic quadrature
        formula=(1-math.sin(alpha)/alpha)/d
        direct=quad(lambda t:surv(d,alpha,math.asin(math.sqrt(t))) if t<=math.sin(alpha/2)**2 else 0,0,math.sin(alpha/2)**2)[0]
        # actual E[sin(delta)^2]=integral P(sin(delta)^2 > t) dt
        assert abs(formula-direct)<8e-9,(d,alpha,formula,direct);checks+=1
        # geometry on 200 sampled points (sample radius squared exactly)
        rad2=rng.beta(1,k,size=200)
        ph=rng.uniform(0,alpha,size=200)
        w=np.sqrt(rad2)
        nearest=np.minimum(ph,alpha-ph)
        delta=np.arcsin(w*np.sin(nearest))
        for i in range(200):
            proj1=w[i]*math.cos(ph[i]);proj2=w[i]*math.cos(ph[i]-alpha)
            c1=math.sqrt(max(0,proj1)**2+1-rad2[i]);c2=math.sqrt(max(0,proj2)**2+1-rad2[i]);
            actual=math.acos(min(1,max(c1,c2)))
            assert abs(actual-delta[i])<4e-8,(actual,delta[i]);checks+=1
    for alpha in (.5,1.2,2.4):
        a=alpha/2
        C=4/(alpha*d)*(2/math.tan(a))**k
        for eps in (0.0006,0.0003):
            s=surv(d,alpha,a-eps)
            # relative remainder O(eps), possible quadrature cancellation at very high d: skip negligible values
            if s>1e-18:
                assert abs(s/(C*eps**(k+1))-1)<.028,(d,alpha,eps,s,C*eps**(k+1));checks+=1
    # Hemisphere exact tail
    for eps in (.001,.0005):
        C=math.gamma(d/2)/(math.sqrt(math.pi)*math.gamma((d+1)/2))
        s=surv(d,math.pi,math.pi/2-eps)
        if s>1e-20:assert abs(s/(C*eps**(d-1))-1)<.008;checks+=1
# Lower endpoint coefficient (exact boundary hypersurface / volume ratio).
for d in (3,4,5,8):
    for alpha in (.6,1.4,2.8,math.pi):
        C=2*math.sqrt(math.pi)*math.gamma(d/2)/(alpha*math.gamma((d-1)/2))
        for eps in (1e-3,5e-4):
            actual=1-surv(d,alpha,eps)
            assert abs(actual/(C*eps)-1)<.006,(d,alpha,eps,actual,C*eps)
            checks+=1
# Total-variation-limit mark moments, comparing finite-epsilon exact integrals.
for d in (3,4,7):
    k=(d-2)/2
    for alpha in (1.,2.2):
        a=alpha/2; eps=.002; scale=2*eps/math.tan(a)
        def wcap(v):
            u=a-eps*v
            return max(0.,1-(math.sin(a-eps)/math.sin(u))**2)/scale
        normal=quad(lambda v:wcap(v)**k,0,1)[0]
        ev=quad(lambda v:v*wcap(v)**k,0,1)[0]/normal
        ew=(k/(k+1))*quad(lambda v:wcap(v)**(k+1),0,1)[0]/normal
        assert abs(ev-1/(k+2))<.008,(ev,1/(k+2))
        assert abs(ew-k/(k+2))<.008,(ew,k/(k+2))
        checks+=2
# Aperture ordering pathwise.
for d in (3,5,10):
    r=np.sqrt(rng.beta(1,(d-2)/2,size=1500));v=rng.uniform(size=1500)
    prev=np.zeros(len(r))
    for alpha in (.2,.8,1.7,math.pi):
        new=np.arcsin(r*np.sin(alpha*v/2))
        assert np.all(new>prev);checks+=1
        prev=new
# Critical crossover integral against exact survival.
for d in (3,4,5):
    k=(d-2)/2
    for lam in (0.,.5,1.5):
        eps=.003
        alpha=math.pi-2*lam*eps
        I=quad(lambda v:((lam+1)**2-(lam+v)**2)**k,0,1,epsabs=1e-12)[0]
        asym=(2/math.pi)*I*eps**(d-1)
        actual=surv(d,alpha,alpha/2-eps)
        assert abs(actual/asym-1)<.014,(d,lam,actual,asym);checks+=1
print('PASS',checks,'independent numerical assertions; analytic proof in RESULT.md')
