"""Shared stdlib-only tools: C4 checks, KST bound, ER_q polarity graphs."""
import itertools, math

def adj_from_edges(n, edges):
    adj = [0]*n
    for u,v in edges:
        adj[u] |= 1<<v; adj[v] |= 1<<u
    return adj

def is_c4_free_mask(n, adj):
    for u in range(n):
        for v in range(u+1, n):
            if bin(adj[u] & adj[v]).count('1') >= 2:
                return False
    return True

def is_c4_free(n, edges):
    return is_c4_free_mask(n, adj_from_edges(n, edges))

def kst_floor(n):
    return math.floor(n/4*(1+math.sqrt(4*n-3)) + 1e-9)

def pair_log(n, edges):
    """KST pair-count certificate data: sum_v C(d,2) <= C(n,2)."""
    deg = [0]*n
    for u,v in edges:
        deg[u]+=1; deg[v]+=1
    s = sum(d*(d-1)//2 for d in deg)
    return deg, s, n*(n-1)//2

# ---- ER_q orthogonal polarity graph (q prime) ----
def er_q(q):
    pts = []
    seen = set()
    for x in itertools.product(range(q), repeat=3):
        if x == (0,0,0): continue
        # normalize: first nonzero coord = 1
        l = next(c for c in x if c != 0)
        inv = pow(l, -1, q)
        key = tuple((c*inv) % q for c in x)
        if key not in seen:
            seen.add(key); pts.append(key)
    n = len(pts)
    assert n == q*q+q+1, (q, n)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if sum(a*b for a,b in zip(pts[i],pts[j])) % q == 0:
                edges.append((i,j))
    return n, edges
