"""Try to PROVE the affine uniform statement via the pigeonhole structure of
minimal Radon partitions, OR find an affine counterexample by smarter search.

Key structural attempt: for 10 points in R^3, consider ALL minimal Radon
partitions (A,B) (disjoint, conv meet, minimal support). Claim attempt: the
FAMILY of minimal partitions has the hitting property that some pair survives
all deletions. Try to prove computationally the combinatorial core: for the
ORIENTED-MATROID level (order type), enumerate... too big. Instead: random
search over LARGER integer boxes with exact_uniform objective on a PAIR SAMPLE
(500 quick pairs) as proxy, then full-certify only promising (<=2 proxy) ones.
"""
import itertools, random, time, sys
sys.path.insert(0,'output/artifacts')
from fractions import Fraction as F
from bigsearch import exact_meet
verts=list(range(10))
PAIRS=[]; seen=set()
for r1 in range(2,9):
    for s in itertools.combinations(verts,r1):
        S=frozenset(s); rest=[v for v in verts if v not in S]
        for r2 in range(2,len(rest)+1):
            for t in itertools.combinations(rest,r2):
                T=frozenset(t)
                a,b=(S,T) if str(sorted(S))<=str(sorted(T)) else (T,S)
                if (a,b) in seen: continue
                seen.add((a,b)); PAIRS.append((sorted(a),sorted(b)))
rng=random.Random(2026)
SAMPLE=rng.sample(PAIRS,400)
print("sample:",len(SAMPLE))
def proxy(cfg):
    CF=[(F(x),F(y),F(z)) for (x,y,z) in cfg]
    n=0
    for (A,B) in SAMPLE:
        ok=True
        for v in range(10):
            if not exact_meet([CF[x] for x in A if x!=v],[CF[x] for x in B if x!=v]):
                ok=False; break
        if ok: n+=1
    return n
t0=time.time(); best=None
for tr in range(40):
    cfg=[(rng.randint(0,9),rng.randint(0,9),rng.randint(0,9)) for _ in range(10)]
    if len(set(cfg))<10: continue
    # skip degenerate-heavy (many coplanar quads)? keep, degeneracy helps meet
    s=proxy(cfg)
    if best is None or s<best[0]: best=(s,cfg); print(f"trial {tr}: proxy={s} t={round(time.time()-t0,1)}",flush=True)
    if time.time()-t0>50: break
print("BEST proxy:",best[0])
