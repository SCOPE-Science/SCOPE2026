#!/usr/bin/env python3
"""Reproduce the three-point Q4 top homology and non-product obstruction.

Standard-library Python 3. Enumerates the full weight-3, degree-3 reduced
Swiatkowski differential, all disjoint simple-cycle triples, and an explicit
integer top cycle. All ranks are exact finite-field or fraction-free integer.
"""
from collections import Counter, defaultdict
from functools import reduce
from itertools import combinations, product
from math import gcd
from pathlib import Path
import json

vertices=range(16)
edges=sorted({tuple(sorted((v,v^(1<<k)))) for v in vertices for k in range(4)})
assert len(edges)==32
edge_idx={e:i for i,e in enumerate(edges)}
incident=defaultdict(list)
for i,(a,b) in enumerate(edges):
    incident[a].append(i); incident[b].append(i)
assert all(len(incident[v])==4 for v in vertices)
local=[(v,k) for v in vertices for k in (1,2,3)]
local_idx={h:i for i,h in enumerate(local)}
cols=[(a,b,c) for a,b,c in combinations(range(48),3) if len({a//3,b//3,c//3})==3]
assert len(cols)==15120
col_idx={c:i for i,c in enumerate(cols)}
row_idx={}
def row(a,b,e):
    key=(min(a,b),max(a,b),e)
    if key not in row_idx:row_idx[key]=len(row_idx)
    return row_idx[key]
differential=[]
for cc in cols:
    out=Counter()
    for pos,h in enumerate(cc):
        v,k=local[h]; other=[cc[j] for j in range(3) if j!=pos]
        for sg,e in ((1,incident[v][k]),(-1,incident[v][0])):
            out[row(*other,e)]+=(-1)**pos * sg
    differential.append({r:z for r,z in out.items() if z})
assert len(row_idx)==34272 and all(len(c)==6 for c in differential)

# Modulo-three rank bounds Q-rank from below, independently of the torus vectors.
def add_mod_basis(basis,vec,p=3):
    vv={i:z%p for i,z in vec.items() if z%p}
    while vv:
        pivot=max(vv)
        if pivot not in basis:
            inv=pow(vv[pivot],-1,p)
            basis[pivot]={i:z*inv%p for i,z in vv.items()}
            return True
        mult=vv[pivot]
        for i,z in basis[pivot].items():
            new=(vv.get(i,0)-mult*z)%p
            if new:vv[i]=new
            else:vv.pop(i,None)
    return False
boundary_basis={}
for cc in differential:add_mod_basis(boundary_basis,cc)
assert len(boundary_basis)==14991, len(boundary_basis)
assert len(cols)-len(boundary_basis)==129

# Canonical cycles: least-numbered vertex first, lower-valued second neighbor.
adj={v:[v^(1<<k) for k in range(4)] for v in vertices}
cycles={}
for length in (4,6,8):
    found={}
    for first in vertices:
        def walk(path):
            if len(path)==length:
                if path[-1] in adj[first] and path[1]<path[-1]:
                    found[tuple(path)]=tuple(path)
                return
            for nxt in adj[path[-1]]:
                if nxt>first and nxt not in path:
                    walk(path+[nxt])
        walk([first])
    cycles[length]=list(found)
assert tuple(len(cycles[d]) for d in (4,6,8))==(24,128,696)

def one_cycle(vv):
    out=Counter()
    for j,v in enumerate(vv):
        incoming=edge_idx[tuple(sorted((vv[j-1],v)))]
        outgoing=edge_idx[tuple(sorted((v,vv[(j+1)%len(vv)])))]
        for s,e in ((1,outgoing),(-1,incoming)):
            if e!=incident[v][0]:
                out[local_idx[v,incident[v].index(e)]]+=s
    return {i:z for i,z in out.items() if z}
prepared={length:[one_cycle(vv) for vv in cycles[length]] for length in cycles}

def three_torus(v1,v2,v3):
    out=Counter()
    for (a,ca),(b,cb),(c,cc) in product(v1.items(),v2.items(),v3.items()):
        hs=(a,b,c)
        sg=(-1)**sum(hs[i]>hs[j] for i in range(3) for j in range(i+1,3))
        out[col_idx[tuple(sorted(hs))]]+=sg*ca*cb*cc
    return {i:z for i,z in out.items() if z}

def boundary_zero(chain):
    out=Counter()
    for c,z in chain.items():
        for r,k in differential[c].items():out[r]+=z*k
    return all(x==0 for x in out.values())

# Rational span via fraction-free integer elimination with primitive normalization.
torus_basis={}
def exact_remainder(cc,install=False):
    vv=dict(cc)
    while vv:
        pivot=max(vv)
        if pivot not in torus_basis:
            if install:
                g=reduce(gcd,(abs(z) for z in vv.values()),0)
                if g>1:vv={i:z//g for i,z in vv.items()}
                torus_basis[pivot]=vv
            return pivot
        previous=torus_basis[pivot]
        a=vv[pivot];d=previous[pivot]
        if d<0:a=-a;d=-d
        for i in list(vv):vv[i]*=d
        for i,z in previous.items():
            new=vv.get(i,0)-a*z
            if new:vv[i]=new
            else:vv.pop(i,None)
        if vv:
            g=reduce(gcd,(abs(z) for z in vv.values()),0)
            if g>1:vv={i:z//g for i,z in vv.items()}
    return None

counts={}; square_tori=[]; square_basis_mod={}
for dims in ((4,4,4),(4,4,6),(4,4,8),(4,6,6)):
    ca,cb,cc=(cycles[d] for d in dims)
    ct=0
    for ia,a in enumerate(ca):
        sa=set(a)
        for ib,b in enumerate(cb):
            if dims[0]==dims[1] and ib<=ia:continue
            sb=set(b)
            if sa & sb:continue
            for ic,c in enumerate(cc):
                if dims[1]==dims[2] and ic<=ib:continue
                if (sa|sb) & set(c):continue
                ct+=1
                chain=three_torus(prepared[dims[0]][ia],prepared[dims[1]][ib],prepared[dims[2]][ic])
                assert boundary_zero(chain)
                if dims==(4,4,4):
                    square_tori.append(chain)
                    add_mod_basis(square_basis_mod,chain)
                    exact_remainder(chain,True)
                else:
                    assert exact_remainder(chain,False) is None
    counts[dims]=ct
assert counts=={(4,4,4):152,(4,4,6):576,(4,4,8):240,(4,6,6):144},counts
assert sum(counts.values())==1112
assert len(torus_basis)==128 and len(square_basis_mod)==128

witness=json.loads(Path(__file__).with_name('nonproduct_cycle.json').read_text(encoding='utf-8'))
extra={int(i):int(z) for i,z in witness['coefficients']}
assert len(extra)==1475 and all(abs(z)<=2 and z!=0 for z in extra.values())
assert all(0<=i<15120 for i in extra)
assert boundary_zero(extra)
# The exact rational test is essential: mod-3 independence alone would not
# exclude a non-saturated integral sublattice.
assert exact_remainder(extra,False) is not None
assert add_mod_basis(square_basis_mod,extra), 'witness should also be independent mod 3'
assert len(square_basis_mod)==129
print('Q4_THREE_PARTICLE_NONPRODUCT_H3_OK')
print('C3_columns=15120 boundary_rank_mod3=14991 free_H3_rank=129')
print('simple_cycle_triples=1112 torus_rational_rank=128 witness_terms=1475')
