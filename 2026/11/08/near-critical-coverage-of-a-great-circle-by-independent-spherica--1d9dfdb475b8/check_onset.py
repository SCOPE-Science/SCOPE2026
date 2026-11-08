"""Reproducible numerical checks for the great-circle cap-coverage onset.

Scientific claims and derivations are in RESULT.md. Computations below
compare independently simulated orientations with exact conditional-spacings
integrals and verify limiting coefficients; simulations are not proofs.

Requires: numpy, scipy.
"""
from math import pi, sin, cos, tan, exp, sqrt, gamma, lgamma, log
import numpy as np
from scipy.special import ndtri
from scipy.stats import qmc


def onset_constant(m, n):
    assert m >= 2 and n >= 3
    t=n*(m+1)/2
    return exp(n*lgamma((m+1)/2)+lgamma(n)+(t-1)*log(2*n)
               +n*(m-1)/2*log(tan(pi/n))-(n-1)*log(2*pi)-lgamma(t))


def exact_near_threshold(m,n,eps,power=17):
    # The nonzero part of the integral lies inside this enlarged ball.
    k=m-1
    dim=n*k
    w=pi/n+eps
    base_R=sqrt(2*n*tan(pi/n))
    R=2*base_R
    pts=qmc.Sobol(d=dim+1,scramble=True,seed=123).random_base2(power)
    gaussian=ndtri(np.clip(pts[:,:dim],1.e-14,1-1.e-14))
    gaussian/=np.linalg.norm(gaussian,axis=1)[:,None]
    y=R*pts[:,dim:dim+1]**(1/dim)*gaussian
    z=eps*np.sum(y.reshape(-1,n,k)**2,axis=2)
    alpha=np.zeros_like(z)
    inside=z<sin(w)**2
    alpha[inside]=np.arccos(np.clip(cos(w)/np.sqrt(1-z[inside]),-1,1))
    excess=np.maximum(0.,2*np.sum(alpha,axis=1)-2*pi)
    vol=pi**(dim/2)*R**dim/gamma(dim/2+1)
    vol_k=pi**(k/2)/gamma(k/2+1)
    return vol*eps**(dim/2)/(vol_k**n*(2*pi)**(n-1))*np.mean(excess**(n-1))


def independent_orientation_mc(m,n,eps,trials,seed=97,batch=100000):
    # Independent full-sphere Gaussians; does not use angular gap proposals.
    rng=np.random.default_rng(seed)
    w=pi/n+eps
    hits=0
    for st in range(0,trials,batch):
        count=min(batch,trials-st)
        x=rng.normal(size=(count,n,m+1))
        x/=np.linalg.norm(x,axis=-1)[:,:,None]
        z=np.sum(x[:,:,2:]**2,axis=-1)
        angles=np.zeros_like(z)
        inside=z<sin(w)**2
        angles[inside]=np.arccos(np.clip(cos(w)/np.sqrt(1-z[inside]),-1,1))
        feas=angles.sum(axis=1)>=pi
        if not np.any(feas):continue
        aa=angles[feas]
        phi=np.mod(np.arctan2(x[feas,:,1],x[feas,:,0]),2*pi)
        order=np.argsort(phi,axis=1)
        phi=np.take_along_axis(phi,order,axis=1)
        aa=np.take_along_axis(aa,order,axis=1)
        gaps=np.diff(np.column_stack((phi,phi[:,0]+2*pi)),axis=1)
        covered=np.all(gaps<=aa+np.roll(aa,-1,axis=1)+1e-12,axis=1)
        hits+=np.count_nonzero(covered)
    return int(hits)


def run():
    cases=((2,3),(2,4),(3,3))
    assert abs(onset_constant(2,4)-64/(5*pi))<1.e-11
    for m,n in cases:
        e=0.02
        q=exact_near_threshold(m,n,e,power=17)
        leading=onset_constant(m,n)*e**(n*(m+1)/2-1)
        ratio=q/leading
        print('coefficient-check',m,n,'K',round(onset_constant(m,n),12),
              'ratio_eps_002',round(ratio,7))
        assert abs(ratio-1)<0.10
    m,n,e=2,4,0.1
    exact=exact_near_threshold(m,n,e,power=17)
    trials=3000000
    hits=independent_orientation_mc(m,n,e,trials)
    measured=hits/trials
    standard_error=max(sqrt(hits),1)/trials
    print('independent-orientation-check',hits,trials,'measured',measured,
          'conditional-integral',exact,'standard_error',standard_error)
    assert hits>30
    assert abs(measured-exact)<5*standard_error+2e-6
    print('GREAT_CIRCLE_RANDOM_CAP_ONSET_CHECKS_OK')

if __name__=='__main__':run()
