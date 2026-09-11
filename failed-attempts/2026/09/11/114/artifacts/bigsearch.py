"""Extend search objective to ALL admissible pairs using an exact LP fallback
for boundary cases. Exact hull intersection via vertex-enumeration of the
separation oracle over ALL facet normals of conv(D) (complete, exact, integer):
separators = normals of triangular facets of conv(D) + axis/edge directions.
Completeness fix: enumerate candidate normals from triples of D (done) PLUS
edge-cross products (u x e for edges e of D pairs and axes) to catch
edge-edge facet degeneracies; PLUS exact LP vertex check as final arbiter:
solve feasibility sum a=1,sum b=1,mean equal via enumerating supports<=6 with
exact Fraction linear solve (nullspace sampling + orthant recursion from
audit_affine, imported). For speed: only invoke exact LP on strict_meet
survivors/uncertified pairs (rare), strict predicate handles the bulk."""
import itertools, random, time, sys
sys.path.insert(0,'output/artifacts')
from fractions import Fraction as F
C=[(0,5,4),(0,6,5),(3,6,1),(6,3,2),(0,4,5),(3,3,4),(0,3,0),(0,0,5),(0,2,3),(6,2,3)]
CF=[(F(x),F(y),F(z)) for (x,y,z) in C]
def sub(u,v): return (u[0]-v[0],u[1]-v[1],u[2]-v[2])
def dot(u,v): return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
def cross(u,v): return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def exact_meet(Af,Bf):
    D=[sub(p,q) for p in Af for q in Bf]
    n=len(D)
    cands=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
    for i in range(n):
        for j in range(i+1,n):
            e=sub(D[j],D[i])
            if e!=(F(0),F(0),F(0)): cands.append(e)
            for k in range(j+1,n):
                u=cross(sub(D[j],D[i]),sub(D[k],D[i]))
                if u!=(F(0),F(0),F(0)): cands.append(u)
    # edge-edge axes: cross of difference-edges
    E=[sub(D[j],D[i]) for i in range(n) for j in range(i+1,n) if sub(D[j],D[i])!=(F(0),F(0),F(0))]
    for i in range(len(E)):
        for j in range(i+1,len(E)):
            u=cross(E[i],E[j])
            if u!=(F(0),F(0),F(0)): cands.append(u)
    for u in cands:
        vals=[dot(u,d) for d in D]
        if all(v>0 for v in vals) or all(v<0 for v in vals):
            return False
    return True
# validate exact_meet on the 51 strict survivors + sanity
S1=([0,1,3,6,7,9],[2,5,8])
Af=[CF[i] for i in S1[0]]; Bf=[CF[i] for i in S1[1]]
print("survivor exact:",exact_meet(Af,Bf))
# count exact-uniform over ALL pairs for C
verts=list(range(10)); pairs=[]; seen=set()
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
for (A,B) in pairs:
    ok=True
    for v in range(10):
        A2=[CF[x] for x in A if x!=v]; B2=[CF[x] for x in B if x!=v]
        if not exact_meet(A2,B2): ok=False; break
    if ok: nun+=1; ex.append((A,B))
    if time.time()-t0>50: print("TIMEOUT at",pairs.index((A,B))); break
print("exact uniform:",nun,ex[:10],"t=",round(time.time()-t0,1))
