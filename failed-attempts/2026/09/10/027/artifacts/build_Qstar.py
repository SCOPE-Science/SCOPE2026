"""Lane 555 fallback: band-graph snake expansion Q* for L0 + D* + checks.
Stdlib only. Tile/quadrilateral data derived from logged triangulation;
gluings forced by endpoint matching. Classical specialization q=1.
Writes tiles.json, Qstar.json, matchings.log.
"""
import json, itertools

VARS = ["a1","b1","b2","b3","c1","c2","c3","f1","f2","f3","f4"]
V = {n:i for i,n in enumerate(VARS)}
# tiles: corners cyclic, sides cyclic labels, diagonal (name, endpoints)
TILES = [
 {"corners":["m1","p1","m3","p2"], "sides":["b1","b3","c2","c1"], "diag":"a1"},
 {"corners":["m2","m1","m3","p1"], "sides":["f1","a1","b3","b2"], "diag":"b1"},
 {"corners":["m1","m2","m3","p1"], "sides":["f1","f2","b3","b1"], "diag":"b2"},
 {"corners":["m2","m3","m1","p1"], "sides":["f2","a1","b1","b2"], "diag":"b3"},
 {"corners":["p1","m1","p2","m3"], "sides":["b1","c1","c2","b3"], "diag":"a1"},
 {"corners":["m1","m3","m4","p2"], "sides":["a1","f3","c3","c1"], "diag":"c2"},
 {"corners":["m3","m4","m1","p2"], "sides":["f3","f4","c1","c2"], "diag":"c3"},
 {"corners":["m4","m1","m3","p2"], "sides":["f4","a1","c2","c3"], "diag":"c1"},
]
# glues: (tileA, tileB, edgelabel, endpoints(surface points))
GLUES = [
 (0,1,"b3",("p1","m3")), (1,2,"f1",("m2","m1")), (2,3,"f2",("m2","m3")),
 (3,4,"b1",("m1","p1")), (4,5,"c1",("m1","p2")), (5,6,"f3",("m3","m4")),
 (6,7,"f4",("m4","m1")), (7,0,"c2",("m3","p2")),
]
XSEQ = ["a1","b1","b2","b3","a1","c2","c3","c1"]  # crossed arcs per tile

parent = {}
def find(a):
    while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
    return a
def union(a,b):
    ra,rb=find(a),find(b)
    if ra!=rb: parent[ra]=rb

# corner node ids
cid = {}
for t,T in enumerate(TILES):
    for k,p in enumerate(T["corners"]):
        cid[(t,k)]="n%d_%d"%(t,k)
        parent[cid[(t,k)]]=cid[(t,k)]

def corner_index(t,pt): return TILES[t]["corners"].index(pt)
for (a,b,label,(p,q)) in GLUES:
    union(cid[(a,corner_index(a,p))], cid[(b,corner_index(b,p))])
    union(cid[(a,corner_index(a,q))], cid[(b,corner_index(b,q))])

# edges: per tile, side k connects corners k,k+1 mod 4
edges = {}  # (repU,repV,label) dedup; keep label
for t,T in enumerate(TILES):
    for k,lab in enumerate(T["sides"]):
        u=find(cid[(t,k)]); v=find(cid[(t,(k+1)%4)])
        key=tuple(sorted([u,v])+[lab])
        edges[key]=lab
E=list(edges.keys())
nodes=sorted(set([find(x) for x in parent]))
print("supernodes:",len(nodes),"edges:",len(E))
assert len(nodes)==16, len(nodes)
assert len(E)==24, len(E)

# adjacency
adj={n:[] for n in nodes}
for (u,v,lab) in E:
    adj[u].append((v,lab)); adj[v].append((u,lab))

# enumerate perfect matchings (recursive backtracking)
matchings=[]
def backtrack(free, chosen):
    if not free:
        matchings.append(list(chosen)); return
    u=min(free, key=lambda n: len([w for w in adj[n] if w[0] in free]))
    nbrs=[(w,lab) for (w,lab) in adj[u] if w in free]
    if not nbrs: return
    for (w,lab) in nbrs:
        free2=set(free); free2.discard(u); free2.discard(w)
        chosen.append((u,w,lab))
        backtrack(free2, chosen)
        chosen.pop()
backtrack(set(nodes), [])
print("perfect matchings:",len(matchings))

DEN=[0]*11
for d in XSEQ: DEN[V[d]]+=1
print("denominator:",dict(zip(VARS,DEN)))

terms=[]
for m in matchings:
    e=[0]*11
    for (u,w,lab) in m: e[V[lab]]+=1
    t=[e[i]-DEN[i] for i in range(11)]
    terms.append(t)

# group identical exponent vectors (coefficients)
from collections import Counter
C=Counter(tuple(t) for t in terms)
print("distinct exponent vectors:",len(C))
Q=sorted([{"exp":list(k),"coeff":v} for k,v in C.items()], key=lambda d:(d["coeff"],d["exp"]))
for d in Q: print(d["coeff"], d["exp"])

json.dump({"VARS":VARS,"TILES":TILES,"GLUES":GLUES,"XSEQ":XSEQ,"DEN":DEN},
          open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-555/output/artifacts/tiles.json","w"),indent=1)
json.dump({"Qstar":Q,"n_terms":len(matchings),"n_distinct":len(C),"denominator":DEN},
          open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-555/output/artifacts/Qstar.json","w"),indent=1)
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-555/output/artifacts/matchings.log","w") as f:
    for i,m in enumerate(matchings):
        f.write("P%d: %s -> exp %s\n"%(i,sorted([lab for (_,_,lab) in m]),terms[i]))
print("wrote tiles.json Qstar.json matchings.log")

# dominance pointedness on mutable part (B_T from seed.json)
B=json.load(open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-555/output/artifacts/seed.json"))["B_T"]
MUTS=7
def minus(a,b): return tuple(a[i]-b[i] for i in range(MUTS))
def in_cone(d, bound=4):
    # is d = B n for some n in N^7 with entries<=bound?
    sols=[]
    for n in itertools.product(range(bound+1),repeat=MUTS):
        if all(x==0 for x in n): continue
        if tuple(sum(B[i][k]*n[k] for k in range(MUTS)) for i in range(MUTS))==d:
            sols.append(n)
    return sols
muts=[tuple(t[:MUTS]) for t in C.keys()]
maximal=[]
for g in muts:
    if not any(h!=g and in_cone(tuple(h[i]-g[i] for i in range(MUTS))) for h in muts):
        maximal.append(g)
print("dominance-maximal mutable degrees:",maximal)
print("pointed:", len(maximal)==1)
