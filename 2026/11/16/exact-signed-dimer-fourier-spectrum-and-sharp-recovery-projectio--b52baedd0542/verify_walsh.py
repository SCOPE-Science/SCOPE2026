#!/usr/bin/env python3
"""Exact reduced Walsh census for matchings of the four-dimensional cube.
Runs using only the Python standard library. No external data files are needed.
"""
from collections import Counter
from itertools import combinations
from math import gcd
import json

D=4
V=1<<D
edges=sorted((u,u^(1<<bit)) for u in range(V) for bit in range(D) if u < (u^(1<<bit)))
assert len(edges)==32
incident=[[] for _ in range(V)]
for idx,(u,v) in enumerate(edges):
    incident[u].append((idx,v))
    incident[v].append((idx,u))

matchings=[]
def enumerate_matchings(rem,chosen):
    if rem==0:
        matchings.append(chosen)
        return
    v=(rem&-rem).bit_length()-1
    for idx,w in incident[v]:
        if (rem>>w)&1:
            enumerate_matchings(rem^(1<<v)^(1<<w),chosen|(1<<idx))
enumerate_matchings((1<<V)-1,0)
assert len(matchings)==272 and len(set(matchings))==272

# Fix one canonical spanning-tree gauge. Signed edge weights differing by
# vertex sign flips contribute the same multiplier magnitude.
parent=list(range(V))
def find(x):
    while parent[x]!=x:
        x=parent[x]
    return x

tree=[]
for idx,(u,v) in enumerate(edges):
    a,b=find(u),find(v)
    if a!=b:
        tree.append(idx)
        parent[a]=b
chords=[idx for idx in range(32) if idx not in tree]
assert len(tree)==15 and len(chords)==17
N=1<<17
frequencies=[0]*N
for m in matchings:
    bits=sum((1<<j) for j,edge_idx in enumerate(chords) if m&(1<<edge_idx))
    frequencies[bits]+=1
assert sorted(set(frequencies)) == [0,1]

def fwht(a):
    stride=1
    while stride<len(a):
        for base in range(0,len(a),2*stride):
            for pos in range(base,base+stride):
                x,y=a[pos],a[pos+stride]
                a[pos]=x+y
                a[pos+stride]=x-y
        stride*=2

fwht(frequencies)
W=frequencies
abs_hist=Counter(abs(x) for x in W)
assert sum(v for v in abs_hist.values())==N
assert sum(x*x for x in W)==N*272
min_positive=min(abs(w) for w in W if w)
zerocount=abs_hist[0]
proj=[int(w!=0) for w in W]
fwht(proj)
proj_abs_sum=sum(abs(x) for x in proj)
assert sum(x*x for x in proj)==N*sum(w!=0 for w in W)

pair_zeros=[]
for i,j in combinations(range(32),2):
    val=sum(1 if (((m>>i)&1)^((m>>j)&1))==0 else -1 for m in matchings)
    if val==0:
        pair_zeros.append((i,j))
assert len(pair_zeros)==96
assert all(len({*edges[i],*edges[j]})==3 for i,j in pair_zeros)
assert all(sum(1 if not (m>>i)&1 else -1 for m in matchings)==136 for i in range(32))

result={
    "graph":"Q4", "vertices":V,"edges":32,"matchings":len(matchings),
    "gauge_dimension":15,"reduced_dimension":17,"reduced_characters":N,
    "zero_reduced":zerocount,"nonzero_reduced":N-zerocount,
    "full_fourier_rank":(N-zerocount)*(1<<15),
    "full_fourier_nullity":zerocount*(1<<15),
    "abs_histogram":{str(k):abs_hist[k] for k in sorted(abs_hist)},
    "min_positive":min_positive,"max_abs":max(abs_hist),
    "minimum_zero_support":2,"two_edge_zero_count":len(pair_zeros),
    "two_edge_zero_description":"adjacent edges, exactly",
    "projection_abs_sum":proj_abs_sum,"projection_denominator":N,
    "projection_norm_fraction":"2597417/32768",
    "parseval_squared_sum":sum(x*x for x in W),
    "gcd_all":gcd(*W)
}
assert result['projection_abs_sum']==10389668
assert result['gcd_all']==8
print(json.dumps(result,sort_keys=True,separators=(',',':')))
