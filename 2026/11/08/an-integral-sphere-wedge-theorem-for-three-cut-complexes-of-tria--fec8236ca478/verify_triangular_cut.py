#!/usr/bin/env python3
"""Finite verification for the integral three-cut homotopy theorem of triangular graphs.

The infinite-dimensional statement is proved mathematically in RESULT.md.
This independent program verifies the universal four-label relative matching,
exhaustive Morse acyclicity in the first natural cases, and the dual membership.
No external packages are required.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb


def graph_edges(n):
    return list(combinations(range(n), 2))


def all_dual_faces(n):
    edges=graph_edges(n); pos={e:i for i,e in enumerate(edges)}
    facets=[]
    for a in range(n):
        facets.append(sum(1<<pos[(min(a,b),max(a,b))] for b in range(n) if b!=a))
    for S in combinations(range(n),4):
        facets.append(sum(1<<pos[e] for e in combinations(S,2)))
    faces=set()
    for facet in facets:
        sub=facet
        while sub:
            faces.add(sub)
            sub=(sub-1)&facet
    return edges,faces


def connected3(edges, triple):
    i,j,k=triple
    return sum(bool(set(edges[a])&set(edges[b])) for a,b in ((i,j),(i,k),(j,k))) >= 2


def direct_test(n, edges, faces):
    # Exhaustively test the definition, independent of the star/K4 facet theorem.
    N=len(edges)
    compatible={sum(1<<a for a in t) for t in combinations(range(N),3)
                if connected3(edges,t)}
    truth=set()
    for f in range(1,1<<N):
        if all(t&f!=t or t in compatible for t in
               (sum(1<<a for a in triple) for triple in combinations([i for i in range(N) if f>>i&1],3))):
            truth.add(f)
    assert truth==faces, (n,len(truth^faces))
    return len(compatible)


def is_positive_star(positive, edges):
    vertices={v for i in positive for v in edges[i]}
    centers=[v for v in sorted(vertices) if all(v in edges[i] for i in positive)]
    return centers


def local_match(n, edges, faces):
    # An order-preserving support map partitions the face poset into Morse fibers.
    W=[i for i,e in enumerate(edges) if 0 in e]
    positive_indices=[i for i,e in enumerate(edges) if 0 not in e]
    positive_mask=sum(1<<i for i in positive_indices)
    groups={}
    for f in faces:
        pos=f&positive_mask
        support=frozenset(v for i in positive_indices if pos>>i&1 for v in edges[i])
        groups.setdefault(support,[]).append(f)
    pairs=[]; crit=[]; local_summary={}
    for support, lst in groups.items():
        remaining=set(lst)
        if not support:
            pivot=1<<W[0]
            for f in list(remaining):
                if f&pivot==0 and f|pivot in remaining:
                    remaining.remove(f);remaining.remove(f|pivot);pairs.append((f,f|pivot))
        else:
            # Cone matches within each subfiber of fixed positive edge subset.
            bypositive={}
            for f in lst: bypositive.setdefault(f&positive_mask,[]).append(f)
            for pos, ff in bypositive.items():
                present=[i for i in positive_indices if pos>>i&1]
                stars=is_positive_star(present,edges)
                if len(support)==4 and not stars:
                    continue  # The 37 faces of a single K4 form a relative poset.
                if len(support)==3 and len(present)==3:
                    apex=min(support)  # Original triangle.
                elif len(support)==2:
                    apex=min(support)  # Original single edge.
                else:
                    assert stars, (n,support,present)
                    apex=stars[0]
                bit=1<<edges.index((0,apex))
                for f in ff:
                    if not f&bit:
                        assert f|bit in remaining, (n,'not a cone',support,pos)
                        remaining.remove(f);remaining.remove(f|bit)
                        pairs.append((f,f|bit))
            if len(support)==4:
                local_edges=[i for i in positive_indices if set(edges[i])<=support]
                assert len(local_edges)==6
                # Lex element matching on 37 nonstar faces.
                for i in local_edges:
                    bit=1<<i
                    candidates=[(f,f|bit) for f in remaining
                                if not f&bit and f|bit in remaining]
                    for low,high in candidates:
                        remaining.remove(low);remaining.remove(high)
                        pairs.append((low,high))
                assert len(remaining)==1 and next(iter(remaining)).bit_count()==4, (n,support,remaining)
                local_summary['four_label_blocks']=local_summary.get('four_label_blocks',0)+1
        crit+=list(remaining)
    assert len(crit)==1+comb(n-1,4)
    assert Counter(f.bit_count() for f in crit)=={1:1,4:comb(n-1,4)}
    assert len(pairs)*2+len(crit)==len(faces)
    return pairs,crit,local_summary


def check_acyclic(faces,pairs):
    # Directed Hasse graph: down except for matched incidences, which go up.
    pairs_set=set(pairs)
    idx={m:i for i,m in enumerate(sorted(faces))}
    indegree=[0]*len(idx); adj=[[] for _ in idx]; incidence=0
    for upper in faces:
        bits=upper
        while bits:
            b=bits&-bits;bits-=b
            lower=upper^b
            if lower not in idx: continue
            incidence+=1
            low,high=idx[lower],idx[upper]
            if (lower,upper) in pairs_set:
                adj[low].append(high);indegree[high]+=1
            else:
                adj[high].append(low);indegree[low]+=1
    q=deque(i for i,v in enumerate(indegree) if v==0)
    visited=0
    while q:
        i=q.popleft();visited+=1
        for j in adj[i]:
            indegree[j]-=1
            if indegree[j]==0:q.append(j)
    assert visited==len(idx),(visited,len(idx))
    return incidence


def verify():
    # The same local relative K4 pattern is repeated for each four-label support.
    for n in range(5,10):
        edges, faces=all_dual_faces(n)
        ct=direct_test(n,edges,faces) if n<=6 else 'not enumerated directly'
        pairs,crit,local=local_match(n,edges,faces)
        incidence=check_acyclic(faces,pairs)
        actual=Counter(f.bit_count() for f in crit)
        print(f'n={n}: |V(J)|={len(edges)}, dual_faces={len(faces)}, '
              f'connected_triples={ct}, matched_pairs={len(pairs)}, '
              f'Hasse_incidences={incidence}, critical={dict(sorted(actual.items()))}, '
              f'four_label_blocks={local["four_label_blocks"]}, acyclic=PASS')
    print('THEOREM_LOCAL_AND_FINITE_CHECKS_PASS')

if __name__=='__main__':verify()
