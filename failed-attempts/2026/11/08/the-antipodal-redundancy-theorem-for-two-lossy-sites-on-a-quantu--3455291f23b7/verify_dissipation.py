"""Independent physical non-Hermitian-loss verification for pair-monitored hypercubes."""
import numpy as np
from scipy.linalg import expm

def adjacency(n):
    N=1<<n; A=np.zeros((N,N))
    for x in range(N):
        for i in range(n): A[x,x^(1<<i)]=1
    return A

def bright_by_eigendecomposition(n,u,v):
    A=adjacency(n)
    w,V=np.linalg.eigh(A)
    P=np.zeros_like(A)
    for val in np.unique(np.round(w,9)):
        B=V[:,np.abs(w-val)<1e-8]
        W=B @ B[[u,v],:].T
        P+=W@np.linalg.pinv(W.T@W, rcond=1e-9)@W.T
    return P

def check():
    runs=0
    for n in range(2,5):
        N=1<<n; A=adjacency(n)
        for d in range(1,n+1):
            u=0; v=(1<<d)-1
            P=bright_by_eigendecomposition(n,u,v)
            H=A.astype(complex)
            H[u,u]-=0.35j
            H[v,v]-=1.05j
            ev=np.linalg.eigvals(H)
            target=N-(n+1 if d==n else 2*n)
            actual=sum(abs(ev.imag)<2e-8)
            assert actual==target,(n,d,actual,target)
            assert max(ev.imag)<1e-8
            slow=min((-e.imag for e in ev if e.imag < -1e-8),default=1)
            T=max(700, 15/slow)
            U=expm(-1j*H*T)
            rho=np.outer(np.arange(1,N+1),np.arange(1,N+1)).astype(complex)
            v0=np.arange(1,N+1).astype(float);v0/=np.linalg.norm(v0)
            remain=np.linalg.norm(U@v0)**2
            expected=1-np.dot(v0,P@v0)
            assert abs(remain-expected)<1e-6,(n,d,remain,expected)
            runs+=1
    print(f'PASS {runs} unequal-loss Hamiltonians, exact nondecaying eigenspace counts and long-time survival projections.')
if __name__=='__main__': check()
