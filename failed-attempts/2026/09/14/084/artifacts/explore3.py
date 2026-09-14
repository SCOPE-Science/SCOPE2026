import networkx as nx, itertools

def props(G, name):
    print("="*60); print(name, "n=",G.number_of_nodes(),"m=",G.number_of_edges())
    print("planar:", nx.check_planarity(G)[0])
    # triangle
    tri=False
    for u,v in G.edges():
        if set(G.neighbors(u))&set(G.neighbors(v)): tri=True; break
    print("triangle:",tri)
    # induced C4: pair at distance2 with >=2 common nbrs (triangle-free => induced)
    c4=False
    for u in G.nodes():
        for w in G.nodes():
            if str(u)>=str(w) or G.has_edge(u,w): continue
            if len(set(G.neighbors(u))&set(G.neighbors(w)))>=2: c4=True; break
        if c4: break
    print("C4:",c4)
    print("connected:",nx.is_connected(G))
    av=list(nx.articulation_points(G)) if nx.is_connected(G) else None
    print("cut-vertices:",av)
    print("bridges:",list(nx.bridges(G)) if nx.is_connected(G) else None)
    iscycle=all(d==2 for _,d in G.degree())
    print("is_cycle:",iscycle)
    nodes=list(G.nodes())
    cps=[]
    if nx.is_connected(G):
        for i in range(len(nodes)):
            for j in range(i+1,len(nodes)):
                u,v=nodes[i],nodes[j]
                if G.has_edge(u,v): continue
                H=G.copy(); H.remove_nodes_from([u,v])
                if not nx.is_connected(H):
                    comps=list(nx.connected_components(H))
                    if all(len(c)>=1 for c in comps):
                        cps.append((u,v,len(comps)))
    print("num_cutpairs:",len(cps))
    for p in cps[:15]: print("  ",p)
    return cps

def subdivided_K4(k=2):
    # each edge of K4 subdivided with k interior vertices
    base=[0,1,2,3]
    G=nx.Graph()
    G.add_nodes_from(base)
    for (u,v) in itertools.combinations(base,2):
        prev=u
        for i in range(k):
            nd=(u,v,i)
            G.add_node(nd)
            G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    return G

def subdivided_wheel(rim=5,k=1):
    # wheel: hub + rim cycle; subdivide each spoke and rim edge with k interior vertices
    G=nx.Graph(); hub='h'
    G.add_node(hub)
    rimnodes=[f"r{i}" for i in range(rim)]
    G.add_nodes_from(rimnodes)
    # rim cycle subdivided
    for i in range(rim):
        u=rimnodes[i]; v=rimnodes[(i+1)%rim]
        prev=u
        for j in range(k):
            nd=(f"rim{i}",j); G.add_node(nd); G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    for i in range(rim):
        u=hub; v=rimnodes[i]; prev=u
        for j in range(k):
            nd=(f"sp{i}",j); G.add_node(nd); G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    return G

for k in [2,3]:
    G=subdivided_K4(k)
    props(G,f"subdiv K4 k={k}")
for rim in [5,6]:
    for k in [1,2]:
        G=subdivided_wheel(rim,k)
        props(G,f"subdiv wheel rim={rim} k={k}")
