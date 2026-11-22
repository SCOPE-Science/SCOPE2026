#!/usr/bin/env python3
"""Supplementary discrete-circle Gram eigenvalue check; requires numpy.
Not a substitute for the all-degree proof.
"""
import numpy as np
for alpha,t,a,b,N,maxfreq in [(.75,2.0,1.,.3,64,200), (1.,.5,1.,.2,64,200)]:
    theta=2*np.pi*np.arange(N)/N
    delta=theta[:,None]-theta[None,:]
    H=np.ones((N,N),dtype=float)
    for l in range(1,maxfreq+1):
        z=np.exp(-t*(l*l)**alpha)
        if z<1.e-300: break
        H+=2*z*np.cos(l*delta)
    K=H*(a+b*(np.cos(theta[:,None])+np.cos(theta[None,:])))
    w=np.linalg.eigvalsh(K)
    print('alpha',alpha,'N',N,'min_eigenvalue',w[0], 'max_diag_deviation',max(0., -np.min(np.diag(K))))
    assert w[0]<-1e-10
    assert np.min(np.diag(K))>0
print('PASS discrete finite-site Gram counterexamples')
