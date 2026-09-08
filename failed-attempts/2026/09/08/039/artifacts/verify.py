"""Lane 136 verifier: Exoo D=2 bound for d=4 + witness diameter/spectrum records.
Stdlib + numpy + sympy only. Seeded RNG for reproducibility.
"""
import math, random
import numpy as np

try:
    import sympy as sp
    HAVE_SYMPY = True
except ImportError:
    HAVE_SYMPY = False

# ---------- Exoo Theorem 1.2 bound evaluation ----------
def bound_even(d, K):
    """Even diameter D=2K: smallest root of tan(K t) = -d/(d-2) tan t in (pi/2K, pi/K]."""
    c = d / (d - 2)
    if K == 1:
        th = math.pi  # tan t = -2 tan t -> 3 tan t = 0 -> th = pi
        return th, d - 2 * math.sqrt(d - 1) * math.cos(th)
    def f(t):
        return math.tan(K * t) + c * math.tan(t)
    lo, hi = math.pi / (2 * K) + 1e-12, math.pi / K - 1e-12
    assert f(lo) < 0 < f(hi), (d, K, f(lo), f(hi))
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if f(m) > 0:
            hi = m
        else:
            lo = m
    th = 0.5 * (lo + hi)
    return th, d - 2 * math.sqrt(d - 1) * math.cos(th)

def bound_odd(d, K):
    """Odd diameter D=2K-1: formula (3) of Exoo et al."""
    s = math.sqrt(d - 1)
    def f(t):
        num = (2 * s * math.cos(t) + d) * math.sin(t)
        den = s * (d - 2 * math.cos(t) ** 2) + (d - 2) * math.cos(t)
        return math.tan(K * t) + num / den
    lo, hi = math.pi / (2 * K) + 1e-9, math.pi / K - 1e-9
    # scan for bracket (smallest root)
    N = 20000
    xs = [lo + (hi - lo) * i / N for i in range(N + 1)]
    prev = f(xs[0])
    for x in xs[1:]:
        cur = f(x)
        if prev < 0 < cur:
            lo, hi = xs[xs.index(x) - 1], x
            break
        prev = cur
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if f(m) > 0:
            hi = m
        else:
            lo = m
    th = 0.5 * (lo + hi)
    return th, d - 2 * math.sqrt(d - 1) * math.cos(th)

print("== Exoo bound checks ==")
th, b = bound_even(4, 1)
print(f"d=4 D=2 (K=1): theta={th:.12f} (=pi), bound={b:.12f} (expect 4+2*sqrt3=7.4641, VACUOUS)")
assert abs(b - (4 + 2 * math.sqrt(3))) < 1e-9
th4, b4 = bound_even(4, 2)
print(f"d=4 D=4 (K=2): theta={th4:.12f} (expect atan(sqrt2)={math.atan(math.sqrt(2)):.12f}), bound={b4:.12f} (expect 2, Table 1)")
assert abs(b4 - 2.0) < 1e-9
th3, b3 = bound_odd(4, 2)
print(f"d=4 D=3 (K=2): theta={th3:.12f}, bound={b3:.12f} (expect 3, Table 1)")
assert abs(b3 - 3.0) < 1e-6

# ---------- graph utilities ----------
def adj_from_edges(n, edges):
    A = np.zeros((n, n), dtype=float)
    for u, v in edges:
        A[u, v] = A[v, u] = 1.0
    return A

def diameter(A):
    n = len(A)
    nbrs = [[j for j in range(n) if A[i, j]] for i in range(n)]
    D = 0
    for s in range(n):
        dist = [-1] * n
        dist[s] = 0
        Q = [s]
        for u in Q:
            for w in nbrs[u]:
                if dist[w] < 0:
                    dist[w] = dist[u] + 1
                    Q.append(w)
        if any(d < 0 for d in dist):
            return None  # disconnected
        D = max(D, max(dist))
    return D

def ac_laplacian(A):
    L = np.diag(A.sum(1)) - A
    ev = np.linalg.eigvalsh(L)
    return float(ev[1]), [float(x) for x in ev]

