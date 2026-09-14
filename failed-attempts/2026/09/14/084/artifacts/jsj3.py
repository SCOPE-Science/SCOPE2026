import networkx as nx, itertools
# Implement exact Dani-Thomas checks:
# geometric realization separation: a,b pairwise separate |G| iff a,b nonadjacent and lie on a common induced cycle? For 2-conn triangle-free graphs, use: a,b separate |G| iff G-{a,b} disconnected OR (a,b adjacent and ...). Since all our essential pairs are nonadjacent, G-{a,b} disc. suffices. For pairs involving degree-2 vertices, need |G| notion: vertices separate arcs. We'll focus on essential vertices + branch analysis.
# (A1): elements of A pairwise separate |G|.
# Key candidate A sets in wheels: for each branch (maximal path between essentials with no interior essential), the triple {endpoint1, endpoint2, interior vertex}? Or whole "side" sets?
# Actually Lemma 3.13: A satisfying (A1) lies on an induced cycle in cyclic order. So candidate A's are subsets of induced cycles where each pair separates.
# Let's enumerate induced cycles (chordless) up to some length and test which vertex sets satisfy (A1),(A2).
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

def separates_geom(G,a,b):
    # |G|-separation for vertices a,b: check G-{a,b} disconnected (covers nonadjacent case); if adjacent, removing open edge... our pairs are nonadjacent mostly.
    if G.has_edge(a,b):
        H=G.copy(); H.remove_edge(a,b)
        # check if a,b separated in remaining? approximate: remove a,b interior? For adjacent we need finer topology; skip (return None)
        return None
    H=G.copy(); H.remove_nodes_from([a,b])
    return not nx.is_connected(H)

def A1(G,A):
    for a,b in itertools.combinations(A,2):
        s=separates_geom(G,a,b)
        if s is None or not s: return False
    return True

def has_subdivK4_containing(G, verts):
    # brute-force subdivided-K4 detection: choose 4 branch vertices among essentials, 6 disjoint paths? expensive. Instead use known: wheel contains subdiv K4 with branch vertices {h, r_i, r_j, r_k} (hub + 3 rim). Check: paths h-r (spokes), r-r (rim arcs), h? need 6 branches: h-ri spokes (3), rim arcs ri-rj, rj-rk, rk-ri (3). Yes! That's a subdivided K4 (possibly with equalities when rim vertices adjacent? branches of length >=... fine).
    return True

for rim in [5,6]:
    G=subdivided_wheel(rim,2)
    ess=[v for v in G.nodes() if G.degree(v)>=3]
    print("="*70); print("rim=",rim)
    # Test candidate A = {h, r0, r1} (hub + 2 adjacent rim): pairwise separate?
    for A in [['h','r0','r1'], ['h','r0','r2'], ['r0','r1','r2'], ['h','r0','r1','r2']]:
        print(" A=",A,"A1=",A1(G,A))
    # Test A = all rim vertices
    rimnodes=[f"r{i}" for i in range(rim)]
    print(" A=rim A1=",A1(G,rimnodes))
    # Test A = all essentials
    print(" A=ess A1=",A1(G,ess))
    # (A2) check for A={h,r0,r1}: is there a subdiv K4 with >=3 of A NOT on one branch?
    # subdiv K4 on {h,r0,r1,r3} (rim=5): branches: spokes h-ri; rim arcs. A={h,r0,r1}: in this K4, h,r0,r1 are 3 of 4 branch vertices => not on single branch => violates (A2)!
    print(" => small sets containing hub+2rim violate (A2) when a 4th essential exists forming K4 with them.")
    # Candidate maximal A satisfying (A1)+(A2): branches! e.g. A = {h, s_i0, s_i1, r_i} (whole spoke subdivision path)? Check A1: do interior degree-2 vertices pairwise separate |G|? Removing two interior spoke vertices: spoke path cut but rest connected? |G| sense: two points on same edge-path DO separate the arc... In |G|, any two points on a branch separate each other? Hmm (A1) "pairwise separate |G|" includes adjacent/interior points.
    # The paper's Fig 3.1 example: theta graphs: A = branch vertex sets? For Theta(n1..nk), ~-classes correspond to branches (each branch = maximal path between a,b). E.g. left graph Theta(1,2,2,3): branches give sets A. So analogously in wheels, each subdivided edge (spoke or rim-arc) with its interior vertices forms a candidate A.
    # Let's test: spoke i path vertices P=[h, s_i0, s_i1, r_i]: pairwise separate |G|?
    P=['h','s0_0','s0_1','r0']
    print(" spoke path A1:",A1(G,P))
    # rim arc path Q=[r0, e0_0, e0_1, r1] (rim=5, arc 0 between r0,r1)
    Q=['r0','e0_0','e0_1','r1']
    print(" rim-arc path A1:",A1(G,Q))
