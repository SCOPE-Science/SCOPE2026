"""Fix standard Mycielski adjacency lists M3, M4, M5; verify invariants exactly (stdlib only)."""
import json, itertools

def mycielski(adj):
    n = len(adj)
    # vertices 0..n-1 original V; n..2n-1 shadows U; 2n apex z
    N = 2*n+1
    nadj = [set() for _ in range(N)]
    for i in range(n):
        for j in adj[i]:
            if j > i:
                nadj[i].add(j); nadj[j].add(i)
    for i in range(n):
        for j in adj[i]:
            nadj[n+i].add(j)  # u_i adjacent to neighbors of v_i
            # (symmetric edge added when processing? need both sides)
        # note: neighbors j are in V
    for i in range(n):
        for j in list(nadj[n+i]):
            nadj[j].add(n+i)
    z = 2*n
    for i in range(n):
        nadj[z].add(n+i); nadj[n+i].add(z)
    return nadj

def canonical_m3():
    # C5
    n=5
    adj=[set() for _ in range(n)]
    for i in range(n):
        j=(i+1)%n
        adj[i].add(j); adj[j].add(i)
    return adj

def edge_list(adj):
    es=[]
    for i in range(len(adj)):
        for j in adj[i]:
            if j>i: es.append([i,j])
    return sorted(es)

def has_triangle(adj):
    n=len(adj)
    for i in range(n):
        for j in adj[i]:
            if j>i:
                if adj[i]&adj[j]: return True
    return False

def k_colorable(adj, k):
    n=len(adj)
    order=sorted(range(n), key=lambda x:-len(adj[x]))
    col=[-1]*n
    # backtracking with forward check
    def bt(idx):
        if idx==n: return True
        v=order[idx]
        used={col[u] for u in adj[v] if col[u]!=-1}
        for c in range(k):
            if c not in used:
                col[v]=c
                if bt(idx+1): return True
                col[v]=-1
        return False
    return bt(0)

def chi_info(adj, name):
    print(f"--- {name}: n={len(adj)}, m={sum(map(len,adj))//2}")
    print(f"  triangle-free: {not has_triangle(adj)}")

M3=canonical_m3()
M4=mycielski(M3)
M5=mycielski(M4)
for G,nm in [(M3,"M3"),(M4,"M4"),(M5,"M5")]:
    chi_info(G,nm)

# colorability (exact backtracking)
print("M3 3-colorable?", k_colorable(M3,3), " 2-colorable?", k_colorable(M3,2))
print("M4 3-colorable?", k_colorable(M4,3))
print("M4 4-colorable?", k_colorable(M4,4))
# M5 4-colorability: 23 vertices backtracking may be heavy; use symmetry + pruning
print("M5 4-colorable? (search...)", k_colorable(M5,4))
print("M5 5-colorable?", k_colorable(M5,5))

# Verify M4 induced in M5 (first 11 vertices)
def induced(adj, S):
    S=set(S)
    return {i:{j for j in adj[i] if j in S} for i in S}
S=list(range(len(M4)))
ok=all(set(M4[i])=={j for j in M5[i] if j in set(S)} for i in S)
print("M4 induced in M5 (first 11 verts)?", ok)
# degrees
print("M4 degrees:", sorted(map(len,M4)))
print("M5 degrees:", sorted(map(len,M5)))

# archive
arch={"M3":{"n":len(M3),"edges":edge_list(M3)},
      "M4":{"n":len(M4),"edges":edge_list(M4)},
      "M5":{"n":len(M5),"edges":edge_list(M5)}}
with open("output/artifacts/mycielski_adj.json","w") as f:
    json.dump(arch,f,indent=1)
print("archived output/artifacts/mycielski_adj.json")
