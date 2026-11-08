"""Separate finite-dimensional checks for two absorbing sites on a flux-threaded cycle.

Requires numpy and scipy. Run with: python verify.py
The universal statement is established analytically, not by this test.
"""
from math import gcd, pi, sin
import numpy as np
from scipy.linalg import eigh, eigvals, svd


def hamiltonian(n, phi, jhop=1.0):
    h = np.zeros((n,n), dtype=complex)
    for x in range(n):
        y=(x+1)%n
        h[x,y] += jhop*np.exp(1j*phi/n)
        h[y,x] += jhop*np.exp(-1j*phi/n)
    return h


def allowed_indices(n,d,mode):
    if mode == 'zero':
        return [2*k for k in range(1,(n-1)//2+1) if (2*k*d)%n==0]
    if mode == 'pi':
        return [t for t in range(1,n,2) if (t*d)%n==0]
    return []


def theory(n,d,mode):
    g=gcd(n,d)
    z=gcd(n,2*d)
    m0=(z-1)//2
    mp=(g//2 if (n//g)%2 else 0)
    t=allowed_indices(n,d,mode)
    m={'zero':m0,'pi':mp,'generic':0}[mode]
    assert len(t)==m, (n,d,mode,m,t)
    survival=lambda j: sum((2/n)*sin(pi*x*j/n)**2 for x in t)
    return m,survival


def numerical_dark(n,d,phi,k0,kd):
    h=hamiltonian(n,phi)
    vals,vecs=eigh(h)
    dark=[]
    k=0
    while k<n:
        end=k+1
        while end<n and abs(vals[end]-vals[k])<1e-8:
            end+=1
        v=vecs[:,k:end]
        _,s,vt=svd(v[[0,d],:],full_matrices=True)
        rk=int(sum(s>1e-9))
        if rk < end-k:
            for x in vt.conj().T[:,rk:].T:
                dark.append(v@x.conj())
        k=end
    if dark:
        q=np.column_stack(dark)
        assert np.linalg.norm(q.conj().T@q-np.eye(len(dark)))<1e-7
        assert np.linalg.norm(q[[0,d],:])<1e-7
        surv=np.sum(abs(q)**2,axis=1)
    else:
        surv=np.zeros(n)
    # Independently check the real spectrum of the non-Hermitian sink operator.
    damp=np.zeros(n)
    damp[0]=k0
    damp[d]=kd
    ev=eigvals(h-0.5j*np.diag(damp))
    count=int(np.sum(abs(ev.imag)<1e-8))
    assert count==len(dark),(n,d,phi,count,len(dark))
    return len(dark),surv


def run():
    tests=0
    for n in range(3,25):
        for d in range(1,n):
            for mode,phi in [('zero',0.),('pi',pi),('generic',0.317*pi)]:
                m,s=theory(n,d,mode)
                k0=0.2+n/23
                kd=1.3+d/17
                mn,sv=numerical_dark(n,d,phi,k0,kd)
                assert mn==m,(n,d,mode,m,mn)
                for j in range(n):
                    assert abs(sv[j]-s(j))<8e-9,(n,d,mode,j,sv[j],s(j))
                tests+=1
            g=gcd(n,d)
            m0,_=theory(n,d,'zero')
            mp,_=theory(n,d,'pi')
            assert ((m0==0 and mp==0)==(g==1)),(n,d,m0,mp)
    # Paired flux examples in opposite directions.
    assert theory(6,2,'zero')[0]==0 and theory(6,2,'pi')[0]==1
    assert abs(theory(6,2,'pi')[1](1)-1/3)<1e-12
    assert theory(8,2,'zero')[0]==1 and theory(8,2,'pi')[0]==0
    # Singularities have finite-size transport ramifications, not finite-rate discontinuities.
    assert theory(12,4,'zero')[0]==1 and theory(12,4,'pi')[0]==2
    print(f'PASS: {tests} independent H0-subspace and non-Hermitian spectral checks,')
    print('      all vertex survival probabilities, arithmetic dimension and placement laws.')

if __name__=='__main__':
    run()
