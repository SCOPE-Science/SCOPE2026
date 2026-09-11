"""Build the full supersingular 2-isogeny graph at p=1009 over Fp2.
Steps: QNR, Phi_2 mod p (self-tested over ZZ), supersingular seed (trace 0),
vectorized Phi_2 neighbor enumeration over all Fp2, BFS closure, all-pairs BFS,
diameter, eccentricities, histogram, diametral pair + shortest path.
Writes output/artifacts/ledger.json
"""
import json, hashlib, time
from collections import deque
import numpy as np

p = 1009
P2 = p * p

# ---------- classical Phi_2 self-test over integers ----------
# Phi_2(X,Y) = X^3+Y^3-X^2Y^2+1488(X^2Y+XY^2)-162000(X^2+Y^2)
#              +40773375 XY+8748000000(X+Y)-157464000000000
C0 = -157464000000000
def phi2_int(X, Y):
    return (X**3 + Y**3 - X**2*Y**2 + 1488*(X**2*Y + X*Y**2)
            - 162000*(X**2 + Y**2) + 40773375*X*Y
            + 8748000000*(X + Y) + C0)

def phi2_at_X_poly(X):
    # returns [c3,c2,c1,c0] in Y over ZZ
    c3 = 1
    c2 = -X**2 + 1488*X - 162000
    c1 = 1488*X**2 + 40773375*X + 8748000000
    c0 = X**3 - 162000*X**2 + 8748000000*X + C0
    return c3, c2, c1, c0

# self-test 1: Phi_2(0,Y) == (Y-54000)^3
c3, c2, c1, c0 = phi2_at_X_poly(0)
assert (c3, c2, c1, c0) == (1, -162000, 8748000000, -54000**3), (c2, c1, c0)
# self-test 2: Phi_2(1728,Y) == (Y-1728)(Y-287496)^2
c3, c2, c1, c0 = phi2_at_X_poly(1728)
e3, e2, e1, e0 = 1, -(1728 + 2*287496), (2*1728*287496 + 287496**2), -(1728*287496**2)
assert (c3, c2, c1, c0) == (e3, e2, e1, e0), "Phi_2(1728,.) mismatch"
# self-test 3: symmetry on random values
import random
random.seed(7)
for _ in range(20):
    a, b = random.randint(-10**6, 10**6), random.randint(-10**6, 10**6)
    assert phi2_int(a, b) == phi2_int(b, a)
print("Phi_2 self-tests OK (exact integer arithmetic)")

