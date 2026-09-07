"""Orbit reduction helpers."""
import sys
sys.path.insert(0,'/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts')
from pipeline_lib import *
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

def all_automorphisms(adj):
    G=to_networkx(adj)
    gm=GraphMatcher(G,G)
    return list(gm.isomorphisms_iter())  # list of dicts old->new

def edge_pair_orbits(adj, pairs, auts):
    # pairs: list of ((a,b),(c,d)) with a<b? Normalize edge order: each edge sorted, pair unordered.
    # For orbit computation, treat pair as frozenset of frozenset edges? But wiring distinguishes order within? For representative reduction, treat unordered.
    # Returns: list of representative indices, orbit partition
    n=len(pairs)
    # canonical key for pair: sort edges
    def norm(pair):
        (a,b),(c,d)=pair
        e1=tuple(sorted((a,b))); e2=tuple(sorted((c,d)))
        return tuple(sorted([e1,e2]))
    # union-find
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(x,y):
        rx,ry=find(x),find(y)
        if rx!=ry: parent[ry]=rx
    # map from normalized pair to index for quick lookup
    key_to_idx={}
    for i,p in enumerate(pairs):
        key_to_idx[norm(p)]=i
    # for each aut, permute each pair and union
    for perm in auts:
        # perm maps old->new
        for i,p in enumerate(pairs):
            (a,b),(c,d)=p
            e1=tuple(sorted((perm[a],perm[b])))
            e2=tuple(sorted((perm[c],perm[d])))
            key=tuple(sorted([e1,e2]))
            j=key_to_idx.get(key)
            if j is not None:
                union(i,j)
    # collect orbits
    from collections import defaultdict
    orbits=defaultdict(list)
    for i in range(n):
        orbits[find(i)].append(i)
    reps=[v[0] for v in orbits.values()]
    return reps, orbits

def vertex_pair_orbits(adj, vpairs, auts):
    n=len(vpairs)
    def norm(e):
        return tuple(sorted(e))
    key_to_idx={norm(p):i for i,p in enumerate(vpairs)}
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(x,y):
        rx,ry=find(x),find(y)
        if rx!=ry: parent[ry]=rx
    for perm in auts:
        for i,(x,y) in enumerate(vpairs):
            key=tuple(sorted((perm[x],perm[y])))
            j=key_to_idx.get(key)
            if j is not None:
                union(i,j)
    from collections import defaultdict
    orbits=defaultdict(list)
    for i in range(n):
        orbits[find(i)].append(i)
    reps=[v[0] for v in orbits.values()]
    return reps, orbits

def dedup_graphs(adjs, time_limit_per_comp=5.0):
    """Dedup list of adjs via explicit isomorphism (GraphMatcher). Returns reps indices and partition.
    Uses invariant pre-filter: girth + number of 5-cycles? For now, use girth + bridgeless? Actually all cubic.
    We'll use sorted cycle-count vector as bucket: count 5-cycles? Let's compute girth + count of shortest cycles via BFS? Simpler: use edge-colorability? No.
    For small lists (<500), just O(N^2) with GraphMatcher is fine."""
    import time
    reps=[]; assign=[]
    rep_graphs_nx=[]
    for idx,adj in enumerate(adjs):
        G=to_networkx(adj)
        found=None
        for ri,rj in enumerate(reps):
            H=rep_graphs_nx[ri]
            gm=GraphMatcher(G,H)
            if gm.is_isomorphic():
                found=rj if False else ri  # position in reps
                assign.append(reps[found])
                break
        else:
            reps.append(idx)
            rep_graphs_nx.append(G)
            assign.append(idx)
    # map to rep index
    # reps are indices into adjs; assign is rep-index pointer? Let's return reps + groups
    from collections import defaultdict
    groups=defaultdict(list)
    for i,a in enumerate(assign):
        # a is idx of rep? Actually assign stores idx of rep graph (original index)
        groups[a].append(i)
    return reps, groups
