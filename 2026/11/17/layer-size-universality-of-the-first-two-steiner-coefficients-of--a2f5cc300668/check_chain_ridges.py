"""Reproduce facet-pair ridge classes for layered chain polytopes.
No external artifacts required; needs NumPy and Python standard library.
"""
from itertools import product, combinations
from math import factorial, comb, acos, sqrt, pi
import numpy as np

def check(sizes):
    r=len(sizes); n=sum(sizes)
    blocks=[]; s=0
    for m in sizes:
        blocks.append(tuple(range(s,s+m)));s+=m
    vs=[np.zeros(n,dtype=int)]
    for b in blocks:
        for mask in range(1,1<<len(b)):
            v=np.zeros(n,dtype=int)
            for j,x in enumerate(b):
                if mask&(1<<j):v[x]=1
            vs.append(v)
    V=np.array(vs)
    normals=[];rhs=[];types=[]
    for i in range(n):
        u=np.zeros(n,dtype=int);u[i]=-1
        normals.append(u);rhs.append(0);types.append(('L',i))
    for ch in product(*blocks):
        u=np.zeros(n,dtype=int);u[list(ch)]=1
        normals.append(u);rhs.append(1);types.append(('U',tuple(ch)))
    ridge_types={'LL':0,'LU':0,'UU':0}
    area_by_type={'LL':0.,'LU':0.,'UU':0.}
    counts={'LL':0,'LU':0,'UU':0}
    for a,b in combinations(range(len(normals)),2):
        ta=types[a];tb=types[b]
        pair=''.join(sorted([ta[0],tb[0]]))
        ix=np.where((V@normals[a]==rhs[a])&(V@normals[b]==rhs[b]))[0]
        isridge=(len(ix)>=n-1 and np.linalg.matrix_rank((V[ix[1:]]-V[ix[0]]).astype(float),tol=1e-8)==n-2)
        if pair=='LL':
            exp=True; i,j=ta[1],tb[1]
            ab=lambda i:next(k for k,B in enumerate(blocks) if i in B)
            if ab(i)==ab(j):
                m=sizes[ab(i)]
                scale=1/(m*(m-1))
            else:
                scale=1/(sizes[ab(i)]*sizes[ab(j)])
        elif pair=='LU':
            L=ta if ta[0]=='L' else tb
            U=tb if ta[0]=='L' else ta
            exp=L[1] not in U[1]
            ab=lambda i:next(k for k,B in enumerate(blocks) if i in B)
            scale=sqrt(r)/(sizes[ab(L[1])])*np.prod([1/sizes[k] for k,B in enumerate(blocks) if U[1][k] in B]) # placeholder not used
        else:
            exp=sum(x!=y for x,y in zip(ta[1],tb[1]))==1
        if isridge!=exp:
            raise AssertionError((sizes,ta,tb,isridge,exp,ix.tolist()))
        if isridge:
            counts[pair]+=1
    expected_ll=comb(n,2)
    expected_lu=sum((n-r) for _ in product(*blocks))
    expected_uu=sum(comb(m,2)*int(np.prod([sizes[k] for k in range(r) if k!=s])) for s,m in enumerate(sizes))
    assert counts=={'LL':expected_ll,'LU':expected_lu,'UU':expected_uu},(counts,expected_ll,expected_lu,expected_uu)
    return counts

if __name__=='__main__':
    profiles=[(2,2),(2,3),(3,3),(2,2,2),(2,3,2),(3,2,3),(2,2,2,2),(2,2,3,2),(2,3,4)]
    inspected=0
    for ms in profiles:
        counts=check(ms); inspected+=sum(counts.values())
        print(ms, counts)
    print('LAYERED_CHAIN_RIDGES_PASS',len(profiles),inspected)
