"""Standalone finite signed-permutation vertex-face rank check for the ridge classification.
Only uses the facet inequalities and vertices; no theorem rules are fed into the rank routine.
"""
from itertools import permutations, product, combinations
import numpy as np

def objects(n):
    V=[]
    for p in permutations(range(n)):
        for sig in product((-1,1),repeat=n):
            v=np.zeros((n,n),dtype=np.int8)
            for i,j in enumerate(p):v[i,j]=sig[i]
            V.append(v.ravel())
    V=np.asarray(V)
    facets=[]
    for axis in ('r','c'):
        for i in range(n):
            for s in product((-1,1),repeat=n):
                a=np.zeros((n,n),dtype=np.int8)
                if axis=='r':a[i,:]=s
                else:a[:,i]=s
                facets.append((axis,i,s,a.ravel()))
    return V,facets

def classified(a,b,n):
    typ,i,s,_=a
    typ2,j,t,_=b
    if typ==typ2:
        if i!=j:return 'right_disjoint' if n>=3 else 'not_ridge'
        h=sum(x!=y for x,y in zip(s,t))
        if h==1 and n>=3:return 'same_support'
        return 'not_ridge'
    if typ=='r':return 'cross' if s[j]==t[i] else 'not_ridge'
    return 'cross' if t[j]==s[i] else 'not_ridge'

def check(n):
    V,facets=objects(n)
    active=np.asarray([(V@a == 1) for typ,i,s,a in facets])
    counts={}
    comparisons=0
    errors=[]
    for ix,iy in combinations(range(len(facets)),2):
        ids=np.where(active[ix] & active[iy])[0]
        if len(ids)>1:
            pts=V[ids].astype(float)
            rank=np.linalg.matrix_rank(pts[1:]-pts[0],tol=1e-7)
        else: rank=0
        real=(rank==n*n-2)
        kind=classified(facets[ix],facets[iy],n)
        predicted=kind!='not_ridge'
        if real!=predicted:errors.append((ix,iy,kind,rank,len(ids)))
        if real: counts[kind]=counts.get(kind,0)+1
        comparisons+=1
    expect={'cross':n*n*2**(2*n-1)}
    if n>=3:expect.update({'right_disjoint':n*(n-1)*2**(2*n),'same_support':n*n*2**n})
    assert counts==expect,(n,counts,expect)
    assert not errors,(n,errors[:10])
    print(f'n={n} vertices={len(V)} facets={len(facets)} pairs_tested={comparisons} ridge_categories={counts} PASS')
if __name__=='__main__':
    for n in (2,3,4):check(n)
