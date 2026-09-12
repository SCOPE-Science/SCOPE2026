from general_shuffle import build_general, uniform_face, shuffle_general, reduce_g, raw
from validate_ops import build_aztec_cj
from collections import Counter
import itertools
n=3
G=build_general(n,uniform_face(n,0.7,1.3))
G,_=shuffle_general(G,n,uniform_face(n,0.7,1.3))
G,_=reduce_g(G)
R=raw(G)
H=build_aztec_cj(2,1,1)
def adj(G2):
    d={v:set() for v in G2.V}
    for (a,b) in G2.E: d[a].add(b); d[b].add(a)
    return d
AR,AH=adj(R),adj(H)
R4=[v for v in R.V if len(AR[v])==4]; H4=[v for v in H.V if len(AH[v])==4]
R2=[v for v in R.V if len(AR[v])==2]; H2=[v for v in H.V if len(AH[v])==2]
found=None
for p4 in itertools.permutations(H4):
    m=dict(zip(R4,p4)); ok=True; m2={}; used=set(p4)
    for v in R2:
        img=set(m[u] for u in AR[v])
        cands=[w for w in H2 if w not in used and set(AH[w])==img]
        if not cands: ok=False; break
        m2[v]=cands[0]; used.add(cands[0])
    if ok: found=(m,m2); break
print("iso found:",found is not None)
if found:
    m,m2=found; m.update(m2)
    for (a,b) in R.E:
        assert tuple(sorted((m[a],m[b]))) in H.E, (a,b)
    print("edge check passed")
    inv={v:k for k,v in m.items()}
    for i in range(2):
        for j in range(2):
            vs=[(inv[('B',(2*i,2*j+1))],inv[('W',(2*i+1,2*j))]),(inv[('B',(2*i,2*j+1))],inv[('W',(2*i+1,2*j+2))]),(inv[('B',(2*i+2,2*j+1))],inv[('W',(2*i+1,2*j))]),(inv[('B',(2*i+2,2*j+1))],inv[('W',(2*i+1,2*j+2))])]
            try:
                e=[R.E[tuple(sorted(p))] for p in vs]
                print(f"face({i},{j}): {[round(v,6) for v in e]}")
            except KeyError:
                print(f"face({i},{j}): not a face under this iso")
