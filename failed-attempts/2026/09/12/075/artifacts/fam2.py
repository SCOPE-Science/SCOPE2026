from general_shuffle import build_general, shuffle_general, reduce_g, raw
from validate_ops import brute_Z, WGraph
def cross_face(n,p,q):
    d={}
    for i in range(n):
        for j in range(n):
            d[(i,j)]=((p,q,q,p) if (i+j)%2==0 else (q,p,p,q))
    return d
def read_faces_uniform(R, m):
    """m: Aztec_2 standard; R reduced with iso mp. Inline iso search here for n-1=2 only."""
    return None
# Direct approach: shuffle B-pattern Aztec_3, reduce, then classify faces via chordless cycles + tips (as before), check uniform-face pattern up to iso.
from two_step import faces_of_graph
from collections import Counter
n=3; p,q=0.714285714,0.384615385
G=build_general(n,cross_face(n,p,q))
zb=brute_Z(G)
print(f"B-pattern Z_3({p:.4f},{q:.4f})={zb:.9f}")
G,Dp=shuffle_general(G,n,cross_face(n,p,q))
G,f=reduce_g(G)
R=raw(G)
print(f"shuffle: Dp={Dp:.9f} f={f} Zr={brute_Z(R):.9f} check={Dp*f*brute_Z(R):.9f}")
print("degs:",dict(Counter(len([e for e in R.E if v in e]) for v in R.V)))
cycs=faces_of_graph(R)
tips=[v for v in R.V if len([e for e in R.E if v in e])==2]
for c in cycs:
    ws=[]
    try:
        for k in range(4):
            ws.append(R.E[tuple(sorted((c[k],c[(k+1)%4])))])
    except KeyError:
        print("non-cyclic set"); continue
    nbt=sum(1 for v in c if v in tips)
    print(f"tips={nbt} w={[round(w,6) for w in ws]}")
