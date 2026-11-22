#!/usr/bin/env python3
"""Exact arithmetic for the Desargues incidence graph and its 14 twist classes.
Requires Python 3.10+ and SymPy (tested with 1.13)."""
from itertools import combinations, permutations
from math import prod
from sympy import Matrix, zeros, eye
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

LABELS=tuple(range(5))
VERTICES=list(combinations(LABELS,2))+list(combinations(LABELS,3))
V_INDEX={v:i for i,v in enumerate(VERTICES)}
N=len(VERTICES)
L=zeros(N)
EDGES=[]
for i,a in enumerate(VERTICES):
    for j,b in enumerate(VERTICES):
        if len(a)==2 and len(b)==3 and set(a).issubset(b):
            EDGES.append((i,j))
            L[i,i]+=1; L[j,j]+=1
            L[i,j]-=1; L[j,i]-=1
assert N==20 and len(EDGES)==30
assert all(L[i,i]==3 for i in range(N))

def invariant_factors(a):
    d=smith_normal_form(a, domain=ZZ)
    vals=[abs(int(d[i,i])) for i in range(min(d.rows,d.cols))]
    assert all(x for x in vals)
    assert all(vals[i+1]%vals[i]==0 for i in range(len(vals)-1))
    return tuple(x for x in vals if x!=1)

def cycle_permutation(parts):
    p=list(range(5)); start=0
    for size in parts:
        for k in range(size): p[start+k]=start+(k+1)%size
        start+=size
    assert start==5
    return tuple(p)

def induced(p, dual):
    mapping=[]
    for v in VERTICES:
        image=tuple(sorted(p[k] for k in v))
        if dual: image=tuple(x for x in LABELS if x not in image)
        mapping.append(V_INDEX[image])
    assert len(set(mapping))==N
    for i,j in EDGES: assert L[mapping[i],mapping[j]]==-1
    return tuple(mapping)

def difference_basis_action(mapping, sink):
    others=[i for i in range(N) if i!=sink]
    bindex={x:i for i,x in enumerate(others)}
    action=zeros(N-1)
    for col,v in enumerate(others):
        if mapping[v]!=sink: action[bindex[mapping[v]],col]+=1
        if mapping[sink]!=sink: action[bindex[mapping[sink]],col]-=1
    return action

def group_data(mapping, sink):
    others=[i for i in range(N) if i!=sink]
    r=L.extract(others,others)
    p=difference_basis_action(mapping,sink)
    fixed=invariant_factors(r.row_join(p-eye(N-1)))
    return invariant_factors(r),fixed,int(r.det())

EXPECTED={
 '5': ((60,), (10,)),
 '41': ((2,24), (4,8)),
 '32': ((12,), (2,)),
 '311': ((60,), (10,)),
 '221': ((4,8,120), (2,8,40)),
 '2111': ((4,40,120), (2,40,40)),
 '11111': ((4,8,40,40,120), (2,2,10,10,10)),
}
PARTS=[(5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1)]
FULL=(4,8,40,40,120)
all_symmetries={induced(p,d) for p in permutations(LABELS) for d in (0,1)}
assert len(all_symmetries)==240
for part in PARTS:
    pp=cycle_permutation(part)
    for dual in (0,1):
        m=induced(pp,dual)
        outputs=[group_data(m,sink) for sink in (0,19)]
        assert outputs[0]==outputs[1]
        full,fixed,trees=outputs[0]
        assert full==FULL and trees==6144000
        assert fixed==EXPECTED[''.join(map(str,part))][dual]
        print('type',part,'dual',dual,'fixed',fixed,'order',prod(fixed))
print('DESARGUES_14_FROBENIUS_COMPONENT_GROUPS_OK')