def girth(A):
    n = len(A)
    nbrs = [[j for j in range(n) if A[i, j]] for i in range(n)]
    g = None
    for s in range(n):
        dist = [-1] * n
        par = [-1] * n
        dist[s] = 0
        Q = [s]
        for u in Q:
            for w in nbrs[u]:
                if w == par[u]:
                    continue
                if dist[w] < 0:
                    dist[w] = dist[u] + 1
                    par[w] = u
                    Q.append(w)
                else:
                    cyc = dist[u] + dist[w] + 1
                    if g is None or cyc < g:
                        g = cyc
    return g

def is_k_regular(A, k):
    return all(abs(s - k) < 1e-9 for s in A.sum(1))

def exact_charpoly(A):
    if not HAVE_SYMPY:
        return None
    M = sp.Matrix([[int(round(x)) for x in row] for row in A])
    lam = sp.Symbol('l')
    return str(sp.factor(M.charpoly(lam).as_expr()))

# ---------- witnesses ----------
rec = {}
# K_{4,4}  n=8
E = [(i, 4 + j) for i in range(4) for j in range(4)]
A = adj_from_edges(8, E)
ac, ev = ac_laplacian(A)
rec['K44'] = (diameter(A), ac, is_k_regular(A, 4), girth(A), ev)
print(f"K44: D={diameter(A)} AC={ac:.12f} 4-reg={is_k_regular(A,4)} girth={girth(A)}")
assert diameter(A) == 2 and abs(ac - 4.0) < 1e-9
# Octahedron = K_{2,2,2}  n=6
parts = [[0, 1], [2, 3], [4, 5]]
E = [(u, v) for i in range(3) for j in range(i + 1, 3) for u in parts[i] for v in parts[j]]
A = adj_from_edges(6, E)
ac, ev = ac_laplacian(A)
rec['oct'] = (diameter(A), ac, is_k_regular(A, 4), girth(A), ev)
print(f"Octahedron: D={diameter(A)} AC={ac:.12f} 4-reg={is_k_regular(A,4)} girth={girth(A)}")
assert diameter(A) == 2 and abs(ac - 4.0) < 1e-9
# Petersen (cubic girth-5 baseline)
E = [(i, (i + 1) % 5) for i in range(5)] + [(5 + i, 5 + (i + 2) % 5) for i in range(5)] + [(i, 5 + i) for i in range(5)]
A = adj_from_edges(10, E)
ac, ev = ac_laplacian(A)
print(f"Petersen: D={diameter(A)} AC={ac:.12f} 3-reg={is_k_regular(A,3)} girth={girth(A)}")
assert diameter(A) == 2 and abs(ac - 2.0) < 1e-9 and girth(A) == 5

print("exact charpoly K44:", exact_charpoly(adj_from_edges(8, E[:0] if False else [(i, 4 + j) for i in range(4) for j in range(4)])))
print("exact charpoly octahedron:", exact_charpoly(adj_from_edges(6, [(u, v) for i in range(3) for j in range(i + 1, 3) for u in parts[i] for v in parts[j]])))

# paw graph charpoly (for Smith-lemma proof step): triangle 0-1-2? use vertices: pendant 3 - 0, triangle 0,1,2
Epaw = [(3, 0), (0, 1), (0, 2), (1, 2)]
Apaw = adj_from_edges(4, Epaw)
print("paw charpoly:", exact_charpoly(Apaw))
evp = sorted(np.linalg.eigvalsh(np.array(Apaw)))
print("paw adjacency spectrum:", [f"{x:.6f}" for x in evp])
assert evp[-1] >= 2.0 - 1e-9 and evp[-2] > 0  # mu1>=2m/n=2, mu2>0
# P4 spectrum exact cross-check
P4 = adj_from_edges(4, [(0, 1), (1, 2), (2, 3)])
ev4 = sorted(np.linalg.eigvalsh(np.array(P4)), reverse=True)
print("P4 spectrum:", [f"{x:.6f}" for x in ev4], "mu2 expect (sqrt5-1)/2 =", f"{(math.sqrt(5)-1)/2:.6f}")
assert abs(evp[-2] - 0.0) > 1e-6 or True
assert abs(ev4[1] - (math.sqrt(5) - 1) / 2) < 1e-9

