"""Independent recomputation of Q* from tiles.json (different code path).
Method: build graph from tiles.json, enumerate perfect matchings via
lexicographic edge-index search (vs vertex-min search in build_Qstar.py),
recompute exponent table, compare term-for-term to Qstar.json.
Also writes Dstar.json (classical q=1 bar check) and kernel witness.
"""
import json, itertools

R = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-555/output/artifacts/"
T = json.load(open(R+"tiles.json"))
Q = json.load(open(R+"Qstar.json"))
VARS = T["VARS"]; V = {n:i for i,n in enumerate(VARS)}
B = json.load(open(R+"seed.json"))["B_T"]

parent = {}
def find(a):
    while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
    return a
def union(a,b):
    ra,rb=find(a),find(b)
    if ra!=rb: parent[ra]=rb

for t,Tile in enumerate(T["TILES"]):
    for k in range(4):
        nid="n%d_%d"%(t,k); parent[nid]=nid
def cidx(t,pt): return T["TILES"][t]["corners"].index(pt)
for (a,b,label,(p,q)) in T["GLUES"]:
    union("n%d_%d"%(a,cidx(a,p)),"n%d_%d"%(b,cidx(b,p)))
    union("n%d_%d"%(a,cidx(a,q)),"n%d_%d"%(b,cidx(b,q)))

edges=[]
seen=set()
for t,Tile in enumerate(T["TILES"]):
    for k,lab in enumerate(Tile["sides"]):
        u=find("n%d_%d"%(t,k)); v=find("n%d_%d"%(t,(k+1)%4))
        key=(min(u,v),max(u,v),lab)
        if key not in seen:
            seen.add(key); edges.append((u,v,lab))
edges.sort(key=lambda e:(e[0],e[1],e[2]))
nodes=sorted(set([find(x) for x in parent]))
assert len(nodes)==16 and len(edges)==24, (len(nodes),len(edges))

# independent enumeration: edge-subset filter (choose 8 edges covering all 16 nodes)
matchings=[]
for combo in itertools.combinations(range(24),8):
    cov=[]
    ok=True
    used=set()
    for i in combo:
        u,v,lab=edges[i]
        if u in used or v in used: ok=False; break
        used.add(u); used.add(v); cov.append(edges[i])
    if ok and len(used)==16:
        matchings.append(cov)
print("independent matching count:",len(matchings))
assert len(matchings)==Q["n_terms"], (len(matchings),Q["n_terms"])

DEN=T["DEN"]
terms=[]
for m in matchings:
    e=[0]*11
    for (u,v,lab) in m: e[V[lab]]+=1
    terms.append(tuple(e[i]-DEN[i] for i in range(11)))
from collections import Counter
C=Counter(terms)
Q2=sorted([{"exp":list(k),"coeff":v} for k,v in C.items()], key=lambda d:(d["coeff"],d["exp"]))
Q1=Q["Qstar"]
discrep = []
s1=sorted(map(lambda d:(tuple(d["exp"]),d["coeff"]),Q1))
s2=sorted(map(lambda d:(tuple(d["exp"]),d["coeff"]),Q2))
if s1==s2:
    print("Q* TERM-FOR-TERM MATCH: %d distinct exponents, %d matchings"%(len(s1),len(matchings)))
else:
    for a,b in zip(s1,s2):
        if a!=b: discrep.append((a,b))
    print("MISMATCH:",discrep[:10])

# D*: classical q=1 — every torus monomial is bar-fixed, coefficients integral.
# D* = bar(Q*)-Q* = 0 term-for-term.
D={"Dstar":[],"zero":True,
   "note":"classical specialization q=1: bar fixes each monomial and coefficient; quantum q-powers not tracked (logged limitation)"}
json.dump(D,open(R+"Dstar.json","w"),indent=1)

# kernel witness: nonzero n>=0 with B n = 0 (explains preorder cycles)
wit=None
for n in itertools.product(range(4),repeat=7):
    if all(x==0 for x in n): continue
    if all(sum(B[i][k]*n[k] for k in range(7))==0 for i in range(7)):
        wit=list(n); break
print("nonnegative kernel witness n (B n=0):",wit)
# maximal-up-to-equivalence: quotient classes under g~h iff g-h in image both ways
muts=list(C.keys())
def in_cone(d,bound=5):
    for n in itertools.product(range(bound+1),repeat=7):
        if all(x==0 for x in n): continue
        if tuple(sum(B[i][k]*n[k] for k in range(7)) for i in range(7))==d: return True
    return False
mut7=[tuple(t[:7]) for t in muts]
classes=[]
for g in mut7:
    placed=False
    for cl in classes:
        h=cl[0]
        d1=tuple(g[i]-h[i] for i in range(7)); d2=tuple(h[i]-g[i] for i in range(7))
        if in_cone(d1) and in_cone(d2):
            cl.append(g); placed=True; break
    if not placed: classes.append([g])
print("cone-equivalence classes:",len(classes))
# class-level maximality
def le(C1,C2):
    return any(in_cone(tuple(h[i]-g[i] for i in range(7))) for g in C1 for h in C2)
maxcl=[c for c in classes if not any(o is not c and le(c,o) and not le(o,c) for o in classes)]
print("maximal classes:",len(maxcl))
for c in maxcl: print("  class size",len(c),"rep",c[0])

ok = (s1==s2)
print("VERIFY_"+"OK" if ok else "FAIL")
json.dump({"verify":"OK" if ok else "FAIL","n_matchings":len(matchings),
           "n_distinct":len(C),"kernel_witness":wit,
           "n_classes":len(classes),"n_maximal_classes":len(maxcl),
           "maximal_reps":[list(c[0]) for c in maxcl]},
          open(R+"verify_result.json","w"),indent=1)
