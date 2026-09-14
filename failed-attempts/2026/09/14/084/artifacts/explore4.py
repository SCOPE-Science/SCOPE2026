import networkx as nx, itertools

def props(G, name, show=12):
    tri=any(set(G.neighbors(u))&set(G.neighbors(v)) for u,v in G.edges())
    c4=False
    for u in G.nodes():
        for w in G.nodes():
            if str(u)>=str(w) or G.has_edge(u,w): continue
            if len(set(G.neighbors(u))&set(G.neighbors(w)))>=2: c4=True; break
        if c4: break
    print("="*60); print(name,"n=",G.number_of_nodes(),"m=",G.number_of_edges(),
          "planar=",nx.check_planarity(G)[0],"tri=",tri,"C4=",c4,
          "cutv=",list(nx.articulation_points(G)) if nx.is_connected(G) else "disc",
          "bridges=",list(nx.bridges(G)) if nx.is_connected(G) else "disc",
          "alldeg2=",all(d==2 for _,d in G.degree()))
    nodes=list(G.nodes()); cps=[]
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            u,v=nodes[i],nodes[j]
            if G.has_edge(u,v): continue
            H=G.copy(); H.remove_nodes_from([u,v])
            if not nx.is_connected(H):
                cps.append((u,v,nx.number_connected_components(H)))
    print("num_cutpairs:",len(cps))
    for p in cps[:show]: print("  ",p)
    return cps

def subdivided_K4(k=2, labels=(0,1,2,3)):
    G=nx.Graph(); G.add_nodes_from(labels)
    for (u,v) in itertools.combinations(labels,2):
        prev=u
        for i in range(k):
            nd=(u,v,i); G.add_node(nd); G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    return G

# Family A: subdivided K4 with branch-length vector varying.
# All subdivided K4s have the same unlabelled JSJ tree shape? Theorem B.1 says all K_{n+1} subdivisions (n>=3) share the same JSJ tree as uncolored/type-preserved tree.
# Actually Theorem B.1(1): all W_{n+1} (fixed n) have isomorphic JSJ trees -- but does it vary with n? Yes: T_{n+1} vs T_{m+1} are isomorphic as trees for all m,n>=3! Read: "there is a type-preserving isomorphism from T_{n+1} to T_{m+1}, for all m,n>=3". Indeed proof says tripartite tree with countably infinite valences -- same for every n.
# So take Gamma = subdiv K4 on vertices {x0..x3} and Lambda = subdiv K5 on {y0..y4}. Both satisfy standing assumptions? Check Lambda= subdiv K5: planar? K5 not planar even subdivided (subdivision preserves planarity? K5 is nonplanar, any subdivision is nonplanar!). So K5 subdivisions are NOT planar. Target requires planar nerve. So Appendix B counterexample is non-planar and doesn't directly answer target.
# Need planar graphs with same JSJ tree but non-QI rigid pieces.
# Planar + subdivided K4-containing: e.g. subdivided wheel W5 (rim 5?) contains subdivided K4? Wheel W5 = K4? Actually W4=K4. Larger wheels contain K4 minors but subdivided K4 subgraphs? Possibly.
# Key Question: find planar graphs Gamma, Lambda with type-preserving isomorphic JSJ trees but different QI types (e.g. distinguished by rigid vertex stabilizers' relative QI type).
# Cashen-Martin: if JSJ has no stars (no subdiv K4), then JSJ tree is complete QI invariant. So a counterexample must use graphs WITH subdivided K4 (stars present) AND planar. Subdivided K4 is planar (K4 planar). So planar examples with stars exist: subdivided K4 itself (k large enough to be C4-free).
# So take Gamma = subdivided K4 with all branches length 3 (say k=3 interior? our k=2 gives branch length 3 edges) and Lambda = subdivided K4 with different branch lengths? But Theorem B.1(2) says any two subdivisions of K_{n+1} (same n) ARE quasi-isometric! So varying branch lengths within K4 doesn't give counterexample.
# Need two planar graphs with same JSJ tree shape but rigid vertex groups of different QI type. Rigid vertex group = <B> where B = essential vertices set satisfying (B1)-(B3). For subdiv K4, B = {4 essential vertices}, <B> = free product of 4 Z/2 = virtually free F3. Its peripheral structure = conjugates of D_ij = <xi,xj>.
# Different n gives different rigid groups: R4 = (Z/2)^*4 vs R5 = (Z/2)^*5? But K5 subdivisions aren't planar.
# Can we get planar graphs whose rigid vertices are R4 vs R5? R5 needs 5 essential vertices in one star => contains subdivided K5? Nonplanar. Hmm.
# Alternative: rigid vertices could be distinguished by the pattern of incident edge groups (valence data) or by internal QI invariants like the "line pattern" (Cashen-Macura) restricted to planar setting.
# For planar graphs, possible rigid blocks: subdivided K4 (4 essentials) or subdivided wheels? Wheel with hub + rim: essential set B = {hub, rim vertices}? Check (B1): any pair of essentials separated leaves rest in one component? For wheel, removing two rim vertices disconnects hub? Let's test computationally which subsets satisfy Dani-Thomas (B1)-(B3) for our candidates.
# Let's implement (B1): B set of essential vertices, |B|>=4? Actually Prop 3.25: (B1) for every pair c1,c2 of essential vertices of Gamma, B\{c1,c2} lies in a single component of Gamma\{c1,c2}. (B2): maximality w.r.t. inclusion among sets satisfying (B1)? and (B3): |B|>=4? Need exact statement; approximate: check (B1) for candidate B = all essential vertices.

def check_B1(G,B):
    ess=[v for v in G.nodes() if G.degree(v)>=3]
    for c1,c2 in itertools.combinations(ess,2):
        H=G.copy(); H.remove_nodes_from([c1,c2])
        rest=[b for b in B if b!=c1 and b!=c2]
        if not rest: continue
        comps=list(nx.connected_components(H))
        # find components containing rest
        idx=set()
        for b in rest:
            for i,c in enumerate(comps):
                if b in c: idx.add(i)
        if len(idx)>1: return False,(c1,c2)
    return True,None

for k in [2,3]:
    G=subdivided_K4(k,labels=(0,1,2,3))
    ess=[v for v in G.nodes() if G.degree(v)>=3]
    print("K4 ess:",ess,"B1(all ess):",check_B1(G,set(ess)))

def subdivided_wheel(rim=5,k=1):
    G=nx.Graph(); hub='h'; G.add_node(hub)
    rimnodes=[f"r{i}" for i in range(rim)]; G.add_nodes_from(rimnodes)
    for i in range(rim):
        u=rimnodes[i]; v=rimnodes[(i+1)%rim]; prev=u
        for j in range(k):
            nd=(f"rim{i}",j); G.add_node(nd); G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    for i in range(rim):
        prev=hub; v=rimnodes[i]
        for j in range(k):
            nd=(f"sp{i}",j); G.add_node(nd); G.add_edge(prev,nd); prev=nd
        G.add_edge(prev,v)
    return G

for rim,k in [(5,1),(5,2),(6,1)]:
    G=subdivided_wheel(rim,k)
    ess=[v for v in G.nodes() if G.degree(v)>=3]
    print(f"wheel rim={rim} k={k} ess count:",len(ess),ess[:8],"B1:",check_B1(G,set(ess)))