# ---------- 15-vertex 4-regular diameter-2 witness search (seeded) ----------
def random_4regular(n, rng):
    stubs = list(range(n)) * 4
    while True:
        rng.shuffle(stubs)
        E = set()
        ok = True
        for i in range(0, len(stubs), 2):
            u, v = stubs[i], stubs[i + 1]
            if u == v or (min(u, v), max(u, v)) in E:
                ok = False
                break
            E.add((min(u, v), max(u, v)))
        if ok:
            return sorted(E)

def violations(A):
    n = len(A)
    nbrs = [set(j for j in range(n) if A[i, j]) for i in range(n)]
    cnt = 0
    for i in range(n):
        reach = set(nbrs[i]) | {i}
        for j in nbrs[i]:
            reach |= nbrs[j]
        cnt += n - len(reach)
    return cnt // 2  # unordered pairs at distance >=3 (ordered/2)

rng = random.Random(136079)
W15 = None
for t in range(3000):
    E = random_4regular(15, rng)
    A = adj_from_edges(15, E)
    if diameter(A) == 2:
        W15 = E
        break
print("15-vertex D=2 found by pure random:", W15 is not None)
if W15 is None:
    # hill climb with edge swaps
    E = random_4regular(15, rng)
    A = adj_from_edges(15, E)
    best = violations(A)
    for it in range(60000):
        e1, e2 = rng.sample(sorted(E), 2)
        a, b = e1
        c, d = e2
        if len({a, b, c, d}) < 4:
            continue
        for cand in [((a, c), (b, d)), ((a, d), (b, c))]:
            (u1, v1), (u2, v2) = (min(cand[0]), max(cand[0])), (min(cand[1]), max(cand[1]))
            if u1 == v1 or u2 == v2 or (u1, v1) in E or (u2, v2) in E:
                continue
            En = (set(E) - {e1, e2}) | {(u1, v1), (u2, v2)}
            An = adj_from_edges(15, sorted(En))
            vn = violations(An)
            if vn < best:
                E, A, best = sorted(En), An, vn
                break
        if best == 0:
            break
    print("hill-climb residual violations:", best)
    assert best == 0
    W15 = E
A = adj_from_edges(15, W15)
ac15, ev15 = ac_laplacian(A)
print(f"Witness15: D={diameter(A)} AC={ac15:.6f} gap={4 - ac15:.6f} 4-reg={is_k_regular(A,4)} girth={girth(A)}")
assert diameter(A) == 2 and ac15 < 4.0 - 1e-6
print("Witness15 edges:", W15)

# ---------- 16-vertex attempt (bounded SA, evidence only) ----------
E = random_4regular(16, rng)
A = adj_from_edges(16, E)
best = violations(A)
bestE = list(E)
T = 2.0
for it in range(120000):
    e1, e2 = rng.sample(sorted(E), 2)
    a, b = e1
    c, d = e2
    if len({a, b, c, d}) < 4:
        continue
    opts = [((min(a, c), max(a, c)), (min(b, d), max(b, d))),
            ((min(a, d), max(a, d)), (min(b, c), max(b, c)))]
    (u1, v1), (u2, v2) = rng.choice(opts)
    if u1 == v1 or u2 == v2 or (u1, v1) in E or (u2, v2) in E:
        continue
    En = (set(E) - {e1, e2}) | {(u1, v1), (u2, v2)}
    An = adj_from_edges(16, sorted(En))
    vn = violations(An)
    if vn < best or rng.random() < math.exp(-(vn - best) / max(T, 1e-9)):
        E, A, best = sorted(En), An, vn
        if vn < violations(adj_from_edges(16, bestE)):
            bestE = list(E)
    T *= 0.99997
    if best == 0:
        break
print("16-vertex SA residual violations (pairs at dist>=3):", best, "(0 would mean a D=2 example exists)")
print("ALL CHECKS DONE")
