#!/usr/bin/env python3
"""Finite exact consistency checks for involution-fixed hypergraph matching spaces."""
from itertools import combinations, product
from math import factorial, comb
import json

def phase_classes(r):
    # Binary transversals up to simultaneous complement.
    return sorted({min(tuple(x),tuple(1-y for y in x)) for x in product((0,1),repeat=r)})

def allowed_from_actual_hyperedges(r,m):
    universe=set(range(2*m))
    hyperedges={frozenset(e) for e in combinations(range(2*m),r)}
    orbit_vertices=set()
    for E in hyperedges:
        T=frozenset((v+m)% (2*m) for v in E)
        if E & T: continue
        block=tuple(sorted(v % m for v in E))
        if len(set(block)) != r: continue
        bits=tuple(int(b+m in E) for b in block)
        bits=min(bits,tuple(1-b for b in bits))
        orbit_vertices.add((block,bits))
    q=2**(r-1)
    assert len(orbit_vertices)==comb(m,r)*q
    for B in combinations(range(m),r):
        assert sum(1 for x in orbit_vertices if x[0]==B)==q
    return sorted(orbit_vertices)

def mod_rank(rows,p):
    rows=[[int(x)%p for x in row] for row in rows]
    if not rows: return 0
    h=len(rows); w=len(rows[0]); rank=0
    for col in range(w):
        t=next((i for i in range(rank,h) if rows[i][col]%p),None)
        if t is None: continue
        rows[rank],rows[t]=rows[t],rows[rank]
        inv=pow(rows[rank][col],-1,p)
        rows[rank]=[(v*inv)%p for v in rows[rank]]
        for j in range(rank+1,h):
            if rows[j][col]:
                f=rows[j][col]
                rows[j]=[(a-f*b)%p for a,b in zip(rows[j],rows[rank])]
        rank+=1
    return rank

def block_boundary(q,k):
    # Top chain of the join of k independent q-vertex discrete spaces.
    facets=list(product(range(q),repeat=k)); rows=[]
    for remove in range(k):
        for choices in product(range(q),repeat=k-1):
            row=[]
            for facet in facets:
                row.append(((-1)**remove) if facet[:remove]+facet[remove+1:]==choices else 0)
            rows.append(row)
    return rows

results={}
for r,m in [(3,3),(3,6),(3,9),(5,5),(5,10)]:
    phases=phase_classes(r); q=len(phases)
    assert q==2**(r-1)
    if m<=6: # Directly enumerate original hyperedges and their disjoint involution-orbits.
        vertices=allowed_from_actual_hyperedges(r,m)
        if r==3 and m==6:
            edges={(i,j) for i,A in enumerate(vertices) for j,B in enumerate(vertices) if j>i and set(A[0]).isdisjoint(B[0])}
            assert len(vertices)==80 and len(edges)==160
            comps=[]; unseen=set(range(len(vertices)))
            while unseen:
                start=unseen.pop(); component={start}; stack=[start]
                while stack:
                    i=stack.pop()
                    for j in list(unseen):
                        if (min(i,j),max(i,j)) in edges:
                            unseen.remove(j);component.add(j);stack.append(j)
                comps.append(component)
            assert len(comps)==10 and all(len(c)==8 for c in comps)
            betti=len(edges)-len(vertices)+len(comps)
            assert betti==90
            results['three_uniform_six_pairs']={'orbit_vertices':len(vertices),'edges':len(edges),'components':len(comps),'first_betti':betti}
    k=m//r
    partition_count=factorial(m)//((factorial(r)**k)*factorial(k))
    betti=partition_count*((q-1)**k)
    results[f'r{r}_m{m}']={'q':q,'k':k,'top_betti':betti,'perfect_partitions':partition_count}
for q,k in [(4,1),(4,2),(4,3),(16,1),(16,2)]:
    if q**k>300:continue
    b=block_boundary(q,k);expected=q**k-(q-1)**k
    ranks={str(p):mod_rank(b,p) for p in [2,3,5,7]}
    assert set(ranks.values())=={expected}
    results[f'block_boundary_q{q}_k{k}']={'boundary_rows':len(b),'top_columns':q**k,'ranks_mod_primes':ranks,'nullity':(q-1)**k}
print(json.dumps({'status':'PASS','checks':results},sort_keys=True,indent=2))
