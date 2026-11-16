#!/usr/bin/env python3
"""Reproduce the four concentration sectors for a coordinate-dominant spherical cell.
All stochastic tests have fixed deterministic seeds. Requires numpy, scipy.
"""
import argparse, math
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import ndtr, gammainc
from scipy.stats import qmc, norm

def spectrum(d, eps=2e-10):
    if d < 3:
        raise ValueError('dimension must be >= 3')
    m=d-1
    def integrate(y):
        if y <= 0.0:
            return np.zeros(4)
        rt=math.sqrt(y)
        F=math.erf(rt/math.sqrt(2))
        if F<1e-150:
            return np.zeros(4)
        f=math.exp(-y/2)/math.sqrt(2*math.pi*y)
        mu1=math.erf(rt/math.sqrt(2))-2*y*f
        mu2=3*math.erf(rt/math.sqrt(2))-(6*y+2*y*y)*f
        a=mu1/F
        v=max(0.,mu2/F-a*a)
        weight=d*f*math.exp(m*math.log(F))
        return weight*np.array([(m*(y-a)**2+v)/(2*d*d), y*a/d,a*a/d,v/(2*d)])
    # 0..infinity integration split controls chi-square singularity near zero
    vals=np.zeros(4)
    for lower,upper in [(0,1),(1,8),(8,40),(40,max(80, 8*math.log(d)+80))]:
        value,error=quad_vec(integrate,lower,upper,epsabs=eps,epsrel=eps)
        vals+=value
    vals=vals/2  # the positive cell is half of the antipodal union for even quadratics
    Z,M,C,D=vals
    mults=(1,m,m*(m-1)//2,m-1)
    expected=(d*(d+1)//2-1)/(2*d)
    tr=float(np.dot(vals,mults))
    assert abs(tr-expected) < 2e-7*expected,(d,vals,tr,expected)
    assert 0 < D < C < M < 1 and D < Z < 1,(d,vals)
    return vals,mults

def independent_angular_test(d,n_power=17):
    """A direct Gaussian Monte Carlo integration without conditioning on the maximum."""
    vals,mults=spectrum(d)
    sob=qmc.Sobol(d,scramble=True,seed=2417+d)
    u=sob.random_base2(n_power)
    G=norm.ppf(np.clip(u,1.e-12,1-1.e-12))
    Y=G*G
    A=(G[:,0] >= 0) & (Y[:,0] >= np.max(Y[:,1:],axis=1))
    m=d-1
    pols=[m*Y[:,0]-Y[:,1:].sum(axis=1), G[:,0]*G[:,1], G[:,1]*G[:,2], Y[:,1]-Y[:,2]]
    denominator=[2*d*m,1,1,4]
    empirical=np.array([np.mean((p**2)*A)/denominator[i] for i,p in enumerate(pols)])
    # The quadratic contrast is a basis element of the last sector
    # with Gaussian squared norm 4 and eigenvalue (c-e)/2.
    assert np.max(np.abs(empirical-vals)) < 0.005, (d,vals,empirical)
    return empirical

if __name__=='__main__':
    for d in [3,4,5,6,8,10,20,50,100,300,1000]:
        v,m=spectrum(d)
        print('d=%4d spectrum=%s mults=%s ratio=%9.6f normalized=%8.5f' %
          (d,np.array2string(v,precision=11),m,max(v)/min(v),max(v)/min(v)/(2*math.log(d)**2)))
    vals,_=spectrum(3)
    expected=np.array([1/6+math.sqrt(3)/(4*math.pi),1/6+math.sqrt(3)/(9*math.pi),1/6-2*math.sqrt(3)/(9*math.pi),1/6-math.sqrt(3)/(4*math.pi)])
    assert np.max(abs(vals-expected))<1e-11, (vals,expected)
    print('Exact three-dimensional cubed-face consistency: PASS')
    for d in [3,4,5,6]:
        estimated=independent_angular_test(d,18)
        print('direct angular d=%d => %s'% (d,estimated))
    print('ALL CHECKS PASSED')

# End of executable verification; the symbolic identity below is tested separately
# by deriving both forms directly from the four raw chi-square moments.
