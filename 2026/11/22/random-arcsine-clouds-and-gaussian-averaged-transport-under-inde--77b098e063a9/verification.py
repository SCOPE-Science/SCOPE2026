#!/usr/bin/env python3
"""Standalone finite-step and distributional checks for a randomly force-kicked tight-binding walk.
No paper, file, service, or package-specific data other than numpy/scipy is required.
"""
import math
import numpy as np
from scipy.special import jv, j0

def finite_sum_second_moment(n, xi):
    rho = math.exp(-1/(2*xi*xi))
    return n*(1+rho)/(1-rho)-2*rho*(1-rho**n)/(1-rho)**2

def sum_kick_phasors(q):
    z=0j
    for a in q:
        z=np.exp(1j*a)*(1+z)
    return z

def check_bessel_and_direct_lattice():
    L=2048
    j=np.arange(L)
    sites=np.where(j < L//2,j,j-L)
    p=np.zeros(L, dtype=np.complex128)
    p[0]=1.0
    gT=0.63
    q=np.array([0.47,-0.21,0.84,-0.37])
    k=2*np.pi*np.fft.fftfreq(L)
    for a in q:
        p=np.fft.ifft(np.fft.fft(p)*np.exp(1j*2*gT*np.cos(k)))
        p*=np.exp(-1j*a*sites)
    S=sum_kick_phasors(q)
    A=2*gT*abs(S)
    observed=np.abs(p)**2
    predicted=jv(sites, A)**2
    err=np.max(abs(observed-predicted))
    assert err<2e-12,err
    assert abs(np.sum(observed)-1)<3e-12
    mom=float(np.sum(sites*sites*observed))
    assert abs(mom-A*A/2)<1e-10
    return {'max_direct_lattice_bessel_error':err,'finite_sample_variance':mom,'predicted_variance':A*A/2}

def check_bessel_identity():
    for a in [0.05, 0.7, 2.4, 11.0, 30.0]:
        m=np.arange(-110,111)
        pm=jv(m,a)**2
        assert abs(pm.sum()-1)<1e-12
        assert abs(np.dot(m*m,pm)-a*a/2)<2e-10
        for k in [0.1,0.5,1.1]:
            calc=np.sum(pm*np.cos(k*m))
            pred=j0(2*a*np.sin(k/2))
            assert abs(calc-pred)<5e-12,(a,k,calc,pred)

def monte_carlo():
    rng=np.random.default_rng(20261118)
    nsamp=22000
    n=360
    xi=0.94
    gT=0.63
    rho=np.exp(-1/(2*xi*xi))
    alpha=(1+rho)/(1-rho)
    S=np.zeros(nsamp,dtype=np.complex128)
    for _ in range(n):
        q=rng.normal(0,1/xi,nsamp)
        S=np.exp(1j*q)*(1+S)
    vals=np.abs(S)**2
    exact=finite_sum_second_moment(n,xi)
    observed=vals.mean()
    assert abs(observed/exact-1)<0.045,(observed,exact)
    w=vals/(n*alpha)
    diffs=[abs(np.mean(w<=t)-(1-np.exp(-t))) for t in [.2,.5,1,1.5,2,3]]
    assert max(diffs)<0.04,diffs
    assert abs(np.var(w)-1)<0.09,np.var(w)
    assert abs(S.real.var()/(n*alpha/2)-1)<0.055
    assert abs(S.imag.var()/(n*alpha/2)-1)<0.055
    # Independently test that the ensemble position characteristic function tends to Gaussian.
    for k in [0.35,0.75,1.1]:
        actual=np.mean(j0(4*gT*np.abs(S)*np.sin(k/(2*np.sqrt(n)))))
        predicted=np.exp(-(gT)**2*alpha*k*k)
        assert abs(actual-predicted)<0.035,(k,actual,predicted)
    return {'n':n,'sample_count':nsamp,'xi':xi,'rho':rho,'alpha':alpha,
            'empirical_E_absS2':observed,'exact_E_absS2':exact,
            'exp_CDF_max_error':max(diffs),'normalized_variance':float(np.var(w)),
            'normalized_real_component_variance':S.real.var()/(n*alpha/2),
            'normalized_imag_component_variance':S.imag.var()/(n*alpha/2)}

if __name__=='__main__':
    check_bessel_identity()
    print('Bessel normalization, second moment, and characteristic function identities: PASS')
    print('Direct lattice evolution:',check_bessel_and_direct_lattice())
    print('Phase CLT, exponential width and Gaussian mixture simulations:',monte_carlo())
    print('ALL CHECKS PASSED')
