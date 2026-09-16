"""Sage-free Gordon-Litherland signature for spherogram Links.
Replicates spherogram white_graph + goeritz_matrix + signature(new_convention=True).
Conventions: positive knots have negative signature (SnapPy>=3 new convention).
"""
import numpy as np
import networkx as nx
from spherogram.links.links import CrossingStrand
from spherogram.links.ordered_set import OrderedSet

def faces_of(link):
    corners = OrderedSet([CrossingStrand(c, i) for c in link.crossings for i in range(4)])
    faces = []
    while len(corners):
        cs0 = corners.pop()
        face = [cs0]
        nxt = cs0
        while True:
            c, e = nxt.crossing, nxt.strand_index
            nxt = CrossingStrand(*c.adjacent[(e + 1) % 4])
            if nxt == cs0:
                faces.append(face)
                break
            else:
                corners.remove(nxt)
                face.append(nxt)
    return faces

def white_graph_edges(link, faces):
    face_of = {corner: n for n, face in enumerate(faces) for corner in face}
    edges = []  # (u,v,sign,crossing)
    for c in link.crossings:
        edges.append((face_of[CrossingStrand(c,0)], face_of[CrossingStrand(c,2)], 1, c))
        edges.append((face_of[CrossingStrand(c,1)], face_of[CrossingStrand(c,3)], -1, c))
    return edges

def goeritz_and_correction(link):
    faces = faces_of(link)
    edges = white_graph_edges(link, faces)
    G = nx.MultiGraph()
    G.add_nodes_from(range(len(faces)))
    for (u,v,s,c) in edges:
        G.add_edge(u, v, sign=s, crossing=c)
    comps = list(nx.connected_components(G))
    if len(comps) > 2:
        raise ValueError('split diagram')
    # spherogram takes components[1] after sort=True; emulate: sort by sorted node list
    comps_sorted = sorted([sorted(c) for c in comps])
    white_nodes = set(comps_sorted[1])
    # Goeritz matrix on white nodes
    V = sorted(white_nodes)
    idx = {v:n for n,v in enumerate(V)}
    N = len(V)
    m = np.zeros((N,N), dtype=int)
    for (u,v,s,c) in edges:
        if u in white_nodes and v in white_nodes:
            m[idx[u],idx[v]] += s
            if u != v:
                m[idx[v],idx[u]] += s
    for i in range(N):
        m[i,i] = -int(np.sum(m[:,i])) + m[i,i]  # careful: diagonal currently has loop contributions doubled? replicate: m[i,i] = -sum(col i)
    # replicate exactly: diagonal = -sum of column (including current diag?) Let's redo cleanly:
    m2 = np.zeros((N,N), dtype=int)
    for (u,v,s,c) in edges:
        if u in white_nodes and v in white_nodes:
            i,j = idx[u], idx[v]
            m2[i,j] += s
            m2[j,i] += s
    # note loops counted twice above; spherogram code: m[(i,j)]+=s for each edge incl loops (adds once to [i,i] for loop), then diag = -sum(column)
    # Our m2 double-counts loops; fix:
    m2 = np.zeros((N,N), dtype=int)
    for (u,v,s,c) in edges:
        if u in white_nodes and v in white_nodes:
            i,j = idx[u], idx[v]
            if i==j:
                m2[i,j] += s
            else:
                m2[i,j] += s
                m2[j,i] += s
    for i in range(N):
        m2[i,i] = -int(np.sum(m2[:,i])) + m2[i,i]
    # Actually spherogram: m[(i,i)] starts with loop sums, then m[(i,i)] = -sum(column). So final diag = -sum(off-diag col). Same as ours.
    Gsub = G.subgraph(white_nodes).copy()
    # correction mu = sum over edges in white graph where edge sign == crossing sign
    mu = 0
    for (u,v,s,c) in edges:
        if u in white_nodes and v in white_nodes:
            if s == c.sign:
                mu += s
    # delete first row/col
    if N >= 1:
        M = m2[1:,1:]
    else:
        M = np.zeros((0,0))
    return M, mu, white_nodes, faces

def signature(link, new_convention=True):
    M, mu, *_ = goeritz_and_correction(link)
    if M.shape[0]==0:
        sig_old = mu
    else:
        w, _ = np.linalg.eigh(M.astype(float))
        # exact integer signature via LDL? use rounding of eigenvalues (symmetric integer matrix, no zero issues generally; but zeros possible)
        tol=1e-8
        npos = int(np.sum(w>tol)); nneg = int(np.sum(w<-tol))
        sig_old = (npos-nneg) + mu
    return -sig_old if new_convention else sig_old

if __name__ == '__main__':
    from spherogram.links.torus import torus_knot
    # calibrate on known knots: right trefoil T(2,3) should be -2 (new convention); figure-8 should be 0
    for name, expect in [('T(2,3)',-2),('T(2,-3)',2),('T(3,4)',-6)]:
        K = torus_knot(name)
        print(name, "sig=", signature(K), "expect", expect)
