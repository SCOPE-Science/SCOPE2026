"""Finite spectral and quadrature checks for staggered block averaging projections.
The infinite-dimensional conclusions require the analytic Fourier and Laplace proofs.
"""
import numpy as np
from math import pi, gamma

def projectors(p, r, periods):
    size=p*periods
    P=np.zeros((size,size))
    Q=np.zeros((size,size))
    for j in range(periods):
        ind=[(j*p+k)%size for k in range(p)]
        P[np.ix_(ind,ind)]=1/p
        ind=[(j*p+r+k)%size for k in range(p)]
        Q[np.ix_(ind,ind)]=1/p
    return P,Q

def spectral_verify(p,r,L):
    P,Q=projectors(p,r,L)
    C=P@Q-Q@P
    actual=np.sort(np.linalg.eigvalsh((-1j)*C))
    a=(p-r)/p; b=r/p
    expected=[]
    for k in range(L):
        theta=2*pi*k/L
        t=abs(a+b*np.exp(1j*theta))
        lam=t*np.sqrt(max(0,1-t*t))
        expected += [-lam,lam]+[0.]*(p-2)
    expected.sort()
    error=max(abs(actual-np.array(expected)))
    assert error<1e-10,(p,r,L,error)
    A=P@Q@P
    nonzero_eigs=np.sort(np.linalg.eigvalsh(A))[-L:]
    expected_A=sorted(abs(a+b*np.exp(2j*pi*k/L))**2 for k in range(L))
    assert np.max(abs(nonzero_eigs-np.array(expected_A)))<1e-10,(p,r,L)
    return error

def heat_profile(p,r,moment_order,N,grid=131072):
    a=(p-r)/p; b=r/p
    th=2*pi*np.arange(grid)/grid
    lambda_=(a*a+b*b+2*a*b*np.cos(th))
    # Delta finite difference on the block indices: sum vanishing moments order k.
    if moment_order==0:
        F=np.ones_like(th,dtype=complex)
        coeff=1
    else:
        F=(np.exp(1j*th)-1)**moment_order
        coeff=1
    norm=np.sqrt(np.mean(lambda_**(2*N)*abs(F)**2))
    predicted=np.sqrt(gamma(moment_order+0.5)/(2*pi*(2*a*b)**(moment_order+0.5)))*N**(-(2*moment_order+1)/4)
    return norm,predicted,norm/predicted

def main():
    checks=0
    for p in range(2,11):
        for r in range(1,p):
            for L in (3,4,5):
                spectral_verify(p,r,L);checks+=1
    print('finite-Bloch spectral instances:',checks)
    phase_checks=0
    for p in range(2,25):
        for r in range(1,p):
            tau=r*(p-r)/p**2
            sharp=(0.5 if tau>=1/8 else 2*np.sqrt(tau*(1-4*tau)))
            theta=np.linspace(0,2*pi,32768,endpoint=False)
            lam=1-4*tau*np.sin(theta/2)**2
            numeric=np.max(np.sqrt(lam*np.maximum(0,1-lam)))
            assert abs(sharp-numeric)<2e-6,(p,r,sharp,numeric)
            phase_checks+=1
    print('sharp commutator norm phase checks:',phase_checks)
    for p,r in ((2,1),(3,1),(7,1),(11,3)):
        for k in (0,1,2):
            actual,predicted,ratio=heat_profile(p,r,k,2000)
            assert abs(ratio-1)<0.015,(p,r,k,ratio)
            print(f'p={p}, r={r}, moment={k}: ratio={ratio:.6f}')
    print('all spectral and asymptotic supplementary checks passed')

if __name__=='__main__':
    main()
