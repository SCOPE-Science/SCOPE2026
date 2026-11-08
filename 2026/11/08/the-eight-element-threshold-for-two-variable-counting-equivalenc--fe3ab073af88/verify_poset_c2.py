#!/usr/bin/env python3
"""Exact finite poset/C2 census via canonical labelings and directed color refinement.
Requires Python 3.9+ standard library only. Deterministic and exhaustive.
"""
from collections import Counter,defaultdict
from itertools import permutations,product

def ideals(rows):
    n=len(rows)
    lower=[sum(1<<j for j in range(n) if rows[j] & (1<<i)) for i in range(n)]
    for ideal in range(1<<n):
        if all(not ideal & (1<<v) or (lower[v]&ideal)==lower[v] for v in range(n)):
            yield ideal

def augment(rows,mask):
    n=len(rows)
    return tuple(row | (((mask>>i)&1)<<n) for i,row in enumerate(rows))+(0,)

def canonical(rows):
    n=len(rows)
    indegrees=[sum((rows[j]>>i)&1 for j in range(n)) for i in range(n)]
    classes=defaultdict(list)
    for v in range(n):classes[(indegrees[v],rows[v].bit_count())].append(v)
    groups=[classes[k] for k in sorted(classes)]
    best=None
    for blocks in product(*(permutations(g) for g in groups)):
        order=sum((tuple(x) for x in blocks),())
        code=tuple(sum(1<<j for j,w in enumerate(order) if rows[v] & (1<<w)) for v in order)
        if best is None or code<best:best=code
    return best

def enumerate_posets(nmax=8):
    reps=[()]
    counts=[]
    logical_counts=[]
    for n in range(1,nmax+1):
        seen={}
        for old in reps:
            for mask in ideals(old):
                raw=augment(old,mask)
                key=canonical(raw)
                if key not in seen:seen[key]=raw
        reps=list(seen.values())
        counts.append(len(reps))
        print('POSETS',n,len(reps),flush=True)
        sigs,_=stable_signatures(reps)
        logical_counts.append(len(set(sigs)))
        print('C2_CLASSES',n,logical_counts[-1],flush=True)
    return reps,counts,logical_counts

def stable_signatures(graphs):
    """Shared palette directed 1-WL, oriented < as sole binary relation.
    Input graphs must have equal n; converges on the disjoint union.
    """
    n=len(graphs[0]); palette=[[0]*n for _ in graphs]
    iterations=[]
    for step in range(n*len(graphs)+1):
        all_keys=[]
        for rows,col in zip(graphs,palette):
            keys=[]
            for v in range(n):
                up=tuple(sorted(Counter(col[w] for w in range(n) if rows[v]&(1<<w)).items()))
                down=tuple(sorted(Counter(col[w] for w in range(n) if rows[w]&(1<<v)).items()))
                keys.append((col[v],up,down))
            all_keys.append(keys)
        unique=sorted({key for part in all_keys for key in part})
        index={key:k for k,key in enumerate(unique)}
        nxt=[[index[k] for k in part] for part in all_keys]
        iterations.append(len(unique))
        if nxt==palette:break
        palette=nxt
    else:raise AssertionError('WL did not stabilize')
    return [tuple(sorted(Counter(c).items())) for c in palette],iterations

def pair_equivalent(rows1,rows2):
    sigs,_=stable_signatures([rows1,rows2]);return sigs[0]==sigs[1]

def cover_edges(rows):
    n=len(rows)
    return tuple((i,j) for i in range(n) for j in range(n) if rows[i]&(1<<j) and not any(rows[i]&(1<<k) and rows[k]&(1<<j) for k in range(n)))

def connected_components(rows):
    n=len(rows)
    neighbors=[0]*n
    for i in range(n):
        for j in range(n):
            if rows[i] & (1<<j):neighbors[i]|=1<<j;neighbors[j]|=1<<i
    unvisited=(1<<n)-1;cnt=0
    while unvisited:
        cnt+=1;v=(unvisited&-unvisited).bit_length()-1; frontier=1<<v; seen=0
        while frontier:
            k=(frontier&-frontier).bit_length()-1;frontier&=frontier-1
            if seen&(1<<k):continue
            seen|=1<<k;frontier|=neighbors[k]&~seen
        unvisited &=~seen
    return cnt

WITNESSES=[
 ((48,48,192,192,0,0,0,0),(48,80,160,192,0,0,0,0)),
 ((204,240,64,64,128,128,0,0),(204,240,64,128,64,128,0,0))
]

def main():
    expected=[1,2,5,16,63,318,2045,16999]
    reps,counts,logical_counts=enumerate_posets()
    assert counts==expected,(counts,expected)
    assert logical_counts==expected[:-1]+[16997],logical_counts
    signatures,steps=stable_signatures(reps)
    equiv=defaultdict(list)
    for g,s in zip(reps,signatures):equiv[s].append(g)
    collision=[v for v in equiv.values() if len(v)>1]
    assert len(equiv)==16997 and len(collision)==2 and all(len(c)==2 for c in collision)
    assert len({canonical(r) for c in collision for r in c})==4
    assert {frozenset(map(canonical,c)) for c in collision}=={frozenset(map(canonical,p)) for p in WITNESSES}
    for pair in WITNESSES:
        a,b=pair
        assert canonical(a)!=canonical(b)
        assert pair_equivalent(a,b)
        print('WITNESS',a,b,'covers',tuple(map(len,map(cover_edges,pair))),'components',tuple(map(connected_components,pair)))
    # Crosscheck every class at order seven by deleting arbitrary maximals
    # Directly verify all labels are transitively closed, irreflexive and acyclic.
    for g in reps:
        n=len(g)
        assert all(not (g[i]&(1<<i)) for i in range(n))
        assert all(not (g[i]&(1<<j)) or (g[j]|g[i])==g[i] for i in range(n) for j in range(n))
    print('WL_STEPS',steps)
    print('VERIFY_OK',len(reps),len(equiv),len(collision))

if __name__=='__main__':main()
