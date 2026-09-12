from general_shuffle import build_general, uniform_face, shuffle_general, reduce_g, raw
from two_step import faces_of_graph
from collections import Counter
n=3; x,y=0.7,1.3
G=build_general(n,uniform_face(n,x,y))
G,_=shuffle_general(G,n,uniform_face(n,x,y))
G,_=reduce_g(G)
R=raw(G)
deg=Counter(len([e for e in R.E if v in e]) for v in R.V)
print("degree dist:",dict(deg))
tips=[v for v in R.V if len([e for e in R.E if v in e])==2]
print("tips:",tips)
cycs=faces_of_graph(R)
for c in cycs:
    ws=[]
    for k in range(4):
        ws.append(R.E[tuple(sorted((c[k],c[(k+1)%4])))])
    nbt=sum(1 for v in c if v in tips)
    print(f"boundary_verts={nbt} weights={[round(w,4) for w in ws]} {[str(v) for v in c]}")
