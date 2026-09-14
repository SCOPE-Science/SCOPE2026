import networkx as nx, itertools
# Deeper JSJ analysis for subdivided wheels.
# Dani-Thomas Prop 3.10 sets A (sim-classes): conditions (A1),(A2),(A3) roughly:
# (A1): A lies on an induced cycle alpha, and every path between points of A stays... (need exact text)
# Instead of reimplementing blindly, extract exact statements from the paper text around Prop 3.10 / 3.25.
# Here: compute candidate A sets: branches (pairs of essentials joined by a subdivided edge-path with interior degree-2 vertices),
# cycles (rim cycle vertex sets, small cycles around hub), and test separation behavior.
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

for rim in [5,6]:
    G=subdivided_wheel(rim,2)
    # induced cycles: rim cycle length?
    rimnodes=[f"r{i}" for i in range(rim)]
    # rim cycle includes subdivision vertices: length = rim*(k+1) = rim*3
    print(f"rim={rim} rim-cycle length={rim*3}")
    # cycle hub-r_i-spoke + rim arc + spoke back: length 2*(k+1)+(k+1)=3*3=9
    print(f"  spoke-rim-spoke triangle-like cycle length={3*3}")
    # list a few induced cycles via cycle_basis and check lengths
    basis=nx.cycle_basis(G)
    from collections import Counter
    print("  cycle_basis lengths:",Counter(len(c) for c in basis), "num:",len(basis))
    # essential-vertex content of basis cycles
    ess=set(v for v in G.nodes() if G.degree(v)>=3)
    for c in basis[:12]:
        print("   len",len(c),"ess:",sorted(set(c)&ess))
