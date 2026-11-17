"""Finite-sample verification of geometric fixed-pair sector decomposition.
Uses 1/2-edge subdivision, graph automorphisms, and explicit index-two characters.
The computation tests a finite discretization, not continuous homotopy equivalences.
"""
from itertools import combinations
import networkx as nx


def compose(a,b):
    return tuple(a[b[i]] for i in range(len(a)))

def subgroup(gs, gens):
    identity=tuple(range(len(next(iter(gs)))))
    out={identity}; pending=[identity]
    while pending:
        u=pending.pop()
        for s in gens:
            v=compose(u,s)
            if v not in out:
                out.add(v);pending.append(v)
    return out

def run():
    cases=0; inspected_pairs=0; sector_pairs=0
    for tree in nx.nonisomorphic_trees(6):
        base_n=tree.number_of_nodes()
        # Insert a midpoint vertex on each original edge.
        subdiv=nx.Graph();subdiv.add_nodes_from(range(base_n))
        mid={frozenset(e):base_n+i for i,e in enumerate(tree.edges())}
        for e,k in mid.items():
            a,b=tuple(e);subdiv.add_edges_from([(a,k),(k,b)])
        N=subdiv.number_of_nodes(); ident=tuple(range(N))
        aut=[]
        for iso in nx.algorithms.isomorphism.GraphMatcher(tree,tree).isomorphisms_iter():
            v=list(range(N))
            for a,b in iso.items():v[a]=b
            for edge,k in mid.items():v[k]=mid[frozenset(iso[x] for x in edge)]
            aut.append(tuple(v))
        assert ident in aut
        for gens in [[ident]]+[[g] for g in aut]+[[g,h] for g,h in combinations(aut[:min(6,len(aut))],2)]:
            H=subgroup(aut,gens)
            # pointwise fixed vertices for each subgroup computed directly.
            global_fixed={v for v in range(N) if all(g[v]==v for g in H)}
            fixed_pairs={frozenset((a,b)) for a,b in combinations(range(N),2)
                         if all(frozenset((g[a],g[b]))==frozenset((a,b)) for g in H)}
            via_trivial={frozenset(p) for p in combinations(sorted(global_fixed),2)}
            via_swapped=set()
            # Enumerate all index-two kernels as kernels of the swap action
            # on each candidate invariant unordered pair.
            chars={}
            for p in fixed_pairs-via_trivial:
                a,b=tuple(p)
                kernel=frozenset(g for g in H if g[a]==a)
                assert len(kernel)*2==len(H)
                chars.setdefault(kernel,set()).add(p)
            for kernel, observed_pairs in chars.items():
                fixed_kernel={v for v in range(N) if all(g[v]==v for g in kernel)}
                HminusK=[g for g in H if g not in kernel]
                g=HminusK[0]
                # The vertices outside the H-fixed locus break into components.
                R=subdiv.subgraph(fixed_kernel-global_fixed)
                cc=list(nx.connected_components(R))
                assert len(cc)%2==0
                for C in cc:
                    assert set(g[x] for x in C) in cc
                    assert set(g[x] for x in C)!=C
                predicted={frozenset((x,g[x])) for x in fixed_kernel-global_fixed}
                assert predicted==observed_pairs, (predicted,observed_pairs)
                via_swapped|=predicted
            assert fixed_pairs==via_trivial|via_swapped
            assert not via_trivial&via_swapped
            cases+=1;inspected_pairs+=len(fixed_pairs);sector_pairs+=len(via_swapped)
    print(f'FIXED_TREE_PAIR_SECTORS_PASS cases={cases} invariant_sample_pairs={inspected_pairs} swapped_sample_pairs={sector_pairs}')
if __name__=='__main__':run()
