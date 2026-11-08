"""Independent orthonormal-basis spectral/capture check. Requires numpy.

This check is numerical and finite; the all-parameter proof is in RESULT.md.
"""
import numpy as np


def case(q,m):
    N=q*m
    pairs=[(i,j) for i in range(N) for j in range(i,N)]
    idx={p:k for k,p in enumerate(pairs)}
    s=len(pairs)
    H=np.zeros((s,s))
    for col,(i,j) in enumerate(pairs):
        if i==j:
            for k in range(N):
                if k//m!=i//m: H[idx[tuple(sorted((i,k)))],col]+=np.sqrt(2)
        else:
            for k in range(N):
                if k//m!=i//m: H[idx[tuple(sorted((k,j)))],col]+=np.sqrt(2) if k==j else 1
                if k//m!=j//m: H[idx[tuple(sorted((k,i)))],col]+=np.sqrt(2) if k==i else 1
    assert np.allclose(H,H.T)
    collision=np.zeros((N,s))
    for i in range(N):collision[i,idx[(i,i)]]=1
    P=np.zeros((s,s))
    nullities={}
    for energy in [0,-m,-2*m,m*(q-1),m*(q-2),2*m*(q-1)]:
        M=np.vstack((H-energy*np.eye(s), collision))
        _,singular,vt=np.linalg.svd(M,full_matrices=True)
        rank=int(np.count_nonzero(singular>1e-8))
        K=vt[rank:].T
        nullities[energy]=s-rank
        P+=K@K.T
    r=m if m>=3 else 1
    t=q*(m-1)
    dim=t*(t+1)//2-q*r+q*(q-2)*(m-1)+q*(q-3)//2
    assert abs(np.trace(P)-dim)<1e-8
    assert np.linalg.norm(P@P-P)<1e-8
    assert np.linalg.norm(H@P-P@H)<1e-8
    assert np.linalg.norm(collision@P)<1e-8
    capture_cross=1-P[idx[(0,m)],idx[(0,m)]]
    capture_same=1-P[idx[(0,1)],idx[(0,1)]]
    assert abs(capture_cross-2/(m*(q-1)))<1e-8
    assert abs(capture_same-(1 if m<=3 else 2/(m-1)))<1e-8
    print(f'PASS orthonormal check: q={q}, m={m}, dark={dim}, cross capture={capture_cross:.12f}, same capture={capture_same:.12f}')


if __name__=='__main__':
    for args in [(3,2),(4,2),(3,3),(4,3),(5,2),(3,4),(4,4)]:case(*args)
