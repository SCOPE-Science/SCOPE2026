"""Independent exhaustive verifier: 21-choose-6 edge subsets, DSU, NumPy FWHT.
Run: python check_subsets.py (requires Python 3 and NumPy).
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from pathlib import Path
import csv
from math import comb
import numpy as np

n=7
edges=list(combinations(range(n),2)); m=len(edges); q=1<<m
assert m==21 and comb(21,6)==54264
cross=[]
for a,b in edges:
    row=[]
    for c,d in edges:
        row.append((a<c<b<d) or (c<a<d<b))
    cross.append(row)

bits=[]
for chosen in combinations(range(m),n-1):
    if any(cross[a][b] for a,b in combinations(chosen,2)):
        continue
    parent=list(range(n))
    def root(v):
        while v!=parent[v]:v=parent[v]
        return v
    acyclic=True
    for ei in chosen:
        a,b=edges[ei]
        ra,rb=root(a),root(b)
        if ra==rb:
            acyclic=False;break
        parent[ra]=rb
    if not acyclic:continue
    z=sum(1<<e for e in chosen)
    bits.append(z)
assert len(bits)==1428 and len(set(bits))==1428

def fwht(x):
    for step in range(m):
        y=x.reshape(-1,2,1<<step)
        a=y[:,0,:].copy();b=y[:,1,:].copy()
        y[:,0,:]=a+b;y[:,1,:]=a-b
    return x
x=np.zeros(q,dtype=np.int32);x[bits]=1
fwht(x)
zeros=np.flatnonzero(x==0)
assert len(zeros)==160484
assert np.count_nonzero(x)==1936668
assert np.min(np.abs(x[x!=0]))==4
assert np.gcd.reduce(np.abs(x))==4
# Check every signed spectral level against the accompanying exact certificate.
with (Path(__file__).resolve().parent/'spectrum_levels.csv').open(newline='') as f:
    expected={int(r['walsh_multiplier']):int(r['multiplicity']) for r in csv.DictReader(f)}
vals, mult=np.unique(x,return_counts=True)
assert expected==dict(zip(map(int,vals),map(int,mult)))
assert int((vals.astype(np.int64)**2@mult.astype(np.int64)))==q*1428
pair_zero=[int(j) for j in zeros if int(j).bit_count()==2]
assert len(pair_zero)==14
pairs=[tuple(edges[i] for i in range(m) if z&(1<<i)) for z in pair_zero]
# Check the unique cancelling orbit: one boundary edge and a disjoint span-3 diagonal,
# with the endpoints of the boundary edge separated from the long chord by a single vertex.
base=frozenset(((0,1),(2,5)))
transformed=set()
for s in range(n):
    for eps in (1,-1):
        es=frozenset(tuple(sorted(((eps*a+s)%n,(eps*b+s)%n))) for a,b in base)
        transformed.add(es)
assert len(transformed)==14
assert {frozenset(p) for p in pairs}==transformed
# All degree-two frequencies partition into 21 dihedral orbits.
from collections import defaultdict
edge_idx={e:i for i,e in enumerate(edges)}
def orbit(i,j):
    ans=set()
    for s in range(n):
        for eps in (1,-1):
            def move(k):
                a,b=edges[k]
                return edge_idx[tuple(sorted(((eps*a+s)%n,(eps*b+s)%n)))]
            ans.add(tuple(sorted((move(i),move(j)))))
    return ans
pool=set(combinations(range(m),2));rows=[]
while pool:
    i,j=min(pool);o=orbit(i,j);pool-=o
    both=sum(bool(t&(1<<i)) and bool(t&(1<<j)) for t in bits)
    rows.append((len(rows)+1,len(o),f'{edges[i][0]}-{edges[i][1]}',f'{edges[j][0]}-{edges[j][1]}',i,j,both))
with (Path(__file__).resolve().parent/'pair_orbits.csv').open(newline='') as f:
    table=list(csv.DictReader(f))
assert len(rows)==len(table)==21 and sum(row[1] for row in rows)==210
for row,r in zip(rows,table):
    orbitid,sz,a,b,i,j,both=row
    onei=sum(bool(t&(1<<i)) for t in bits)
    onej=sum(bool(t&(1<<j)) for t in bits)
    W=1428-2*(onei+onej)+4*both
    assert [str(z) for z in (orbitid,sz,a,b,onei,onej,both,W)]==list(r.values())
# Independently recompute each two-edge character via inclusion moments.
incidence=Counter(e for t in bits for e in range(m) if t>>e&1)
for v in pair_zero:
    i,j=[k for k in range(m) if v>>k&1]
    both=sum(bool(t&(1<<i)) and bool(t&(1<<j)) for t in bits)
    assert 1428-2*(incidence[i]+incidence[j])+4*both==0
flag=(x!=0).astype(np.int32)
fwht(flag)
s=int(np.abs(flag).astype(np.int64).sum())
assert s==312904152
assert Fraction(s,q)==Fraction(39113019,262144)
print('SUBSET_WALSH_PASS count=1428 zeros=160484 rank=1936668 gcd=4 min=4 pairzeros=14 projection_norm=39113019/262144')
