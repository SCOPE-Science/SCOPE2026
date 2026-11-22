#!/usr/bin/env python3
"""Exact isomorphism-class enumeration for connected cubic bipartite 12-vertex graphs.
Uses only the Python standard library and the adjacent GRAPH_DATA.json.
"""
import json
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path

DATA = json.loads(Path(__file__).with_name('GRAPH_DATA.json').read_text(encoding='utf-8'))
CHOOSE3 = [sum(1 << j for j in triple) for triple in combinations(range(6),3)]
PERMS = list(permutations(range(6)))

def connected(rows):
    seen={0}; todo=[0]
    while todo:
        v=todo.pop()
        if v<6:
            neighbors=(6+j for j in range(6) if rows[v] & (1<<j))
        else:
            neighbors=(i for i in range(6) if rows[i] & (1<<(v-6)))
        for w in neighbors:
            if w not in seen:
                seen.add(w);todo.append(w)
    return len(seen)==12

def transpose(rows):
    return tuple(sum(1<<i for i,r in enumerate(rows) if (r>>j)&1) for j in range(6))

def canonical_one_side(rows):
    # Every row permutation disappears under sorting; all column relabellings are tested.
    return min(tuple(sorted(sum(1<<perm[j] for j in range(6) if (r>>j)&1)
                            for r in rows)) for perm in PERMS)

def canonical(rows):
    # Connected bipartite graphs have a unique two-color partition up to swapping shores.
    return min(canonical_one_side(rows),canonical_one_side(transpose(rows)))

def edges(rows):
    return {tuple(sorted((i,6+j))) for i,r in enumerate(rows) for j in range(6) if (r>>j)&1}

def fourth_cycles(rows):
    # Every square corresponds to two left vertices and two common right neighbors.
    return sum(k*(k-1)//2 for i,j in combinations(range(6),2)
               for k in [(rows[i]&rows[j]).bit_count()])

def main():
    classes={}; considered=0
    # Every graph can relabel a left-side vertex as 0 and its three neighbors as 6,7,8.
    # Relabel the remaining left vertices to nondecreasing neighbor masks.
    for tail in combinations_with_replacement(CHOOSE3,5):
        rows=(7,)+tail
        if any(sum((r>>j)&1 for r in rows)!=3 for j in range(6)):
            continue
        if not connected(rows):
            continue
        considered+=1
        classes.setdefault(canonical(rows),rows)
    expected={tuple(g['row_masks']) for g in DATA['graphs']}
    assert considered==147, considered
    assert len(classes)==5, len(classes)
    assert set(classes)==expected,(set(classes),expected)
    for g in DATA['graphs']:
        rows=g['row_masks']
        assert canonical(rows)==tuple(rows)
        assert fourth_cycles(rows)==g['squares']
        assert len(edges(rows))==18
    # Verify the standard named graphs through explicit graph-isomorphism witnesses.
    # These are vertex relabellings from bipartite representatives to standard forms.
    def mapped_edges(rows, perm):
        return {tuple(sorted((perm[i],perm[j]))) for i,j in edges(rows)}
    prism_perm=(0,11,7,4,2,9,6,5,1,10,8,3)
    prism_edges={tuple(sorted((i,(i+1)%6))) for i in range(6)}
    prism_edges|={tuple(sorted((i+6,((i+1)%6)+6))) for i in range(6)}
    prism_edges|={(i,i+6) for i in range(6)}
    # Alternative verified explicit isomorphisms can be found by exhaustive 12-vertex bijection;
    # the canonical classification itself does not depend on graph naming.
    if mapped_edges(DATA['graphs'][2]['row_masks'],prism_perm)!=prism_edges:
        # The stored vertex labels use canonical row order; derive the isomorphism constructively.
        def find_map(rows, model_edges):
            adj=[set() for _ in range(12)]
            for a,b in edges(rows):adj[a].add(b);adj[b].add(a)
            target=[set() for _ in range(12)]
            for a,b in model_edges:target[a].add(b);target[b].add(a)
            chosen=[-1]*12;used=set()
            def rec(k):
                if k==12:return tuple(chosen)
                # Choose the unmapped vertex with most already mapped neighbors.
                i=max((v for v in range(12) if chosen[v]<0),key=lambda v:sum(chosen[w]>=0 for w in adj[v]))
                for j in range(12):
                    if j in used:continue
                    if all(((w in adj[i])==(chosen[w] in target[j])) for w in range(12) if chosen[w]>=0):
                        chosen[i]=j;used.add(j)
                        ans=rec(k+1)
                        if ans is not None:return ans
                        used.remove(j);chosen[i]=-1
                return None
            return rec(0)
        p=find_map(DATA['graphs'][2]['row_masks'],prism_edges)
        assert p is not None
    # Franklin LCF [5,-5]^6 on the Hamiltonian 12-cycle.
    franklin_edges={tuple(sorted((i,(i+1)%12))) for i in range(12)}
    franklin_edges|={tuple(sorted((i,(i+5)%12 if i%2==0 else (i-5)%12))) for i in range(12)}
    # Distinguish the Franklin class by the explicit spectrum-indicative number of squares
    # and independently verify it through an isomorphism search.
    if 'find_map' not in locals():
        # No assumption about a previously computed mapping.
        def find_map(rows, model_edges):
            adj=[set() for _ in range(12)]
            for a,b in edges(rows):adj[a].add(b);adj[b].add(a)
            target=[set() for _ in range(12)]
            for a,b in model_edges:target[a].add(b);target[b].add(a)
            chosen=[-1]*12;used=set()
            def rec(k):
                if k==12:return tuple(chosen)
                i=max((v for v in range(12) if chosen[v]<0),key=lambda v:sum(chosen[w]>=0 for w in adj[v]))
                for j in range(12):
                    if j in used:continue
                    if all(((w in adj[i])==(chosen[w] in target[j])) for w in range(12) if chosen[w]>=0):
                        chosen[i]=j;used.add(j)
                        ans=rec(k+1)
                        if ans is not None:return ans
                        used.remove(j);chosen[i]=-1
                return None
            return rec(0)
    assert find_map(DATA['graphs'][4]['row_masks'],franklin_edges) is not None
    print('CLASSIFICATION_PASS normalized_connected_candidates=147 isomorphism_classes=5')
    for g in DATA['graphs']:
        print(g['id'],'rows=',g['row_masks'],'squares=',g['squares'])
    print('NAMED_GRAPH_ISOMORPHISMS_PASS hexagonal_prism Franklin_LCF_5_minus5')
if __name__=='__main__':main()
