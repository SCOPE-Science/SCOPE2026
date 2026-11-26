#!/usr/bin/env python3
"""Exact bounded tree percolation topology census (standard library only)."""
from collections import defaultdict,Counter
from itertools import combinations
from math import comb
import json

def centers(adj):
    n=len(adj)
    if n<=2:return list(range(n))
    degree=[len(a) for a in adj]
    leaves=[i for i,d in enumerate(degree) if d<=1]
    left=n
    while left>2:
        left-=len(leaves)
        new=[]
        for u in leaves:
            for v in adj[u]:
                degree[v]-=1
                if degree[v]==1:new.append(v)
        leaves=new
    return leaves

def rooted_code(adj,u,pa=-1):
    return '('+''.join(sorted(rooted_code(adj,v,u) for v in adj[u] if v!=pa))+')'

def canon(adj):return min(rooted_code(adj,c) for c in centers(adj))

def all_trees(limit=11):
    trees={canon([()]):[()]}
    yield 1,trees
    for n in range(2,limit+1):
        next_trees={}
        for adj in trees.values():
            for u in range(n-1):
                adj2=[tuple(sorted((*adj[i],n-1))) if i==u else adj[i] for i in range(n-1)]
                adj2.append((u,))
                code=canon(adj2)
                if code not in next_trees:next_trees[code]=adj2
        trees=next_trees
        yield n, trees

def boundary_profile(adj):
    n=len(adj)
    neighbors=[sum(1<<v for v in adj[u]) for u in range(n)]
    degree=[len(a) for a in adj]
    profile=Counter()
    for mask in range(1,1<<n):
        k=mask.bit_count()
        current=mask & (-mask)
        visited=0
        while current:
            visited|=current
            frontier=0
            tmp=current
            while tmp:
                bit=tmp&-tmp
                v=bit.bit_length()-1
                frontier|=neighbors[v]
                tmp-=bit
            current=frontier & mask & ~visited
        if visited==mask:
            b=sum(degree[v] for v in range(n) if mask>>v&1)-2*(k-1)
            profile[k,b]+=1
    return tuple(sorted((k,b,v) for (k,b),v in profile.items()))

def edge_profile(adj):
    n=len(adj)
    edges=sorted((u,v) for u in range(n) for v in adj[u] if u<v)
    coeff=Counter()
    for sub in range(1<<len(edges)):
        p=list(range(n))
        def root(u):
            while p[u]!=u:u=p[u]
            return u
        for j,(u,v) in enumerate(edges):
            if (sub>>j)&1:
                ru,rv=root(u),root(v)
                p[ru]=rv
        comp=Counter(root(u) for u in range(n))
        for sz in comp.values():coeff[sz,sub.bit_count()]+=sz
    return coeff

def bridge_profile(profile,n):
    coeff=Counter()
    for k,b,cnt in profile:
        extra=n-k-b
        for t in range(extra+1):coeff[k,k-1+t]+=k*cnt*comb(extra,t)
    return coeff

def distance_profile(adj):
    n=len(adj)
    c=Counter()
    for src in range(n):
        q=[src];ds={src:0}
        for u in q:
            for v in adj[u]:
                if v not in ds:ds[v]=ds[u]+1;q.append(v)
        for val in ds.values():c[val]+=1
    return tuple(c.get(i,0) for i in range(n))

def degree_profile(adj):return tuple(sorted(map(len,adj)))

def main():
    expected={1:1,2:1,3:1,4:2,5:3,6:6,7:11,8:23,9:47,10:106,11:235}
    count={}; collision={}; pair=None; num_at_11=None
    for n,trees in all_trees():
        count[str(n)]=len(trees)
        assert len(trees)==expected[n],(n,len(trees))
        grouped=defaultdict(list)
        for code, adj in trees.items():
            prof=boundary_profile(adj)
            grouped[prof].append((code,adj))
        repeated=[v for v in grouped.values() if len(v)>1]
        collision[str(n)]=[len(v) for v in repeated]
        assert not repeated if n<11 else len(repeated)==1 and len(repeated[0])==2
        if n==11:
            pair=repeated[0];num_at_11=len(repeated)
    assert pair is not None
    # Independently corroborate with enumeration over all bond-edge states.
    coeffs=[]; vertices=[]
    for code,adj in pair:
        P=boundary_profile(adj)
        e=edge_profile(adj)
        assert e==bridge_profile(P,len(adj))
        coeffs.append(e)
        vertices.append({"canonical_code":code,"edges":[[u,v] for u in range(len(adj)) for v in adj[u] if u<v],
                        "degrees":degree_profile(adj),"ordered_distance_hist":distance_profile(adj)})
    assert coeffs[0]==coeffs[1]
    # Discrete random experiment exact p=1/2 distribution, denominator n*2^(n-1).
    dist=[{"size":k,"numerator":sum(c for (size,j),c in coeffs[0].items() if size==k),
            "denominator":len(pair[0][1])*2**(len(pair[0][1])-1)} for k in range(1,12)]
    assert sum(i["numerator"] for i in dist)==11*1024
    report={"tree_counts":count,"collision_class_sizes_by_n":collision,
            "witnesses":vertices,
            "identical_coefficients":[[k,j,c] for (k,j),c in sorted(coeffs[0].items())],
            "p_half_probabilities":dist,"shared_boundary_subtree_profile":[[k,b,c] for k,b,c in boundary_profile(pair[0][1])],
            "unique_pair_count_at_11":num_at_11,
            "checked_every_nonisomorphic_tree_through_order":11,
            "method":"center-rooted canonical leaf-addition census; exact connected-subset boundary counts; independent exact bond-edge-state check"}
    print(json.dumps(report,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
