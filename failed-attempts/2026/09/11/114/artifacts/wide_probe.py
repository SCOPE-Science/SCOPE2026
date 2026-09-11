import itertools, random, time
from fractions import Fraction as F
def sub(u,v): return (u[0]-v[0],u[1]-v[1],u[2]-v[2])
def dot(u,v): return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
def cross(u,v): return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def xmeet(Af,Bf):
    D=[sub(p,q) for p in Af for q in Bf]; n=len(D)
    cands=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
    for i in range(n):
        for j in range(i+1,n):
            e=sub(D[j],D[i])
            if e!=(0,0,0): cands.append(e)
            for k in range(j+1,n):
                u=cross(sub(D[j],D[i]),sub(D[k],D[i]))
                if u!=(0,0,0): cands.append(u)
    for u in cands:
        vals=[dot(u,d) for d in D]
        if all(v>0 for v in vals) or all(v<0 for v in vals): return False
    return True
verts=list(range(10)); rng=random.Random(77)
PROBE=[([0,2,4,6],[1,3,5]),([0,2,4,7],[1,3,5]),([1,3,5,7],[2,4,6,8]),([0,3],[2,4,9]),([0,1,3,6,7,9],[2,5,8])]
t0=time.time()
for tr in range(6):
    cfg=[(rng.randint(0,30),rng.randint(0,30),rng.randint(0,30)) for _ in range(10)]
    if len(set(cfg))<10: continue
    CF=[(F(x),F(y),F(z)) for (x,y,z) in cfg]
    res=[]
    for (A,B) in PROBE:
        ok=all(xmeet([CF[x] for x in A if x!=v],[CF[x] for x in B if x!=v]) for v in range(10))
        res.append(ok)
    print(f"wide{tr}: {res} t={round(time.time()-t0,1)}",flush=True)
    if time.time()-t0>50: break
