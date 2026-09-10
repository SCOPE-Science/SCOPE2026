"""Independent replay checker for lane-500 seed Q0 (stdlib only). Verifies:
 G0 group axioms (2^20 assoc via tables), center/derived, delta B3+B4, mu A1-A3,
 loop Latin, Inn-abelian (distinct-perm pairwise commute), center/quotient/class-3 witness,
 Inn orders/group order. Prints VERIFY_OK on success."""
import json, time, collections
t0=time.time(); N=128
G=json.load(open("output/artifacts/group_table.json"))["MUL"]
S=json.load(open("output/artifacts/loop_table.json"))["ST"]
seed=json.load(open("output/artifacts/seed_Q0.json"))
def ua(i): return i&7
def ca(i): return (i>>3)&15
# 1 group axioms
assert all(G[0][b]==b and G[a][0]==a for a in range(N) for b in range(N)), "identity"
INV=[None]*N
for a in range(N):
    for b in range(N):
        if G[a][b]==0 and G[b][a]==0: INV[a]=b; break
assert all(v is not None for v in INV), "inverses"
for a in range(N):
    Ga=G[a]
    for b in range(N):
        ab=G[a][b]; Gab=G[ab]; Gb=G[b]
        for c in range(N):
            assert Gab[c]==Ga[Gb[c]], f"assoc {a},{b},{c}"
print("group OK")
def comm(a,b): return G[G[G[INV[a]][INV[b]]][a]][b]
def conj(z,w): return G[G[INV[w]][z]][w]
DER=sorted(set(comm(a,b) for a in range(N) for b in range(N)))
Z=[a for a in range(N) if all(G[a][b]==G[b][a] for b in range(N))]
assert DER==seed["derived"] and Z==seed["M_center"], "center/derived"
print("center/derived OK", len(DER), len(Z))
# 2 delta from seed D matrix
D=seed["D_matrix"]
def dM(m,u):
    m3=ca(m)&7; r=0
    for i in range(3):
        for j in range(3):
            if D[i][j] and (m3>>i)&1 and (u>>j)&1: r^=1
    return r
def db(a,b): return dM(a,ua(b))^dM(b,ua(a))
Gprime={a for a in range(N) if ua(a)==0 and (ca(a)&8)==0}
for x in range(N):
    for y in range(N):
        for z in range(N):
            if x in Gprime or y in Gprime or z in Gprime:
                assert db(G[x][y],z)==db(x,z)^db(y,z), "B3"
print("B3 OK")
for x in range(N):
    for y in range(N):
        for z in range(N):
            l=conj(conj(z,y),x)^(db(comm(z,y),x)<<6)
            r=conj(conj(z,x),y)^(db(comm(z,x),y)<<6)
            assert l==r, f"B4 {x},{y},{z}"
print("B4 OK")
c12=comm(1,2); c23=comm(2,4)
assert (db(c12,4)^db(c23,1)^db(comm(4,1),2))==1, "g witness"
print("g-nontrivial OK")
# 3 mu
def mu(a,b): return dM(a,ua(b))
for x in range(N):
    for y in range(N):
        assert (mu(x,y)^mu(y,x))==db(x,y), "A1"
Mset={a for a in range(N) if ua(a)==0}
for x in range(N):
    for y in range(N):
        for z in range(N):
            if x in Mset or y in Mset or z in Mset:
                assert mu(G[x][y],z)==(mu(x,z)^mu(y,z)), "A2"
                assert mu(x,G[y][z])==(mu(x,y)^mu(x,z)), "A3"
print("mu A1-A3 OK")
# 4 loop = group twisted by mu?
for a in range(N):
    for b in range(N):
        assert S[a][b]==(G[a][b]^(mu(a,b)<<6)), "loop table"
assert all(S[0][b]==b and S[a][0]==a for a in range(N) for b in range(N))
for a in range(N):
    assert sorted(S[a])==list(range(N)) and sorted(S[x][a] for x in range(N))==list(range(N))
print("loop Latin OK")
# 5 Inn replay
def comp(p,q): return [p[q[i]] for i in range(N)]
def invp(p):
    q=[0]*N
    for i,v in enumerate(p): q[v]=i
    return q
Lx=[[S[x][y] for y in range(N)] for x in range(N)]
Rx=[[S[y][x] for y in range(N)] for x in range(N)]
gens=[]
for x in range(N):
    for y in range(N):
        gens.append(comp(invp(Lx[S[x][y]]),comp(Lx[x],Lx[y])))
        gens.append(comp(invp(Rx[S[x][y]]),comp(Rx[y],Rx[x])))
for x in range(N): gens.append(comp(invp(Rx[x]),Lx[x]))
assert all(g[0]==0 for g in gens)
U=list({tuple(g):g for g in gens}.values())
assert len(U)==64, f"distinct {len(U)}"
for i in range(len(U)):
    for j in range(i+1,len(U)):
        a,b=U[i],U[j]
        for v in range(N):
            assert a[b[v]]==b[a[v]], "Inn noncommute"
print("Inn abelian OK (64 distinct)")
# 6 class 3
ZQ=[z for z in range(N) if all(g[z]==z for g in U)]
assert ZQ==[0,64], f"Z(Q) {ZQ}"
def can(a): return a&~64
reps=[a for a in range(N) if not (a&64)]
def qm(a,b): return can(S[a][b])
assert any(qm(a,b)!=qm(b,a) for a in reps for b in reps), "quotient abelian?"
Z2=[a for a in reps if all(qm(a,b)==qm(b,a) for b in reps)]
assert len(Z2)==8, f"Z2 {len(Z2)}"
x,y,z,w0,w1=seed["assoc_witness"]
assert S[S[x][y]][z]==w0 and S[x][S[y][z]]==w1 and w0!=w1
print("class-3 OK: |Z|=2, Q/Z nonabelian, |Z2/Z|=8, assoc witness", seed["assoc_witness"])
# 7 Inn orders + group order
def porder(p):
    cur=list(p); k=1
    while not all(c==i for i,c in enumerate(cur)): cur=comp(p,cur); k+=1; assert k<=4
    return k
from collections import Counter
print("Inn orders:", dict(Counter(porder(g) for g in U)))
seen={tuple(range(N))}; q=collections.deque([list(range(N))])
while q:
    a=q.popleft()
    for b in U:
        d=tuple(comp(a,b))
        if d not in seen: seen.add(d); q.append(list(d))
assert len(seen)==64
print("Inn group order 64 OK")
print("VERIFY_OK", round(time.time()-t0,1), "s")
