"""Full spider-all + reduce for each inner shift; check reduced combinatorics (face count) and weights."""
from general_shuffle import build_general, uniform_face, reduce_g, raw
from validate_ops import brute_Z, WGraph
from two_step import faces_of_graph
from collections import Counter
def shuffle_shift(n, facedict, s):
    G=build_general(n, facedict)
    Dp=1.0
    for i in range(n):
        for j in range(n):
            corners=[('B',(2*i,2*j+1)),('W',(2*i+1,2*j)),('B',(2*i+2,2*j+1)),('W',(2*i+1,2*j+2))]
            v0,v1,v2,v3=corners
            ws=[]
            for (x,y) in [(v0,v1),(v1,v2),(v2,v3),(v3,v0)]:
                ws.append(G.E.pop(tuple(sorted((x,y)))))
            Delta=ws[0]*ws[2]+ws[1]*ws[3]; Dp*=Delta
            Pts=[]
            for k,vk in enumerate(corners):
                p=('P',i,j,k); G.V[p]=1-G.V[vk]; Pts.append(p)
            for k,vk in enumerate(corners):
                G.add_edge(vk,Pts[k],1.0)
            W=[ws[(k+s)%4]/Delta for k in range(4)]
            for k in range(4):
                G.add_edge(Pts[k],Pts[(k+1)%4],W[k])
    return G,Dp
for s in [0,1,2,3]:
    n=3; x,y=0.7,1.3
    G,Dp=shuffle_shift(n,uniform_face(n,x,y),s)
    zb=brute_Z(build_general(n,uniform_face(n,x,y)))
    G,f=reduce_g(G)
    R=raw(G)
    cycs=faces_of_graph(R)
    print(f"shift={s}: V={len(R.V)} E={len(R.E)} 4cycles={len(cycs)} check={Dp*f*brute_Z(R):.8f} vs {zb:.8f} degs={dict(Counter(len([e for e in R.E if v in e]) for v in R.V))}")
