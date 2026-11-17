#!/usr/bin/env python3
"""Independent spectral projector checks of dark-state site survival law."""
from math import gcd,pi,sin
from itertools import product
import numpy as np
from scipy.linalg import eigh, expm

def setup(L):
    n=1+sum(v-1 for v in L)
    H=np.zeros((n,n))
    positions=[]; j=1
    for v in L:
        row=[]; old=0
        for h in range(1,v):
            H[j,old]=H[old,j]=1.
            row.append(j);old=j;j+=1
        positions.append(row)
    return H,positions

def formula(L):
    n=1+sum(x-1 for x in L)
    diag=np.zeros(n);j=1
    for i,length in enumerate(L):
        for h in range(1,length):
            v=0.
            for b in range(2,length+1):
                if length%b: continue
                inds=[idx for idx,t in enumerate(L) if t%b==0]
                if len(inds)<2: continue
                inv=sum(1./L[idx] for idx in inds)
                fac=(1.-(1./length)/inv)
                for a in range(1,b):
                    if gcd(a,b)==1:
                        v+=2./length*sin(pi*a*h/b)**2*fac
            diag[j]=v;j+=1
    return diag

def dark_projector(H):
    energies,U=eigh(H); n=len(energies);out=np.zeros((n,n));i=0
    while i<n:
        j=i+1
        while j<n and abs(energies[j]-energies[i])<1e-7: j+=1
        W=U[:,i:j]
        p=W[0,:]
        block=W@W.T
        if np.dot(p,p)>1e-12:
            z=W@p
            block-=np.outer(z,z)/np.dot(p,p)
        out+=block
        i=j
    return out

def explicit_projector(L):
    H, positions=setup(L)
    out=np.zeros_like(H)
    for b in range(2,max(L)+1):
        inds=[i for i,v in enumerate(L) if v%b==0]
        if len(inds)<2: continue
        for a in range(1,b):
            if gcd(a,b)!=1: continue
            W=np.zeros((H.shape[0],len(inds)))
            for k,i in enumerate(inds):
                W[positions[i],k]=[np.sqrt(2/L[i])*sin(pi*a*h/b) for h in range(1,L[i])]
            d=np.array([1/np.sqrt(L[i]) for i in inds])
            z=W@d
            out+=W@W.T-np.outer(z,z)/np.dot(d,d)
    return out

c=0;biggest=0.
for q in (3,4):
    lengths=(2,3,4,5) if q==3 else (2,3,4)
    for L in product(lengths,repeat=q):
        H,_=setup(L);P=dark_projector(H);theory=formula(L)
        err=np.max(abs(P.diagonal()-theory))
        biggest=max(biggest,err)
        assert err<2e-9,(L,err)
        assert np.linalg.norm(P@P-P)<1e-8
        assert np.linalg.norm(P-explicit_projector(L))<2e-9, L
        c+=1
print('PASS spectral dark projection vs every site formula:',c,'spider graphs;', 'max error',biggest)
# Independent non-Hermitian finite-time convergence for examples not too weakly coupled
samples=[(2,2,2),(2,3,5),(2,3,6),(3,3,4),(3,4,5),(2,4,6)]
for L in samples:
    H,_=setup(L);D=dark_projector(H)
    for gamma in (0.7,2.0):
        K=H.astype(complex)-0.5j*gamma*np.diag([1]+[0]*(H.shape[0]-1))
        U=expm(-1j*K*800)
        measured=np.real(np.sum(np.abs(U)**2,axis=0))
        predicted=D.diagonal()
        if np.max(abs(measured-predicted))>3e-5:
            raise AssertionError((L,gamma,np.max(abs(measured-predicted))))
print('PASS direct lossy evolution at t=800:',len(samples)*2,'Hamiltonians')
