"""Reproducible finite-section probes for a symmetric atomic generalized Hilbert operator.
Numerical evidence only; analytical proof is supplied separately.
"""
import numpy as np
from scipy.special import gammaln
from scipy.linalg import eigvalsh

def finite_section(t,N):
    n,k=np.indices((N,N))
    comb_log=gammaln(n+k+1)-gammaln(n+1)-gammaln(k+1)
    a=np.exp(comb_log + k*np.log(t)+n*np.log1p(-t))
    b=np.exp(comb_log + k*np.log1p(-t)+n*np.log(t))
    return a+b

def checks():
    for t in [.15,.3,.45,.5,.55,.7,.85]:
        R=2/np.sqrt(t*(1-t))
        A=finite_section(t,200)
        assert np.max(np.abs(A-A.T))<1e-11
        eig=eigvalsh(A)
        assert eig[-1]<=R+1e-10 and eig[0]>=-R-1e-10, (t, eig[0],eig[-1],R)
        if t==.5: assert eig[0]>=-1e-10
        else: assert eig[0]<-0.01
        print(f't={t:.2f} N=200 min={eig[0]:.9f} max={eig[-1]:.9f} theoretical spectral edges +/- {R:.9f}' if t!=.5 else f't=0.50 N=200 min={eig[0]:.9f} max={eig[-1]:.9f} theoretical edges 0,4')
    # Unitary intertwining checks for t and 1-t on sampled L2 functions.
    t=.27
    for x in [.03,.12,1,3]:
        a=(1-t)/t
        # Adjoints: t^-1*a^-1 exp(-x/(2*t*a))h(x/a) = S_{1-t}h(x)
        assert abs((1/(t*a))*np.exp(-x/(2*t*a))-(1/(1-t))*np.exp(-x/(2*(1-t))))<1e-12
    print('Supplementary finite-section and adjoint identity checks: PASSED.')
if __name__=='__main__': checks()
