#!/usr/bin/env python3
"""Finite supplementary checks for a paired-automorphism Hardy Gram theorem."""
import numpy as np

count = 0
for a, t in [(0.4, 0.5), (0.4, 1j), (0.3, 1), (0.7, -0.2+0.3j), (0.4, -1), (0.2, 0.3-0.8j)]:
    u, v = abs(1+t)**2, abs(1-t)**2
    aa, bb = (1+a*a)/(1-a*a), 2*a/(1-a*a)
    eta = 1/aa
    Llo = (aa*(u+v)-np.sqrt(aa**2*(u-v)**2+4*bb**2*u*v))/2
    Lhi = (aa*(u+v)+np.sqrt(aa**2*(u-v)**2+4*bb**2*u*v))/2
    for theta in np.linspace(-np.pi,np.pi,41):
        z = np.exp(1j*theta)
        denom=1-2*a*a*np.cos(theta)+a**4
        F=(1-a*a)/denom*np.array([[1+a*a,-a*(1+z)],[-a*(1+z.conjugate()),1+a*a]],complex)
        Fi=np.array([[1+a*a,a*(1+z)],[a*(1+z.conjugate()),1+a*a]],complex)/(1-a*a)
        assert np.allclose(F@Fi,np.eye(2),atol=1e-12);count+=1
        D=np.diag([1+t,1-t]);M=D.conj().T@F@D
        vals=np.linalg.eigvalsh(M)
        assert vals[0]>=Llo-1e-10 and vals[0]<=eta*min(u,v)+1e-10;count+=1
        assert vals[1]>=eta*max(u,v)-1e-10 and vals[1]<=Lhi+1e-10;count+=1
        assert np.linalg.norm(M-M.conj().T)<1e-10;count+=1
    for N in (50,100):
        idx=np.arange(N);d=np.where(idx%2==0,1+t,1-t)
        H=(-a)**np.abs(idx[:,None]-idx[None,:])
        G=d.conj()[:,None]*H*d[None,:]
        ew=np.linalg.eigvalsh(G)
        assert ew[0]>=Llo-1e-9 and ew[-1]<=Lhi+1e-9;count+=1
        # The extremal eigenvalues approach symbol bounds as N grows.
        assert ew[0]<Llo+0.04 and ew[-1]>Lhi-(0.20 if N==50 else 0.05);count+=1
    assert np.isclose(eta*abs(u-v),4*eta*abs(t.real));count+=1
print(f'PAIRED_AUTOMORPHIC_GRAM_CHECK_OK {count}')
