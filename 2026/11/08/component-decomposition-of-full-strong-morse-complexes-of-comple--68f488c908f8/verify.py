#!/usr/bin/env python3
"""Independent finite checks for full strong matching complexes of multipartite graphs."""
import itertools, collections

def experiment(sizes):
    part = [p for p,n in enumerate(sizes) for _ in range(n)]
    n=len(part)
    arcs = {(v,u) for v in range(n) for u in range(n) if part[v]!=part[u]}
    found=set()
    n_orders=0
    for order in itertools.permutations(range(n)):
        arr=[]; earlier=[]
        for v in order:
            before = [u for u in earlier if part[v]!=part[u]]
            if len(before)==1:arr.append((v,before[0]))
            earlier.append(v)
        f=frozenset(arr);found.add(f)
        # Key property: every gradient is supported on just one pair of parts
        pairs={tuple(sorted((part[v],part[u]))) for v,u in arr}
        assert len(pairs)<=1, ('cross-pair gradient',sizes,order)
        n_orders+=1
    # Build all faces from actual permutation gradients.
    faces={frozenset()}
    for f in found:
        for k in range(1,len(f)+1):
            for s in itertools.combinations(f,k):faces.add(frozenset(s))
    # Independently construct the pairwise stars and two flap types.
    expected={frozenset()}
    for i,j in itertools.combinations(range(len(sizes)),2):
        A=[v for v in range(n) if part[v]==i]
        B=[v for v in range(n) if part[v]==j]
        generators=[]
        for a in A: generators.append({(b,a) for b in B})
        for b in B: generators.append({(a,b) for a in A})
        for a in A:
            for b in B:
                generators.append({(b,a)}|{(x,b) for x in A if x!=a})
                generators.append({(a,b)}|{(y,a) for y in B if y!=b})
        for f in generators:
            for k in range(1,len(f)+1):
                for s in itertools.combinations(f,k):expected.add(frozenset(s))
    assert faces==expected,(sizes,'facet discrepancy',len(faces^expected))
    # Direct connected components of the 1-skeleton.
    vertices=[next(iter(f)) for f in faces if len(f)==1]
    adj={v:set() for v in vertices}
    for f in faces:
        if len(f)==2:
            x,y=tuple(f);adj[x].add(y);adj[y].add(x)
    comps=[]; unseen=set(vertices)
    while unseen:
        v=unseen.pop(); stack=[v];c={v}
        while stack:
            for w in adj[stack.pop()]:
                if w in unseen:unseen.remove(w);stack.append(w);c.add(w)
        comps.append(c)
    target=sorted([2*sizes[i]*sizes[j]-sizes[i]-sizes[j]+1 for i,j in itertools.combinations(range(len(sizes)),2)])
    assert len(comps)==len(target),(sizes,len(comps))
    # Each component corresponds exactly to an unordered pair of parts.
    comp_pairs=[]
    for c in comps:
        pairs={tuple(sorted((part[v],part[u]))) for v,u in c}
        assert len(pairs)==1
        comp_pairs.append(next(iter(pairs)))
    assert set(comp_pairs)==set(itertools.combinations(range(len(sizes)),2))
    # f-vector and alternating Euler rank for each connected piece.
    ranks=[]
    for pair in comp_pairs:
        counts=collections.Counter()
        for f in faces:
            if f and all(tuple(sorted((part[v],part[u])))==pair for v,u in f):counts[len(f)-1]+=1
        reduced_euler = sum((-1)**d*c for d,c in counts.items())-1
        claimed=2*sizes[pair[0]]*sizes[pair[1]]-sizes[pair[0]]-sizes[pair[1]]+1
        assert reduced_euler == -claimed,(pair,counts,reduced_euler,claimed)
        ranks.append(claimed)
    assert sorted(ranks)==target
    return n_orders,len(faces),len(comps),sum(ranks),max(len(f) for f in faces)

for sizes in ((2,2,2),(2,2,3),(2,3,3),(2,2,2,2),(3,3,3)):
    a=experiment(sizes)
    print('OK sizes=%s orders=%d faces=%d components=%d total_H1_rank=%d max_face_size=%d'%((sizes,)+a))
print('ALL_VERIFY_OK')
