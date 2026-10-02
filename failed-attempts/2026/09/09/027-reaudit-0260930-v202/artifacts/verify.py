"""Independent verifier: replays census.json from stored edges/faces/positions.
Checks:
 (1) closed-triangulation audit per type (E=3n-6, F=2n-4, min-degree>=3, 2 faces/edge),
     degree/defect exactness, Gauss-Bonnet sum=12;
 (2) Bobenko W from quaternion formula vs stored W, W(v)>=0, cyclic-order independence;
 (3) pairwise non-isomorphism within each n by exact backtracking iso decision
     procedure (degree/neighbor-signature/triangle-count ordered search);
 (4) flip-closure: every flippable edge-flip of every stored type is isomorphic to a
     stored type of the same n.
Completeness argument: (4) shows the stored set per n is flip-closed; with Wagner's
theorem (flip-graph of n-vertex triangulated spheres is connected) and the n=4 base
(K4), flip-closure certifies no type is missing. Agreement of per-n counts
(1,1,2,5,14,50) with OEIS A000109 is corroboration only, not the completeness proof.
Distinct defect-multiset counts are certified as 1,1,2,5,13,33 for n=4..9.
Stdlib + numpy.
"""
import json, math, os
import numpy as np

ART = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(ART, "census.json")))
TOL = 1e-9

def qmul(q1, q2):
    w1,x1,y1,z1 = q1; w2,x2,y2,z2 = q2
    return (w1*w2-x1*x2-y1*y2-z1*z2, w1*x2+x1*w2+y1*z2-z1*y2,
            w1*y2-x1*z2+y1*w2+z1*x2, w1*z2+x1*y2-y1*x2+z1*w2)

def beta(P, x1, x2, x3, x4):
    def sub(p,q): return (p[0]-q[0],p[1]-q[1],p[2]-q[2])
    a,b,c,d = sub(P[x1],P[x2]),sub(P[x2],P[x3]),sub(P[x3],P[x4]),sub(P[x4],P[x1])
    qa=(0.0,*a); qb=(0.0,*b); qc=(0.0,*c); qd=(0.0,*d)
    q = qmul(qmul(qmul(qa,qb),qc),qd)
    nq = math.sqrt(sum(t*t for t in q))
    assert nq > 1e-12
    return math.acos(max(-1.0,min(1.0,-q[0]/nq)))

# ---------- exact isomorphism decision procedure ----------
def adj_matrix(n, edges):
    a = [[0]*n for _ in range(n)]
    for u,v in edges:
        a[u][v] = a[v][u] = 1
    return a

def node_keys(adj):
    n = len(adj)
    degs = [sum(r) for r in adj]
    tri = [0]*n
    for i in range(n):
        nb = [j for j in range(n) if adj[i][j]]
        c = 0
        for a in range(len(nb)):
            for b in range(a+1, len(nb)):
                if adj[nb[a]][nb[b]]:
                    c += 1
        tri[i] = c
    keys = []
    for i in range(n):
        ns = tuple(sorted(degs[j] for j in range(n) if adj[i][j]))
        keys.append((degs[i], ns, tri[i]))
    return keys

def iso_exists(adjA, adjB):
    n = len(adjA)
    if n != len(adjB):
        return False
    kA, kB = node_keys(adjA), node_keys(adjB)
    if sorted(kA) != sorted(kB):
        return False
    cand = {i: [j for j in range(n) if kB[j] == kA[i]] for i in range(n)}
    order = sorted(range(n), key=lambda i: (len(cand[i]), str(kA[i])))
    mapping = {}
    used = [False]*n
    def bt(k):
        if k == n:
            return True
        i = order[k]
        for j in cand[i]:
            if used[j]:
                continue
            ok = True
            for i2, j2 in mapping.items():
                if adjA[i][i2] != adjB[j][j2]:
                    ok = False
                    break
            if ok:
                mapping[i] = j
                used[j] = True
                if bt(k+1):
                    return True
                del mapping[i]
                used[j] = False
        return False
    return bt(0)

EXP = {4:1,5:1,6:2,7:5,8:14,9:50}
EXP_DISTINCT = {4:1,5:1,6:2,7:5,8:13,9:33}
by_n = {}
for t in C["types"]:
    by_n.setdefault(t["n"], []).append(t)
assert sorted(by_n) == [4,5,6,7,8,9], sorted(by_n)
assert {n: len(v) for n, v in by_n.items()} == EXP, {n: len(v) for n, v in by_n.items()}
assert len(C["types"]) == 73

