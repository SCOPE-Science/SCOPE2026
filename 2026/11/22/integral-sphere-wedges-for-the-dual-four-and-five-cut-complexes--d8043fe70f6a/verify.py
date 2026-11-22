#!/usr/bin/env python3
"""Exact face-poset certificate for two dual cut complexes of L(Petersen).

Only Python 3's standard library is used. All sets are bitmasks on 15 vertices.
"""
from itertools import combinations
from collections import defaultdict, Counter, deque
from hashlib import sha256
import json


def graph():
    # Petersen vertices are the ten two-subsets of a five-set;
    # Petersen edges join disjoint two-subsets.
    points = tuple(combinations(range(5), 2))
    p_edges = tuple((a,b) for a,b in combinations(range(10), 2)
                    if not (set(points[a]) & set(points[b])))
    assert len(p_edges) == 15
    # Vertices of L(P) are these fifteen Petersen edges.
    adjacency = [0] * 15
    for i,j in combinations(range(15), 2):
        if set(p_edges[i]) & set(p_edges[j]):
            adjacency[i] |= 1 << j
            adjacency[j] |= 1 << i
    assert all(x.bit_count() == 4 for x in adjacency)
    return points, p_edges, tuple(adjacency)


def connected(mask, adjacency):
    seen = mask & -mask
    while True:
        updated = seen
        for i in range(len(adjacency)):
            if seen & (1 << i): updated |= adjacency[i] & mask
        if updated == seen: break
        seen = updated
    return seen == mask


def dual_faces(k, adjacency):
    n = len(adjacency)
    bad = tuple(mask for mask in range(1 << n)
                if mask.bit_count() == k and not connected(mask, adjacency))
    faces = {mask for mask in range(1, 1 << n)
             if not any(mask & b == b for b in bad)}
    for f in faces:
        for i in range(n):
            if f & (1 << i) and f != 1 << i:
                assert f ^ (1 << i) in faces
    return bad, faces


def matching(faces, n):
    active = set(faces)
    pairs = []
    counts = []
    for i in range(n):
        matches = sorted((f, f | 1 << i) for f in active
                         if not f & (1 << i) and f | (1 << i) in active)
        assert len(set(u for u,v in matches) | set(v for u,v in matches)) == 2 * len(matches)
        for lo,hi in matches:
            active.remove(lo)
            active.remove(hi)
        counts.append(len(matches))
        pairs += matches
    assert len(faces) == 2 * len(pairs) + len(active)
    return pairs, active, counts


def prove_acyclic(faces, pairs, n):
    # Every Hasse cover points down except a matching cover, which points up.
    matched = set(pairs)
    deg = {f:0 for f in faces}
    arrows = defaultdict(list)
    covers = 0
    for hi in faces:
        if hi.bit_count() < 2: continue
        for i in range(n):
            if not hi >> i & 1: continue
            lo = hi ^ (1 << i)
            if lo not in faces: raise AssertionError('not a simplicial complex')
            if (lo,hi) in matched:
                a,b = lo,hi
            else:
                a,b = hi,lo
            arrows[a].append(b)
            deg[b] += 1
            covers += 1
    ready=deque(x for x in sorted(faces) if deg[x]==0)
    processed=0
    while ready:
        v=ready.popleft();processed+=1
        for w in arrows[v]:
            deg[w]-=1
            if not deg[w]: ready.append(w)
    assert processed==len(faces), 'closed gradient path'
    return covers, processed


def mod2_betti(faces, n):
    bydim=defaultdict(list)
    for f in sorted(faces): bydim[f.bit_count()-1].append(f)
    ranks = {}
    for d in sorted(bydim):
        if d == 0:
            ranks[d]=0
            continue
        ix={f:i for i,f in enumerate(bydim[d-1])}
        pivots={}
        for f in bydim[d]:
            col=0
            for i in range(n):
                if f>>i&1: col ^= 1 << ix[f ^ (1 << i)]
            while col:
                top=col.bit_length()-1
                if top in pivots:col^=pivots[top]
                else:pivots[top]=col;break
        ranks[d]=len(pivots)
    betti={d:len(bydim[d])-ranks[d]-ranks.get(d+1,0)-(d==0)
           for d in bydim}
    assert all(x>=0 for x in betti.values())
    return {str(d):x for d,x in betti.items() if x},dict(sorted(Counter(f.bit_count()-1 for f in faces).items()))


def main():
    pts,edges,adj = graph()
    output={'graph':{'vertices':len(edges),'edges':sum(x.bit_count() for x in adj)//2,
                     'definition':'line graph of Kneser KG(5,2), edges listed lexicographically as endpoint-index pairs',
                     'petersen_two_subsets':list(pts),'petersen_edges':list(edges)}}
    for k in (4,5):
        bad,faces = dual_faces(k,adj)
        pairs,critical,counts=matching(faces,len(adj))
        covers,processed=prove_acyclic(faces,pairs,len(adj))
        betti,fvec=mod2_betti(faces,len(adj))
        crit=dict(sorted(Counter(str(f.bit_count()-1) for f in critical).items()))
        expected={4:{'0':1,'2':196},5:{'0':1,'3':624}}[k]
        assert crit == expected, (k,crit)
        assert betti == {str(k-2):expected[str(k-2)]}
        # compact fully reproducible certificate hash: sorted matched pairs
        listing=''.join(f'{a}:{b}\n' for a,b in pairs).encode()
        output[str(k)]={'disconnected_k_sets':len(bad),'dual_faces':len(faces),
                    'f_vector':{str(x):y for x,y in fvec.items()},
                    'matching_pairs':len(pairs),'matching_pairs_sha256':sha256(listing).hexdigest(),
                    'vertex_stage_match_counts':counts,'critical_cells':crit,
                    'gradient_Hasse_cover_relations':covers,'acyclic_topological_sort_vertices':processed,
                    'reduced_mod2_betti':betti}
    print(json.dumps(output,sort_keys=True,indent=2))

if __name__=='__main__':main()
