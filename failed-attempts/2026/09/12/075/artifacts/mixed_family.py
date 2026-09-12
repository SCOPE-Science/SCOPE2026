"""Identify the mixed weight pattern after one shuffle, with POSITIONS.
Key: track positions of inner vertices. Inner vertex created at face (i,j) has a KNOWN geometric home.
Rewrite shuffle with position tags: inner P-vertex of face (i,j) gets pos ('F',i,j,k).
After reduction (contractions merge vertices), positions blur — but EDGES of reduced graph are inner-square edges, each belonging to a parent face!
Each inner-square edge has weight parent_w/Delta_parent in {1/(2x),1/(2y)}. The reduced graph's edges = subset of inner-square edges (those not removed during peel/contract).
Map each surviving edge to parent face parity → reconstruct pattern on Aztec_{n-1} faces."""
from validate_ops import WGraph, build_aztec_cj, brute_Z

def shuffle_tagged(n, a, b):
    G = build_aztec_cj(n, a, b)
    Dp = 1.0
    # tag original vertices with positions (they already have them)
    for i in range(n):
        for j in range(n):
            w = a if (i+j)%2==0 else b
            corners=[('B',(2*i,2*j+1)),('W',(2*i+1,2*j)),('B',(2*i+2,2*j+1)),('W',(2*i+1,2*j+2))]
            v0,v1,v2,v3=corners
            ws=[]
            for (xx,yy) in [(v0,v1),(v1,v2),(v2,v3),(v3,v0)]:
                ws.append(G.E.pop(tuple(sorted((xx,yy)))))
            Delta=ws[0]*ws[2]+ws[1]*ws[3]
            Dp*=Delta
            Pts=[]
            for k,vk in enumerate(corners):
                p=('P',i,j,k)
                assert p not in G.V
                G.V[p]=1-G.V[vk]; Pts.append(p)
            for k,vk in enumerate(corners):
                G.add_edge(vk,Pts[k],1.0)
            W=[ws[(k+2)%4]/Delta for k in range(4)]
            for k in range(4):
                G.add_edge(Pts[k],Pts[(k+1)%4],(W[k],i,j,k))  # tag weight with parent face
    return G, Dp

def reduce_tagged(G):
    factor=1.0
    def wval(e):
        w=G.E[e]; return w[0] if isinstance(w,tuple) else w
    changed=True
    while changed:
        changed=False
        pend=[v for v in list(G.V) if len(G.nbrs(v))==1]
        handled=set()
        for v in pend:
            if v in handled or v not in G.V: continue
            nb=G.nbrs(v)
            if not nb: continue
            (vp,w)=nb[0]
            factor*=wval(tuple(sorted((v,vp))))
            handled.add(v); handled.add(vp)
            for (u,ww) in G.nbrs(vp): G.E.pop(tuple(sorted((vp,u))),None)
            for (u,ww) in G.nbrs(v): G.E.pop(tuple(sorted((v,u))),None)
            G.V.pop(v,None); G.V.pop(vp,None)
            changed=True
        if changed: continue
        for v in list(G.V):
            nb=G.nbrs(v)
            if len(nb)==2 and abs(wval(tuple(sorted((v,nb[0][0]))))-1.0)<1e-12 and abs(wval(tuple(sorted((v,nb[1][0]))))-1.0)<1e-12:
                (x,_),(y,_)=nb
                assert G.V[x]==G.V[y]
                G.E.pop(tuple(sorted((v,x)))); G.E.pop(tuple(sorted((v,y))))
                G.V.pop(v)
                for (u,ww) in G.nbrs(y):
                    G.E.pop(tuple(sorted((y,u))),None)
                    if u!=x:
                        key=tuple(sorted((x,u)))
                        assert key not in G.E
                        G.E[key]=ww
                G.V.pop(y)
                changed=True
                break
    return G, factor

G,Dp=shuffle_tagged(3,0.7,1.3)
G,f=reduce_tagged(G)
print("factor:",f,"V,E:",len(G.V),len(G.E))
for e,w in G.E.items():
    val,fi,fj,fk = w
    print(f"edge {e[0]}--{e[1]}: val={val:.6f} parent=({fi},{fj})k={fk}")
