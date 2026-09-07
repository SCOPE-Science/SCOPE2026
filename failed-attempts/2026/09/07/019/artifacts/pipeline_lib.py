"""Lane 23 pipeline: Blanusa x Petersen order-26 dot-product census.
Pure Python + networkx. All definitions explicit; no assumed invariants.
"""
import itertools, sys, time, hashlib, json, os
from collections import deque

# ---------- basic graph utils (adj as list[set]) ----------

def adj_from_edgelist(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    return adj

def edgelist_from_adj(adj):
    es=[]
    for u in range(len(adj)):
        for v in adj[u]:
            if v>u: es.append((u,v))
    return sorted(es)

def is_cubic(adj):
    return all(len(nb)==3 for nb in adj)

def bfs_girth(adj):
    n=len(adj)
    best=None
    for s in range(n):
        dist=[-1]*n; parent=[-1]*n
        dist[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for w in adj[u]:
                if dist[w]==-1:
                    dist[w]=dist[u]+1; parent[w]=u; q.append(w)
                elif parent[u]!=w and parent[w]!=u:
                    # found cycle: dist[u]+dist[w]+1
                    # only count if w already visited and not trivial back edge;
                    # to avoid double, require dist[w]<=dist[u]
                    c=dist[u]+dist[w]+1
                    if best is None or c<best:
                        best=c
        if best==3:
            return 3
    return best

def has_bridge_networkx(nxG):
    import networkx as nx
    return any(True for _ in nx.bridges(nxG))

def to_networkx(adj):
    import networkx as nx
    G=nx.Graph()
    G.add_nodes_from(range(len(adj)))
    for u in range(len(adj)):
        for v in adj[u]:
            if v>u: G.add_edge(u,v)
    return G

# ---------- seeds ----------

def petersen_adj():
    # outer 0-1-2-3-4-0, spokes i-(i+5), inner 5-7-9-6-8-5 (step 2 mod 5 shifted by 5)
    n=10; edges=[]
    for i in range(5):
        edges.append((i,(i+1)%5))
        edges.append((i,i+5))
    inner=[5,7,9,6,8]
    for i in range(5):
        edges.append((inner[i],inner[(i+1)%5]))
    return adj_from_edgelist(n, edges)

def flower_j5_adj():
    # J5: k=2, indices 0..4, V = a_i,b_i,c_i,d_i; map: a_i=4*i, b_i=4*i+1, c_i=4*i+2, d_i=4*i+3
    n=20; edges=[]
    def A(i): return 4*(i%5)+0
    def B(i): return 4*(i%5)+1
    def C(i): return 4*(i%5)+2
    def D(i): return 4*(i%5)+3
    for i in range(5):
        edges.append((B(i),A(i))); edges.append((B(i),C(i))); edges.append((B(i),D(i)))
        edges.append((A(i),A(i+1)))
        edges.append((C(i),D(i+1)))
        edges.append((D(i),C(i+1)))
    return adj_from_edgelist(n, edges)

# ---------- dot product ----------

def dot_product(G_adj, H_adj, ab, cd, x, y, wiring):
    """Exhaustive wiring: wiring in 0..7.
    Let N(x)\\{y}=[x1,x2] sorted, N(y)\\{x}=[y1,y2] sorted.
    wiring bit0: swap within first block; bit1: swap within second; bit2: block swap.
    type0 (bit2=0): {a,b}->{x1,x2}, {c,d}->{y1,y2}; type1: crossed.
    Returns adjacency of order n1+n2-2.
    ab=(a,b), cd=(c,d) with given order (a,b etc. matter for wiring enumeration).
    """
    n1=len(G_adj); n2=len(H_adj)
    a,b=ab; c,d=cd
    Nx=sorted([w for w in H_adj[x] if w!=y])
    Ny=sorted([w for w in H_adj[y] if w!=x])
    assert len(Nx)==2 and len(Ny)==2, (Nx,Ny)
    x1,x2=Nx; y1,y2=Ny
    b0=wiring&1; b1=(wiring>>1)&1; b2=(wiring>>2)&1
    if b0: x1,x2=x2,x1
    if b1: y1,y2=y2,y1
    if b2==0:
        new_edges=[(a,x1),(b,x2),(c,y1),(d,y2)]
        # map H' vertices: keep track: H vertex w (w!=x,y) maps to new index
    else:
        new_edges=[(a,y1),(b,y2),(c,x1),(d,x2)]
    # Build new graph: vertices 0..n1-1 are G; H' vertices reindexed n1..
    hmap={}
    nxt=n1
    for w in range(n2):
        if w==x or w==y: continue
        hmap[w]=nxt; nxt+=1
    N=n1+n2-2
    adj=[set() for _ in range(N)]
    def addE(u,v):
        adj[u].add(v); adj[v].add(u)
    # G edges except ab,cd
    for u in range(n1):
        for v in G_adj[u]:
            if v>u:
                if (u==a and v==b) or (u==b and v==a) or (u==c and v==d) or (u==d and v==c):
                    continue
                addE(u,v)
    # H edges with both ends != x,y
    for u in range(n2):
        if u==x or u==y: continue
        for v in H_adj[u]:
            if v>u:
                if v==x or v==y: continue
                addE(hmap[u],hmap[v])
    # translate new_edges: endpoints in G stay, endpoints in H map via hmap
    # new_edges currently (g_endpoint, h_endpoint)
    mapped=[]
    for g,h in new_edges:
        # g is G vertex, h is H vertex (x1 etc.)
        mapped.append((g,hmap[h]))
    for u,v in mapped:
        addE(u,v)
    return adj

def independent_edge_pairs(adj):
    es=edgelist_from_adj(adj)
    out=[]
    m=len(es)
    for i in range(m):
        a,b=es[i]
        for j in range(i+1,m):
            c,d=es[j]
            if len({a,b,c,d})==4:
                out.append(((a,b),(c,d)))
    return out

def adjacent_vertex_pairs(adj):
    return edgelist_from_adj(adj)

# ---------- Hamiltonian solvers ----------

def ham_cycle_A(adj, time_limit=10.0, return_cycle=False):
    """Solver A: DFS from start=0, neighbours ordered by fewest onward moves,
    with connectivity + degree pruning. Returns cycle list or True/False."""
    import time as _t
    n=len(adj)
    if n<3: return (None if return_cycle else False)
    t0=_t.time()
    timed_out=[False]
    adjL=[sorted(nb) for nb in adj]
    start=0
    # quick degree check: all deg>=2 needed for Ham cycle
    for v in range(n):
        if len(adj[v])<2:
            return (None if return_cycle else False)
    path=[start]
    visited=[False]*n
    visited[start]=True
    result=[None]
    # precompute neighbour sets
    sys.setrecursionlimit(10000)
    # order: sort initial neighbours
    def unvisited_neighbours(u):
        return [w for w in adjL[u] if not visited[w]]

    def prune(current):
        # degree pruning: every unvisited vertex must have >=2 neighbours in unvisited+{current,start}
        # and >=1? For cycle, internal unvisited need 2 connections within allowed set.
        # allowed = unvisited set + current + start
        # Also connectivity: unvisited must be connected via allowed edges + current/start bridges?
        # Cheap checks first.
        # 1) degree check
        for v in range(n):
            if not visited[v]:
                cnt=0
                for w in adjL[v]:
                    if not visited[w] or w==current or w==start:
                        cnt+=1
                if cnt<2:
                    return True  # prune
                # also if v adjacent to current/start only? fine
        # 2) connectivity: BFS from current over unvisited+start
        seen=set([current])
        stack=[current]
        # allow moving to unvisited or start
        while stack:
            u=stack.pop()
            for w in adjL[u]:
                if w==start:
                    if w not in seen:
                        seen.add(w); stack.append(w)
                elif not visited[w]:
                    if w not in seen:
                        seen.add(w); stack.append(w)
                # visited non-start vertices not allowed
        # all unvisited + start must be seen
        for v in range(n):
            if (not visited[v]) and v not in seen:
                return True
        if start not in seen:
            return True
        return False

    # To avoid expensive prune at every node, apply every few depths? Apply always for n<=26 (cheap).
    def dfs(current):
        if _t.time()-t0>time_limit:
            timed_out[0]=True
            return True  # signal stop
        if len(path)==n:
            if start in adj[current]:
                result[0]=path[:]+[start]
                return True
            return False
        # prune
        if prune(current):
            return False
        cands=unvisited_neighbours(current)
        # order by number of onward unvisited moves (fail-first)
        def key(w):
            return sum(1 for z in adjL[w] if not visited[z])
        cands.sort(key=key)
        for w in cands:
            # additional pruning: don't go to start early
            visited[w]=True; path.append(w)
            if dfs(w):
                if result[0] is not None or timed_out[0]:
                    return True
            path.pop(); visited[w]=False
            if timed_out[0]:
                return True
        return False

    dfs(start)
    if timed_out[0]:
        raise TimeoutError("ham_cycle_A timeout")
    if return_cycle:
        return result[0]
    return result[0] is not None

def ham_cycle_B(adj, time_limit=10.0, return_cycle=False):
    """Solver B (independent path): iterative stack, different start & ordering,
    different pruning (only degree-1/isolated check + component count via union of unvisited).
    Start vertex = min-degree vertex (for cubic all same -> start=n-1 to differ from A)."""
    import time as _t
    n=len(adj)
    if n<3: return (None if return_cycle else False)
    for v in range(n):
        if len(adj[v])<2:
            return (None if return_cycle else False)
    t0=_t.time()
    adjL=[sorted(nb, reverse=True) for nb in adj]  # different order
    start=n-1  # different start
    # We'll do recursive DFS but with different prune: check no unvisited vertex becomes isolated
    # from unvisited set except possibly connected to path ends (current, start).
    path=[start]
    visited=[False]*n
    visited[start]=True
    result=[None]
    sys.setrecursionlimit(10000)
    def pruneB(current):
        # check each unvisited has at least one unvisited neighbour or is adjacent to both ends?
        # For Hamiltonian cycle, every unvisited vertex needs >=2 incident allowed edges (unvisited+current+start)
        # Same as A but implemented differently + connectivity via counting components of induced unvisited subgraph
        for v in range(n):
            if not visited[v]:
                c=0
                for w in adj[v]:
                    if not visited[w] or w==current or w==start:
                        c+=1
                if c<2:
                    return True
        # component check: count components of unvisited induced subgraph; each component must touch
        # both {current} and ... actually a component must have >=2 attachments to (path ends) unless it's the whole set?
        # Simplified independent check: BFS components of unvisited; if >1 components, each must have
        # at least 2 edges to {current,start} U other components? We'll just check each component has >=2 boundary edges.
        comp_id=[-1]*n
        nc=0
        for v in range(n):
            if (not visited[v]) and comp_id[v]==-1:
                # bfs
                q=[v]; comp_id[v]=nc
                qi=0
                while qi<len(q):
                    u=q[qi]; qi+=1
                    for w in adj[u]:
                        if (not visited[w]) and comp_id[w]==-1:
                            comp_id[w]=nc; q.append(w)
                nc+=1
        if nc<=1:
            return False
        # multiple components: each needs >=2 connections to (current/start/other?) For cycle, need overall 2-connected-ish.
        # Require each component has at least 2 edges to (outside component but allowed: current/start)
        # Actually edges between components don't exist by def, so only to current/start.
        for ci in range(nc):
            boundary=0
            for v in range(n):
                if comp_id[v]==ci:
                    for w in adj[v]:
                        if w==current or w==start:
                            boundary+=1
            if boundary<2:
                return True
        return False

    def dfs(current):
        if _t.time()-t0>time_limit:
            raise TimeoutError("ham_cycle_B timeout")
        if len(path)==n:
            if start in adj[current]:
                result[0]=path[:]+[start]
                return True
            return False
        if pruneB(current):
            return False
        cands=[w for w in adjL[current] if not visited[w]]
        # order differently: most-constrained first but with reverse tie-break
        cands.sort(key=lambda w: (sum(1 for z in adj[w] if not visited[z]), -w))
        for w in cands:
            visited[w]=True; path.append(w)
            r=dfs(w)
            if r and result[0] is not None:
                return True
            path.pop(); visited[w]=False
        return False
    try:
        dfs(start)
    except TimeoutError:
        raise
    if return_cycle:
        return result[0]
    return result[0] is not None

def ham_path_solver(adj, time_limit=10.0):
    """Hamiltonian path existence (for hypotraceability screen). Simple DFS with pruning."""
    import time as _t
    n=len(adj)
    if n==0: return False
    if n==1: return True
    t0=_t.time()
    adjL=[sorted(nb) for nb in adj]
    # try each start? For path, fix start at 0..? To decide existence, need to try all starts worst-case.
    # But for our screen (G and G-v), we can try starts 0..n-1 with pruning and early exit.
    sys.setrecursionlimit(10000)
    for start in range(n):
        visited=[False]*n
        visited[start]=True
        path=[start]
        found=[False]
        def dfs(cur):
            if _t.time()-t0>time_limit:
                raise TimeoutError("ham_path timeout")
            if len(path)==n:
                found[0]=True
                return True
            # connectivity prune: unvisited must be connected (via unvisited + cur)
            # quick degree: each unvisited (except maybe) needs >=1 allowed neighbour
            # check connectivity via BFS from cur
            # Build seen
            seen=set([cur])
            stack=[cur]
            while stack:
                u=stack.pop()
                for w in adjL[u]:
                    if not visited[w] and w not in seen:
                        seen.add(w); stack.append(w)
            for v in range(n):
                if not visited[v] and v not in seen:
                    return False
            cands=[w for w in adjL[cur] if not visited[w]]
            cands.sort(key=lambda w: sum(1 for z in adjL[w] if not visited[z]))
            for w in cands:
                visited[w]=True; path.append(w)
                if dfs(w): return True
                path.pop(); visited[w]=False
            return False
        try:
            if dfs(start):
                return True
        except TimeoutError:
            raise
        if _t.time()-t0>time_limit:
            raise TimeoutError("ham_path timeout outer")
    return False

def is_3_edge_colorable(adj, time_limit=15.0):
    """Backtracking 3-edge-coloring. Fix first vertex's incident edges to 0,1,2 to break symmetry.
    Returns True if colorable."""
    import time as _t
    t0=_t.time()
    es=edgelist_from_adj(adj)
    m=len(es)
    # adjacency edge incidence: for each vertex, list of edge indices
    n=len(adj)
    vert_edges=[[] for _ in range(n)]
    for i,(u,v) in enumerate(es):
        vert_edges[u].append(i); vert_edges[v].append(i)
    color=[-1]*m
    # order edges: BFS from 0? Use static order with most constrained first: sort by ... simple: order as given but fix first vertex
    # Find vertex 0 incident edges
    e0=vert_edges[0]
    assert len(e0)==3
    for idx,c in zip(e0,[0,1,2]):
        color[idx]=c
    # remaining order: sort by number of colored neighbours (dynamic). We'll implement DFS picking uncolored edge with most colored neighbours.
    def select_edge():
        best=-1; bestscore=-1
        for i in range(m):
            if color[i]==-1:
                u,v=es[i]
                # count distinct colors used on incident colored edges
                used=set()
                for j in vert_edges[u]:
                    if color[j]!=-1: used.add(color[j])
                for j in vert_edges[v]:
                    if color[j]!=-1: used.add(color[j])
                score=len(used)*10  # prefer constrained
                # tie-break: degree-like (number of incident uncolored?) Use index
                if score>bestscore:
                    bestscore=score; best=i
        return best
    sys.setrecursionlimit(10000)
    res=[False]
    def dfs(ncolored):
        if _t.time()-t0>time_limit:
            raise TimeoutError("edge coloring timeout")
        if ncolored==m:
            res[0]=True
            return True
        i=select_edge()
        u,v=es[i]
        used=set()
        for j in vert_edges[u]:
            if color[j]!=-1: used.add(color[j])
        for j in vert_edges[v]:
            if color[j]!=-1: used.add(color[j])
        for c in range(3):
            if c not in used:
                color[i]=c
                if dfs(ncolored+1): return True
                color[i]=-1
        return False
    try:
        dfs(len(e0))
    except TimeoutError:
        raise
    return res[0]

def delete_vertex(adj, v):
    n=len(adj)
    mp=[-1]*n
    nxt=0
    for u in range(n):
        if u==v: continue
        mp[u]=nxt; nxt+=1
    N=n-1
    nadj=[set() for _ in range(N)]
    for u in range(n):
        if u==v: continue
        for w in adj[u]:
            if w==v: continue
            if mp[u]<mp[w] or True:
                nadj[mp[u]].add(mp[w])
    # symmetrize (above adds both? we add directed; ensure symmetric)
    # Actually loop adds each directed edge; sets handle it.
    return nadj

def verify_ham_cycle(adj, cyc):
    if cyc is None: return False
    n=len(adj)
    if len(cyc)!=n+1: return False
    if cyc[0]!=cyc[-1]: return False
    seen=set(cyc[:-1])
    if len(seen)!=n or set(seen)!=set(range(n)): return False
    for i in range(n):
        if cyc[i+1] not in adj[cyc[i]]: return False
    return True
