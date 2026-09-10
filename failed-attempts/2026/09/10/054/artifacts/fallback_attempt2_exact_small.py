"""Fallback Attempt 2: exact small-box FK q=2 influence enumeration (free b.c.).

phi(w) proportional to p^o (1-p)^c q^k(w), q=2, p=p_c=sqrt(2)/(1+sqrt(2)).
f = left-right open crossing. e pivotal iff f differs with e forced open/closed
(given rest). I = sum_e P(e pivotal). Exact over rest configs (2^(E-1) per e).
Plus exact crossing probability, plus scale-up infeasibility table.
Stdlib only.
"""
import math
from fractions import Fraction as Fr

q = 2
pc = math.sqrt(2) / (1 + math.sqrt(2))

def grid(W, H):
    verts = [(x, y) for y in range(H + 1) for x in range(W + 1)]
    idx = {v: i for i, v in enumerate(verts)}
    edges = []
    for x, y in verts:
        if x < W:
            edges.append((idx[(x, y)], idx[(x + 1, y)]))
        if y < H:
            edges.append((idx[(x, y)], idx[(x, y + 1)]))
    left = {idx[(0, y)] for y in range(H + 1)}
    right = {idx[(W, y)] for y in range(H + 1)}
    return len(verts), edges, left, right

def connected_sets(n, edges, mask):
    parent = list(range(n))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for i, (a, b) in enumerate(edges):
        if (mask >> i) & 1:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
    return find

def crosses(n, edges, left, right, mask):
    find = connected_sets(n, edges, mask)
    cl = {find(v) for v in left}
    return any(find(v) in cl for v in right)

def components(n, edges, mask):
    find = connected_sets(n, edges, mask)
    return len({find(v) for v in range(n)})

def exact(W, H, p):
    n, edges, left, right = grid(W, H)
    E = len(edges)
    # crossing probability: full enumeration with float weights
    Z = 0.0
    pf = 0.0
    for mask in range(1 << E):
        o = bin(mask).count("1")
        k = components(n, edges, mask)
        w = (p ** o) * ((1 - p) ** (E - o)) * (q ** k)
        Z += w
        if crosses(n, edges, left, right, mask):
            pf += w
    pf /= Z
    # influences: loop rest per edge
    I = 0.0
    for e in range(E):
        piv = 0.0
        for rest in range(1 << (E - 1)):
            lo = rest & ((1 << e) - 1)
            hi = (rest >> e) << (e + 1)
            m0 = lo | hi
            m1 = m0 | (1 << e)
            if crosses(n, edges, left, right, m1) != crosses(n, edges, left, right, m0):
                o0 = bin(m0).count("1")
                o1 = o0 + 1
                k0 = components(n, edges, m0)
                k1 = components(n, edges, m1)
                piv += (p ** o0) * ((1 - p) ** (E - o0)) * (q ** k0)
                piv += (p ** o1) * ((1 - p) ** (E - o1)) * (q ** k1)
        I += piv / Z
    return E, pf, I

for W, H in ((2, 1), (3, 2)):
    E, pf, I = exact(W, H, pc)
    print(f"box {W}x{H}: E={E} P(cross)={pf:.6f} I={I:.6f}")

print("\nscale-up: exact enumeration needs 2^E configs")
for W, H in ((4, 2), (8, 4), (256, 128)):
    E = (H + 1) * W + (W + 1) * H
    print(f"box {W}x{H}: E={E} log10(2^E)={E * math.log10(2):.1f}")
print("CONCLUSION: exact route dies above E~20; no monotone transfer of "
      "small-box I to 256x128 proved. Exact-computation route BLOCKED.")
