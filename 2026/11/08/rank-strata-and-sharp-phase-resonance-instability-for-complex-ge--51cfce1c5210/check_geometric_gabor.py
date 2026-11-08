"""Numerical cross-checks for geometric-window cyclic Gabor projector ranks.
Runs direct projector-matrix SVD, numerical ambiguity sums, closed-form
ambiguities and near-resonance stability slopes; finite checks supplement proof.
"""
import numpy as np
from math import gcd

assertions=0

def check(ok,what):
    global assertions
    assertions+=1
    if not ok: raise AssertionError(f'{what}: assertion {assertions}')

def direct_A(N,z):
    g=np.array([z**j for j in range(N)],dtype=np.complex128)
    g/=np.linalg.norm(g)
    w=np.exp(2j*np.pi/N)
    return np.array([[sum(g[j]*np.conjugate(g[(j-a)%N]) * w**(b*j) for j in range(N))
                      for b in range(N)] for a in range(N)])

def closed_A(N,z):
    r=abs(z)
    if r==1: raise ValueError('formula requires r unequal 1')
    phi=np.angle(z); W=z**N; w=np.exp(2j*np.pi/N)
    S=sum(r**(2*j) for j in range(N))
    return np.array([[r**(-a)*np.exp(1j*a*phi)/S * (
      np.conjugate(W)*(1-W)+(1-np.conjugate(W))*(r*r*w**b)**a)/(1-r*r*w**b)
      for b in range(N)] for a in range(N)])

def direct_sv(N,z):
    g=np.array([z**j for j in range(N)],dtype=np.complex128)
    g/=np.linalg.norm(g); w=np.exp(2j*np.pi/N)
    P=[]
    for p in range(N):
        shifted=np.roll(g,p)
        for b in range(N):
            v=shifted * np.array([w**(b*j) for j in range(N)])
            P.append(np.outer(v,np.conjugate(v)).flatten())
    return np.linalg.svd(np.array(P),compute_uv=False)

def predict_rank(N,z):
    r=abs(z)
    if r < 1e-14: return N
    W=z**N
    if abs(r-1)>1e-9:
        if N%2==0 and abs(W.imag)<1e-9: return N*N-N//2
        return N*N
    if abs(W-1)<1e-8: return N
    return N*N+N-sum(gcd(a,N) for a in range(N))-(int(N%2==0 and abs(W+1)<1e-8))

for N in range(2,11):
    for z in (0.53*np.exp(0.119j),1.34*np.exp(0.207j),
              1.17*np.exp(1j*np.pi/N),0.73,
              1.0*np.exp(0.29j),np.exp(1j*np.pi/N),
              np.exp(2j*np.pi/N)):
        A=direct_A(N,z)
        check(abs(A[0,0]-1)<1e-11,('normalization',N,z))
        if abs(abs(z)-1)>1e-9:
            Ac=closed_A(N,z)
            check(np.max(abs(A-Ac))<1e-10,('closed',N,z,np.max(abs(A-Ac))))
        check(np.count_nonzero(abs(A)>3e-9)==predict_rank(N,z),('rank',N,z,predict_rank(N,z),np.count_nonzero(abs(A)>3e-9)))
        if N<=6:
            sv=direct_sv(N,z)
            check(np.max(abs(np.sort(sv)-np.sort(np.sqrt(N)*abs(A.flatten()))))<1e-10,('singular spectrum',N,z))

for N in (2,4,6,8,10,12):
    for r in (0.55,1.25,1.8):
        for eta,phi0 in ((+1,0),(-1,np.pi/N)):
            parity=1 if eta==1 else 0
            D=max(abs(1-r*r*np.exp(2j*np.pi*b/N)) for b in range(N) if b%2==parity)
            predicted=(abs(r**N-eta)*D)/(r**(N/2)*abs(r*r-1))
            for delta in (2e-3,1e-3,5e-4):
                z=r*np.exp(1j*(phi0+delta/N))
                A=direct_A(N,z)
                cond=1/min(abs(A.flatten()))
                check(abs(cond*abs(delta)/predicted-1)<0.04,('slope',N,r,eta,delta,cond*abs(delta)/predicted))
print(f'GEOMETRIC_GABOR_CHECKS_PASS {assertions}')
