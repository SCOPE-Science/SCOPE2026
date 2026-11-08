#!/usr/bin/env python3
"""Finite-dimensional numerical cross-checks for the double-disk Fock concentration theorem.

These are numerical corroborations, not the infinite-dimensional proof.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh
from scipy.special import gammaln


def coherent(z, N):
    """Array of normalized coherent-state monomial coefficients at points z."""
    z = np.asarray(z, dtype=complex).reshape(-1)
    k = np.arange(N)
    # Products computed recursively without using complex logarithms.
    out = np.empty((len(z), N), dtype=complex)
    out[:, 0] = np.exp(-np.pi*np.abs(z)**2/2)
    for j in range(1,N):
        out[:,j] = out[:,j-1] * np.sqrt(np.pi/j) * z
    return out


def disk_matrix(center, area, N=64, n_rad=22, n_angle=80):
    xi, wi = leggauss(n_rad)
    theta = 2*np.pi*np.arange(n_angle)/n_angle
    radii = np.sqrt(area/np.pi)*np.sqrt((xi+1)/2)
    A = np.zeros((N,N), dtype=complex)
    for r,w in zip(radii,wi):
        points=center+r*np.exp(1j*theta)
        C=coherent(points,N)
        A += (area*w/(2*n_angle))*(C.T @ C.conj())
    return (A+A.conj().T)/2


def check():
    tests=0
    for R in [0.45, 1.1]:
        lam0=-math.expm1(-R)
        lam1=lam0-R*math.exp(-R)
        assert lam0>lam1>0; tests+=1
        for dist in [2.1,2.6,3.1]:
            r=math.sqrt(R/math.pi)
            assert dist>2*r;tests+=1
            plus=disk_matrix(dist/2,R)
            minus=disk_matrix(-dist/2,R)
            A=plus+minus
            evals,evec=eigh(A,subset_by_index=(61,63))
            evals=evals[::-1]
            evec=evec[:,::-1]
            s=math.exp(-math.pi*dist*dist/2)
            p=coherent(np.array([dist/2]),64).reshape(-1)
            m=coherent(np.array([-dist/2]),64).reshape(-1)
            q=float(np.vdot(p,minus@p).real)
            bound=R*math.exp(-math.pi*(dist-r)**2)
            assert 0<=q<=bound*(1+1e-9); tests+=1
            assert abs(np.vdot(p,m)-s)<1e-12;tests+=1
            catp=(p+m)/np.sqrt(2*(1+s))
            catm=(p-m)/np.sqrt(2*(1-s))
            mus=(lam0+q+2*lam0*s)/(1+s)
            mua=(lam0+q-2*lam0*s)/(1-s)
            assert evals[0]>=mus-2e-12 and evals[1]>=mua-2e-12;tests+=1
            assert abs(evals[0]-mus)<3e-3 and abs(evals[1]-mua)<3e-3;tests+=1
            assert evals[1]>evals[2]+.01;tests+=1
            assert abs(np.vdot(catp,evec[:,0]))>.98;tests+=1
            assert abs(np.vdot(catm,evec[:,1]))>.98;tests+=1
            # Splitting constant approaches the single-disk top eigenvalue.
            measured=(evals[0]-evals[1])/(2*s)
            assert abs(measured/lam0-1)<.05;tests+=1
            print(f'area={R:.2f}, separation={dist:.2f}, lambda_1={evals[0]:.10g}, '
                  f'lambda_2={evals[1]:.10g}, normalized splitting={measured/lam0:.7f}, '
                  f'lambda_3={evals[2]:.8g}')
    print(f'DOUBLE_DISK_CHECKS_PASS {tests}')

if __name__=='__main__':
    check()
