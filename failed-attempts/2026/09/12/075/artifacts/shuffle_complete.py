"""Complete the shuffle: peel degree-1 (pendant+leg forced), contract degree-2, identify Aztec_{n-1}."""
import math
from validate_ops import WGraph, build_aztec_cj, brute_Z, spider

def reduce_graph(G):
    """Pendant removal + deg-2 contraction until clean. Returns (G, factor) with Z_orig = factor * Z(G)."""
    factor = 1.0
    changed = True
    while changed:
        changed = False
        # pendants
        pend = [v for v in list(G.V) if len(G.nbrs(v)) == 1]
        # process pendant pairs carefully: remove v, v' and ALL edges at v'
        handled = set()
        for v in pend:
            if v in handled or v not in G.V: continue
            nb = G.nbrs(v)
            if not nb: continue
            (vp, w) = nb[0]
            factor *= w
            handled.add(v); handled.add(vp)
            for (u, ww) in G.nbrs(vp):
                G.E.pop(tuple(sorted((vp, u))), None)
            for (u, ww) in G.nbrs(v):
                G.E.pop(tuple(sorted((v, u))), None)
            G.V.pop(v, None); G.V.pop(vp, None)
            changed = True
        if changed: continue
        # deg-2 contraction: v with nbrs (x,wx),(y,wy), wx=wy=1 required for exactness; else urban-style?
        # General deg-2 (series) reduction: Z-preserving only if weights 1? For general weights use "series rule":
        # replace path x-v-y by edge (x,y) with weight wx*wy, times... NOT Z-preserving in general dimer models!
        # (Series reduction changes Z unless one weight is normalized.) So only contract when both weights are 1.
        for v in list(G.V):
            nb = G.nbrs(v)
            if len(nb) == 2 and abs(nb[0][1]-1.0)<1e-12 and abs(nb[1][1]-1.0)<1e-12:
                (x,_),(y,_) = nb
                assert G.V[x] == G.V[y], "contraction needs same color endpoints"
                G.E.pop(tuple(sorted((v,x)))); G.E.pop(tuple(sorted((v,y))))
                G.V.pop(v)
                # union edges of x and y onto x... standard: merge y into x
                for (u,ww) in G.nbrs(y):
                    G.E.pop(tuple(sorted((y,u))), None)
                    if u != x:
                        key=tuple(sorted((x,u)))
                        assert key not in G.E, f"multi-edge {key}"
                        G.E[key]=ww
                G.V.pop(y)
                changed = True
                break
    return G, factor

def full_shuffle(n, a, b):
    G = build_aztec_cj(n, a, b)
    zb = brute_Z(G)
    Dp = 1.0
    for i in range(n):
        for j in range(n):
            corners=[('B',(2*i,2*j+1)),('W',(2*i+1,2*j)),('B',(2*i+2,2*j+1)),('W',(2*i+1,2*j+2))]
            Dp *= spider(G, corners)
    G2, f = reduce_graph(G)
    zr = brute_Z(G2)
    print(f"n={n} Z_before={zb:.10f} Delta_prod={Dp:.10f} reduce_factor={f:.10f} Z_reduced={zr:.10f}")
    print(f"   check: Z_before =?= Dp * f * Z_reduced: {Dp*f*zr:.10f} match={abs(zb-Dp*f*zr)<1e-8}")
    print(f"   reduced: V={len(G2.V)} E={len(G2.E)} (Aztec_{n-1} has V={2*(n-1)*n}, E={4*(n-1)**2})")
    # edge weight multiset of reduced graph
    from collections import Counter
    ws = Counter(round(w,9) for w in G2.E.values())
    print(f"   weight multiset: {dict(ws)}")
    return G2, Dp, f, zb

for n in [2,3]:
    full_shuffle(n, 0.7, 1.3)
    print()
