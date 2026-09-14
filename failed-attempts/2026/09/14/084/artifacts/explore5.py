import networkx as nx, itertools

def basics(G):
    tri=any(set(G.neighbors(u))&set(G.neighbors(v)) for u,v in G.edges())
    c4=False
    for u in G.nodes():
        for w in G.nodes():
            if str(u)>=str(w) or G.has_edge(u,w): continue
            if len(set(G.neighbors(u))&set(G.neighbors(w)))>=2: c4=True; break
        if c4: break
    return tri,c4

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

# Wheels contain triangles when k=0; with k>=1 subdivision they are triangle-free. C4? rim=5,k=1 was C4-free. Good.
# Both wheels satisfy standing assumptions (planar, triangle-free, C4-free, connected, no cut-vertex/edge, not cycle, have cut pairs).
# Their JSJ trees: essential set B = all essentials satisfies (B1). Maximal? likely the star set. So each has ONE orbit of V3 stars? Plus V2 orbits = branches? Need to compare JSJ trees of wheel5 vs wheel6.
# By Theorem 3.37: V2 orbits <-> sets A satisfying (A1)-(A3) with <A> not 2-ended. V3 orbits <-> sets B satisfying (B1)-(B3).
# For subdivided complete graphs K_{n+1}, proof of B.1 says: V2 orbits = branches (one orbit), V3 = single orbit {x0..xn}, no approx pairs. JSJ tree = same tripartite shape for all n>=3.
# For wheels: V2 orbits: branches between essential vertices? Each branch (hub-ri spoke, rim-arc) is a set A of its 2 endpoints? Those have <A> 2-ended => V1 not V2. Hmm: branches give ~-pairs (V1), not V2. What gives V2 (hanging)? A set A with <A> infinite non-2-ended: e.g. a cycle? Wheels contain many induced cycles >=5: e.g. rim cycle (all rim vertices) => <A> = RACG on cycle = cocompact Fuchsian? That would be hanging? Actually hanging vertex stabilizers are maximal hanging Fuchsian. A cycle C_n (n>=5) defines a Fuchsian group. Does the rim cycle satisfy (A1)-(A3)? Possibly.
# Let's instead directly compare using known result: Cashen-Martin structure invariant / Behrstock-Neumann: QI type of rigid vertex pair (R_{n+1}, lines) distinguished by n via Whitehead graph cut-set size = n (Appendix B). For wheels, rigid groups are R_6 (wheel5: 6 essentials) vs R_7 (wheel6: 7 essentials)? If both JSJ trees are the "same shape" (one V3 orbit, branches one V2/V1 orbit...), then wheel5 vs wheel6 would be a planar counterexample EXACTLY parallel to Appendix B!
# But wait: are the JSJ trees of wheel5-subdivision and wheel6-subdivision type-preservingly isomorphic? Need: same number of V-orbits of each subtype? V2 orbits might differ (different cycle structures). Let's examine more carefully.
# In K_{n+1} subdivisions, V2 orbits: "for each i<j, branch between xi and xj" -- but those branches have <A> 2-ended (dihedral), so they'd be V1 (sim-pairs), yet proof says "one orbit in V2 corresponding to the branch between xi and xj". Hmm, that suggests branches with interior vertices?? Let's re-read: branches contain subdivided vertices; the set A for a branch = {xi, xj} plus interior? No...
# Actually for 3-convex subdivisions, cut pairs {xi,xj}? Removing xi,xj leaves the branch interior as one component plus rest. The pair {xi,xj} separates into exactly 2 components => valence 2 => sim-pair (V1), not V2. But proof says V2. So my mapping is off: maybe branches here mean something else (the stars of...). Let me recheck: proof says "there is one orbit in V2 corresponding to the branch between xi and xj". Perhaps because each branch interior vertex plus endpoints form set A with <A> = ... hmm.
# Alternative: read Prop 3.10 (A1)-(A3): A can have >2 vertices. E.g. A = {xi, xj} is not maximal; the maximal A containing a branch might be larger.
# To avoid guessing, let's implement Dani-Thomas (A1)-(A3) conditions? They're complex. Instead, use a cleaner disproof route that does NOT require computing full JSJ by hand: use divergence / thickness / hypergraph index? No -- those are global QI invariants; if global QI types differ but JSJ trees agree, that already disproves "JSJ tree complete" but target asks about RELATIVE rigidity of rigid pieces.
# Target question precisely: "If Bowditch JSJ trees are type-preservingly isomorphic, must W_Gamma and W_Lambda be QI when every rigid vertex stabilizer is regarded together with its incident peripheral subgroups (equivalently, after matching JSJ trees, are corresponding rigid vertex pairs relatively QI)?"
# This is asking: does type-preserving iso + relative QI of rigid pairs imply global QI? Or: are matched rigid pairs automatically relatively QI?
# Reading: "must W_Gamma and W_Lambda be quasi-isometric when every rigid vertex stabilizer is regarded together with its incident two-ended peripheral subgroups (equivalently, after matching the JSJ trees, are the corresponding rigid vertex pairs relatively quasi-isometric)?"
# Ambiguous: (a) "Assume additionally that matched rigid pairs are relatively QI; does global QI follow?" or (b) "Does type-preserving iso AUTOMATICALLY imply matched rigid pairs are relatively QI?"
# Interpretation (a) is the natural "relative rigidity" program (Behrstock-Neumann/Cashen-Martin): JSJ tree + relative QI of rigid vertices = complete invariant. The question asks whether this holds in this class. Answer likely YES by Cashen-Martin Theorem 3.9 + Papasoglu? Actually Cashen-Martin [14] Thm 3.9 says: for 1-ended hyperbolic groups not cocompact Fuchsian, if JSJ trees have no... hmm. Let me recall: Cashen-Martin "Quasi-isometries between groups with two-ended splittings" proves that a type-preserving iso of JSJ trees + relative QIs of rigid vertex groups (coarsely respecting peripherals) can be assembled into a global QI (their "tree of quasi-isometries" / "QI tree" theorem). That would make (a) TRUE as a direct application.
# Interpretation (b) asks whether rigid pairs are automatically relatively QI given only tree iso -- that's FALSE in general (Appendix B shows rigid groups R_{n+1} with different n have same tree but are not even absolutely QI... though non-planar).
# The parenthetical "(equivalently, after matching the JSJ trees, are the corresponding rigid vertex pairs relatively quasi-isometric)?" suggests interpretation (b): the claim is that tree iso forces relative QI of rigid pairs. That would be the "relative quasi-isometric rigidity for rigid JSJ pieces" title.
# So target = (b): tree iso => rigid pairs relatively QI. To DISPROVE, need planar Gamma, Lambda with type-preserving isomorphic JSJ trees but a matched rigid pair NOT relatively QI.
# Appendix B gives non-planar examples (subdiv K4 vs subdiv K5? no wait, B.1(1) says all W_{n+1} have isomorphic JSJ trees for all n>=3, and (3) says different n are not QI). But K5 subdivisions are non-planar, violating target's planarity. Also B.1(3) distinguishes ABSOLUTE QI, not relative QI of rigid pairs. But the non-QI proof goes through the rigid vertex groups + peripheral line patterns, so it likely also shows rigid pairs not relatively QI. Still non-planar.
# For a PLANAR disproof, need planar graphs with same JSJ tree but different rigid-pair relative QI type. Wheels W5 vs W6 (subdivided) are planar candidates! Both likely have a single rigid star B = all essentials (size 6 vs 7). Rigid groups R6 = (Z/2)^*6 (virtually F5) vs R7 = (Z/2)^*7 (virtually F6), with peripheral line patterns from incident edge groups. If their JSJ trees are type-preservingly isomorphic, then relative QI would imply... hmm, but F5 vs F6 ARE QI (all free groups QI to each other? F2 QI F_n for all n>=2? Yes, all finite-rank free groups with rank>=2 are QI). But RELATIVE QI (preserving line patterns) may fail, distinguished by Whitehead-graph cut-set invariant as in Appendix B (min cut-set size n vs m).
# So plan: Gamma = subdivided wheel W5 (hub+5 rim), Lambda = subdivided wheel W6 (hub+6 rim), both 3-convex-ish subdivisions (k large enough for C4-free + 3-convex). Show: (i) both satisfy all target hypotheses incl. planar; (ii) JSJ trees type-preservingly isomorphic (single V3 orbit, ...); (iii) rigid pairs NOT relatively QI (different min cut-set sizes via Cashen-Macura/Appendix B argument).
# Step (ii) is the hard part: need V2/V1 orbit structures to match. Wheels of different rim lengths might have different numbers of V2 orbits (e.g. different cycle types). Hmm. In K_{n+1} case all branches are symmetric (S_{n+1} symmetry) so one V2 orbit. Wheels have 2 branch types (spokes vs rim arcs) => possibly 2 V2 orbits, but SAME for W5 and W6 (both have spokes+rim arcs). Rim cycle: W5 rim is C5-based, W6 rim C6-based; hanging Fuchsian from rim cycle? Both have "rim" orbit. So plausibly the orbit STRUCTURES agree (same counts), with only the rigid star differing (6 vs 7 essentials). The trees could still be type-preservingly isomorphic as colored trees (valences infinite countable everywhere, orbit counts matching).
# This is credible but verifying (ii) rigorously in remaining time is heavy. Alternative cleaner: use "cycles of generalized thetas"? Or simpler: take Gamma = subdivided K4 (rigid R4) and Lambda = subdivided wheel W5 (rigid R6)? Their JSJ trees: K4-subdiv has 1 V3 orbit + 1 branch orbit; wheel has 1 V3 + 2 branch orbits => trees NOT isomorphic (different quotient graphs). Bad.
# W5 vs W6 seems the right pair. Let's verify standing assumptions + 3-convexity + compute JSJ orbit data as far as possible computationally, then check QI-distinguishing invariant.
# First check: subdivided wheels with k=2 (each edge subdivided into 3?) are they 3-convex? 3-convex = every path between essential vertices has >=3 edges. With k=2 interior per edge, minimal paths have 3 edges. Yes.
# C4-free? wheel rim=5,k=1 was C4-free per explore3. rim=6,k=1 C4-free. Good. But 3-convex needs k>=2? k=1 gives paths of length 2 between essentials (hub-spoke-rim: hub to rim via 1 interior = 2 edges). Hmm 3-convex requires >=3 edges, so need k>=2. But k=2 wheels: C4? explore3 says wheel rim5 k2 C4-free? It printed C4: False. Good.
# So use k=2 subdivided wheels W5, W6. Both planar, triangle-free, C4-free, no cut-vertex/edge, not cycles, have cut pairs. 
# Next: determine JSJ trees. This requires implementing (A)/(B) conditions or finding a smarter argument.
# Actually, maybe there's an even cleaner pair: "theta-graphs glued to wheels"? Hmm.
# Let me first verify hypotheses + symmetry + cut-pair structure for W5k2 vs W6k2, then think about JSJ.

for rim,k in [(5,2),(6,2)]:
    G=subdivided_wheel(rim,k)
    tri,c4=basics(G)
    print(f"wheel rim={rim} k={k}: n={G.number_of_nodes()} planar={nx.check_planarity(G)[0]} tri={tri} C4={c4} conn={nx.is_connected(G)} cutv={list(nx.articulation_points(G))} bridges={list(nx.bridges(G))} alldeg2={all(d==2 for _,d in G.degree())}")
    nodes=list(G.nodes()); cps=[]
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            u,v=nodes[i],nodes[j]
            if G.has_edge(u,v): continue
            H=G.copy(); H.remove_nodes_from([u,v])
            if not nx.is_connected(H):
                cps.append((u,v,nx.number_connected_components(H)))
    print("  num cut pairs:",len(cps))
    from collections import Counter
    print("  comp-count histogram:",Counter(c[2] for c in cps))
