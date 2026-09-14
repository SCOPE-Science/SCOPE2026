import networkx as nx, itertools

def has_triangle(G):
    for u,v in G.edges():
        if set(G.neighbors(u)) & set(G.neighbors(v)): return True
    return False
def induced_C4(G):
    for u in G.nodes():
        for w in G.nodes():
            if u>=w or G.has_edge(u,w): continue
            if len(set(G.neighbors(u))&set(G.neighbors(w)))>=2: return True
    return False
def cut_pairs(G):
    out=[]; nodes=list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            u,v=nodes[i],nodes[j]
            if G.has_edge(u,v): continue
            H=G.copy(); H.remove_nodes_from([u,v])
            if not nx.is_connected(H): out.append((u,v))
    return out

def suspension_of_graph(H, apexes=('a','b')):
    # suspension: join H with 2 nonadjacent vertices
    G=nx.Graph(); a,b=apexes
    G.add_nodes_from([a,b]); G.add_nodes_from(H.nodes())
    G.add_edges_from(H.edges())
    for v in H.nodes():
        G.add_edge(a,v); G.add_edge(b,v)
    return G

# need triangle-free suspension => H edgeless (else a-x-y triangle? a-x,a-y,x-y triangle). So rigid suspension piece must be over independent set => cactus-like.
# Try: rigid piece = suspension of 3 isolated vertices {x,y,z} => K_{2,3}, has induced C4! not allowed.
# suspension of 2 isolated => C4. not allowed.
# So for hyperbolic no-C4, rigid vertex stabilizers (gen. Fuchsian on suspensions) can't be suspensions?? Actually rigid = maximal non-cylinder hanging piece.
# Let's instead look at Dani-Thomas class "Standing Assumptions": no triangles, no separating vertex/edge, not a cycle, has cut pair. JSJ pieces from cut pairs.
# Known: generalized theta graphs give NO rigid vertices (only cylinder+hanging). To get rigid vertices we need more complex graphs e.g. two theta graphs glued along a branch?
# Construct: take theta(a,b;3 branches len3) and subdivide/attach a "rigid" block R between a and one branch so cut-pair structure stays a star but rigid piece graph differs.

def theta(a,b,npaths,plen):
    G=nx.Graph(); G.add_nodes_from([a,b])
    for k in range(npaths):
        seq=[a]+[f"p{k}_{i}" for i in range(1,plen)]+[b]
        for x in seq[1:-1]:
            G.add_node(x)
        for x,y in zip(seq,seq[1:]): G.add_edge(x,y)
    return G

# Candidate rigid-containing graph: "laddered theta": take branch p0 and replace middle edge with a diamond-free rigid gadget?
# Simplest: glue two thetas sharing the pair {a,b}: theta with branches of lengths (3,3,3) vs (3,3,4)?
# Both have single essential cut pair {a,b}; JSJ tree: star with one cylinder vertex (a,b) + 3 (or 3) hanging vertices? Actually each branch gives a hanging piece; no rigid vertices.
# For rigid vertices: need a subgraph separated by a cut pair that is not a star of cycles. E.g. take base = square with diagonals? Must stay triangle-free & C4-free & planar.
# Example: take the 3-branch theta above (call T(a,b) with branch lens 3,3,3). Now on branch 0, insert a "cross-bar": add vertex q connected to p0_1 and p1_1? That creates C4? p0_1-a-p1_1-q-p0_1 = C4. Bad.
# Alternative known source of rigid vertices in RACGs: "cycles of generalized thetas" (Dani-Stark-Thomas). A cycle of thetas: arrange k theta blocks in a ring glued at cut pairs. The ring structure yields rigid vertices? Actually those papers study commensurability;JSJ: each theta contributes cylinder vertices.
# Let's brute-force search small planar triangle/C4-free graphs with a cut pair and check JSJ piece types via Dani-Thomas visual construction approximatively: compute maximal "pieces" = ?
# Simpler discriminant: hangings vs rigid determined by whether piece graph is a "generalized theta with all branches subdivided" vs contains a "rigid" subgraph (2-connected, not a cycle, no cut pair inside?).
# Let's enumerate candidate graphs: two thetas glued along a branch edge, with branch lengths varied, and test planarity/triangle/C4 and cut-pair sets.

def glue_thetas():
    # Graph A: theta(a,b; branches lens [3,3,3]); Graph B: theta(a,b; [3,3,4])
    # both share only a,b? That union has branches [3,3,3,3,3,4]-like? cut pair (a,b) with 6 components. JSJ star, no rigid.
    pass

# Try "H" graph: vertices a,b with three internally disjoint paths, but subdivide one path's interior vertex into a theta gadget:
# Branch0: a - x1 - x2 - b. Replace x1 by a pair (x1a,x1b) forming small theta(a?..) hmm.
# Concrete: vertices: a,b; path1: a-u1-u2-b; path2: a-v1-v2-b; path3: a-w1-m-w2-b where m is replaced by theta(w1,w2; 2 branches w1-z1-w2, w1-z2-w2)? Then {w1,w2} is another cut pair nested inside branch3.
# Check triangle/C4-freeness and planarity.
G=nx.Graph()
G.add_edges_from([('a','u1'),('u1','u2'),('u2','b'),('a','v1'),('v1','v2'),('v2','b'),('a','w1'),('w1','z1'),('z1','w2'),('w1','z2'),('z2','w2'),('w2','b')])
print("planar",nx.check_planarity(G)[0],"tri",has_triangle(G),"C4",induced_C4(G))
print("cutverts",set(nx.articulation_points(G)),"bridges",list(nx.bridges(G)))
print("cutpairs:",cut_pairs(G))
print("degrees:",dict(G.degree()))
