#!/usr/bin/env python3
"""Independent finite verification of monophonic-position classification on L(K_n)."""
from itertools import combinations
from math import comb

def inspect(n):
    base=list(combinations(range(n),2)); q=len(base)
    neighbors=[set(j for j,f in enumerate(base) if i!=j and len(set(e)&set(f))==1) for i,e in enumerate(base)]
    # Enumerate every induced path in the line graph using adjacency, not root paths.
    path_masks=set()
    def dfs(path,used):
        if len(path)>=3: path_masks.add(used)
        for v in neighbors[path[-1]]:
            if used>>v&1: continue
            if any(v in neighbors[w] for w in path[:-1]): continue
            dfs(path+[v],used | (1<<v))
    for v in range(q):dfs([v],1<<v)
    forbidden=set()
    for mask in path_masks:
        inds=[i for i in range(q) if mask>>i&1]
        for tri in combinations(inds,3):forbidden.add(sum(1<<i for i in tri))
    actual=[True]*(1<<q)
    # Any selected triple is forbidden iff all its members occur on some induced path.
    for mask in range(1<<q):
        if mask.bit_count()<3:continue
        actual[mask]=not any(mask&t==t for t in forbidden)
    counted=[0]*(q+1);facets=[0]*(q+1)
    for mask in range(1<<q):
        k=mask.bit_count()
        expected=k<=2 or all(j in neighbors[i] for i,j in combinations([t for t in range(q) if mask>>t&1],2))
        assert actual[mask]==expected,(n,mask,actual[mask],expected)
        if actual[mask]:
            counted[k]+=1
            if not any(actual[mask | 1<<j] for j in range(q) if not mask>>j&1):facets[k]+=1
    predicted=[0]*(q+1); predicted[0]=1;predicted[1]=q;predicted[2]=comb(q,2)
    for k in range(3,n):predicted[k]=n*comb(n-1,k)
    predicted[3]+=comb(n,3)
    assert counted==predicted,(n,counted,predicted)
    if n>=4:
        f=[0]*(q+1);f[2]=3*comb(n,4);f[3]=comb(n,3);f[n-1]+=n
        assert facets==f,(n,facets,f)
    # Euler characteristic as independent check of proposed homotopy type.
    chi=sum((-1)**(k-1)*counted[k] for k in range(1,q+1))
    if n>=4:assert chi==1-3*comb(n,4)+comb(n-1,3),(n,chi)
    print('n=',n,'vertices=',q,'induced_path_masks=',len(path_masks),'forbidden_triples=',len(forbidden),'faces=',sum(counted),'facets=',sum(facets),'chi=',chi)

if __name__=='__main__':
    for n in (3,4,5,6):inspect(n)
    print('VERIFY_OK')
