import networkx as nx, itertools
# The A1 tests above used graph-node deletion, but |G| separation for degree-2 interior points needs arc-topology.
# E.g. spoke path P=[h,s0_0,s0_1,r0]: removing two interior vertices s0_0,s0_1 as GRAPH nodes disconnects? H.copy-remove leaves h,r0 connected via rest of wheel => connected => A1 False under graph-deletion. But |G|-sense: points in the INTERIOR of edges... hmm s0_0 IS a vertex; |G|-{s0_0,s0_1}: the spoke arc is cut, but h,r0 reconnect through the rest => still connected?! So indeed spoke interiors don't pairwise separate. Good -- so branches are NOT the A sets here (unlike theta graphs). The structure differs because wheels are 2-connected through the rest.
# So what ARE the maximal (A1)+(A2) sets? Candidates: cut pairs {a,b} with k>=3 components gave approx-pairs (V1). Here essential cut pairs give only 2 components => not approx. sim-pairs (V1c): A={a,b} 2-ended with (A1)-(A3)? {h,r0}: separates into 2 comps; valence 2. Is {h,r0} maximal w.r.t. (A1)? Adding any third vertex breaks (A1) (tests above show {h,r0,r1} HAS A1 True though!). Hmm {h,r0,r1} satisfies A1. So {h,r0} not maximal; need (A2),(A3) analysis.
# {h,r0,r1} satisfies A1 (both rims). Does it satisfy A2? Need: every subdiv K4 containing >=3 of {h,r0,r1} has all of A on one branch. K4 on branch-vertices {h,r0,r1,r3}: contains h,r0,r1 as three branch vertices => NOT on one branch => (A2) FAILS. So {h,r0,r1} fails A2. What about {h,r0}? Any subdiv K4 containing >=3 vertices of a 2-set: impossible => (A2) VACUOUSLY true. So {h,r0} satisfies A1+A2. Maximal (A3)? Adding any vertex v: {h,r0,v} must fail A1 or A2. v=r1: A1 holds, A2 fails (shown) => so adding r1 breaks A2, fine, consistent with maximality IF every other v breaks A1 or A2. v = spoke interior s0_0: {h,r0,s0_0}? A1? s0_0 with h: adjacent => |G| separation? Points h and s0_0 adjacent on spoke: removing them from |G|... the spoke arc between them is open edge; rest of graph connects h-side to r0-side? Likely still connected => fails A1. So maximality plausible.
# Thus: each essential cut pair {h,ri} and {ri,rj(adjacent)} yields a ~-pair (V1, valence 2)! These are the "Type 1c" vertices.
# Are there infinite ~-classes (V2/hanging)? Need A with <A> not 2-ended satisfying A1+A2+A3. Candidates: larger sets on induced cycles. Tests show {h,r0,r1,r2}, rim sets fail A1. Hmm. What about sets including degree-2 vertices on cycles? E.g. full induced cycle vertex set C (length 9 spoke-rim-spoke cycle: h,s_i0,s_i1,r_i,e_k,r_j,s_j1,s_j0?...). Pairwise separation along a cycle: two vertices of a cycle separate |cycle| but do they separate |G|? Removing two cycle vertices may leave G connected via outside paths => A1 fails unless the cycle is "separating". In wheels, small cycles are not separating (rest connects around). So likely NO infinite ~-classes at all! I.e., no V2 vertices.
# Then JSJ tree: V1 = ~-pairs (essential cut pairs, valence 2) + valence-2 subdivisions; V3 = one star orbit (B = all essentials); NO V2, NO approx-pairs (no cut pair with >=3 comps... essential cut pairs have 2 comps; non-essential cut pairs involve degree-2 vertices, not essential pairs; approx-pairs need essential? Cor 3.5: {a,b} cut pair with k>=3 or 2(k-1)>=... here max comps=2 => no approx pairs).
# So T_Gamma: bipartite-ish: V3 star vertices connected via V1 valence-2 vertices... wait V1 valence-2 sim-pairs connect to V3 stars; plus added V1d midpoints? With no V2, edges: sim-pair (V1) connects to V3 star. Degree of V3 = infinite; degree of V1 = 2. Quotient: one V3 orbit + orbits of V1 (spoke-type {h,ri} and rim-type {ri,rj}).
# For rim=5: V1 orbits: {h,ri} (all symmetric under D5? hub fixed, rim transitive => one orbit) and {ri,rj} adjacent rim pairs (one orbit). For rim=6: same: 2 V1 orbits. Same orbit counts!
# The quotient graph of groups: star vertex with peripheral edge groups <h,ri> (dihedral) and <ri,rj> (dihedral). The underlying UNCOLORED tree: V3 infinite-degree nodes joined through V1 degree-2 nodes: this is a "subdivided" regular-ish tree. As colored trees (V1 vs V3 + stabilizer valence data), rim5 vs rim6 quotients have same shape (1 V3 orbit, 2 V1 orbits). Stabilizer of V3: <B> = virtually free on 6 vs 7 generators. Edge patterns: in rim5, each star has how many incident {h,ri}-type vs {ri,rj}-type edges? The star B contains cut pairs {h,ri} (5 of them) and {ri,rj} adjacent (5). In rim6: 6 and 6. Local incidence counts differ (5+5 vs 6+6) but in the TREE each V3 vertex has INFINITE degree (countably many of each type, by W-translates), so the trees are still isomorphic as colored trees! (This mirrors App B: T_{n+1} all isomorphic despite different n.)
# Let's verify counts: cut pairs within B (both endpoints in B): rim5: (h,ri)x5 + adjacent rim pairs x5 = 10. rim6: 6+6=12. Also nonadjacent rim pairs? {r0,r2} rim5: A1 False => not a cut pair (confirmed: cut pair list shows only adjacent rim pairs + spokes). Good.
# Also need: B maximal (B2) and |B|>=4 (B3): yes. Is B the UNIQUE V3 orbit? Could there be other B' satisfying (B1)-(B3)? E.g. subsets? (B2) maximality + Lemma 3.30 constraints. For wheels, plausibly unique. Also need no other stars. We'll argue via symmetry + (B1) checks.
# Next: relative QI of rigid pairs: R6 vs R7 with peripheral line patterns. Adapting App B/Cashen-Macura: min cut-set sizes differ (5? vs 6?). In App B, rigid group R_{n+1} = (Z/2)^{*(n+1)}, peripherals D_{ij} for all i<j; min cut-set size = n. For wheels, peripherals are only the 10 (resp 12) cut pairs within B, not all pairs. The Whitehead-graph invariant needs recomputation: F5 with line pattern from 10 cyclic subgroups vs F6 with 12. The minimal cut-set sizes: need to compute. If they differ => rigid pairs not relatively QI => TARGET DISPROVED (reading (b)).
# Let's compute Whitehead graphs for both patterns and their min cut-set sizes.

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
    ess=sorted(v for v in G.nodes() if G.degree(v)>=3)
    print("rim",rim,"ess",ess)
    # cut pairs within ess
    cps=[]
    for i in range(len(ess)):
        for j in range(i+1,len(ess)):
            u,v=ess[i],ess[j]
            if G.has_edge(u,v): continue
            H=G.copy(); H.remove_nodes_from([u,v])
            if not nx.is_connected(H): cps.append((u,v))
    print(" cut pairs in B:",cps, "count",len(cps))
