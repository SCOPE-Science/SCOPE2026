from general_shuffle import build_general, uniform_face, shuffle_general, reduce_g, raw
from validate_ops import brute_Z, WGraph
from two_step import faces_of_graph
from collections import Counter

def shuffle_subset(G, n, facedict, pred):
    Dp=1.0
    for i in range(n):
        for j in range(n):
            if not pred(i,j): continue
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
                G.add_edge(Pts[k],Pts[(k+1)%4],W[k])
    return G,Dp

for pred,lbl in [(lambda i,j:(i+j)%2==0,"even"),(lambda i,j:(i+j)%2==1,"odd")]:
    n=3; x,y=0.7,1.3
    G=build_general(n,uniform_face(n,x,y))
    zb=brute_Z(G)
    G,Dp=shuffle_subset(G,n,uniform_face(n,x,y),pred)
    G,f=reduce_g(G)
    R=raw(G)
    print(f"subset={lbl}: Dp={Dp:.6f} f={f:.6f} V={len(R.V)} E={len(R.E)} Zr={brute_Z(R):.9f} check={Dp*f*brute_Z(R):.9f} vs {zb:.9f}")
    print("  degrees:",dict(Counter(len([e for e in R.E if v in e]) for v in R.V)))
