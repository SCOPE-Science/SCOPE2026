"""Exact finite combinatorial and involution-eigenspace checks for the even-cycle bounded-independence quotient."""
from itertools import combinations
from sympy import Matrix, eye

def verify(d):
    n=2*d
    A=set(range(0,n,2)); B=set(range(1,n,2))
    independent=[]
    for S in combinations(range(n),d):
        T=set(S)
        if all((i+1)%n not in T for i in S):
            independent.append(T)
    assert len(independent)==2 and {frozenset(S) for S in independent}=={frozenset(A),frozenset(B)}
    labels=[sorted(A),sorted(B)]
    # Ambient bases for the two shore augmentation representations.
    basis=[]
    for shore in labels:
        last=shore[-1]
        for i in shore[:-1]:
            v=[0]*n; v[i]=1;v[last]=-1;basis.append(v)
    m=len(basis)
    transformed=[]
    for v in basis:
        w=[0]*n
        for j in range(n):w[(j+d)%n]=v[j]
        transformed.append(w)
    # Coordinates in the ambient basis are entries outside the two chosen last vertices.
    keep=[i for shore in labels for i in shore[:-1]]
    T=Matrix(m,m,lambda row,col:transformed[col][keep[row]])
    assert T*T==eye(m)
    p=m-(T-eye(m)).rank();q=m-(T+eye(m)).rank()
    expected_p=(d-2 if d%2==0 else d-1)
    expected_q=(d if d%2==0 else d-1)
    assert (p,q)==(expected_p,expected_q)
    assert T.det()==1
    torsion_degrees=list(range(p+1,p+q-1,2)) if q>=4 else []
    assert not torsion_degrees or (d>=4 and torsion_degrees[-1]<2*d-3)
    print('d=%d independent_max=%d plus=%d minus=%d quotient_top=%d torsion_degrees=%s'%(
        d,len(independent),p,q,2*d-3,torsion_degrees))

if __name__=='__main__':
    for d in range(2,9):verify(d)
    print('ALL_VERIFY_OK d_range=2..8 exact_integer_matrices=true')
