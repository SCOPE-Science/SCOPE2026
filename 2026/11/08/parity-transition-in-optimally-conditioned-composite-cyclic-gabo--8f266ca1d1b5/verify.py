#!/usr/bin/env python3
"""Direct numerical checks for a one-impulse cyclic Gabor operator frame.

Run: python3 verify.py (requires NumPy). The all-order minimax is proved
analytically; finite spectra serve only as independent computations.
"""
import math
import numpy as np


def best_parameters(n):
    if n % 2:
        return np.sqrt(n), math.pi
    return np.sqrt(n), math.pi + math.pi / (2*n)


def predicted_margin(n):
    h=math.pi/(2*n)
    if n%2:
        return math.sin(h)/(math.sqrt(n)-1)
    return math.sin(h)/(math.sqrt(n)-math.cos(h))


def direct_singular_values(n,r,phi):
    z = r*np.exp(1j*phi)
    b = n+abs(z)**2+2*z.real
    g = np.ones(n,dtype=complex)
    g[0]+=z
    g/=math.sqrt(b)
    omega = np.exp(2j*np.pi/n)
    mats=[]
    for a in range(n):
        tg=np.roll(g,a)
        for q in range(n):
            h=tg*omega**(q*np.arange(n))
            P=np.outer(h,np.conjugate(h))
            mats.append(P.T.flatten()) # tr(X P) with X coordinates row-flattened
    A=np.stack(mats,axis=0)
    return np.linalg.svd(A,compute_uv=False)


def ambiguity_magnitudes(n,r,phi):
    z=r*np.exp(1j*phi)
    B=n+r*r+2*z.real
    arr=[1.0]
    arr.extend([abs(r*r+2*z.real)/B]*(n-1))
    arr.extend([abs(n+2*z.real)/B]*(n-1))
    for a in range(1,n):
        for b in range(1,n):
            arr.append(abs(np.conjugate(z)+z*np.exp(2j*np.pi*a*b/n))/B)
    return np.sort(np.array(arr))


def main():
    tests=0
    for n in [6,8,9,10,12,14,15,16]:
        r,phi=best_parameters(n)
        sig=direct_singular_values(n,r,phi)
        predicted=np.sqrt(n)*ambiguity_magnitudes(n,r,phi)
        assert np.allclose(np.sort(sig),predicted,rtol=1e-9,atol=1e-9)
        tests+=n*n
        assert abs(min(sig)/max(sig)-predicted_margin(n))<1e-9
        tests+=1
        for dr,dp in [(0.75,0.1),(1.25,-0.2),(0.5,0.3)]:
            alt=ambiguity_magnitudes(n,r*dr,phi+dp)[0]
            assert alt < predicted_margin(n)+1e-9
            tests+=1
        print('n={} margin={:.12f}, kappa={:.9f}'.format(n,predicted_margin(n),1/predicted_margin(n)))
    print('DIRECT_SPECTRA_PASS',tests)

if __name__=='__main__': main()
