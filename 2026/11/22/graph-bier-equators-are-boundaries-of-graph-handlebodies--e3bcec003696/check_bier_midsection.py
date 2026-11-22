"""Finite-chain checks for deleted products of graphs and Alexander duals."""
from itertools import combinations
from math import comb
import numpy as np


def graph_edges(n, kind):
    if kind == 'path':
        return {(i, i+1) for i in range(n-1)}
    if kind == 'cycle':
        return {(min(i,(i+1)%n), max(i,(i+1)%n)) for i in range(n)}
    if kind == 'complete':
        return set(combinations(range(n),2))
    raise ValueError(kind)


def produce_chains(n, kind):
    edges = graph_edges(n, kind)
    allv = frozenset(range(n))
    k = [(i,) for i in range(n)] + sorted(edges)
    # Alexander dual faces of K: [n]\\B is NOT a face of K.
    dual = []
    for r in range(1,n+1):
        for b in combinations(range(n),r):
            outside=tuple(sorted(allv-set(b)))
            if outside not in k and outside != ():
                dual.append(b)
    cells={i:[] for i in range(n-2)}
    for a in k:
        for b in dual:
            if set(a).isdisjoint(b):
                cells[len(a)+len(b)-2].append((a,b))
    mats={}
    for dim in range(1,n-2):
        old=cells[dim-1]
        old_ids={c:j for j,c in enumerate(old)}
        arr=np.zeros((len(old),len(cells[dim])), dtype=np.int64)
        for ci,(a,b) in enumerate(cells[dim]):
            for i in range(len(a)):
                if len(a)>1:
                    a2=a[:i]+a[i+1:]
                    arr[old_ids[a2,b],ci]+=(-1)**i
            for j in range(len(b)):
                if len(b)>1:
                    b2=b[:j]+b[j+1:]
                    arr[old_ids[a,b2],ci]+=(-1)**(j+len(a)-1)
        mats[dim]=arr
    return cells,mats,edges


def rank_mod(a,p):
    a=np.array(a,dtype=np.int64,copy=True)%p
    m,n=a.shape
    r=0
    for c in range(n):
        hits=np.flatnonzero(a[r:,c])
        if len(hits)==0:continue
        j=r+int(hits[0])
        if j!=r:a[[r,j]]=a[[j,r]]
        a[r]=(a[r]*pow(int(a[r,c]),-1,p))%p
        for j in range(r+1,m):
            x=int(a[j,c])
            if x:a[j]=(a[j]-x*a[r])%p
        r+=1
        if r==m:break
    return r


def verify(n,kind,p=101):
    cells,mats,edges=produce_chains(n,kind)
    for d in range(2,n-2):
        assert not np.any(mats[d-1] @ mats[d]), 'boundary-square failure'
    g=len(edges)-n+1
    ranks={d:rank_mod(mat,p) for d,mat in mats.items()}
    dims={d:len(c) for d,c in cells.items()}
    betti=[dims[i]-ranks.get(i,0)-ranks.get(i+1,0) for i in dims]
    expected=[0]*(n-2)
    expected[0]=1
    expected[1]+=g
    expected[n-4]+=g
    expected[n-3]=1
    assert betti==expected, (n,kind,betti,expected)
    print(f'n={n}, graph={kind}, cycle_rank={g}, cells={list(dims.values())}, mod_{p}_betti={betti}, all_checks=PASS')

if __name__ == '__main__':
    for n in (5,6):
        for kind in ('path','cycle','complete'):
            verify(n,kind,p=101)
            verify(n,kind,p=2)
