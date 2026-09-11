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
verts=list(range(10))
rng=random.Random(78)
cfg=[(rng.randint(0,30),rng.randint(0,30),rng.randint(0,30)) for _ in range(10)]
CF=[(F(x),F(y),F(z)) for (x,y,z) in cfg]
print("cfg:",cfg)
pairs=[]; seen=set()
for r1 in range(2,9):
    for s in itertools.combinations(verts,r1):
        S=frozenset(s); rest=[v for v in verts if v not in S]
        for r2 in range(2,len(rest)+1):
            for t in itertools.combinations(rest,r2):
                T=frozenset(t)
                a,b=(S,T) if str(sorted(S))<=str(sorted(T)) else (T,S)
                if (a,b) in seen: continue
                seen.add((a,b)); pairs.append((sorted(a),sorted(b)))
print("total:",len(pairs))
t0=time.time(); nun=0; ex=[]
for k,(A,B) in enumerate(pairs):
    ok=True
    for v in range(10):
        if not xmeet([CF[x] for x in A if x!=v],[CF[x] for x in B if x!=v]): ok=False; break
    if ok:
        nun+=1
        if len(ex)<6: ex.append((A,B))
    if time.time()-t0>52: print("TIMEOUT at",k); break
print("uniform:",nun,ex,"t=",round(time.time()-t0,1))
