"""Independent verifier for the PRESET FALLBACK (stdlib + numpy only).
Reloads output/artifacts/Phi_64x125.csv (64x125), recomputes the H_3(Z_5)
word metric from the group law + generators {a^+-1,b^+-1} via BFS, then checks
all 7750 unordered pairs: L = d_H^{1/2}/||Phi diff||, max(L)/min(L) <= 8,
min denominator > 0. Prints VERIFY_PASS/VERIFY_FAIL + JSON.
"""
import json, math
from collections import deque
import numpy as np

MOD = 5
def mul(p, q):
    x,y,z = p; x2,y2,z2 = q
    return ((x+x2)%MOD, (y+y2)%MOD, (z+z2+x*y2)%MOD)
def inv(p):
    x,y,z = p
    return ((-x)%MOD, (-y)%MOD, (x*y-z)%MOD)

a=(1,0,0); b=(0,1,0)
S=[a,b,inv(a),inv(b)]
pts=[(x,y,z) for x in range(MOD) for y in range(MOD) for z in range(MOD)]
idx={p:i for i,p in enumerate(pts)}
n=len(pts); assert n==125
nbrs=[[idx[mul(p,s)] for s in S] for p in pts]
D=np.zeros((n,n),dtype=int)
for s in range(n):
    dist=np.full(n,-1); dist[s]=0; q=deque([s])
    while q:
        u=q.popleft()
        for w in nbrs[u]:
            if dist[w]<0:
                dist[w]=dist[u]+1; q.append(w)
    assert (dist>=0).all(); D[s]=dist

T=np.loadtxt("output/artifacts/Phi_64x125.csv", delimiter=",")
assert T.shape==(64,125), T.shape
N,nc=T.shape; assert N<=64
Phi=T.T
SQ=np.sqrt(D.astype(float))
d2=np.zeros((n,n))
for k in range(N):
    c=Phi[:,k]; d2+=(c[:,None]-c[None,:])**2
E=np.sqrt(np.maximum(d2,0.0))
iu=np.triu_indices(n,1); assert len(iu[0])==7750
den=E[iu]; num=SQ[iu]
assert (den>0).all()
Lr=num/den
ratio=float(Lr.max()/Lr.min())
out={"N":N,"pairs":7750,"diameter":int(D.max()),
     "min_denominator":float(den.min()),"min_L":float(Lr.min()),
     "max_L":float(Lr.max()),"max_over_min":ratio,
     "criterion_max_over_min_le_8":bool(ratio<=8.0),
     "VERDICT":"VERIFY_PASS" if (ratio<=8.0 and (den>0).all()) else "VERIFY_FAIL"}
print(json.dumps(out,indent=2))
json.dump(out,open("output/artifacts/fallback_verification.json","w"),indent=2)
