#!/usr/bin/env python3
"""Reproduce cubical-cell tangential dipole concentration spectra.

Requires numpy, scipy. All integrations and randomized tests are independent
of the theoretical representation-theoretic diagonalization.
"""
from math import sqrt, pi, atan
import numpy as np
from scipy.special import erf, gammaln, ndtri
from scipy.integrate import quad
from scipy.stats import qmc

def max_moments(d):
    def survival(z):
        if z == 0: return 1.0
        return -np.expm1(d*np.log(erf(z/sqrt(2))))
    ez = quad(survival, 0, 16, epsabs=2e-12, epsrel=2e-12)[0]
    ez2 = quad(lambda z: 2*z*survival(z), 0, 16, epsabs=2e-12, epsrel=2e-12)[0]
    er = sqrt(2)*np.exp(gammaln((d+1)/2)-gammaln(d/2))
    return ez/er, ez2/d

def predicted(d):
    s,t=max_moments(d)
    a=(d-2+t)/(2*(d-1)**2)
    b=(1+(d-2)*t)/(4*(d-1))
    c=s/(2*sqrt(2*(d-1)))
    low,high=np.linalg.eigvalsh([[a,c],[c,b]])
    mid=(1-t)/(2*(d-1))
    multiplicity_mid=1+(d-1)*(d-2)//2
    spec=np.sort([low]*(d-1)+[mid]*multiplicity_mid+[high]*(d-1))
    assert len(spec)==d*(d+1)//2
    assert 0<low<mid<high<1
    assert abs(spec.sum()-(d+1)/4)<1e-10
    return s,t,spec

def sampled_gram(d,power):
    n=2**power
    u=qmc.Sobol(d,scramble=True,seed=7129+d).random_base2(power)
    x=ndtri(u)
    x/=np.linalg.norm(x,axis=1)[:,None]
    face=(x[:,0]>=np.max(np.abs(x[:,1:]),axis=1))
    # Exact full-sphere normalized field values.
    es=np.eye(d)[None,:,:]-x[:,:,None]*x[:,None,:]
    es*=sqrt(d/(d-1))
    rotations=[]
    for i in range(d):
        for j in range(i+1,d):
            v=np.zeros_like(x)
            v[:,j]=x[:,i]
            v[:,i]=-x[:,j]
            rotations.append(v*sqrt(d/2))
    fields=np.concatenate([es, np.stack(rotations,axis=1)],axis=1)
    gram=np.einsum('n,nia,nja->ij',face.astype(float),fields,fields,optimize=True)/n
    return np.linalg.eigvalsh(gram),face.mean(),np.trace(gram)

def main():
    for d in (2,3,4,6):
        s,t,theory=predicted(d)
        computed,fraction,trace=sampled_gram(d,18)
        error=float(np.max(np.abs(theory-computed)))
        print('dimension',d,'s',format(s,'.12g'),'t',format(t,'.12g'),
              'min',format(theory[0],'.12g'), 'max',format(theory[-1],'.12g'),
              'qmc_max_eigen_error',format(error,'.6g'),
              'observed_area',format(fraction,'.9g'), 'trace',format(trace,'.9g'))
        assert error < 0.0018, (d,error)
        assert abs(fraction-1/(2*d))<0.0018
    s,t,_=predicted(3)
    assert abs(s-(3*sqrt(2)/pi)*atan(1/sqrt(2)))<2e-12
    assert abs(t-(1/3+2/(pi*sqrt(3))))<2e-12
    print('EXACT d=3 cubic-face moment identities: PASS')
    try:
        import sympy as S
        d,s,t=S.symbols('d s t',real=True)
        a=(d-2+t)/(2*(d-1)**2)
        b=(1+(d-2)*t)/(4*(d-1))
        c2=s**2/(8*(d-1))
        mid=(1-t)/(2*(d-1))
        target=((d*t-1)**2-(d-1)**2*s**2)/(8*(d-1)**3)
        assert S.factor((a-mid)*(b-mid)-c2-target)==0
        assert S.factor((d-1)*(a+b)+(1+(d-1)*(d-2)/2)*mid-(d+1)/4)==0
        print('SYMBOLIC eigenvalue crossing and trace identities: PASS')
    except ImportError:
        print('sympy absent: optional symbolic test skipped')
    print('ALL TESTS PASSED')
if __name__=='__main__': main()
