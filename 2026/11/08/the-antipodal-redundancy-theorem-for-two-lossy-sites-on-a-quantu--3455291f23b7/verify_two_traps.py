"""Self-contained tests of two-site absorption on a binary hypercube.
Usage: python verify_two_traps.py
"""
from math import comb
import numpy as np

def K(n,k,r):
    return sum((-1)**j*comb(r,j)*comb(n-r,k-j) for j in range(max(0,k-(n-r)),min(k,r)+1))

def shell_matrix(n,k):
    N=1<<n
    return np.array([[K(n,k,(x^y).bit_count()) /N for y in range(N)] for x in range(N)],float)

def formula_prob(n,u,v,x):
    N=1<<n
    d=(u^v).bit_count()
    ans=0.0
    for k in range(n+1):
        a=comb(n,k)/N; b=K(n,k,d)/N
        c=K(n,k,(x^u).bit_count())/N
        e=K(n,k,(x^v).bit_count())/N
        if d==n or k in (0,n):
            ans+=c*c/a
        else:
            ans+=(a*(c*c+e*e)-2*b*c*e)/(a*a-b*b)
    return ans

def spectral_bright(n,u,v):
    N=1<<n
    result=np.zeros((N,N))
    for k in range(n+1):
        E=shell_matrix(n,k)
        W=E[:,[u,v]]
        result+=W@np.linalg.pinv(W.T@W,rcond=1e-10)@W.T
    return result

def krylov_bright(n,u,v):
    N=1<<n
    A=np.zeros((N,N))
    for x in range(N):
        for i in range(n):A[x,x^(1<<i)]=1
    W=np.eye(N)[:,[u,v]]
    parts=[W]
    for k in range(n):
        W=A@W
        parts.append(W)
    Q=np.column_stack(parts)
    U,s,_=np.linalg.svd(Q,full_matrices=False)
    rank=int(sum(s>1e-7*s[0]))
    return U[:,:rank]@U[:,:rank].T,rank

def test():
    count=0
    for n in range(2,7):
        N=1<<n
        for d in range(1,n+1):
            u=0;v=(1<<d)-1
            P=spectral_bright(n,u,v)
            R,rank=krylov_bright(n,u,v)
            expected=n+1 if d==n else 2*n
            assert rank==expected,(n,d,rank,expected)
            assert np.linalg.norm(P-R)<3e-7,(n,d,np.linalg.norm(P-R))
            assert np.linalg.norm(P@P-P)<3e-7
            assert abs(np.trace(P)-expected)<3e-7
            for x in range(N):
                f=formula_prob(n,u,v,x)
                assert abs(f-P[x,x])<3e-8,(n,d,x,f,P[x,x])
                assert -1e-8<f<1+1e-8
                count+=1
            assert abs(np.mean(np.diag(P))-expected/N)<1e-8
    print(f'PASS n=2..6, all representative Hamming separations, {count} site checks; spectral vs independent Krylov.')
if __name__=='__main__':test()
