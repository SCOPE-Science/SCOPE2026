import networkx as nx, itertools

def has_triangle(G):
    for u,v in G.edges():
        if len(set(G.neighbors(u)) & set(G.neighbors(v)))>0:
            return True
    return False

def has_induced_C4(G):
    # triangle-free => any 4-cycle is induced; check girth
    nodes=list(G.nodes())
    # brute: any pair at distance 2 with >=2 common neighbors => C4
    for u in nodes:
        for w in nodes:
            if u>=w: continue
            if G.has_edge(u,w): continue
            cn=list(set(G.neighbors(u))&set(G.neighbors(w)))
            if len(cn)>=2:
                return True, (u,w,cn)
    return False, None

def cut_vertices(G): return set(nx.articulation_points(G))
def bridges(G): return set(nx.bridges(G))
def cut_pairs(G):
    # nonadjacent pairs whose removal disconnects
    pairs=[]
    nodes=list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            u,v=nodes[i],nodes[j]
            if G.has_edge(u,v): continue
            H=G.copy(); H.remove_nodes_from([u,v])
            if not nx.is_connected(H):
                pairs.append((u,v,nx.number_connected_components(H)))
    return pairs

def theta(a='a',b='b',npaths=3,plen=3):
    G=nx.Graph()
    G.add_nodes_from([a,b])
    for k in range(npaths):
        prev=a
        for i in range(1,plen):
            nd=f"p{k}_{i}" if i<plen-1 or True else None
            # interior nodes + connect
            if i<plen:
                if i==plen-1:
                    # last interior? Actually path length plen: a - v1 - ... - v_{plen-1} - b
                    pass
                G.add_node(f"p{k}_{i}")
        # edges: a-p1-p2-...-b ; plen=3: a-p1,p1-p2,p2-b
        seq=[a]+[f"p{k}_{i}" for i in range(1,plen)]+[b] if plen>1 else [a,b]
        # for plen=3: seq=[a,p1,p2,b]
        for x,y in zip(seq,seq[1:]):
            G.add_edge(x,y)
    return G

for plen in [3]:
    G=theta(plen=plen)
    print("nodes",G.number_of_nodes(),"edges",G.number_of_edges())
    print("planar?",nx.check_planarity(G)[0])
    print("triangle?",has_triangle(G))
    print("C4?",has_induced_C4(G))
    print("cutverts?",cut_vertices(G))
    print("bridges?",bridges(G))
    print("is cycle?", all(d==2 for _,d in G.degree()))
    cps=cut_pairs(G)
    print("num cut pairs:",len(cps))
    for p in cps[:20]: print(p)
