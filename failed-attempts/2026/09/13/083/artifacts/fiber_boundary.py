"""Fiber boundary weights from taut surface weights; switch-rule inference."""
import pickle
import snappy
import flipper.kernel.taut as Tt
from snappy.snap import t3mlite as t3m

WDIR = "output/artifacts"
V = snappy.Manifold(f"{WDIR}/V_flipper_veering.tri")
W = V.without_hyperbolic_structure()
tri = t3m.Mcomplex(W)
TS = Tt.TautStructure.from_triangulation(W)
w = TS.surface.weights
print("face weights:", w, flush=True)
F = {0: 14, 1: 13, 2: 11, 3: 7}
# face weight per (tet, face)
fw = {}
for t in tri.Tetrahedra:
    for j in range(4):
        fw[(t.Index, j)] = w[t.Class[F[j]].Index]
for i in range(6):
    print(f"tet {i}:", {j: fw[(i, j)] for j in range(4)}, flush=True)
# A(i,v,w) = fw[(i,j1)] + fw[(i,j2)], {j1,j2} = faces containing edge (v,w) = {j != v,w}
A = {}
for i in range(6):
    for v in range(4):
        for w_ in range(4):
            if w_ == v:
                continue
            js = [j for j in range(4) if j != v and j != w_]
            A[(i, v, w_)] = fw[(i, js[0])] + fw[(i, js[1])]
# x(side ((i,v),j)) = sum_{w != v,j} A(i,v,w)
D = pickle.load(open(f"{WDIR}/track_data.pkl", "rb"))
branches = D["branches"]
bkey = {}
for b, members in enumerate(branches):
    for s in members:
        bkey[s] = b
x = [0] * len(branches)
for i in range(6):
    for v in range(4):
        for j in range(4):
            if j == v:
                continue
            x[bkey[((i, v), j)]] += sum(A[(i, v, w_)] for w_ in range(4) if w_ != v and w_ != j)
print("fiber boundary branch weights:", x, flush=True)
# check switch equations under each rule: x_L =? x_s1 + x_s2
WSTAR = {0: 2, 1: 3, 2: 0, 3: 1}
def large_side(v, rule):
    opp = WSTAR[v]
    others = [j for j in range(4) if j != v and j != opp]
    if rule == 0:
        return opp
    sides = sorted(j for j in range(4) if j != v)
    return sides[(sides.index(opp) + rule) % 3]
for rule in [0, 1, 2]:
    ok = 0; bad = []
    for i in range(6):
        for v in range(4):
            L = bkey[((i, v), large_side(v, rule))]
            ss = [bkey[((i, v), j)] for j in range(4) if j != v and j != large_side(v, rule)]
            if x[L] == x[ss[0]] + x[ss[1]]:
                ok += 1
            else:
                bad.append(((i, v), x[L], x[ss[0]], x[ss[1]]))
    print(f"rule {rule}: {ok}/24 switches hold", flush=True)
    for b_ in bad[:8]:
        print("   ", b_, flush=True)