# (1)+(2): closedness, defects, Willmore replay
worst = 0.0
for t in C["types"]:
    n = t["n"]; E=[tuple(e) for e in t["edges"]]; F=[tuple(f) for f in t["faces"]]
    assert len(E)==3*n-6 and len(F)==2*n-4, t["id"]
    deg=[0]*n
    for u,v in E: deg[u]+=1; deg[v]+=1
    assert all(d >= 3 for d in deg), t["id"]
    assert deg==t["degrees"], t["id"]
    assert [6-x for x in deg]==t["defects_pi_over_3"], t["id"]
    assert sum(t["defects_pi_over_3"])==12, t["id"]  # Gauss-Bonnet
    P={k:tuple(t["pos"][k]) for k in range(n)}
    ef={}
    for f in F:
        for a,b in [(f[0],f[1]),(f[0],f[2]),(f[1],f[2])]:
            ef.setdefault(tuple(sorted((a,b))),[]).append(tuple(f))
    assert all(len(v)==2 for v in ef.values()), t["id"]
    assert set(ef) == set(tuple(sorted(e)) for e in E), t["id"]
    W=0.0; Wv={k: -2*math.pi for k in range(n)}
    for (u,v),(f1,f2) in ef.items():
        A=[x for x in f1 if x!=u and x!=v][0]; B=[x for x in f2 if x!=u and x!=v][0]
        b1=beta(P,u,A,v,B); b2=beta(P,u,B,v,A)
        assert abs(b1-b2)<1e-9,(t["id"],b1,b2)
        W+=b1; Wv[u]+=b1; Wv[v]+=b1
    W-=math.pi*n
    assert all(v>-1e-9 for v in Wv.values()),(t["id"],Wv)
    d=abs(W-t["W"]); worst=max(worst,d)
    assert d<TOL,(t["id"],W,t["W"])
print("closedness+defect+Willmore replay OK: ntypes=73 worst_|Wreplay-Wstored|=%.3e" % worst)

# distinct defect multisets
from collections import Counter
for n in sorted(by_n):
    ms = Counter(tuple(sorted(t["defects_pi_over_3"])) for t in by_n[n])
    assert len(ms) == EXP_DISTINCT[n], (n, len(ms), EXP_DISTINCT[n])
    assert sum(ms.values()) == EXP[n], (n, ms)
print("distinct-defect multisets OK: %s" % ({n: EXP_DISTINCT[n] for n in sorted(by_n)},))

# (3): pairwise non-isomorphism within each n
adj_by_n = {n: [adj_matrix(n, [tuple(e) for e in t["edges"]]) for t in by_n[n]] for n in by_n}
total_pairs = 0
for n in sorted(adj_by_n):
    adjs = adj_by_n[n]
    npairs = 0
    for i in range(len(adjs)):
        for j in range(i+1, len(adjs)):
            assert not iso_exists(adjs[i], adjs[j]), (n, by_n[n][i]["id"], by_n[n][j]["id"])
            npairs += 1
    total_pairs += npairs
    print("n=%d pairwise non-isomorphism OK: %d types, %d pairs all non-isomorphic" % (n, len(adjs), npairs))
print("non-isomorphism total pairs checked: %d" % total_pairs)

# (4): flip-closure within each n
total_flips = 0
nonflip = 0
for n in sorted(by_n):
    adjs = adj_by_n[n]
    nclosed = 0
    for t, adj in zip(by_n[n], adjs):
        F=[tuple(f) for f in t["faces"]]
        eset = set(tuple(sorted(e)) for e in t["edges"])
        ef={}
        for f in F:
            for a,b in [(f[0],f[1]),(f[0],f[2]),(f[1],f[2])]:
                ef.setdefault(tuple(sorted((a,b))),[]).append(tuple(f))
        for (u,v),(f1,f2) in ef.items():
            A=[x for x in f1 if x!=u and x!=v][0]; B=[x for x in f2 if x!=u and x!=v][0]
            if A == B or tuple(sorted((A,B))) in eset:
                nonflip += 1
                continue  # non-flippable hinge (boundary-equivalent); nothing to check
            new_edges = [e for e in eset if e != tuple(sorted((u,v)))] + [tuple(sorted((A,B)))]
            nadj = adj_matrix(n, new_edges)
            assert any(iso_exists(nadj, c) for c in adjs), (t["id"], (u,v))
            nclosed += 1
    total_flips += nclosed
    print("n=%d flip-closure OK: %d flippable hinges land in stored set" % (n, nclosed))
print("flip-closure total flippable hinges checked: %d (non-flippable skipped: %d)" % (total_flips, nonflip))
print("COMPLETENESS: flip-closure per n + Wagner flip-connectivity + K4 base => no missing type; A000109 agreement is corroboration only.")

print("VERIFY_OK ntypes=73 worst_|Wreplay-Wstored|=%.3e pairs=%d flips=%d" % (worst, total_pairs, total_flips))
ws=sorted(C["types"],key=lambda t:t["W"],reverse=True)
print("argmax %s W=%.9f runner-up %s W=%.9f margin=%.9f"%(
    ws[0]["id"],ws[0]["W"],ws[1]["id"],ws[1]["W"],ws[0]["W"]-ws[1]["W"]))