# ---------- field setup ----------
def legendre(a):
    return pow(a % p, (p - 1) // 2, p)

d = next(a for a in range(2, p) if legendre(a) == p - 1)
print("QNR d =", d)
assert legendre(d) == p - 1

# Phi_2 coeffs mod p
C = {
    'x3y0': 1, 'x0y3': 1, 'x2y2': (-1) % p,
    'x2y1': 1488 % p, 'x1y2': 1488 % p,
    'x2y0': (-162000) % p, 'x0y2': (-162000) % p,
    'x1y1': 40773375 % p, 'x1y0': 8748000000 % p,
    'x0y1': 8748000000 % p, 'x0y0': (C0 % p),
}
print("Phi_2 const mod p =", C['x0y0'])

def coeffs_in_Y(j0, j1):
    """Coefficients (c2,c1,c0) of Phi_2(j,Y) with j=(j0,j1) in Fp2. Each returned as (a,b)."""
    a, b = j0 % p, j1 % p
    # j^2 = (a^2+d b^2, 2ab)
    j20 = (a*a + d*b*b) % p
    j21 = (2*a*b) % p
    # c2 = -j^2 + 1488 j - 162000
    m = 1488 % p
    c2 = ((-j20 + m*a - 162000) % p, (-j21 + m*b) % p)
    # c1 = 1488 j^2 + 40773375 j + 8748000000
    k = 40773375 % p
    q = 8748000000 % p
    c1 = ((m*j20 + k*a + q) % p, (m*j21 + k*b) % p)
    # c0 = j^3 - 162000 j^2 + 8748000000 j + C0
    # j^3 = j^2*j
    j30 = (j20*a + d*j21*b) % p
    j31 = (j20*b + j21*a) % p
    n = (-162000) % p
    c0 = ((j30 + n*j20 + q*a + C['x0y0']) % p, (j31 + n*j21 + q*b) % p)
    return c2, c1, c0

def check_coeffs_against_int(j0, j1):
    c2, c1, c0 = coeffs_in_Y(j0, j1)
    # only valid for j in Fp (b=0, small a>=0): compare with integer poly
    _, ec2, ec1, ec0 = phi2_at_X_poly(j0)
    assert c2 == (ec2 % p, 0) and c1 == (ec1 % p, 0) and c0 == (ec0 % p, 0)

for j in [0, 1, 5, 1728 % p, 1008]:
    check_coeffs_against_int(j, 0)
print("mod-p coefficient reduction OK")

# ---------- supersingular seed over Fp: trace 0 <=> #E = p+1 = 1010 ----------
def count_points(a, b):
    tot = 0
    for x in range(p):
        v = (x**3 + a*x + b) % p
        if v == 0:
            continue
        tot += 1 if pow(v, (p-1)//2, p) == 1 else -1
    return p + 1 + tot

seed = None
for a in range(0, 20):
    for b in range(1, 20):
        if (4*a**3 + 27*b**2) % p == 0:
            continue
        if count_points(a, b) == p + 1:
            seed = (a, b)
            break
    if seed:
        break
print("seed curve y^2=x^3+%dx+%d, #E(Fp) = %d" % (seed[0], seed[1], count_points(*seed)))
sa, sb = seed
jnum = (1728 * 4 * sa**3) % p
jden = (4*sa**3 + 27*sb**2) % p
j_seed = (jnum * pow(jden, p-2, p)) % p
print("seed j =", j_seed)

# ---------- vectorized Fp2 root finding ----------
U = np.repeat(np.arange(p, dtype=np.int64), p)   # a-coords of all Fp2 elems
V = np.tile(np.arange(p, dtype=np.int64), p)     # b-coords
d64 = np.int64(d)
P64 = np.int64(p)

def fp2_add2(A0, A1, c):
    return (A0 + c[0]) % P64, (A1 + c[1]) % P64

def fp2_mul2(A0, A1, B0, B1):
    return (A0*B0 + d64*B1*A1) % P64, (A0*B1 + A1*B0) % P64

def neighbors_of(j0, j1):
    """All Y in Fp2 with Phi_2(j,Y)=0. Returns sorted list of (u,v) plus multiplicities info."""
    c2, c1, c0 = coeffs_in_Y(j0, j1)
    Y0, Y1 = U, V
    # Horner: ((Y + c2) Y + c1) Y + c0
    Z0 = (Y0 + c2[0]) % P64
    Z1 = (Y1 + c2[1]) % P64
    Z0, Z1 = fp2_mul2(Z0, Z1, Y0, Y1)
    Z0 = (Z0 + c1[0]) % P64
    Z1 = (Z1 + c1[1]) % P64
    Z0, Z1 = fp2_mul2(Z0, Z1, Y0, Y1)
    Z0 = (Z0 + c0[0]) % P64
    Z1 = (Z1 + c0[1]) % P64
    idx = np.nonzero((Z0 == 0) & (Z1 == 0))[0]
    return [(int(U[i]), int(V[i])) for i in idx]

# sanity: every value occurs with total multiplicity 3 over algebraic closure;
# over Fp2 count distinct roots in {1,2,3}
t0 = time.time()
jn = neighbors_of(j_seed, 0)
t1 = time.time()
print("seed neighbors:", jn, "scan time %.2fs" % (t1-t0))
assert len(jn) >= 1

# ---------- BFS closure ----------
idx_of = {}
verts = []
adj = {}
loops = []
t_start = time.time()
queue = deque()
j0 = (j_seed, 0)
idx_of[j0] = 0
verts.append(j0)
queue.append(j0)
while queue:
    j = queue.popleft()
    ns = neighbors_of(*j)
    nb = []
    for w in ns:
        if w == j:
            loops.append(idx_of[j])
            continue
        if w not in idx_of:
            idx_of[w] = len(verts)
            verts.append(w)
            queue.append(w)
        nb.append(idx_of[w])
    # symmetrization check later; store distinct sorted
    adj[idx_of[j]] = sorted(set(nb))
t_bfs = time.time() - t_start
n = len(verts)
print("vertices:", n, "BFS time %.1fs" % t_bfs)

# symmetry check: Phi_2 symmetric => undirected
for i in range(n):
    for k in adj[i]:
        assert i in adj[k], (i, k)
print("adjacency symmetric OK")

# degree stats (simple-graph degree; multiset degree should be 3 counting multiplicity+loops)
# verify total incident multiplicity: for each vertex, #Fp2-roots counting mult = 3?
# (distinct simple neighbors + loops, with multiplicities from derivative check skipped;
#  record distinct counts)
degs = sorted(len(adj[i]) for i in range(n))
print("simple-degree min/max:", degs[0], degs[-1])
n_loops = len(loops)
print("loops:", n_loops, "at", sorted(set(loops)))

# ---------- all-pairs BFS ----------
def bfs(s):
    dist = [-1]*n
    dist[s] = 0
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for w in adj[u]:
            if dist[w] < 0:
                dist[w] = dist[u] + 1
                dq.append(w)
    return dist

assert all(x >= 0 for x in bfs(0)), "graph disconnected!"
Dmat = [bfs(s) for s in range(n)]
ecc = [max(row) for row in Dmat]
from collections import Counter
hist = sorted(Counter(ecc).items())
D = max(ecc)
print("diameter:", D)
print("ecc histogram:", hist)
diam_pairs = [(i, k) for i in range(n) for k in range(i+1, n) if Dmat[i][k] == D]
print("#diam pairs:", len(diam_pairs), "first:", diam_pairs[0])
ia, ib = diam_pairs[0]

# shortest path ia -> ib
def short_path(a, b):
    dist = [-1]*n
    par = [-1]*n
    dist[a] = 0
    dq = deque([a])
    while dq:
        u = dq.popleft()
        if u == b:
            break
        for w in adj[u]:
            if dist[w] < 0:
                dist[w] = dist[u] + 1
                par[w] = u
                dq.append(w)
    assert dist[b] == D
    path = [b]
    while path[-1] != a:
        path.append(par[path[-1]])
    return path[::-1]

path = short_path(ia, ib)
assert len(path) == D + 1
# verify each link satisfies Phi_2 = 0 mod p (integer check)
for u, w in zip(path[:-1], path[1:]):
    (a0, a1), (b0, b1) = verts[u], verts[w]
    # Phi_2(j_u, j_w): evaluate with Fp2 arithmetic via coeffs
    c2, c1, c0 = coeffs_in_Y(a0, a1)
    # Horner at Y=(b0,b1)
    Z0, Z1 = (b0 + c2[0]) % p, (b1 + c2[1]) % p
    Z0, Z1 = (Z0*b0 + d*Z1*b1) % p, (Z0*b1 + Z1*b0) % p
    Z0, Z1 = (Z0 + c1[0]) % p, (Z1 + c1[1]) % p
    Z0, Z1 = (Z0*b0 + d*Z1*b1) % p, (Z0*b1 + Z1*b0) % p
    Z0, Z1 = (Z0 + c0[0]) % p, (Z1 + c0[1]) % p
    assert (Z0, Z1) == (0, 0), (u, w)
print("diametral path links satisfy Phi_2=0 OK")

ledger = {
    "p": p,
    "fp2": {"basis": "s^2=%d" % d, "d": d},
    "phi2": "X^3+Y^3-X^2Y^2+1488(X^2Y+XY^2)-162000(X^2+Y^2)+40773375XY+8748000000(X+Y)-157464000000000",
    "seed_curve": {"a": sa, "b": sb, "count_fp": p + 1, "j": j_seed},
    "n_vertices": n,
    "vertices": [[a, b] for (a, b) in verts],
    "adjacency": {str(i): adj[i] for i in range(n)},
    "loops": sorted(set(loops)),
    "diameter": D,
    "eccentricities": ecc,
    "ecc_histogram": hist,
    "n_diametral_pairs": len(diam_pairs),
    "diametral_pair": [ia, ib],
    "diametral_jpair": [list(verts[ia]), list(verts[ib])],
    "diametral_path": path,
    "diametral_path_j": [list(verts[i]) for i in path],
}
blob = json.dumps(ledger, sort_keys=True).encode()
ledger["sha256"] = hashlib.sha256(blob).hexdigest()
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-883/output/artifacts/ledger.json", "w") as f:
    json.dump(ledger, f, indent=1)
print("wrote ledger, sha256 =", ledger["sha256"])
print("n =", n, "D =", D, "hist =", hist)
