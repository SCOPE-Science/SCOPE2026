"""Finite numerical diagnostics for rank-one two-basis trace-power kernel formulas.

All continuous-dimension and equality claims are proved analytically in RESULT.md;
these tests examine selected examples and near-critical derivatives only.
"""
import math
import numpy as np

COUNT = 0

def verify(condition, msg):
    global COUNT
    if not condition:
        raise AssertionError(msg)
    COUNT += 1

def dft(d):
    i=np.arange(d)[:,None];j=np.arange(d)[None,:]
    return np.exp(2j*np.pi*i*j/d)/math.sqrt(d)

def matrix_data(U,r):
    d=U.shape[0]
    B=np.abs(U)**2
    A=B**r
    G=np.block([[np.eye(d),A],[A.T,np.eye(d)]])
    return B,A,G

def h(B):
    return -float(np.sum(np.where(B>0,B*np.log(np.where(B>0,B,1)),0)))/B.shape[0]

def numeric_test(U,r,label):
    B,A,G=matrix_data(U,r)
    d=len(U)
    verify(np.allclose(U.conj().T@U,np.eye(d),atol=2e-12),label+' unitary')
    verify(np.allclose(B.sum(axis=0),1,atol=2e-12) and np.allclose(B.sum(axis=1),1,atol=2e-12),label+' doubly stochastic')
    sv=np.linalg.svd(A,compute_uv=False)
    eig=np.linalg.eigvalsh(G)
    expected=np.sort(np.r_[1-sv,1+sv])
    verify(np.allclose(eig,expected,rtol=1e-10,atol=2e-11),label+' singular spectrum')
    verify(abs(eig[0]-(1-sv[0]))<1e-11,label+' smallest eigenvalue')
    if r<1-1e-10:
        verify(eig[0] >= 1-d**(1-r)-2e-10,label+' uniform sharp lower bound')
    if r>1+1e-10:
        verify(eig[0]>=-1e-10,label+' positivity beyond one')

for d in (2,3,4,5,7):
    U=dft(d)
    for r in (0.12,0.5,0.73,0.9,0.999,1.0,1.001,1.13,1.6,2.5):
        numeric_test(U,r,'fourier-%d'%d)
        B,A,G=matrix_data(U,r)
        eig=np.linalg.eigvalsh(G)
        verify(abs(eig[0]-(1-d**(1-r)))<1e-10,'Fourier sharp edge')
        verify(np.max(np.abs(eig[1:-1]-1))<1e-10,'Fourier flat middle')
    eps=0.0001
    negative=(np.linalg.eigvalsh(matrix_data(U,1-eps)[2])[0])/(-eps)
    positive=(np.linalg.eigvalsh(matrix_data(U,1+eps)[2])[0])/(eps)
    verify(abs(negative-math.log(d))<0.0005,'Fourier left entropy slope')
    verify(abs(positive-math.log(d))<0.0005,'Fourier right entropy slope')

rng=np.random.default_rng(3821)
for d in (2,3,4,5):
    for trial in range(16):
        Z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        Q,R=np.linalg.qr(Z)
        Q=Q*np.conjugate(np.diag(R)/np.abs(np.diag(R)))
        for r in (0.3,0.8,0.9998,1.0002,1.7):
            numeric_test(Q,r,'Haar-%d-%d'%(d,trial))
        eps=0.00002
        for sign in (-1,1):
            actual=np.linalg.eigvalsh(matrix_data(Q,1+sign*eps)[2])[0]/eps
            target=h(np.abs(Q)**2)*(1 if sign==1 else -1)
            verify(abs(actual-target)<0.0003,'Haar entropy slope')

# Square support-connected blocks with distinct mean entropies, including singleton blocks.
U0=np.block([[dft(2),np.zeros((2,3))],[np.zeros((3,2)),dft(3)]])
U1=np.block([[np.eye(1),np.zeros((1,3))],[np.zeros((3,1)),dft(3)]])
for U,blocks in ((U0,(dft(2),dft(3))),(U1,(np.eye(1),dft(3)))):
    hvals=[h(np.abs(X)**2) for X in blocks]
    for r in (0.4,0.9,0.999,1,1.001,1.3,1.8):
        numeric_test(U,r,'reducible')
    for sign in (-1,1):
        eps=0.00003
        eig=np.linalg.eigvalsh(matrix_data(U,1+sign*eps)[2])[0]/eps
        target=(min(hvals) if sign==1 else -max(hvals))
        verify(abs(eig-target)<0.0002,'block entropy extremum')
    eig=np.linalg.eigvalsh(matrix_data(U,1)[2])
    verify(np.sum(np.abs(eig)<1e-8)==len(blocks),'nullity = component count')

for d in (2,4,6):
    U=np.eye(d,dtype=complex)
    for r in (0.2,0.5,0.99,1,1.01,1.7):
        numeric_test(U,r,'monomial')
        eig=np.linalg.eigvalsh(matrix_data(U,r)[2])
        verify(np.sum(np.abs(eig)<1e-9)==d,'monomial nullity')

print('TWO_BASIS_TRACE_KERNEL_CHECK_OK',COUNT)
