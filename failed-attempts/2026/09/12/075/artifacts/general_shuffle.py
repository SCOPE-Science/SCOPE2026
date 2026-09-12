"""General shuffle: arbitrary face weights (4-tuple per face). Apply to mixed pattern; test return to uniform."""
from validate_ops import WGraph, brute_Z

def build_general(n, facedict):
    """fac“edict[(i,j)] = (w01,w02,w10,w11): weight of edges B(2i,2j+1)-W(2i+1,2j), B(2i,2j+1)-W(2i+1,2j+2), B(2i+2,2j+1)-W(2i+1,2j), B(2i+2,2j+1)-W(2i+1,2j+2)."""
    G=WGraph()
    W=[(i,j) for i in range(1,2*n,2) for j in range(0,2*n+1,2)]
    B=[(i,j) for i in range(0,2*n+1,2) for j in range(1,2*n,2)]
    for w in W: G.V[('W',w)]=0
    for b in B: G.V[('B',b)]=1
    for (i,j),four in facedict.items():
        vB1=('B',(2*i,2*j+1)); vB2=('B',(2*i+2,2*j+1)); vW1=('W',(2*i+1,2*j)); vW2=('W',(2*i+1,2*j+2))
        G.add_edge(vB1,vW1,four[0]); G.add_edge(vB1,vW2,four[1])
        G.add_edge(vB2,vW1,four[2]); G.add_edge(vB2,vW2,four[3])
    return G

def uniform_face(n,x,y):
    return {(i,j):((x,x,x,x) if (i+j)%2==0 else (y,y,y,y)) for i in range(n) for j in range(n)}
    return {(i,j):((x,x,x,x) if (i+j)%2==0 else (y,y,y,y)) for i in range(n) for j in range(n)}

def shuffle_general(G, n, facedict):
    """Spider at every face. Returns (G2, Delta_prod, newfacedict_info). Inner weights tagged by parent."""
    Dp=1.0
    for i in range(n):
        for j in range(n):
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
                G.V[p]=1-G.V[vk]; Pts.append(p)
            for k,vk in enumerate(corners):
                G.add_edge(vk,Pts[k],1.0)
            W=[ws[(k+2)%4]/Delta for k in range(4)]
            for k in range(4):
                G.add_edge(Pts[k],Pts[(k+1)%4],(W[k],i,j,k))
    return G,Dp

def reduce_g(G):
    factor=1.0
    def wv(e):
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
            factor*=wv(tuple(sorted((v,vp))))
            handled.add(v); handled.add(vp)
            for (u,ww) in G.nbrs(vp): G.E.pop(tuple(sorted((vp,u))),None)
            for (u,ww) in G.nbrs(v): G.E.pop(tuple(sorted((v,u))),None)
            G.V.pop(v,None); G.V.pop(vp,None)
            changed=True
        if changed: continue
        for v in list(G.V):
            nb=G.nbrs(v)
            if len(nb)==2 and abs(wv(tuple(sorted((v,nb[0][0]))))-1.0)<1e-12 and abs(wv(tuple(sorted((v,nb[1][0]))))-1.0)<1e-12:
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
    return G,factor

def raw(G):
    H=WGraph(); H.V=dict(G.V)
    for e,w in G.E.items():
        H.E[e]=w[0] if isinstance(w,tuple) else w
    return H

if __name__=="__main__":
    n=3; x,y=0.7,1.3
    G=build_general(n,uniform_face(n,x,y))
    zb=brute_Z(G)
    G,Dp=shuffle_general(G,n,uniform_face(n,x,y))
    G,f=reduce_g(G)
    print(f"shuffle1: Z={zb:.9f} Dp={Dp:.9f} f={f} Dp*f*Zr={Dp*f*brute_Z(raw(G)):.9f} V,E={len(G.V)},{len(G.E)}")
