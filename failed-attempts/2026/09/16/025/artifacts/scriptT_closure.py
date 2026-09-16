"""Script T: understand D scaling — D(a,n-a)/n^2 GROWS with n off-optimum (Theta(n) growth
means D is Theta(n^3) off-optimum: expected, since wrong split loses Theta(n^3) B-edges).
So induction on ARBITRARY cover-lemma partitions cannot close with O(n^2) envelope unless
the partition is nearly-optimal in B-mass. Restate: need cover lemma to give partition
with MISS (B-edges absent) + nonB small? Let's define properly:
e(H) = |H cap B(X,Y)| + nonB <= |B(X,Y)| + nonB = C(a,2)b + nonB.
Induction: e(H) <= C(a,2)b + [e(H[Y]) <= brec(b)+Cb^2] + nonB.
Excess over brec(n): E(n) = e(H)-brec(n) <= Cb^2 + nonB - D(a,b). Since D>=0 HELPS.
Wait — D>=0 always (brec optimal), so E(n) <= Cb^2 + nonB REGARDLESS of split quality!
The script-S/R worry was misposed: we need E(n)<=Cn^2, i.e. Cb^2+nonB<=Cn^2: TRUE since
b<=n. The deficit D only helps. The REAL issue is different: INDUCTION HYPOTHESIS applies
to H[Y] (needs H[Y] C7-free: yes, induced) — fine. So closure is TRIVIAL given cover lemma?!
Check: E(n) <= C b^2 + K n^2 <= (C+K) n^2. Set C'=C+K: need E(n)<=C'n^2: holds with C'=C+K.
One-step: assume e(m)<=brec(m)+Cm^2 all m<n; then e(H)<=C(a,2)b+brec(b)+Cb^2+Kn^2
= brec(n)-D +Cb^2+Kn^2 <= brec(n)+(C+K)n^2. So C'=C+K works: fixed point C=K? bootstrap:
base C0 s.t. holds for small n; C_{next}=C+K... DIVERGES unless K=0? No: we need SINGLE C
with C>=C+K: impossible for K>0! The envelope brec+Cn^2 is NOT preserved: constant grows
each level (recursion depth Theta(n)? no—depth is log? V2 shrinks by factor .366: depth
O(log n), constant would grow per level -> C log n: gives O(n^2 log n), NOT O(n^2)!
FIX: need slack from D or from b<<n: Cb^2 with b<=0.37n: Cb^2<=0.14Cn^2 << Cn^2: room Kn^2
absorbed if K+0.14C<=C, i.e. K<=0.86C: HOLDS for C>=K/0.86! The recursion contracts because
b is a FRACTION of n. But cover-lemma partition might give b close to n (bad split)!
Need cover lemma to ALSO force b<=theta*n with theta<1 (bounded away from n), i.e. the
partition must be balanced-ish (a>=c*n). If a>=c*n then Cb^2<=C(1-c)^2n^2 and closure needs
K + C(1-c)^2 <= C, i.e. C >= K/(1-(1-c)^2) = K/(2c-c^2). Finite! Great.
So required cover lemma: partition with nonB<=Kn^2 AND a>=c*n (linear top part).
Verify numerically: with c=0.5: C>=K/0.75; b<=0.5n gives Cb^2<=0.25Cn^2: K+0.25C<=C ok.
Script S data: D only helps further. So the REAL cover lemma needs: min over partitions
with |X|>=c*n of nonB <= K n^2. Small-n test: check min-nonB under |X|>=n/2."""
import itertools, random, sys
sys.path.insert(0, 'output/artifacts')

def build_brec_local(n, CH, B):
    edges = set(); depth = {}
    def rec(verts, d):
        m = len(verts)
        if m <= 2:
            for v in verts: depth[v] = d
            return
        a = CH[m]
        V1 = verts[:a]; V2 = verts[a:]
        for v in V1: depth[v] = d
        for i in range(len(V1)):
            for j in range(i+1, len(V1)):
                for w in V2:
                    edges.add(tuple(sorted((V1[i], V1[j], w))))
        rec(V2, d+1)
    rec(list(range(n)), 0)
    return edges

from math import comb
N = 60
b = [0]*(N+1); ch = [0]*(N+1)
for n in range(3, N+1):
    best = -1; ba = 0
    for a in range(n+1):
        v = comb(a, 2)*(n-a) + b[n-a]
        if v > best: best = v; ba = a
    b[n] = best; ch[n] = ba

# import detector without triggering scriptE2 experiments: copy minimal detector
def make_link(E):
    from collections import defaultdict
    L = defaultdict(set)
    for (x, y, z) in E:
        L[(x, y)].add(z); L[(x, z)].add(y); L[(y, x)].add(z)
        L[(y, z)].add(x); L[(z, x)].add(y); L[(z, y)].add(x)
    return L

def has_C7(E, n, cap=1):
    L = make_link(E); found = []
    sys.setrecursionlimit(10000)
    def bt(path, used):
        if len(found) >= cap: return True
        k = len(path)
        if k == 7:
            if tuple(sorted((path[5], path[6], path[0]))) not in E: return False
            if tuple(sorted((path[6], path[0], path[1]))) not in E: return False
            found.append(tuple(path)); return True
        if k <= 1:
            for v in range(n):
                if v in used: continue
                path.append(v); used.add(v)
                if bt(path, used) and len(found) >= cap: return True
                path.pop(); used.discard(v)
            return False
        for v in L.get((path[-2], path[-1]), ()):
            if v in used: continue
            path.append(v); used.add(v)
            if bt(path, used) and len(found) >= cap: return True
            path.pop(); used.discard(v)
        return False
    for v0 in range(n):
        if bt([v0], {v0}) and len(found) >= cap: break
    return found

def B_edges(X, Y):
    E = set(); X = sorted(X)
    for i in range(len(X)):
        for j in range(i+1, len(X)):
            for w in Y:
                E.add(tuple(sorted((X[i], X[j], w))))
    return E

def cover_constrained(E, n, c=0.5):
    best = None
    for mask in range(1 << (n-1)):
        X = {0} | {i+1 for i in range(n-1) if mask & (1 << i)}
        Y = set(range(n)) - X
        if len(X) < c*n: continue
        BE = B_edges(X, Y)
        nonB = len(set(E) - BE)
        if best is None or nonB < best[0]:
            best = (nonB, sorted(X), sorted(Y))
    return best

for n in [7, 8]:
    E0 = build_brec_local(n, ch, b)
    print(f"n={n} brec-partition check:")
    print("  B_rec, |X|>=n/2:", cover_constrained(E0, n))
    all3 = [t for t in itertools.combinations(range(n), 3) if t not in E0]
    rng = random.Random(7)
    for trial in range(3):
        rng.shuffle(all3)
        cur = set(E0)
        for t in all3:
            cur.add(t)
            if has_C7(cur, n, cap=1): cur.discard(t)
        print(f"  augmented |E|={len(cur)}, |X|>=n/2:", cover_constrained(cur, n))
