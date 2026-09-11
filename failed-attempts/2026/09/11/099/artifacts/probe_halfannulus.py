"""Bounded recovery probe for lane-963.

Monte-Carlo probe of radial arm-connection probabilities in half-annulus
H(1,R) on mesh-1 triangular lattice (axial coords), p=1/2, upper half-plane.
Events (via union-find):
  O   = open connects inner ring to outer ring
  C   = closed connects inner ring to outer ring
  O&C = two-arm proxy (a RIGOROUS upper bound on any alternating O-C-O
        three-arm event, since 3-arm implies both O and C).
Purpose: calibrate the scale of B(1,R) and show the constant-scale
uncertainty that blocks audit-grade certification. NOT a proof.
"""
import math, random, sys

SQ3 = math.sqrt(3.0)
# triangular lattice neighbors in axial (q, r)
NBR = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))

def build(R, d_in=2.0, d_out=1.0):
    sites, index = [], {}
    r = 0
    while True:
        y = SQ3 / 2 * r
        if y > R:
            break
        # |x| bound from x^2+y^2<=R^2
        xmax = math.sqrt(max(R * R - y * y, 0.0))
        # x = q + r/2  => q in [-xmax - r/2, xmax - r/2]
        qlo = int(math.ceil(-xmax - r / 2)) - 1
        qhi = int(math.floor(xmax - r / 2)) + 1
        for q in range(qlo, qhi + 1):
            x = q + r / 2
            d = math.hypot(x, y)
            if d <= R:
                index[(q, r)] = len(sites)
                sites.append((x, y, d))
        r += 1
    inner = [i for i, s in enumerate(sites) if s[2] <= d_in]
    outer = [i for i, s in enumerate(sites) if s[2] >= R - d_out]
    adj = []
    for (q, r), i in index.items():
        nb = []
        for dq, dr in NBR:
            j = index.get((q + dq, r + dr))
            if j is not None and r + dr >= 0:
                nb.append(j)
        adj.append(nb)
    return sites, inner, outer, adj

def trial(n, inner_set, outer_set, adj, rng):
    parent = list(range(n))
    parent_c = list(range(n))
    def find(p, a):
        while p[a] != a:
            p[a] = p[p[a]]
            a = p[a]
        return a
    def union(p, a, b):
        ra, rb = find(p, a), find(p, b)
        if ra != rb:
            p[ra] = rb
    open_site = [rng.random() < 0.5 for _ in range(n)]
    for i in range(n):
        for j in adj[i]:
            if j > i and open_site[i] == open_site[j]:
                union(parent if open_site[i] else parent_c, i, j)
    in_roots_o = {find(parent, i) for i in inner_set if open_site[i]}
    out_o = any(find(parent, j) == r for j in outer_set if open_site[j] for r in in_roots_o)
    in_roots_c = {find(parent_c, i) for i in inner_set if not open_site[i]}
    out_c = any(find(parent_c, j) == r for j in outer_set if not open_site[j] for r in in_roots_c)
    return out_o, out_c

def run(R, nsamples, seed):
    rng = random.Random(seed)
    sites, inner, outer, adj = build(R)
    n = len(sites)
    no = nc = nb = 0
    for _ in range(nsamples):
        o, c = trial(n, inner, outer, adj, rng)
        no += o
        nc += c
        nb += (o and c)
    return n, no / nsamples, nc / nsamples, nb / nsamples

if __name__ == "__main__":
    for R, ns, seed in ((6, 60000, 11), (10, 40000, 22), (16, 15000, 33)):
        n, po, pc, pb = run(R, ns, seed)
        lo = 0.001 * R ** -2.05
        hi = 0.5 * R ** -1.95
        print(f"R={R} nsites={n} nsamples={ns}: P(O)={po:.4f} P(C)={pc:.4f} "
              f"P(O&C proxy, upper bnd on 3-arm)={pb:.5f}  window@R=[{lo:.2e},{hi:.2e}]",
              flush=True)
    print("extrapolation: proxy is an UPPER bound on B(1,R); "
          "B(1,R)*R^2 scale vs allowed [8e-4*R^-0.05*1e0 ... ] see worklog",
          flush=True)
