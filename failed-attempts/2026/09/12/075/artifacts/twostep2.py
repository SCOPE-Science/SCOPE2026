"""Distinguish inner faces from outer cycle; then shuffle-2 on true faces."""
from general_shuffle import build_general, uniform_face, shuffle_general, reduce_g, raw
from validate_ops import brute_Z, WGraph
from two_step import faces_of_graph
import itertools

n=3; x,y=0.7,1.3
G=build_general(n,uniform_face(n,x,y))
zb=brute_Z(G)
G,Dp1=shuffle_general(G,n,uniform_face(n,x,y))
G,f1=reduce_g(G)
R=raw(G)
print(f"after shuffle1: Z check {Dp1*f1*brute_Z(R):.9f} vs {zb:.9f}")
cycs=faces_of_graph(R)
# Outer face: use vertex coordinates. Reconstruct coords: P(i,j,k) home = parent face center (2i+1,2j+1) + corner offset.
off={0:(-1,-1),1:(1,-1),2:(1,1),3:(-1,1)}
def coord(v):
    _,i,j,k=v; return (2*i+1+0.3*off[k][0], 2*j+1+0.3*off[k][1])
# outer cycle = the one enclosing largest area (shoelace)
def area(cyc):
    # order the cycle first
    adj={v:set() for v in cyc}
    for a in cyc:
        for b in cyc:
            if a!=b and tuple(sorted((a,b))) in R.E: adj[a].add(b)
    start=cyc[0]; order=[start]; prev=None; cur=start
    for _ in range(len(cyc)):
        nxt=[u for u in adj[cur] if u!=prev][0]
        prev,cur=cur,nxt
        if cur==start: break
        order.append(cur)
    pts=[coord(v) for v in order]
    return abs(sum(pts[k][0]*pts[(k+1)%len(pts)][1]-pts[(k+1)%len(pts)][0]*pts[k][1] for k in range(len(pts))))/2, order
infos=sorted(((area(c)[0],c) for c in cycs), reverse=True)
for A,c in infos:
    print(f"area={A:.3f} cycle={[str(v) for v in c]}")
Amax,cmax=infos[0]
inner=[c for A,c in infos[1:]]
print("num inner:",len(inner))
# shuffle 2: spider the 4 inner faces (in some cyclic corner order), reduce, read Aztec_1
def spider_face(G2, cyc_ordered):
    # order must be cyclic B,W,B,W; find one
    u0,u1,u2,u3=cyc_ordered
    assert G2.V[u0]!=G2.V[u1]
    ws=[]
    for (xx,yy) in [(u0,u1),(u1,u2),(u2,u3),(u3,u0)]:
        ws.append(G2.E.pop(tuple(sorted((xx,yy)))))
    Delta=ws[0]*ws[2]+ws[1]*ws[3]
    Pts=[]
    for k,vk in enumerate([u0,u1,u2,u3]):
        p=('Q',vk); G2.V[p]=1-G2.V[vk]; Pts.append(p)
    for k,vk in enumerate([u0,u1,u2,u3]):
        G2.add_edge(vk,Pts[k],1.0)
    W=[ws[(k+2)%4]/Delta for k in range(4)]
    for k in range(4):
        G2.add_edge(Pts[k],Pts[(k+1)%4],W[k])
    return Delta
# order each inner cycle
def order_cycle(cyc):
    adj={v:set() for v in cyc}
    for a in cyc:
        for b in cyc:
            if a!=b and tuple(sorted((a,b))) in R.E: adj[a].add(b)
    start=[v for v in cyc if R.V[v]==1][0]
    order=[start]; prev=None; cur=start
    for _ in range(len(cyc)):
        nxt=[u for u in adj[cur] if u!=prev][0]
        prev,cur=cur,nxt
        if cur==start: break
        order.append(cur)
    return order
G2=R; Dp2=1.0
orders=[order_cycle(c) for c in inner]
for o in orders:
    Dp2*=spider_face(G2, o)
print("Dp2=",Dp2)
G2,f2=reduce_g(G2)
print(f"after shuffle2: V={len(G2.V)} E={len(G2.E)} f2={f2}")
for e,w in G2.E.items():
    print(f"  {e}: {w}")
print("Z double-check:",Dp1*f1*Dp2*f2*brute_Z(G2),"vs",zb)
