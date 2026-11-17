#!/usr/bin/env python3
"""Independent finite checks for symmetry-fixed independence complexes of Woodroofe-class graphs.
Pure Python 3 standard library; run: python verify.py .
"""
from itertools import combinations, permutations

def edges_on(n, edge_mask):
    pairs=list(combinations(range(n),2))
    return frozenset(p for i,p in enumerate(pairs) if edge_mask>>i&1)

def edge_exists(edges,a,b): return (min(a,b),max(a,b)) in edges

def forbidden_cycle(n,edges):
    for k in range(4,n+1):
        if k==5: continue
        for S in combinations(range(n),k):
            E=sum(edge_exists(edges,a,b) for a,b in combinations(S,2))
            if E!=k:continue
            # A k-vertex induced graph with k edges is a k-cycle iff degree 2 throughout and connected.
            if not all(sum(edge_exists(edges,a,b) for b in S if b!=a)==2 for a in S):continue
            seen={S[0]};front=[S[0]]
            while front:
                v=front.pop()
                for w in S:
                    if w not in seen and edge_exists(edges,v,w):seen.add(w);front.append(w)
            if len(seen)==k:return (k,S)
    return None

def group_closure(n, gens):
    ident=tuple(range(n));group={ident};stack=[ident]
    while stack:
        p=stack.pop()
        for g in gens:
            q=tuple(p[g[i]] for i in range(n))
            if q not in group:group.add(q);stack.append(q)
    return sorted(group)

def orbit_graph(n,edges,group):
    unseen=set(range(n));orbits=[]
    while unseen:
        v=min(unseen);O=tuple(sorted({h[v] for h in group}));orbits.append(O);unseen.difference_update(O)
    good=[O for O in orbits if all(not edge_exists(edges,a,b) for a,b in combinations(O,2))]
    Q=frozenset((i,j) for i,j in combinations(range(len(good)),2)
        if any(edge_exists(edges,a,b) for a in good[i] for b in good[j]))
    return good,Q

def fixed_face_masks(n,edges,group):
    faces=set()
    for mask in range(1<<n):
        V=[i for i in range(n) if mask>>i&1]
        if any(edge_exists(edges,a,b) for a,b in combinations(V,2)):continue
        if all(sum(1<<h[i] for i in V)==mask for h in group):faces.add(mask)
    return faces

def model_face_masks(good,Q):
    faces=set()
    for mask in range(1<<len(good)):
        S=[i for i in range(len(good)) if mask>>i&1]
        if any((i,j) in Q for i,j in combinations(S,2)):continue
        faces.add(sum(1<<v for i in S for v in good[i]))
    return faces

def verify(n,E,G):
    for g in G:
        assert all(edge_exists(E,a,b)==edge_exists(E,g[a],g[b]) for a,b in combinations(range(n),2))
    good,Q=orbit_graph(n,E,G)
    assert forbidden_cycle(len(good),Q) is None, (n,E,G,good,Q)
    F=fixed_face_masks(n,E,G)
    M=model_face_masks(good,Q)
    assert F==M, (n,E,G,good,Q,F,M)
    return len(F)

def set_partitions(items):
    if not items:
        yield []
        return
    x,*rest=items
    for P in set_partitions(rest):
        yield [(x,)]+P
        for i in range(len(P)):
            yield P[:i]+[(x,)+P[i]]+P[i+1:]

def equitable_independent_quotient(n,E,P):
    if any(edge_exists(E,u,v) for O in P for u,v in combinations(O,2)):
        return None
    for O in P:
        for T in P:
            degrees={sum(edge_exists(E,u,v) for v in T) for u in O}
            if len(degrees)>1:
                return None
    return frozenset((i,j) for i,j in combinations(range(len(P)),2)
        if any(edge_exists(E,u,v) for u in P[i] for v in P[j]))

def main():
    graphs=0;groups=0;faces=0;nontrivial=0;eq_partitions=0
    for n in range(1,6):
        perms=list(permutations(range(n)))
        for mask in range(1<<(n*(n-1)//2)):
            E=edges_on(n,mask)
            if forbidden_cycle(n,E) is not None:continue
            graphs+=1
            for P in set_partitions(list(range(n))):
                Q=equitable_independent_quotient(n,E,P)
                if Q is not None:
                    eq_partitions+=1
                    assert forbidden_cycle(len(P),Q) is None, (n,E,P,Q)
            for p in perms:
                if not all(edge_exists(E,a,b)==edge_exists(E,p[a],p[b]) for a,b in combinations(range(n),2)):continue
                G=group_closure(n,[p]);groups+=1
                if len(G)>1:nontrivial+=1
                faces+=verify(n,E,G)
    # Additional noncyclic actions, including a genuine pentagon and chordal graphs.
    extras=[
      (5, frozenset((i,(i+1)%5) if i<(i+1)%5 else ((i+1)%5,i) for i in range(5)), [(1,2,3,4,0),(0,4,3,2,1)]),
      (4, frozenset((0,i) for i in (1,2,3)), [(0,2,3,1),(0,2,1,3)]),
      (6, frozenset([(0,1),(2,3),(4,5)]), [(2,3,4,5,0,1),(1,0,2,3,4,5)]),
      (6, frozenset(combinations(range(6),2)), [(1,2,0,3,4,5),(0,2,1,3,4,5)]),
    ]
    for n,E,gens in extras:
        G=group_closure(n,gens); groups+=1;nontrivial+=1
        assert max(len(group_closure(n,[g])) for g in G)<len(G), "extra action must be noncyclic"
        faces+=verify(n,E,G)
    print('WOODROOFE_ORBIT_CLASS_TESTS_PASS')
    print('eligible_graphs_n_le_5=',graphs)
    print('independent_equitable_partitions=',eq_partitions)
    print('cyclic_and_noncyclic_group_actions=',groups)
    print('nontrivial_group_actions=',nontrivial)
    print('fixed_and_model_faces_compared=',faces)
    print('noncyclic_cases=',len(extras))
    print('scope=finite_checks_only; general_theorem_requires_proof')
if __name__=='__main__':main()
