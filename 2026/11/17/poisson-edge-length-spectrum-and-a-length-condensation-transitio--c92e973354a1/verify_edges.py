"""Exact small-dimensional checks of the Euclidean edge metric for partial permutohedra."""
from itertools import permutations, combinations
from collections import Counter
from math import factorial
from fractions import Fraction
import sympy as sp

def vertices(m,n):
    out=set()
    for k in range(m+1):
        for support in combinations(range(m),k):
            for vals in permutations(range(n-k+1,n+1)):
                x=[0]*m
                for i,v in zip(support,vals): x[i]=v
                out.add(tuple(x))
    return sorted(out)

def facets(m,n):
    f=[]
    for i in range(m):
        a=[0]*m;a[i]=-1;f.append((tuple(a),0))
    for k in range(1,m+1):
        for S in combinations(range(m),k):
            a=[int(i in S) for i in range(m)]
            f.append((tuple(a),k*n-k*(k-1)//2))
    return f

def candidate_edges(m,n):
    e=set()
    for v in vertices(m,n):
        support=sorted((v[i],i) for i in range(m) if v[i])
        for t in range(len(support)-1):
            u=list(v);i=support[t][1];j=support[t+1][1]
            u[i],u[j]=u[j],u[i]
            e.add(tuple(sorted((v,tuple(u)))))
        for i in range(m):
            if not v[i]:
                u=list(v);u[i]=n-len(support)
                e.add(tuple(sorted((v,tuple(u)))))
    return e

def exact_edges(m,n):
    v=vertices(m,n)
    fs=facets(m,n)
    act=[]
    for x in v:
        act.append({k for k,(a,b) in enumerate(fs) if sum(a[i]*x[i] for i in range(m))==b})
    e=set()
    for i,j in combinations(range(len(v)),2):
        both=act[i]&act[j]
        if not both:continue
        rr=sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix([fs[k][0] for k in both])).rank()
        if rr==m-1:e.add((v[i],v[j]))
    return e

def check(m,n):
    pred=candidate_edges(m,n)
    obs=exact_edges(m,n)
    assert pred==obs,(m,n,len(pred),len(obs),list(pred^obs)[:4])
    nv=len(vertices(m,n)); ne=len(obs)
    assert ne==m*nv//2
    lengths=Counter(sum((a-b)**2 for a,b in zip(v,w)) for v,w in obs)
    model=Counter({2:sum((k-1)*factorial(m)//factorial(m-k) for k in range(2,m+1))//2})
    for j in range(1,m+1):model[(n-m+j)**2]+=factorial(m)//factorial(j-1)
    assert lengths==model,(m,n,lengths,model)
    print('EDGE_SPECTRUM_OK',m,n,'vertices',nv,'edges',ne,'squared_length_counts',sorted(lengths.items()))

if __name__=='__main__':
    for m in range(2,5):
        for n in [m,m+2]:check(m,n)
    print('PARTIAL_PERMUTOHEDRON_EDGE_PASS')
