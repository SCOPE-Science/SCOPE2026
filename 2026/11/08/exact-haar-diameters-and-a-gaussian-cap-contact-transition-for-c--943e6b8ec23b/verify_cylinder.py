"""Supplementary numerical verification of random cylinder section diameters.

Run: python verify_cylinder.py (numpy, scipy required).
Finite experiments supplement, and do not replace, the proof.
"""
import math
import numpy as np
from scipy.special import betainc
from scipy.optimize import minimize


def theoretical_radius(q,h):
    """Q is an orthonormal d-by-m basis; last coordinate is cylinder axis."""
    b=np.linalg.norm(q[-1,:]);a=math.sqrt(max(0.,1-b*b))
    return math.sqrt(1+min(h*h,(b/a)**2 if a>1e-12 else float('inf')))


def independent_optimizer(q,h):
    """Numerical constrained maximization in the section, not using the radius formula."""
    m=q.shape[1]
    def obj(t):return -float(np.dot(t,t))
    def horiz(t):
        x=q@t
        return 1.-float(np.dot(x[:-1],x[:-1]))
    def vert(t):
        z=(q@t)[-1]
        return h*h-z*z
    constraints=[{'type':'ineq','fun':horiz},{'type':'ineq','fun':vert}]
    starts=[np.zeros(m)]
    rng=np.random.default_rng(30317)
    for _ in range(40):
        t=rng.normal(size=m);t=t/(1+np.linalg.norm(t))
        starts.append(t)
    best=0.
    for t in starts:
        out=minimize(obj,t,method='SLSQP',constraints=constraints,options={'ftol':5e-11,'maxiter':200})
        if horiz(out.x)>-1e-6 and vert(out.x)>-1e-6:
            best=max(best,np.linalg.norm(out.x))
    return best


def cdf_radius(d,m,h,r):
    if r<1: return 0.
    if r>=math.hypot(1,h): return 1.
    t=math.sqrt(r*r-1)
    return betainc(m/2,(d-m)/2,t*t/(1+t*t))


def main():
    rng=np.random.default_rng(971251)
    cnt=0
    for d,m in [(3,2),(4,2),(5,2),(5,3),(6,4)]:
        for h in [.4,1.8,4.]:
            for _ in range(6):
                q,_=np.linalg.qr(rng.normal(size=(d,m)))
                brute=independent_optimizer(q,h)
                exact=theoretical_radius(q,h)
                assert abs(brute-exact)<3e-5,(d,m,h,brute,exact)
                cnt+=1
    for d,m in [(3,2),(4,2),(8,3),(10,7),(30,12)]:
        b=rng.beta(m/2,(d-m)/2,size=90000)
        t=np.sqrt(b/(1-b))
        for h in [.3,1.2,3.4]:
            r=np.sqrt(1+np.minimum(h*h,t*t))
            for s in [.2*h,.5*h,.85*h]:
                v=math.hypot(1,s)
                empirical=np.mean(r<=v)
                theory=cdf_radius(d,m,h,v)
                assert abs(empirical-theory)<.011,(d,m,h,s,empirical,theory)
                cnt+=1
            atom=np.mean(t>=h)
            exact_atom=1-betainc(m/2,(d-m)/2,h*h/(1+h*h))
            assert abs(atom-exact_atom)<.011,(d,m,h,atom,exact_atom)
            cnt+=1
    for d in [500,2000,8000]:
        m=round(.4*d);k=d-m
        h0=math.sqrt(m/k)
        for u in [-1,0,1]:
            h=h0+u/math.sqrt(d)
            atom=1-betainc(m/2,k/2,h*h/(1+h*h))
            asym=.5*math.erfc(u*(1-.4))
            assert abs(atom-asym)<.035,(d,m,u,atom,asym)
            cnt+=1
    for d in [500,2000,8000]:
        for k in [1,2,4]:
            from scipy.stats import chi2
            h=1.2*math.sqrt(d)
            atom=1-betainc((d-k)/2,k/2,h*h/(1+h*h))
            asym=chi2.cdf(1/1.2**2,k)
            assert abs(atom-asym)<.008,(d,k,atom,asym)
            cnt+=1
    print(f'PASS {cnt} numerical tests: independent optimization, beta CDF, two asymptotic regimes')

if __name__=='__main__':main()
