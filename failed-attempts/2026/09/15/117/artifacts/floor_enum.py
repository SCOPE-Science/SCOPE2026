"""Enumerate genus-0 degree-d floor diagrams for P^2 and verify N_d.

Model (Brugalle-Mikhalkin, reconstructed):
- vertices (floors) 0..d-1 ordered bottom-to-top
- bounded elevators: multiset of directed edges i->j (i<j), weights >=1
- divergence: u_v = 1 + out(v) - in(v) >= 0  (unbounded downward ends at v)
- genus 0: bounded-edge graph connected and E = d-1 (tree)
- multiplicity mu(D) = prod_e w(e)^2
- marking poset: floors chain v0<...<v{d-1}; bounded bead b_e: vi < b_e < vj;
  unbounded bead c at floor v: c < v_v. Markings = linear extensions / Aut.
"""
import itertools
from functools import lru_cache


def gen_bounded(d, max_w=None):
    if max_w is None:
        max_w = d
    pairs = [(i, j) for i in range(d) for j in range(i + 1, d)]
    # E = d-1 bounded edges (with repetition of pairs allowed, weights 1..max_w)
    # Represent as multiset: sequence of (pair, weight) nondecreasing to avoid dupes.
    items = [(p, w) for p in pairs for w in range(1, max_w + 1)]
    results = []

    def rec(start, chosen):
        if len(chosen) == d - 1:
            yield list(chosen)
            return
        for k in range(start, len(items)):
            chosen.append(items[k])
            yield from rec(k, chosen)  # allow reuse (parallel edges)
            chosen.pop()

    # d=1: E=0 -> single empty diagram
    if d == 1:
        yield []
        return
    yield from rec(0, [])


def diagram_data(d, edges):
    out_w = [0] * d
    in_w = [0] * d
    for (i, j), w in edges:
        out_w[i] += w
        in_w[j] += w
    u = [1 + out_w[v] - in_w[v] for v in range(d)]
    return out_w, in_w, u


def connected(d, edges):
    if d == 1:
        return True
    adj = [set() for _ in range(d)]
    for (i, j), w in edges:
        adj[i].add(j)
        adj[j].add(i)
    seen = {0}
    stack = [0]
    while stack:
        a = stack.pop()
        for b in adj[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return len(seen) == d


def enumerate_diagrams(d):
    out = []
    for edges in gen_bounded(d):
        out_w, in_w, u = diagram_data(d, edges)
        if any(x < 0 for x in u):
            continue
        if not connected(d, edges):
            continue
        mu = 1
        for (i, j), w in edges:
            mu *= w * w
        out.append({"edges": edges, "u": u, "mu": mu})
    return out


def count_markings(d, edges, u):
    # Build poset elements:
    # floors 0..d-1 (ids 0..d-1)
    # bounded beads: one per bounded edge (id d..d+E-1)
    # unbounded beads: sum u (ids after)
    E = len(edges)
    Ub = sum(u)
    n = d + E + Ub
    # predecessors sets
    pred = [set() for _ in range(n)]
    # floors chain
    for v in range(1, d):
        pred[v].add(v - 1)
    bid = d
    edge_bead = []
    for (i, j), w in edges:
        edge_bead.append(bid)
        pred[bid].add(i)
        # bead < vj
        pred[j].add(bid)
        bid += 1
    # unbounded beads at floor v: bead < v
    unb_beads_at = {}
    for v in range(d):
        lst = []
        for _ in range(u[v]):
            pred[bid].add(-1)  # placeholder none; bead minimal except < v
            pred[bid].discard(-1)
            pred[v].add(bid)
            lst.append(bid)
            bid += 1
        unb_beads_at[v] = lst
    assert bid == n
    # Count linear extensions via subset DP
    # predmask[e] = bitmask of strict predecessors
    predmask = [0] * n
    for e in range(n):
        m = 0
        for p in pred[e]:
            m |= 1 << p
        predmask[e] = m
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(placed):
        if placed == (1 << n) - 1:
            return 1
        t = 0
        for e in range(n):
            if not (placed >> e) & 1:
                if (predmask[e] & ~placed) == 0:
                    t += dp(placed | (1 << e))
        return t

    total = dp(0)
    # Automorphism order: unbounded ends at same floor identical (u_v!);
    # parallel identical (same pair+weight) bounded edges identical (m!).
    import math
    aut = 1
    for v in range(d):
        aut *= math.factorial(u[v])
    seen = {}
    for key in edges:
        seen[key] = seen.get(key, 0) + 1
    for c in seen.values():
        aut *= math.factorial(c)
    return total, aut, n


def main():
    import math
    for d in [1, 2, 3, 4]:
        diags = enumerate_diagrams(d)
        print(f"=== d={d}: {len(diags)} diagrams")
        tot = 0
        for D in diags:
            edges, u, mu = D["edges"], D["u"], D["mu"]
            total, aut, n = count_markings(d, edges, u)
            contrib = mu * total // aut
            assert (mu * total) % aut == 0, (mu, total, aut)
            tot += contrib
            print(f"  edges={edges} u={u} mu={mu} linExt={total} aut={aut} contrib={contrib}")
        print(f"  TOTAL d={d}: {tot}  (expect N = " + {1: 1, 2: 1, 3: 12, 4: 620}[d].__str__() + ")")
        print()


if __name__ == "__main__":
    main()
