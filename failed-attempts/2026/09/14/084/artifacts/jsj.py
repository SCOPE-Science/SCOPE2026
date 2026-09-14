import networkx as nx, itertools
# Build subdivided wheels with labeled nodes and analyze Dani-Thomas structures.
def subdivided_wheel(rim=5,k=2):
    G=nx.Graph(); hub='h'; G.add_node(hub)
    rimnodes=[f"r{i}" for i in range(rim)]; G.add_nodes_from(rimnodes)
    for i in range(rim):
        u=rimnodes[i]; v=rimnodes[(i+1)%rim]; prev=u
        for j in range(k):
            nd=f"e{i}_{j}"; G.add_node(nd); G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    for i in range(rim):
        prev=hub; v=rimnodes[i]
        for j in range(k):
            nd=f"s{i}_{j}"; G.add_node(nd); G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    return G

def cut_pairs(G):
    nodes=list(G.nodes()); out=[]
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            u,v=nodes[i],nodes[j]
            if G.has_edge(u,v): continue
            H=G.copy(); H.remove_nodes_from([u,v])
            if not nx.is_connected(H):
                out.append((u,v))
    return out

for rim in [5,6]:
    G=subdivided_wheel(rim,2)
    ess=set(v for v in G.nodes() if G.degree(v)>=3)
    print("="*70); print(f"rim={rim} ess({len(ess)}):",sorted(ess))
    cps=cut_pairs(G)
    # classify cut pairs: both essential? count components; check single-vertex components
    for (u,v) in cps:
        H=G.copy(); H.remove_nodes_from([u,v])
        comps=list(nx.connected_components(H))
        sing=sum(1 for c in comps if len(c)==1)
        print(f"  cutpair ({u},{v}) both_ess={u in ess and v in ess} ncomp={len(comps)} singletons={sing} sizes={sorted(map(len,comps))}")
