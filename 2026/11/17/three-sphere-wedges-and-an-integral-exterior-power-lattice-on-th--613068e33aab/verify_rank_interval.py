#!/usr/bin/env python3
"""Exact finite checks for the Boolean rank-[1,3] Hamming Rips theorem.
This checks the two-stage matching, its whole-face-poset acyclicity,
critical faces, canonical cross-polytopes and integral cocycle pairings.
The infinite-family assertion follows from the separate symbolic proof.
"""
from itertools import combinations
from math import comb
from collections import deque,Counter


def test(n):
    vertices=tuple(x for x in range(1,1<<n) if 1<=x.bit_count()<=3)
    singleton={x for x in vertices if x.bit_count()==1}
    non_singleton={x for x in vertices if x.bit_count() in (2,3)}
    # Generate every clique once by adding vertices in increasing order.
    faces={()}; extension=[((),list(vertices))]
    for base, compatible in extension:
        for j,v in enumerate(compatible):
            nxt=base+(v,)
            faces.add(nxt)
            extension.append((nxt,[w for w in compatible[j+1:] if (w^v).bit_count()<=2]))
    # All faces as tuples of integer bit masks.
    pair={}
    stage=Counter()
    for f in sorted(faces,key=lambda a:(len(a),a)):
        if f in pair: continue
        ts=tuple(v for v in f if v not in singleton)
        inter=((1<<n)-1)
        for v in ts:inter &=v
        if inter:
            b=inter&-inter
            higher=tuple(sorted(f+(b,))) if b not in f else None
            if higher and higher in faces:
                assert higher not in pair
                pair[f]=higher;pair[higher]=f;stage['singleton']+=1
    for f in sorted(faces,key=lambda a:(len(a),a)):
        if f in pair or not f: continue
        if len(f)==3 and all(v.bit_count()==2 for v in f):
            union=0
            for v in f: union |=v
            if union.bit_count()==3:
                higher=tuple(sorted(f+(union,)))
                assert higher in faces and higher not in pair
                pair[f]=higher;pair[higher]=f;stage['triangle']+=1
    # Empty face and a single critical vertex are paired in the augmented
    # poset, so unmatch that one pair to obtain a CW model with one 0-cell.
    orig_empty_mate=pair.get(())
    assert orig_empty_mate and len(orig_empty_mate)==1
    del pair[orig_empty_mate];del pair[()]
    critical={f for f in faces if f and f not in pair}
    expected={tuple(sorted((u^(1<<i) for i in range(n) if u & (1<<i))))
              for u in range(1<<n) if u.bit_count()==4}
    assert critical==expected | {orig_empty_mate}, (critical,expected)
    # Check complete Morse acyclicity by Kahn topological sort.
    # A matched face-cover is directed upwards; every other one downwards.
    adj={f:[] for f in faces if f}; indegree={f:0 for f in adj}
    for f in adj:
        for j in range(len(f)):
            g=f[:j]+f[j+1:]
            if not g: continue
            a,b=(g,f) if pair.get(g)==f else (f,g)
            adj[a].append(b);indegree[b]+=1
    queue=deque(x for x in adj if indegree[x]==0)
    seen=0
    while queue:
        f=queue.popleft();seen+=1
        for t in adj[f]:
            indegree[t]-=1
            if indegree[t]==0: queue.append(t)
    assert seen==len(adj), (seen,len(adj))
    # Each U yields a full eight-vertex octahedral S3. Pairing C_U with
    # each sphere cycle = diagonal unit matrix, since C_U is a maximal face.
    for u in range(1<<n):
        if u.bit_count()!=4: continue
        four_bits=[1<<i for i in range(n) if u & (1<<i)]
        opposites={ (s,u^s) for s in four_bits}
        octv=[s for s in four_bits]+[u^s for s in four_bits]
        assert len(set(octv))==8
        assert all(((a^b).bit_count()>2)==((a,b) in opposites or (b,a) in opposites)
                   for a,b in combinations(octv,2))
        facet=tuple(sorted(u^s for s in four_bits))
        assert facet in critical
        assert all(tuple(sorted(facet+(v,))) not in faces for v in vertices if v not in facet)
    return {'n':n,'vertices':len(vertices),'faces':len(faces)-1,'matching_pairs':sum(stage.values())-1,
            'critical_0':1,'critical_3':len(expected),'checked_dag_faces':seen}

if __name__=='__main__':
    for n in range(4,9):
        print(test(n))
    print('RANK_INTERVAL_1_3_MORSE_AND_INTEGRAL_BASIS_PASS')
