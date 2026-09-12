from general_shuffle import build_general, uniform_face, shuffle_general, reduce_g, raw
from validate_ops import build_aztec_cj
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
# backtracking with color classes: R colors are P2/P3?? check: R.V values
from collections import Counter
print("R colorvals:",Counter(R.V.values()),"H:",Counter(H.V.values()))
# order R verts by (color, degree)
order=sorted(R.V, key=lambda v:(R.V[v],len(AR[v])))
mp={}; used=set()
def bt(k):
    if k==len(order): return True
    v=order[k]
    for w in H.V:
        if w in used or H.V[w]!=R.V[v]: continue
        if any((mp.get(u) is not None and mp[u] not in AH[w]) or (u in AR[v] and False) for u in []): pass
        # consistency: mapped nbrs of v must be nbrs of w; mapped non-nbrs... check adjacency both ways on mapped set
        ok=True
        for u,mu in mp.items():
            if (u in AR[v]) != (mu in AH[w]): ok=False; break
        if not ok: continue
        mp[v]=w; used.add(w)
        if bt(k+1): return True
        del mp[v]; used.discard(w)
    return False
print("searching...")
print("iso:",bt(0))
if mp:
    for (a,b) in R.E:
        assert tuple(sorted((mp[a],mp[b]))) in H.E
    print("edge check passed")
    inv={v:k for k,v in mp.items()}
    for i in range(2):
        for j in range(2):
            pairs=[(('B',(2*i,2*j+1)),('W',(2*i+1,2*j))),(('B',(2*i,2*j+1)),('W',(2*i+1,2*j+2))),(('B',(2*i+2,2*j+1)),('W',(2*i+1,2*j))),(('B',(2*i+2,2*j+1)),('W',(2*i+1,2*j+2)))]
            try:
                e=[R.E[tuple(sorted((inv[a],inv[b])))] for a,b in pairs]
                print(f"face({i},{j}): {[round(v,6) for v in e]}")
            except KeyError:
                print(f"face({i},{j}): not a face under this iso")
