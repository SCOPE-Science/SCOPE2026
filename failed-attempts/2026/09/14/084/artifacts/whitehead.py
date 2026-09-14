import itertools
# Rigid vertex group R = <B | x^2=1> = (Z/2)^*|B|, index-2 free subgroup F(B) with basis y_i = x0*x_i.
# Peripheral line pattern: for each cut pair {bi,bj} in B, dihedral D_{ij}=<bi,bj> gives cyclic <bi bj> in F.
# Express each w_{ij} = bi*bj as word in y-basis, build Whitehead graph, compute min cut-set size.
# Basis: fix x0 = h. y_i = h*r_i for each rim vertex r_i. F5 (rim5) rank 5; F6 (rim6) rank 6.
# Words:
#  spoke pairs (h, r_i): h*r_i = y_i.
#  rim pairs (r_i, r_j): r_i*r_j = (r_i*h)*(h*r_j) = y_i^{-1} y_j.
# So line pattern L5 = {y_i} (5) + {y_i^{-1} y_j for adjacent rim pairs} (5 adjacencies: cycle C5).
# L6 = {y_i} (6) + {y_i^{-1} y_j for C6 adjacencies} (6).
# Whitehead graph: vertices {y_i^{+-1}}; for each word, edges between consecutive letters (cyclically, including inverse).
# For y_i (length 1): edge between y_i and y_i^{-1} (loop-like single edge).
# For y_i^{-1} y_j: cyclic pairs: (y_i^{-1}, y_j) and (y_j^{-1}... wait cyclic: word w = a b with a=y_i^{-1}, b=y_j; cyclic adjacent pairs: (a,b) and (b^{-1},a^{-1}) = (y_j^{-1}, y_i). Standard Whitehead: vertices 2n, edge for each adjacent pair in cyclic word.
# Min cut-set: min number of VERTICES whose removal disconnects? or EDGES? In Cashen-Macura/App B, "cut sets of size n" refer to edge cut-sets? App B text: "the cut sets of size n are of two types: the n edges incident to some vertex or the n edges connecting positive to inverses" -- EDGES. And "smallest cut sets in the decomposition space have size exactly n" = minimal number of points removed to disconnect decomposition space. The Whitehead graph edge-cut corresponds to decomposition-space cut sets.
# So compute edge-connectivity of Whitehead graphs? For App B K_{n+1} case: words {y_i} + {y_j^{-1} y_k for ALL j<k}: Whitehead has edge y_i--y_i^{-1} each i, plus y_j--y_k and y_j^{-1}--y_k^{-1} for all j!=k. Min edge-cut = n. Let's verify our computation reproduces n=3 for K4 (n+1=4 essentials => n=3): words y1,y2,y3 + y1^{-1}y2,y1^{-1}y3,y2^{-1}y3 (all pairs). Then check edge-connectivity == 3. If yes, method validated; then compute for wheel patterns.

import networkx as nx

def whitehead(n, adj):
    # n = rank (rim count), adj = list of (i,j) pairs (indices into 0..n-1) for rim-rim words y_i^{-1} y_j
    G=nx.MultiGraph()
    verts=[f"y{i}+" for i in range(n)]+[f"y{i}-" for i in range(n)]
    G.add_nodes_from(verts)
    for i in range(n):
        G.add_edge(f"y{i}+",f"y{i}-")  # word y_i
    for (i,j) in adj:
        # word y_i^{-1} y_j: cyclic adjacencies (y_i-, y_j+) and (y_j-, y_i+)
        G.add_edge(f"y{i}-",f"y{j}+")
        G.add_edge(f"y{j}-",f"y{i}+")
    return G

def min_edge_cut_size(G):
    # brute force: try k=1,2,...: check all subsets of edges of size k for disconnection. Graph small enough? K4-case: 6 nodes, edges: 3 + 6 = 9 (multiedges possible? y_i-y_i- single; pair edges distinct). brute force over subsets feasible for small k.
    import itertools
    edges=list(G.edges(keys=True))
    # simple connectivity ignoring multiplicities first via edge_connectivity on simple? MultiGraph edge connectivity: use nx.edge_connectivity (works on multigraph? convert: multiplicity matters). We'll brute force with MultiGraph copies.
    nodes=list(G.nodes())
    # quick upper bound via nx.edge_connectivity of simple version? just brute force k ascending
    for k in range(1,len(edges)+1):
        for combo in itertools.combinations(range(len(edges)),k):
            H=G.copy()
            # remove by key
            for idx in sorted(combo,reverse=True):
                u,v,kk=edges[idx]
                H.remove_edge(u,v,kk)
            if not nx.is_connected(H):
                return k
    return None

# Validation: K4 pattern (n=3, all pairs)
K4adj=[(0,1),(0,2),(1,2)]
G= whitehead(3,K4adj)
print("K4-pattern nodes",G.number_of_nodes(),"edges",G.number_of_edges())
print(" min edge cut:",min_edge_cut_size(G), "(expect 3 per App B)")
# K5 pattern (n=4, all pairs) expect 4
K5adj=list(itertools.combinations(range(4),2))
G5=whitehead(4,K5adj)
print("K5-pattern edges",G5.number_of_edges())
print(" min edge cut:",min_edge_cut_size(G5), "(expect 4)")
