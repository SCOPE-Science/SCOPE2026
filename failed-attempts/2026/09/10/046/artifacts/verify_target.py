"""Exact stdlib-only verification of TARGET witness for Theta(2,3,3).
Vertices order: [a,b,p,q1,q2,r1,r2]. All checks are exact integer brute force."""
import itertools
V = ['a','b','p','q1','q2','r1','r2']
E = [(0,2),(2,1),(0,3),(3,4),(4,1),(0,5),(5,6),(6,1)]  # 8 edges
assert len(E)==8 and len(V)==7
# (1) all vertex covers + minimal covers
covers=[tuple((m>>i)&1 for i in range(7)) for m in range(128)
        if all(((m>>u)&1)+((m>>v)&1)>=1 for u,v in E)]
tau=min(sum(c) for c in covers)
minc=[c for c in covers if sum(c)==tau]
print("num_covers=%d tau=%d num_minimal=%d"%(len(covers),tau,len(minc)))
for c in minc: print("  mincover",dict(zip(V,c)))
assert len(covers)==27 and tau==4 and len(minc)==6
# every minimal cover meets {a,b}
assert all(c[0]+c[1]>=1 for c in minc)
# (2) witness w = a b p^3 q1^3 q2^3 r1^3 r2^3
w=(1,1,3,3,3,3,3)
sums=sorted(w[u]+w[v] for u,v in E)
print("edge_sums(w)=",sums)
assert all(s>=4 for s in sums), "w must lie in J^(4)"
# (3) w not in J^3: no triple of minimal covers is coordinatewise <= w
triples=list(itertools.product(minc,repeat=3))
print("num_triples=%d"%len(triples))
bad=[t for t in triples if all(t[0][k]+t[1][k]+t[2][k]<=w[k] for k in range(7))]
print("dividing_triples=%d"%len(bad))
assert bad==[], "w must lie outside J^3"
# (4) w minimal in J^(4): dropping any coordinate breaks an edge constraint
for v in range(7):
    f=list(w); f[v]-=1
    assert any(f[u]+f[x]<4 for u,x in E), v
print("minimality: OK (each coordinate protected by a tight edge)")
# (5) exact alpha(J^(m)) for m<=6 (cap m suffices: some coordinate >m can be lowered)
for m in range(1,7):
    best=min(sum(e) for e in itertools.product(range(m+1),repeat=7)
             if all(e[u]+e[v]>=m for u,v in E))
    print("alpha(J^(%d))=%d"%(m,best))
print("VERIFY_OK")
