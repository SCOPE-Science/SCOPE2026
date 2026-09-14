# Verify the wheel pair satisfies ALL target hypotheses literally, and record JSJ-relevant visual data.
# Target hypotheses: finite, connected, triangle-free, planar, no separating vertex/edge, no induced C4,
# not a cycle, admits a cut pair; W one-ended hyperbolic non-cocompact-Fuchsian with nontrivial JSJ.
import networkx as nx, itertools, json

def check(G, name):
    rep = {}
    rep['finite']=True; rep['n']=G.number_of_nodes(); rep['m']=G.number_of_edges()
    rep['connected']=nx.is_connected(G)
    rep['triangle_free']=not any(set(G.neighbors(u))&set(G.neighbors(v)) for u,v in G.edges())
    rep['planar']=nx.check_planarity(G)[0]
    rep['no_separating_vertex']=len(list(nx.articulation_points(G)))==0
    rep['no_separating_edge']=len(list(nx.bridges(G)))==0
    # no induced C4: triangle-free + no pair with >=2 common neighbors
    c4=[(u,w) for u in G.nodes() for w in G.nodes() if str(u)<str(w) and not G.has_edge(u,w) and len(set(G.neighbors(u))&set(G.neighbors(w)))>=2]
    rep['no_induced_C4']=len(c4)==0
    rep['not_a_cycle']=not all(d==2 for _,d in G.degree())
    nodes=list(G.nodes()); cps=[]
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            u,v=nodes[i],nodes[j]
            if G.has_edge(u,v): continue
            H=G.copy(); H.remove_nodes_from([u,v])
            if not nx.is_connected(H): cps.append([str(u),str(v)])
    rep['has_cut_pair']=len(cps)>0; rep['num_cut_pairs']=len(cps)
    # W consequences (Davis/Moussong/Dani-Thomas): 1-ended (conn+no seps), hyperbolic (triangle-free+no C4... square-free), non-Fuchsian (not cycle), nontrivial JSJ (cut pair)
    return rep, cps

def wheel(rim,k):
    G=nx.Graph(); G.add_node('h')
    rn=[f"r{i}" for i in range(rim)]; G.add_nodes_from(rn)
    for i in range(rim):
        u=rn[i]; v=rn[(i+1)%rim]; prev=u
        for j in range(k):
            nd=f"e{i}_{j}"; G.add_node(nd); G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    for i in range(rim):
        prev='h'; v=rn[i]
        for j in range(k):
            nd=f"s{i}_{j}"; G.add_node(nd); G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    return G

out={}
for rim in [5,6]:
    G=wheel(rim,2)
    rep,cps=check(G,f"W{rim}")
    out[f"W{rim}"]=rep
    print(f"W{rim}:",json.dumps(rep))
    assert all([rep['connected'],rep['triangle_free'],rep['planar'],rep['no_separating_vertex'],rep['no_separating_edge'],rep['no_induced_C4'],rep['not_a_cycle'],rep['has_cut_pair']]), "hypothesis failed!"
print("ALL TARGET HYPOTHESES VERIFIED for both wheels")
json.dump(out,open('output/artifacts/hypothesis_check.json','w'),indent=1)
# subdivided K4 check (contains stars; also satisfies hypotheses) for context
def sk4(k):
    G=nx.Graph(); G.add_nodes_from([0,1,2,3])
    for (u,v) in itertools.combinations([0,1,2,3],2):
        prev=u
        for i in range(k):
            nd=(u,v,i); G.add_node(nd); G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    return G
G=sk4(2); rep,_=check(G,"K4"); print("subdivK4:",json.dumps(rep))
