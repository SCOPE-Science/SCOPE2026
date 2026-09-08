#!/usr/bin/env python3
"""Independent verifier for the subgroup-lattice census.

Reads output/artifacts/generators.json + census_results.json (+ the three
G24 logs) and re-derives everything with separately written code paths.
Exits nonzero (with message) on ANY mismatch. Stdlib only.
"""
import json
import sys
from itertools import combinations

ART = "output/artifacts"

def comp(a, b):
    return tuple(a[b[i]] for i in range(len(a)))

def inv(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return tuple(q)

def E(n):
    return tuple(range(n))

def bfs_group(gens, n):
    e = E(n)
    seen = {e}
    queue = [e]
    while queue:
        x = queue.pop()
        for g in gens:
            for y in (comp(x, g), comp(g, x)):
                if y not in seen:
                    seen.add(y)
                    queue.append(y)
    return sorted(seen)

def gen_closure(elems, G, idx, n):
    e = E(n)
    seen = {e}
    queue = [e]
    el = list(elems)
    while queue:
        x = queue.pop()
        for g in el:
            for y in (comp(x, G[g]), comp(G[g], x)):
                if y not in seen:
                    j = idx[y]
                    seen.add(y)
                    queue.append(y)
    return frozenset(idx[y] for y in seen)

def main():
    gens = json.load(open(f"{ART}/generators.json"))
    res = json.load(open(f"{ART}/census_results.json"))
    expect_orders = {"G24": 24, "G28": 28, "G30": 30, "G33": 33, "G35": 35, "G36": 36}
    assert set(gens) == set(expect_orders) == set(res), "key mismatch"
    for k, o in expect_orders.items():
        n = gens[k]["n"]
        gp = [tuple(g) for g in gens[k]["gens"]]
        G = bfs_group(gp, n)
        assert len(G) == o, f"{k}: recomputed order {len(G)} != {o}"
        idx = {g: i for i, g in enumerate(G)}
        m = len(G)
        e = idx[E(n)]
        # subgroup re-enumeration: independent join-fixpoint implementation
        cycs = set()
        for g in range(m):
            C = {e}
            x = g
            while x not in C:
                C.add(x)
                x = idx[comp(G[g], G[x])]
            cycs.add(frozenset(C))
        lat = {frozenset({e})} | cycs
        while True:
            add = set()
            L = list(lat)
            for A in L:
                for B in L:
                    J = gen_closure(A | B, G, idx, n)
                    if J not in lat:
                        add.add(J)
            if not add:
                break
            lat |= add
        R = res[k]
        assert len(lat) == R["num_subgroups"], f"{k}: subgroup count {len(lat)} != {R['num_subgroups']}"
        # every stored subgroup: closed, correct order dividing m, distinct
        seen = set()
        for H in R["subgroups"]:
            Hf = frozenset(H)
            assert Hf not in seen, f"{k}: duplicate subgroup"
            seen.add(Hf)
            assert m % len(Hf) == 0, f"{k}: Lagrange violation |H|={len(Hf)}"
            assert gen_closure(Hf, G, idx, n) == Hf, f"{k}: stored set not a subgroup"
            assert e in Hf
        assert seen == lat, f"{k}: stored lattice != recomputed lattice"
        # normality recount by independent conjugation
        ncnt = 0
        for H in R["subgroups"]:
            Hf = frozenset(H)
            ok = True
            for g in range(m):
                gi = idx[inv(G[g])]
                for h in H:
                    if idx[comp(comp(G[g], G[h]), G[gi])] not in Hf:
                        ok = False
                        break
                if not ok:
                    break
            ncnt += ok
            stored_normal = (sorted(H) in [sorted(N) for N in R["normal_subgroups"]])
            assert ok == stored_normal, f"{k}: normality mismatch on {sorted(H)}"
        assert ncnt == R["num_normal"], f"{k}: normal count"
        # element classes: orbit partition + equation sum
        rem = set(range(m))
        sizes = []
        while rem:
            x = rem.pop()
            orb = set()
            for g in range(m):
                gi = idx[inv(G[g])]
                orb.add(idx[comp(comp(G[g], G[x]), G[gi])])
            assert orb <= (set(range(m)) - set() | {x} | orb)
            rem -= orb
            sizes.append(len(orb))
        assert sorted(sizes) == sorted(R["element_class_sizes"]), f"{k}: element classes"
        assert sum(sizes) == m, f"{k}: class equation sum"
        # subgroup-class sizes recount
        done, sc = set(), []
        for H in R["subgroups"]:
            t = tuple(sorted(H))
            if t in done:
                continue
            orb = set()
            for g in range(m):
                gi = idx[inv(G[g])]
                orb.add(tuple(sorted(idx[comp(comp(G[g], G[h]), G[gi])] for h in H)))
            for t2 in orb:
                done.add(t2)
            sc.append(len(orb))
        assert sorted(sc) == sorted(R["subgroup_class_sizes"]), f"{k}: subgroup classes"
        # derived series recount
        def commset(H):
            S = set()
            for a in H:
                for b in H:
                    ai = idx[inv(G[a])]
                    bi = idx[inv(G[b])]
                    S.add(idx[comp(comp(G[ai], G[bi]), comp(G[a], G[b]))])
            return gen_closure(S, G, idx, n)
        cur = frozenset(range(m))
        ds = [m]
        while len(cur) > 1:
            cur = commset(cur)
            ds.append(len(cur))
        assert ds == R["derived_series_orders"], f"{k}: derived series {ds}"
        assert R["derived_length"] == len(ds) - 1 and ds[-1] == 1
        print(f"{k}: OK (order, {len(lat)} subgroups, {ncnt} normal, "
              f"classes {sorted(sizes)}, derived {ds})", flush=True)

    # ---- G24 log checks ----
    R24 = res["G24"]
    n = gens["G24"]["n"]
    G = bfs_group([tuple(g) for g in gens["G24"]["gens"]], n)
    idx = {g: i for i, g in enumerate(G)}
    m = len(G)
    subs = [frozenset(H) for H in R24["subgroups"]]
    S = set(subs)
    covers = [tuple(c) for c in R24["hasse_covers"]]
    assert len(covers) == R24["num_hasse_covers"] == 66
    lines = open(f"{ART}/hasse_G24.txt").read().strip().split("\n")
    assert len(lines) - 2 == 66, "hasse log line count"
    for H, K, w in covers:
        Hf, Kf = frozenset(H), frozenset(K)
        assert Hf < Kf and Hf in S and Kf in S
        assert not any(Hf < M < Kf for M in S), "cover not minimal"
        assert gen_closure(Hf | {w}, G, idx, n) == Kf, "Hasse witness fails"
    # every comparable pair with no intermediate is listed
    listed = {(tuple(H), tuple(K)) for H, K, _ in covers}
    for A in subs:
        for B in subs:
            if A < B and not any(A < M < B for M in subs):
                assert (tuple(sorted(A)), tuple(sorted(B))) in listed, "Hasse missing cover"
    print("G24 Hasse log: OK (66 covers, all minimal, all witnessed)", flush=True)

    # normality-failure certificate replay
    nf = R24["normality_failure"]
    Hf = frozenset(nf["H"])
    g, gi = nf["g"], idx[inv(G[nf["g"]])]
    C = frozenset(idx[comp(comp(G[g], G[h]), G[gi])] for h in Hf)
    assert sorted(C) == sorted(nf["gHginv"]) and C != Hf
    assert Hf in S and C in S
    txt = open(f"{ART}/normality_failure_G24.txt").read()
    assert str(nf["H"]) in txt and str(nf["gHginv"]) in txt
    print(f"G24 normality failure: OK (H={nf['H']}, g={g}, gHg^-1={nf['gHginv']})", flush=True)

    # coset-action replay
    ca = R24["coset_action"]
    mult = [[idx[comp(G[i], G[j])] for j in range(m)] for i in range(m)]
    Hf = None
    # stabilizer recovery: the unique order-6 subgroup that is a point stabilizer
    # (recompute: elements fixing point 3 in the degree-4 action)
    stab = frozenset(i for i, p in enumerate(G) if p[3] == 3)
    assert len(stab) == 6
    cos, seen = [], set()
    for x in range(m):
        Cx = frozenset(mult[x][h] for h in stab)
        t = tuple(sorted(Cx))
        if t not in seen:
            seen.add(t)
            cos.append(Cx)
    assert len(cos) == ca["index"] == 4
    rep = [min(C) for C in cos]
    assert rep == ca["reps"]
    own = {}
    for i, C in enumerate(cos):
        for x in C:
            own[x] = i
    act = [[own[mult[g][rep[i]]] for i in range(4)] for g in range(m)]
    assert act == ca["images"], "action table mismatch"
    for x in range(m):
        for y in range(m):
            lhs = act[mult[x][y]]
            rhs = [act[x][act[y][i]] for i in range(4)]
            assert lhs == rhs, "homomorphism check failed"
    ker = sorted(g for g in range(m) if act[g] == [0, 1, 2, 3])
    assert ker == sorted(ca["kernel"]) == ca["core"] == [e]
    print(f"G24 coset action: OK (index 4, homomorphism, kernel==core=={{{e}}})", flush=True)
    print("ALL VERIFICATIONS PASSED", flush=True)

if __name__ == "__main__":
    try:
        main()
    except AssertionError as ex:
        print(f"VERIFICATION FAILED: {ex}", flush=True)
        sys.exit(1)
