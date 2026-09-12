"""Track checkerboard phase through shuffle by rebuilding reduction inline with vertex labels kept."""
from validate_ops import WGraph, build_aztec_cj, brute_Z, spider

def reduce_graph_keep(G):
    factor = 1.0
    changed = True
    while changed:
        changed = False
        pend = [v for v in list(G.V) if len(G.nbrs(v)) == 1]
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
        for v in list(G.V):
            nb = G.nbrs(v)
            if len(nb) == 2 and abs(nb[0][1]-1.0)<1e-12 and abs(nb[1][1]-1.0)<1e-12:
                (x,_),(y,_) = nb
                assert G.V[x] == G.V[y]
                G.E.pop(tuple(sorted((v,x)))); G.E.pop(tuple(sorted((v,y))))
                G.V.pop(v)
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

def shuffle_reduce(n,a,b):
    G = build_aztec_cj(n, a, b)
    Dp=1.0
    for i in range(n):
        for j in range(n):
            corners=[('B',(2*i,2*j+1)),('W',(2*i+1,2*j)),('B',(2*i+2,2*j+1)),('W',(2*i+1,2*j+2))]
            Dp*=spider(G,corners)
    G,f=reduce_graph_keep(G)
    return G,Dp,f

G,Dp,f = shuffle_reduce(3,0.7,1.3)
print("V,E:",len(G.V),len(G.E),"factor:",f)
# Identify surviving original-labeled vertices vs inner P vertices
orig=[v for v in G.V if isinstance(v,tuple) and v[0] in ('B','W')]
print("num orig-labeled:",len(orig))
for e,w in sorted(G.E.items(), key=lambda t:-t[1]):
    print(f"  {e}: {w:.9f}")
