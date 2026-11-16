#!/usr/bin/env python3
"""Exact comparison of noncrossing and nonnesting partition Walsh transforms."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import csv
import sys

def partitions(n):
    def rec(a,k):
        if len(a)==n:
            yield tuple(a)
        else:
            for j in range(k+2):
                yield from rec(a+[j], max(k,j))
    yield from rec([0],0)

def noncrossing(p):
    n=len(p)
    return not any(p[a]==p[c] and p[b]==p[d] and p[a]!=p[b]
                   for a,b,c,d in combinations(range(n),4))

def arcs(p):
    return {pair for v in set(p) for pair in zip([i for i,x in enumerate(p) if x==v],
                                                [i for i,x in enumerate(p) if x==v][1:])}

def nonnesting(p):
    A=arcs(p)
    return not any((a,d) in A and (b,c) in A
                   for a,b,c,d in combinations(range(len(p)),4))

def rgs_from_blocks(blocks,n):
    labels=[None]*n
    for bi,block in enumerate(blocks):
        for x in block: labels[x]=bi
    mapping={}; return tuple(mapping.setdefault(x,len(mapping)) for x in labels)

def nn_via_root_antichains(n):
    roots=list(combinations(range(n),2));result=set()
    for bits in range(1<<len(roots)):
        chosen=[roots[i] for i in range(len(roots)) if (bits>>i)&1]
        if any((a<=c and d<=b) or (c<=a and b<=d)
               for (a,b),(c,d) in combinations(chosen,2)):
            continue
        parent=list(range(n))
        def find(i):
            while parent[i]!=i: i=parent[i]
            return i
        for a,b in chosen: parent[find(a)]=find(b)
        blocks={}
        for i in range(n): blocks.setdefault(find(i),[]).append(i)
        p=rgs_from_blocks(blocks.values(),n)
        assert arcs(p)==set(chosen)
        result.add(p)
    return result

def edge_mask(p,edges):
    return sum((1<<i) for i,(a,b) in enumerate(edges) if p[a]==p[b])

def spectrum(sets,n):
    edges=list(combinations(range(n),2));N=1<<len(edges)
    supp={edge_mask(p,edges) for p in sets}
    assert len(supp)==len(sets)
    indicator=[int(i in supp) for i in range(N)]
    h=1
    while h<N:
        for base in range(0,N,2*h):
            for j in range(h):
                u=indicator[base+j];v=indicator[base+j+h]
                indicator[base+j]=u+v;indicator[base+j+h]=u-v
        h*=2
    direct=[sum(1 if ((t&x).bit_count()&1)==0 else -1 for x in supp) for t in range(N)]
    assert direct==indicator
    assert sum(v*v for v in direct)==N*len(supp)
    return Counter(direct),direct

def main():
    expected={(2):(1,1),(3):(0,0),(4):(16,16),(5):(0,119)}
    hist={}
    for n in range(2,6):
        allp=list(partitions(n))
        nc={p for p in allp if noncrossing(p)}
        nn={p for p in allp if nonnesting(p)}
        nn2=nn_via_root_antichains(n)
        assert nn==nn2,(n,len(nn),len(nn2))
        assert len(nc)==len(nn)==[0,1,2,5,14,42][n]
        hnc,vec_nc=spectrum(nc,n);hnn,vec_nn=spectrum(nn,n)
        assert (hnc[0],hnn[0])==expected[n]
        if n<=4: assert hnc==hnn
        if n==5:
            assert hnc!=hnn and len(vec_nc)==1024
            hist={'NC':hnc,'NN':hnn}
            assert min(abs(x) for x in vec_nc if x)>0
            assert 1024-hnn[0]==905
            assert hnn[0]==119
        print(f'n={n} Catalan={len(nc)} NC_zero={hnc[0]} NN_zero={hnn[0]}')
    with open(sys.argv[1],newline='') as f:
        got={}
        reader=csv.DictReader(f)
        assert reader.fieldnames==['multiplier','noncrossing','nonnesting']
        for row in reader:
            key=int(row['multiplier']); assert key not in got
            got[key]=(int(row['noncrossing']),int(row['nonnesting']))
    exp={k:(hist['NC'][k],hist['NN'][k]) for k in set(hist['NC'])|set(hist['NN'])}
    assert got==exp
    print('CATALAN_NN_NC_FOURIER_SPLIT_PASS n=5 frequencies=1024 NC_rank=1024 NN_rank=905 NN_zeros=119')
if __name__=='__main__':
    assert len(sys.argv)==2
    main()
