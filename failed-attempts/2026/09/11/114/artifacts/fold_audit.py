"""Folded-interval PL search: vertices -> colinear points with multiplicities.
f(i) = x_{m(i)} on x-axis; conv(A) cap conv(B) = interval overlap (closed).
Uniform pair needs overlap after every deletion. Since images are colinear,
compute EXACTLY with Fractions (no orientation gap): meet iff
max(min A2, min B2) <= min(max A2, max B2).
Search: random multiplicity patterns + random distinct positions; also
structured adversarial patterns (alternating clusters). Report min-uniform.
"""
import itertools, random
from fractions import Fraction as F

def audit(pos):
    n = len(pos)
    verts = list(range(n))
    pairs = []
    seen = set()
    for r1 in range(2, n-1):
        for s in itertools.combinations(verts, r1):
            S = frozenset(s)
            rest = tuple(v for v in verts if v not in S)
            for r2 in range(2, len(rest)+1):
                for t in itertools.combinations(rest, r2):
                    T = frozenset(t)
                    a,b = (S,T) if str(sorted(S))<=str(sorted(T)) else (T,S)
                    if (a,b) in seen: continue
                    seen.add((a,b))
                    pairs.append((sorted(a),sorted(b)))
    nun = 0; ex = []
    for (A,B) in pairs:
        ok = True
        for v in range(n):
            A2=[pos[x] for x in A if x!=v]; B2=[pos[x] for x in B if x!=v]
            if max(min(A2),min(B2)) > min(max(A2),max(B2)):
                ok=False; break
        if ok:
            nun+=1
            if len(ex)<4: ex.append((A,B))
    return len(pairs), nun, ex

# baseline distinct
print(audit([F(i) for i in range(10)]))
# clustered multiplicities: 5 clusters of 2
rng = random.Random(3)
best=None
for tr in range(200):
    # random map 10 verts -> 4 distinct rational positions
    pos=[F(rng.randint(0,3)) for _ in range(10)]
    # need each deletion-nonempty automatically true (|.|>=2)
    tot,nun,ex=audit(pos)
    if best is None or nun<best[0]:
        best=(nun,pos,ex)
print("best4:", best)
for tr in range(200):
    pos=[F(rng.randint(0,2)) for _ in range(10)]
    tot,nun,ex=audit(pos)
    if nun==0:
        print("ZERO uniform found:", pos); break
else:
    print("no zero in 3-position family")
