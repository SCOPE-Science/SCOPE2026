"""Exact cellular incidence checker for mixed deleted-product manifolds.
Public reproducibility: does not rely on symbolic topology packages.
"""
from itertools import combinations

def perm_sign(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def canonical_facet_sign(A,B,N):
    absent=set(range(N))-set(A)-set(B)
    assert len(absent)==1
    return perm_sign(tuple(A)+tuple(B)+(next(iter(absent)),))

def induce(seq,permutation):
    return tuple(sorted(permutation[i] for i in seq))

def induced_sign(seq,permutation):
    return perm_sign(tuple(permutation[i] for i in seq))

def verify(p,q):
    N=p+q+3
    facets={}
    incidence={}
    vertices=range(N)
    for A in combinations(vertices,p+1):
        for B in combinations(tuple(v for v in vertices if v not in A),q+1):
            eps=canonical_facet_sign(A,B,N)
            facets[(A,B)]=eps
            for i in range(len(A)):
                face=(A[:i]+A[i+1:],B)
                incidence[face]=incidence.get(face,0)+eps*(-1)**i
            for j in range(len(B)):
                face=(A,B[:j]+B[j+1:])
                incidence[face]=incidence.get(face,0)+eps*(-1)**(p+j)
    assert incidence and not any(incidence.values()), (p,q,{f:val for f,val in incidence.items() if val})
    for i in range(N-1):
        sigma=list(range(N));sigma[i],sigma[i+1]=sigma[i+1],sigma[i]
        for (A,B),eps in facets.items():
            target=(induce(A,sigma),induce(B,sigma))
            coefficient=eps*induced_sign(A,sigma)*induced_sign(B,sigma)
            assert coefficient==-facets[target]
    if p==q:
        for (A,B),eps in facets.items():
            assert eps*(-1)**(p*q)==-facets[(B,A)]
    return {'p':p,'q':q,'N':N,'facets':len(facets),'codimension_one_cells':len(incidence),'all_boundary_coefficients':0,'adjacent_transposition_degree':-1,'swap_degree':-1 if p==q else None}

if __name__=='__main__':
    for pair in [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3),(1,4),(4,1),(2,4)]:
        print(verify(*pair))
