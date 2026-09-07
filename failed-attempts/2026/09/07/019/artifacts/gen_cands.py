"""Generate orbit-representative B x P dot products (order 26), dedup, invariants."""
import sys, time, json
sys.path.insert(0,'/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts')
from pipeline_lib import *
from orbits_lib import *
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
from collections import defaultdict

def count_short_cycles(adj, kmax=7):
    # count distinct simple cycles of length k (undirected, each cycle counted once)
    # brute DFS from each vertex with ordering to avoid duplicates: only count cycles where start is minimal id in cycle
    n=len(adj)
    counts={k:0 for k in range(3,kmax+1)}
    # for each start s, DFS paths of length up to kmax, ending at neighbour of s
    sys.setrecursionlimit(10000)
    for s in range(n):
        # paths starting at s, visited set, current
        stack=[(s,[s],set([s]))]
        while stack:
            cur,path,seen=stack.pop()
            if len(path)>kmax: continue
            for w in adj[cur]:
                if w==s and len(path)>=3:
                    k=len(path)
                    if k<=kmax:
                        # check s is minimal in cycle to count once
                        if s==min(path):
                            counts[k]+=1
                elif w not in seen and w>s and len(path)<kmax:
                    # require all intermediate vertices > s? To ensure minimality, require w>s (since s minimal)
                    # but path may contain vertices <s? we already restrict, so skip
                    if any(u<s for u in path):
                        continue
                    stack.append((w,path+[w],seen|{w}))
                elif w not in seen and len(path)<kmax:
                    # allow w<s? then this cycle won't be counted at s (will be counted at smaller start), skip to prune
                    pass
        # Note: each undirected cycle counted twice (two directions)? Our DFS counts both directions from s? Path [s,...] direction matters: cycle s-a-b-s vs s-b-a-s are distinct paths but same undirected cycle. We count both? Let's divide by 2.
    for k in counts: counts[k]//=2
    return counts

def invariant_key(adj):
    g=bfs_girth(adj)
    cc=count_short_cycles(adj, kmax=6)
    # diameter via networkx? compute all-pairs shortest
    # use BFS from each node
    n=len(adj)
    maxd=0
    for s in range(n):
        dist=[-1]*n; dist[s]=0
        from collections import deque
        q=deque([s])
        while q:
            u=q.popleft()
            for w in adj[u]:
                if dist[w]==-1:
                    dist[w]=dist[u]+1; q.append(w)
        maxd=max(maxd,max(dist))
    return (g,cc[5] if 5 in cc else 0,cc[6] if 6 in cc else 0,maxd)

if __name__=="__main__":
    P=petersen_adj()
    pairsP=independent_edge_pairs(P)
    autsP=all_automorphisms(P)
    repsPE,_=edge_pair_orbits(P,pairsP,autsP)
    vpP=adjacent_vertex_pairs(P)
    repsPV,_=vertex_pair_orbits(P,vpP,autsP)
    print("P edge reps:",len(repsPE),"vertex reps:",len(repsPV), flush=True)
    # rebuild B seeds deterministically (same as before)
    candsPP=[]
    for ri in repsPE:
        ab,cd=pairsP[ri]
        for rj in repsPV:
            x,y=vpP[rj]
            for w in range(8):
                candsPP.append(dot_product(P,P,ab,cd,x,y,w))
    # dedup to get B1,B2 (use previous logic: first of each orbit type)
    repsPP,groupsPP=dedup_graphs(candsPP)
    print("P.P distinct:",len(repsPP),repsPP, flush=True)
    # Identify B1 (Aut4) vs B2 (Aut8)? Our earlier cands order: repsPE=[?,?], candsPP[0] is first pair, candsPP[8] second pair.
    # After dedup, repsPP should be [0,8]. Let's map.
    B_adjs=[candsPP[r] for r in repsPP]
    # sort by |Aut| to have deterministic B18_1 (|Aut|=4), B18_2 (|Aut|=8)
    def aut_size(a):
        G=to_networkx(a)
        return len(list(GraphMatcher(G,G).isomorphisms_iter()))
    sizes=[aut_size(a) for a in B_adjs]
    print("B sizes:",sizes, flush=True)
    order=sorted(range(len(B_adjs)), key=lambda i: sizes[i])
    B1=B_adjs[order[0]]; B2=B_adjs[order[1]]
    print("B1 Aut",sizes[order[0]],"B2 Aut",sizes[order[1]], flush=True)
    print("B1 edges",edgelist_from_adj(B1), flush=True)
    print("B2 edges",edgelist_from_adj(B2), flush=True)
    # Now orbit reps for B1,B2
    for Bi,label in [(B1,"B18_1"),(B2,"B18_2")]:
        auts=all_automorphisms(Bi)
        pairs=independent_edge_pairs(Bi)
        reps,_=edge_pair_orbits(Bi,pairs,auts)
        vp=adjacent_vertex_pairs(Bi)
        reps2,_=vertex_pair_orbits(Bi,vp,auts)
        print(f"{label}: |Aut|={len(auts)} edge-pair-orbits={len(reps)} vertex-orbits={len(reps2)}", flush=True)
