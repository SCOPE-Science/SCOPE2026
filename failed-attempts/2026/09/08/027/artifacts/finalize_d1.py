"""finalize_d1.py — deterministic certification of flip-distance-1 skeleton atlas (fast).

Writes census_d1.json. Only wall-cross regularity certs (seconds); flips without
a wall-cross cert are recorded with heights=null (regularity UNCERTIFIED there).
"""
import json
import os
import random
from fractions import Fraction as F

from honeycomb_flip import (PTS, IDX, N, lower_triangulation, check_triangulation,
                            skeleton_core, connectivity, canon, all_flips,
                            genus_check, is_K4, plane)

DELTAS = [F(1, 1000), F(1, 100), F(1, 10), F(1, 2), F(1, 1), F(3, 1)]


def build_T0():
    r = random.Random(1000 + 2)
    h0 = [F(x * x + y * y) * 100 + F(r.randint(0, 9999), 100) for (x, y) in PTS]
    T0 = sorted(lower_triangulation(h0))
    return h0, T0


def quad_of_flip(T0sorted, nT):
    S1 = set(tuple(t) for t in nT)
    removed = [t for t in T0sorted if t not in S1]
    assert len(removed) == 2
    A, B = set(removed[0]), set(removed[1])
    shared = A & B
    assert len(shared) == 2
    c = (A - shared).pop()
    d = (B - shared).pop()
    a, b = tuple(shared)
    return a, b, c, d


def directed_cert(h0, target, quad):
    tgt = sorted(tuple(t) for t in target)
    for v in quad:
        others = [u for u in quad if u != v]
        LP = [(PTS[u][0], PTS[u][1], F(h0[u])) for u in others]
        pl = plane(*LP)
        if pl is None:
            continue
        A, B, C = pl
        xv, yv = PTS[v]
        tstar = (A * F(xv) + B * F(yv) + C) - F(h0[v])
        for dlt in DELTAS:
            for sgn in (1, -1):
                h = [F(x) for x in h0]
                h[v] = h[v] + tstar + sgn * dlt
                tris = lower_triangulation(h)
                if tris is not None and sorted(tris) == tgt:
                    return ([str(x) for x in h],
                            {"method": "wall-cross", "moved_vertex": v,
                             "tstar": str(tstar), "delta": str(sgn * dlt)})
    return None, None


def main():
    h0, T0 = build_T0()
    assert sorted(lower_triangulation(h0)) == T0
    ok, msg = check_triangulation(T0)
    assert ok, msg
    assert genus_check(T0) == 3
    n0, e0 = skeleton_core(T0)
    assert is_K4(n0, e0)
    assert connectivity(n0, e0)["edge_conn"] == 3

    flips = all_flips(T0)
    classes = {}
    for e, nT in flips:
        classes.setdefault(canon(nT), []).append((e, nT))

    rows = []
    for i, key in enumerate(sorted(classes, key=lambda k: classes[k][0][0])):
        e, nT = classes[key][0]
        a, b, c, d = quad_of_flip(T0, nT)
        nodes, elist = skeleton_core(nT)
        conn = connectivity(nodes, elist)
        assert genus_check(nT) == 3
        ok, m = check_triangulation(nT)
        assert ok, m
        h, method = directed_cert(h0, nT, (a, b, c, d))
        ec = conn["edge_conn"]
        rows.append({
            "orbit": i,
            "flipped_edge": [[int(a_) for a_ in p] for p in e],
            "quad_vertices": [int(v) for v in (a, b, c, d)],
            "new_tris": [[int(x) for x in t] for t in nT],
            "regularity_heights": h,
            "cert_method": method,
            "regular_certified": h is not None,
            "core_nodes": nodes,
            "core_edges": [[int(u) for u in ee] for ee in elist],
            "edge_conn": ec,
            "n_two_cuts": len(conn["two_cuts"]),
            "two_cuts": conn["two_cuts"],
        })
        print(f"orbit {i}: edge={e} ec={ec} cuts={len(conn['two_cuts'])} "
              f"cert={'YES' if h else 'NO'}", flush=True)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "census_d1.json"), "w") as f:
        json.dump({
            "T0_tris_idx": [[int(x) for x in t] for t in T0],
            "T0_heights": [str(F(x)) for x in h0],
            "points": [[int(a) for a in p] for p in PTS],
            "T0_core_nodes": n0,
            "T0_core_edges": [[int(u) for u in ee] for ee in e0],
            "rows": rows,
        }, f, indent=1)
    print(f"wrote census_d1.json: {len(rows)} rows, "
          f"{sum(1 for r_ in rows if r_['regular_certified'])}/{len(rows)} regular-certified",
          flush=True)


if __name__ == "__main__":
    main()
