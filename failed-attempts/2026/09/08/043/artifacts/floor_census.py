"""Floor-diagram enumeration for P^2, degrees 3-4, genus 0 (rational).

Convention (Brugalle-Mikhalkin / Fomin-Mikhalkin, labeled floor diagrams):
- vertices 0..d-1 (floors), edges directed i->j, i<j, positive integer weights.
- divergence div(v) = outflow(v) - inflow(v) <= 1 for all v.
- genus g = E - d + 1 with E = #edges (slots; parallel edges count separately).
- connected.
- complex multiplicity = prod w^2; real (all-real-point Welschinger) multiplicity
  = 0 if any even weight else prod w.
- marking: subdivide each edge slot with a midpoint m (i->m->j); attach
  s_v = 1 - div(v) short vertices pointing into v; add floor chain
  0->1->...->d-1 (markings increase on floors). nu(D) = #linear extensions / |Aut|.
- N_d = sum mult_C * nu; W_d = sum mult_R * nu.
Calibration targets: N3=12, N4=620 (Kontsevich), W3=8, W4=240 (Welschinger).
"""
import itertools
import json
import math
from functools import lru_cache


def connected(combo, d):
    parent = list(range(d))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    for (i, j) in combo:
        union(i, j)
    return len({find(v) for v in range(d)}) == 1


def divergence(combo, wts, d):
    # Fomin-Mikhalkin convention: div = INFLOW - OUTFLOW <= 1.
    div = [0] * d
    for (i, j), w in zip(combo, wts):
        div[i] -= w
        div[j] += w
    return div


def count_linear_extensions(n, pred):
    """pred[v] = bitmask of predecessors of v. DP over subsets."""
    dp = [0] * (1 << n)
    dp[0] = 1
    full = (1 << n) - 1
    for mask in range(1 << n):
        cur = dp[mask]
        if not cur:
            continue
        for v in range(n):
            if mask & (1 << v):
                continue
            if pred[v] & ~mask == 0:
                dp[mask | (1 << v)] += cur
    return dp[full]


def marking_count(combo, wts, d):
    div = divergence(combo, wts, d)
    shorts = [1 - x for x in div]
    assert all(s >= 0 for s in shorts), f"negative shorts {shorts}"
    E = len(combo)
    # node indexing: floors 0..d-1; shorts next; midpoints last
    idx = d
    short_nodes = []
    for v in range(d):
        lst = []
        for _ in range(shorts[v]):
            lst.append(idx)
            idx += 1
        short_nodes.append(lst)
    mid_nodes = []
    for _ in range(E):
        mid_nodes.append(idx)
        idx += 1
    n = idx
    pred = [0] * n
    # floor chain
    for v in range(1, d):
        pred[v] |= (1 << (v - 1))
    # shorts point into floor
    for v in range(d):
        for s in short_nodes[v]:
            pred[v] |= (1 << s)
    # edge slots subdivided
    for (i, j), m in zip(combo, mid_nodes):
        pred[m] |= (1 << i)
        pred[j] |= (1 << m)
    le = count_linear_extensions(n, pred)
    # automorphisms: shorts at same floor; parallel same-weight midpoints
    aut = 1
    for v in range(d):
        aut *= math.factorial(shorts[v])
    from collections import Counter
    c = Counter(zip(combo, wts))
    for k in c.values():
        aut *= math.factorial(k)
    assert le % aut == 0, f"non-integral marking {le}/{aut}"
    return le // aut, shorts


def census(d, cap=7):
    pairs = [(i, j) for i in range(d) for j in range(i + 1, d)]
    E = d - 1  # genus 0
    rows = []
    hit_cap = False
    for combo in itertools.combinations_with_replacement(pairs, E):
        if not connected(combo, d):
            continue
        for wts in itertools.product(range(1, cap + 1), repeat=E):
            if any(w == cap for w in wts):
                # would signal incompleteness; record and continue check
                div = divergence(combo, wts, d)
                if all(x <= 1 for x in div):
                    hit_cap = True
                continue
            div = divergence(combo, wts, d)
            if not all(x <= 1 for x in div):
                continue
            nu, shorts = marking_count(combo, wts, d)
            multC = 1
            for w in wts:
                multC *= w * w
            if any(w % 2 == 0 for w in wts):
                multR = 0
            else:
                multR = 1
                for w in wts:
                    multR *= w
            rows.append({
                "d": d,
                "edges": [list(e) for e in combo],
                "weights": list(wts),
                "div": div,
                "shorts": shorts,
                "nu": nu,
                "multC": multC,
                "multR": multR,
                "cC": multC * nu,
                "cR": multR * nu,
            })
    return rows, hit_cap


def main():
    out = {}
    for d, Nexp, Wexp in [(3, 12, 8), (4, 620, 240)]:
        rows, hit_cap = census(d)
        N = sum(r["cC"] for r in rows)
        W = sum(r["cR"] for r in rows)
        print(f"d={d}: diagrams={len(rows)} N={N} (exp {Nexp}) W={W} (exp {Wexp}) hit_cap={hit_cap}")
        assert not hit_cap, "weight cap hit: enumeration incomplete"
        assert N == Nexp, f"N mismatch d={d}"
        if W != Wexp:
            print(f"    REAL-DISCREPANCY d={d}: diagram-only odd-weight rule gives {W}, reference Welschinger is {Wexp}. Table kept; see DRAFT for analysis.")
        out[d] = rows
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "floor_census.json"), "w") as f:
        json.dump({str(k): v for k, v in out.items()}, f, indent=1)
    print("wrote floor_census.json")


if __name__ == "__main__":
    main()
