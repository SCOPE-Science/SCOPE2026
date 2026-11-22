#!/usr/bin/env python3
"""Exact finite certificate verifier for the octagonal square-graph tolerance complex.
Only the Python 3 standard library is required. Run: python check.py
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

N = 8
V = range(N)

def graph_edge(a,b):
    return a != b and min((a-b)%N,(b-a)%N)<=2

def graph_clique(q):
    return all(graph_edge(a,b) for a,b in combinations(q,2))

def tolerance_one(q):
    return any(graph_clique(set(q)-{v}) for v in q)

# Full powerset enumeration uses the original tolerance-one definition.
F = {tuple(s) for k in range(1,N+1) for s in combinations(V,k) if tolerance_one(s)}
assert Counter(map(len,F)) == {1:8, 2:28, 3:56, 4:32}
assert all(not graph_clique(c) for c in combinations(V,4))

certificate_path = Path(__file__).with_name('collapse_certificate.json')
cert = json.loads(certificate_path.read_text(encoding='utf-8'))
assert cert['vertex_count'] == N
assert len(cert['collapse_pairs']) == 40
work = set(F)
for count, (sigma_list,tau_list) in enumerate(cert['collapse_pairs'],1):
    sigma,tau=tuple(sigma_list),tuple(tau_list)
    assert sigma==tuple(sorted(sigma)) and tau==tuple(sorted(tau))
    assert sigma in work and tau in work
    assert len(tau)==len(sigma)+1 and set(sigma)<set(tau)
    # The listed free face has exactly one strict coface, not merely one facet.
    cofaces=[x for x in work if set(sigma)<set(x)]
    assert cofaces==[tau], (count,sigma,cofaces)
    work.remove(sigma);work.remove(tau)
assert Counter(map(len,work))=={1:8,2:20,3:16}
for k in (1,2,3):
    assert [list(q) for q in sorted(work) if len(q)==k] == cert['residual_faces'][str(k)]
assert 8-20+16 == 4

# Independent rank audit of the remaining 2-boundary matrix over Z.
# It is not used to infer the fundamental group or the integral homotopy type.
edges=sorted(f for f in work if len(f)==2)
triangles=sorted(f for f in work if len(f)==3)
index={e:i for i,e in enumerate(edges)}
columns=[]
for triangle in triangles:
    col={index[tuple(x for j,x in enumerate(triangle) if j!=i)]:(-1)**i for i in range(3)}
    columns.append(col)

def field_rank(cols,p):
    pivots={}
    for orig in cols:
        col={j:v%p for j,v in orig.items() if v%p}
        while col:
            i=min(col)
            if i not in pivots:
                z=pow(col[i],-1,p)
                pivots[i]={j:(v*z)%p for j,v in col.items() if (v*z)%p}
                break
            x=col[i]
            for j,v in pivots[i].items():
                nv=(col.get(j,0)-x*v)%p
                if nv:col[j]=nv
                else:col.pop(j,None)
    return len(pivots)
assert field_rank(columns,2)==13 and field_rank(columns,101)==13

# Independently verify the induced dihedral permutations preserve all faces.
def sign(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def signed_traces(a,reflection):
    permutation=lambda x:((a-x) if reflection else (a+x))%N
    assert {tuple(sorted(permutation(v) for v in f)) for f in F}==F
    ts=[0,0,0,0]
    for f in F:
        im=[permutation(i) for i in f]
        if tuple(sorted(im))==f:
            ts[len(f)-1]+=sign(im)
    chi=sum((-1)**k * ts[k] for k in range(4))
    return ts,chi-1
rot=[];ref=[]
for a in V:
    rot.append(signed_traces(a,False)[1]);ref.append(signed_traces(a,True)[1])
assert rot == [3,-1,-1,-1,3,-1,-1,-1],rot
assert ref == [-1,1,-1,1,-1,1,-1,1],ref
assert signed_traces(0,False)[0] == [8,28,56,32]
assert signed_traces(4,False)[0] == [0,-4,0,0]
assert signed_traces(0,True)[0] == [2,-2,-6,-2]
assert signed_traces(1,True)[0] == [0,-4,0,2]
assert sum(rot)==0 and sum(rot+ref)==0
print('VERIFIED: 124 nonempty faces; 40 valid elementary collapses; final (8,20,16); boundary rank 13 (mod 2 and 101).')
print('D8 homology rotation traces:',rot)
print('D8 homology reflection traces:',ref)
print('D8 rational fixed-subspace ranks: rotation 0; full D8 0; even-axis reflection 1; odd-axis reflection 2.')
