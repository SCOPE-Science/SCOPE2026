"""Two shuffles: extract mixed facedict on Aztec_{n-1} after shuffle 1, then shuffle it (general faces)."""
from general_shuffle import build_general, uniform_face, shuffle_general, reduce_g, raw, WGraph
from validate_ops import brute_Z
import math

def extract_facedict(G, m):
    """Recover Aztec_m face 4-tuples from reduced graph by matching vertex geometry.
    Reduced vertices are P(i,j,k). Map to Aztec_m CJ coords: need embedding.
    INSTEAD: rebuild the mixed Aztec_{n-1} graph directly: its vertices are the P's;
    its faces: new face at each old vertex v = cycle of P's around v. Enumerate new faces
    by old vertices and read edge weights. Then translate to standard CJ labeling by
    matching adjacency structure... simpler: just shuffle the REDUCED graph in place!
    The reduced graph IS an Aztec_{n-1} (same combinatorics); spider its faces.
    Find its faces as chordless 4-cycles? For Aztec_2 (12v,16e): faces = ? Use planarity-independent approach:
    faces of Aztec_m in CJ coords: (i,j) has corners B(2i,2j+1),W(2i+1,2j),B(2i+2,2j+1),W(2i+1,2j+2).
    Our reduced graph has arbitrary labels. Find graph isomorphism to standard Aztec_{n-1} by canonical labeling (brute force small n)."""
    return None

def faces_of_graph(G):
    """Find all chordless 4-cycles (u0,u1,u2,u3) alternating colors. Return as corner lists."""
    verts=list(G.V)
    adj={v:set() for v in verts}
    for (a,b) in G.E: adj[a].add(b); adj[b].add(a)
    cycs=set()
    for u0 in verts:
        for u1 in adj[u0]:
            for u2 in adj[u1]:
                if u2==u0: continue
                for u3 in adj[u2]:
                    if u3 in (u0,u1,u2): continue
                    if u0 in adj[u3]:
                        # chordless?
                        if u2 in adj[u0] or u3 in adj[u1]: continue
                        cycs.add(tuple(sorted([u0,u1,u2,u3])))
    return cycs

n=3; x,y=0.7,1.3
G=build_general(n,uniform_face(n,x,y))
G,Dp=shuffle_general(G,n,uniform_face(n,x,y))
G,f=reduce_g(G)
R=raw(G)
cycs=faces_of_graph(R)
print(f"reduced Aztec_2: V={len(R.V)} E={len(R.E)} chordless-4cycles={len(cycs)} (Aztec_2 has 4 faces + outer? )")
for c in sorted(cycs):
    ws=[]
    for k in range(4):
        ws.append(R.E[tuple(sorted((c[k],c[(k+1)%4])))])
    print(f"  {[str(v)[:12] for v in c]} weights={[round(w,6) for w in ws]}")
