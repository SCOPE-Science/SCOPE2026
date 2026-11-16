#!/usr/bin/env python3
"""Exact reproducible integer computations for Petersen-tree Fourier projectors."""
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction
from math import gcd
from functools import reduce
import csv
from pathlib import Path

HERE=Path(__file__).resolve().parent.parent
PAIRS=list(combinations(range(5),2))
EDGES=[(i,j) for i,j in combinations(range(10),2) if set(PAIRS[i]).isdisjoint(PAIRS[j])]
assert len(EDGES)==15
EDGE_ID={e:i for i,e in enumerate(EDGES)}
SIZE=1<<15

def fwht(v):
    v=list(v)
    for k in range(15):
        half=1<<k
        for base in range(0,SIZE,half*2):
            for x in range(base,base+half):
                a,b=v[x],v[x+half]
                v[x],v[x+half]=a+b,a-b
    return v

def bareiss(A):
    a=[list(row) for row in A]
    n=len(a)
    prev=1
    sign=1
    for k in range(n-1):
        if a[k][k]==0:
            p=next((i for i in range(k+1,n) if a[i][k]),None)
            if p is None:return 0
            a[k],a[p]=a[p],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[n-1][n-1]

def tree_indicator():
    F=[0]*SIZE
    for indices in combinations(range(15),9):
        parent=list(range(10))
        def root(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        valid=True
        for i in indices:
            u,v=EDGES[i];ru,rv=root(u),root(v)
            if ru==rv:
                valid=False;break
            parent[ru]=rv
        if valid:
            F[sum(1<<i for i in indices)]=1
    return F

def det_weighted_laplacian(mask):
    A=[[0]*9 for _ in range(9)]
    for j,(u,v) in enumerate(EDGES):
        s=1-2*((mask>>j)&1)
        if u<9:A[u][u]+=s
        if v<9:A[v][v]+=s
        if u<9 and v<9:A[u][v]-=s;A[v][u]-=s
    return bareiss(A)

def edge_perms():
    out=[]
    for p in permutations(range(5)):
        vert=[PAIRS.index(tuple(sorted((p[i],p[j])))) for i,j in PAIRS]
        q=[EDGE_ID[tuple(sorted((vert[u],vert[v])))] for u,v in EDGES]
        out.append(q)
    assert len(set(map(tuple,out)))==120
    return out

def orbits(perms):
    seen=bytearray(SIZE)
    answer=[]
    for mask in range(SIZE):
        if seen[mask]:continue
        orb=set()
        for p in perms:
            res=0
            for j in range(15):
                if (mask>>j)&1:res|=1<<p[j]
            orb.add(res)
        for o in orb:seen[o]=1
        assert min(orb)==mask
        answer.append((mask,len(orb)))
    assert sum(v for _,v in answer)==SIZE
    return answer

def main():
    f=tree_indicator()
    assert sum(f)==2000
    w=fwht(f)
    assert w[0]==2000
    assert sum(v*v for v in w)==SIZE*2000
    os=orbits(edge_perms())
    assert len(os)==396
    # Independently validate every character value using exact integer Bareiss determinants.
    for mask in range(SIZE):
        assert det_weighted_laplacian(mask)==w[mask]
    ah=Counter(abs(v) for v in w)
    expected={0:13912,16:11710,48:1140,64:4160,80:914,112:120,128:240,144:360,240:60,256:120,400:30,2000:2}
    assert ah==expected
    assert reduce(gcd,w)==16
    rank=SIZE-ah[0]
    assert rank==18856
    orbit_hist=Counter()
    for rep,sz in os:orbit_hist[abs(w[rep])]+=sz
    assert orbit_hist==ah
    z=fwht([int(x!=0) for x in w])
    assert z[0]==rank
    assert sum(t*t for t in z)==SIZE*rank
    total=sum(map(abs,z))
    assert total==1172832
    norm=Fraction(total,SIZE)
    assert norm==Fraction(36651,1024)
    assert sum(abs(x) for x in w)==738560
    # Test complement parity and non-switching-invariance of signed-tree sum.
    assert all(w[mask^ (SIZE-1)]==-w[mask] for mask in range(SIZE))
    incident=sum(1<<j for j,(u,v) in enumerate(EDGES) if u==0 or v==0)
    assert incident.bit_count()==3 and w[incident]!=w[0]
    cert=HERE/'certificates'/'petersen_frequency_orbits.csv'
    if cert.exists():
        with cert.open(newline='',encoding='utf-8') as ff:
            rows=list(csv.DictReader(ff))
        assert len(rows)==396
        assert [(int(r['representative_mask']),int(r['orbit_size']),int(r['walsh_coefficient'])) for r in rows]==[(mask,sz,w[mask]) for mask,sz in os]
    hist=HERE/'certificates'/'petersen_absolute_spectrum.csv'
    if hist.exists():
        with hist.open(newline='',encoding='utf-8') as ff: rows=list(csv.DictReader(ff))
        assert [(int(r['absolute_value']),int(r['count'])) for r in rows]==sorted(ah.items())
    print(f'PETERSEN_TREE_WALSH_PASS trees=2000 signings={SIZE} orbits={len(os)} rank={rank} gcd=16 projection={norm.numerator}/{norm.denominator}')
    return os,w,ah,z

if __name__=='__main__':main()
