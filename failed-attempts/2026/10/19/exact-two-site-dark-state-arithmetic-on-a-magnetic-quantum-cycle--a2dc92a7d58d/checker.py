"""Numerical independent checks of magnetic-cycle two-site absorber dark-state classification.

Requirements: Python 3.10+, NumPy; run python quantum_two_sinks_checker.py.
Finite matrices check examples, not the proof for all cycle lengths.
"""
import math
import numpy as np
from scipy.linalg import expm

checks=0

def verify(x,msg):
    global checks
    if not bool(x):
        raise AssertionError(msg)
    checks+=1

def formula(n,d,phase):
    if phase==0:
        return (math.gcd(n,2*d)-1)//2
    if phase==math.pi:
        h=math.gcd(n,d)
        return h//2 if (n//h)%2==1 else 0
    return 0

def numerical(n,d,phase):
    j=np.arange(n)
    h=np.zeros((n,n),dtype=np.complex128)
    for k in range(n):
        m=(k+1)%n
        h[k,m]+=np.exp(1j*phase/n)
        h[m,k]+=np.exp(-1j*phase/n)
    es,v=np.linalg.eigh(h)
    total=0
    k=0
    while k<n:
        ell=k+1
        while ell<n and abs(es[ell]-es[k])<1e-8:
            ell+=1
        section=v[:,k:ell]
        sampling=section[[0,d],:]
        s=np.linalg.svd(sampling,compute_uv=False)
        total+= (ell-k)-sum(t>1e-8 for t in s)
        k=ell
    return total,h

for n in range(3,46):
    for d in range(1,n):
        for phi in [0,math.pi,math.pi/3]:
            got,H=numerical(n,d,phi)
            expected=formula(n,d,phi)
            verify(got==expected,f'mismatch n={n},d={d},phi={phi}, expected={expected}, got={got}')
            if phi==0 or phi==math.pi:
                verify(np.linalg.norm(H-H.conj().T)<1e-12,'Hermitian Hamiltonian')

for n in range(3,20):
    for d in range(1,n):
        for phi in (0, math.pi, math.pi/3):
            expected=formula(n,d,phi)
            _, H=numerical(n,d,phi)
            gamma=0.83
            sink=np.zeros(n)
            sink[[0,d]]=1
            eig=np.linalg.eigvals(H-1j*gamma*np.diag(sink))
            zero_im=sum(abs(z.imag)<3e-8 for z in eig)
            verify(zero_im==expected,'lossless eigenvalue count')

for n,d in [(5,1),(6,2),(6,3),(8,2),(9,3),(12,4)]:
    for phi in (0.,math.pi, math.pi/3):
        expected=formula(n,d,phi)/(n-2)
        _,H=numerical(n,d,phi)
        absorber=np.zeros(n)
        absorber[[0,d]]=1.
        G=H-1j*0.9*np.diag(absorber)
        evolution=expm(-1j*G*2500.)
        initial=[j for j in range(n) if j not in (0,d)]
        average=sum(np.linalg.norm(evolution[:,j])**2 for j in initial)/(n-2)
        verify(abs(average-expected)<2e-6,'finite-time survival versus lossless plateau')

print('PASS:',checks,'finite-matrix assertions')
