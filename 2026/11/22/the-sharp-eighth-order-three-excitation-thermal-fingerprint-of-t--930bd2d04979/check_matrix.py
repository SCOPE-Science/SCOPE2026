"""Independent exact sparse-matrix spectral-moment verifier.
Requires NumPy and SciPy; builds the two base Hamiltonians algebraically.
"""
import itertools
import numpy as np
from scipy.sparse import csr_matrix

I4=np.eye(4,dtype=np.int64)
J4=np.ones((4,4),dtype=np.int64)
P=np.roll(I4,1,axis=1)
Arook=np.kron(J4-I4,I4)+np.kron(I4,J4-I4)
Ashri=(np.kron(P+P.T,I4)+np.kron(I4,P+P.T)
       +np.kron(P,P)+np.kron(P.T,P.T))

def validate_base(A):
    assert A.shape==(16,16)
    assert (A==A.T).all() and (np.diag(A)==0).all()
    assert (A.sum(axis=0)==6).all() and set(np.unique(A))=={0,1}
    assert np.array_equal(A@A,4*np.eye(16,dtype=np.int64)+2*np.ones((16,16),dtype=np.int64))
    return sum(all(A[u,v] for u,v in itertools.combinations(S,2)) for S in itertools.combinations(range(16),4))

assert validate_base(Arook)==8
assert validate_base(Ashri)==0

T=tuple(itertools.combinations(range(16),3))

def three_excitation_hamiltonian(A):
    rr=[];cc=[]
    for i,S in enumerate(T):
        old=set(S)
        for j,U in enumerate(T):
            if i>=j:continue
            missing=old-set(U)
            added=set(U)-old
            if len(missing)==1 and len(added)==1:
                x=next(iter(missing));y=next(iter(added))
                if A[x,y]:rr.extend((i,j));cc.extend((j,i))
    return csr_matrix((np.ones(len(rr),dtype=np.int64),(rr,cc)),shape=(560,560))

moments=[]
for label,A in [('rook',Arook),('shrikhande',Ashri)]:
    H=three_excitation_hamiltonian(A)
    assert H.nnz==8736
    B=csr_matrix(np.eye(560,dtype=np.int64))
    values=[560]
    for k in range(1,9):
        B=B@H
        values.append(int(sum(B.diagonal())))
    moments.append(values)
    print(label,values)
assert moments[0][:8]==moments[1][:8]
assert moments[0][8]-moments[1][8]==2193408
print('PASS: independently generated graph, Hamiltonian and exact matrix-power traces')
