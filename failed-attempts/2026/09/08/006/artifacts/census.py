#!/usr/bin/env python3
"""From-scratch subgroup-lattice census for six permutation groups.

Orders 24 (S4), 28 (D28), 30 (S3xC5), 33 (C33), 35 (C35), 36 (S3xS3).
Stdlib only. Any failed internal check raises -> nonzero exit (failed run).

Method notes (auditable, no CAS):
- Permutations as image-tuples. Groups by BFS closure from stated generators.
- Subgroups: cyclic subgroups + iterated-join fixpoint. Complete because every
  subgroup H is the join of the cyclic subgroups of its elements, so the
  fixpoint (closed under binary joins, starting from all cyclics + {1}) is the
  full lattice. Independently cross-checked: closure of every 1- and 2-element
  subset is present, and (in verify.py) an independent brute-force closure test
  re-checks every subset claim.
- Normality: full conjugation test gHg^-1 == H for all g.
- Element classes: conjugation orbits; class-equation sum asserted == |G|.
- Derived series by commutator closure; nilpotency via Sylow-count uniqueness.
"""
import json

# ---------------- permutations (image tuples) ---------------------------------
def compose(a, b):
    """a after b: (a*b)(i) = a(b(i))."""
    return tuple(a[b[i]] for i in range(len(a)))

def invert(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return tuple(q)

def ident(n):
    return tuple(range(n))

def cyc(n, c):
    p = list(range(n))
    k = len(c)
    for i in range(k):
        p[c[i]] = c[(i + 1) % k]
    return tuple(p)

def closure(gens, n):
    e = ident(n)
    S = {e}
    stack = [e]
    gens = list(gens)
    while stack:
        x = stack.pop()
        for g in gens:
            for y in (compose(g, x), compose(x, g)):
                if y not in S:
                    S.add(y)
                    stack.append(y)
    return S

# ---------------- group container ----------------------------------------------
def build(name, n, gens, expected_order):
    G = sorted(closure(gens, n))
    assert len(G) == expected_order, f"{name}: order {len(G)} != {expected_order}"
    idx = {g: i for i, g in enumerate(G)}
    e = idx[ident(n)]
    mult = [[idx[compose(G[i], G[j])] for j in range(len(G))] for i in range(len(G))]
    inv = [idx[invert(G[i])] for i in range(len(G))]
    conj = [[mult[i][mult[j][inv[i]]] for j in range(len(G))] for i in range(len(G))]
    return {"name": name, "n": n, "perms": G, "idx": idx, "e": e,
            "mult": mult, "inv": inv, "conj": conj, "m": len(G),
            "gen_perms": [tuple(g) for g in gens]}

def close_set(B, D):
    mult, e = D["mult"], D["e"]
    S = {e}
    stack = [e]
    B = list(B)
    while stack:
        x = stack.pop()
        for g in B:
            for y in (mult[g][x], mult[x][g]):
                if y not in S:
                    S.add(y)
                    stack.append(y)
    return frozenset(S)

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def all_subgroups(D):
    """Cyclic subgroups + iterated-join fixpoint (complete; see docstring)."""
    from itertools import combinations
    m, e, mult = D["m"], D["e"], D["mult"]
    cycs = set()
    for g in range(m):
        C, x = {e}, g
        while x not in C:
            C.add(x)
            x = mult[g][x]
        cycs.add(frozenset(C))
    S = {frozenset({e})} | cycs
    changed = True
    while changed:
        changed = False
        news = set()
        L = list(S)
        for A in L:
            for B in L:
                J = close_set(A | B, D)
                if J not in S:
                    news.add(J)
        if news:
            S |= news
            changed = True
    subs = sorted(S, key=lambda H: (len(H), sorted(H)))
    for H in subs:
        assert len(H) in divisors(D["m"]), f"{D['name']}: |H|={len(H)} !| {D['m']}"
        assert close_set(H, D) == H, f"{D['name']}: claimed subgroup not closed"
    Sset = set(subs)
    for g in range(m):
        assert close_set({g}, D) in Sset
    for a, b in combinations(range(m), 2):
        assert close_set({a, b}, D) in Sset, f"{D['name']}: 2-gen closure missing"
    return subs

def element_classes(D):
    m, conj = D["m"], D["conj"]
    seen = [False] * m
    cls = []
    for x in range(m):
        if not seen[x]:
            C = {conj[g][x] for g in range(m)}
            for y in C:
                seen[y] = True
            cls.append(sorted(C))
    assert sum(map(len, cls)) == m, "class equation does not sum to |G|"
    return cls

def is_normal(D, H):
    m, conj = D["m"], D["conj"]
    for g in range(m):
        for h in H:
            if conj[g][h] not in H:
                return False
    return True

def comm(a, b, D):
    mult, inv = D["mult"], D["inv"]
    return mult[inv[a]][mult[inv[b]][mult[a][b]]]

def derived_subgroup(D, H):
    H = list(H)
    gens = {comm(a, b, D) for a in H for b in H}
    return close_set(gens, D)

def sylow_factorization(m):
    pf, t, p = {}, m, 2
    while p * p <= t:
        while t % p == 0:
            pf[p] = pf.get(p, 0) + 1
            t //= p
        p += 1 if p == 2 else 2
    if t > 1:
        pf[t] = pf.get(t, 0) + 1
    return pf

def analyse(D):
    m = D["m"]
    subs = all_subgroups(D)
    ecls = element_classes(D)
    normal = [H for H in subs if is_normal(D, H)]
    key = {H: tuple(sorted(H)) for H in subs}
    seen, sorbits = set(), []
    for H in subs:
        if key[H] in seen:
            continue
        orb = {tuple(sorted(frozenset(D["conj"][g][h] for h in H))) for g in range(m)}
        for k in orb:
            seen.add(k)
        sorbits.append(sorted(orb))
    series = [frozenset(range(m))]
    while len(series[-1]) > 1:
        N = derived_subgroup(D, series[-1])
        assert N <= series[-1]
        series.append(N)
        assert len(series) < 10
    assert len(series[-1]) == 1, f"{D['name']}: derived series did not reach 1"
    mult = D["mult"]
    Z = frozenset(x for x in range(m)
                  if all(mult[x][y] == mult[y][x] for y in range(m)))
    pf = sylow_factorization(m)
    sylow_counts = {str(q): sum(1 for H in subs if len(H) == q ** a)
                    for q, a in pf.items()}
    nilpotent = all(c == 1 for c in sylow_counts.values())
    return {
        "order": m,
        "num_subgroups": len(subs),
        "num_normal": len(normal),
        "subgroup_class_sizes": sorted(map(len, sorbits)),
        "subgroup_classes": [[[int(z) for z in H] for H in orb] for orb in sorbits],
        "element_class_sizes": sorted(map(len, ecls)),
        "class_equation": f"{'+'.join(map(str, sorted(map(len, ecls))))}={m}",
        "derived_series_orders": [len(H) for H in series],
        "derived_length": len(series) - 1,
        "centre_order": len(Z),
        "sylow_counts": sylow_counts,
        "nilpotent": nilpotent,
        "solvable": True,
        "subgroups": [sorted(H) for H in subs],
        "normal_subgroups": [sorted(H) for H in normal],
    }

def hasse(D, subs):
    S = list(map(frozenset, subs))
    covers = []
    for H in S:
        for K in S:
            if H < K:
                if not any(H < M < K for M in S):
                    w = next(v for v in K - H if close_set(H | {v}, D) == K)
                    covers.append((sorted(H), sorted(K), w))
    lt = {(tuple(sorted(H)), tuple(sorted(K))) for H, K, _ in covers}
    reach = set(lt)
    changed = True
    while changed:
        changed = False
        for a, b in list(reach):
            for c, d in list(lt):
                if b == c and (a, d) not in reach:
                    reach.add((a, d))
                    changed = True
    for H in S:
        for K in S:
            if H < K:
                assert (tuple(sorted(H)), tuple(sorted(K))) in reach, "Hasse incomplete"
    return covers

def main():
    G = {}
    # G24 = S4 via V4 <s> and point-stabilizer S3 fixing 4 (topic: V4 ⋊ S3)
    G["G24"] = build("G24=S4", 4, [tuple([1, 0, 3, 2]), tuple([2, 3, 0, 1]),
                                    cyc(4, [0, 1, 2]), cyc(4, [0, 1])], 24)
    # G28 = D28 = C14 ⋊ C2
    r = tuple((i + 1) % 14 for i in range(14))
    s = tuple((14 - i) % 14 for i in range(14))
    assert compose(s, s) == ident(14) and compose(compose(s, r), s) == invert(r)
    G["G28"] = build("G28=D28", 14, [r, s], 28)
    # G30 = S3 x C5 on disjoint supports, commuting factors
    a = (1, 2, 0, 3, 4, 5, 6, 7)
    b = (1, 0, 2, 3, 4, 5, 6, 7)
    c = (0, 1, 2, 4, 5, 6, 7, 3)
    assert compose(a, c) == compose(c, a) and compose(b, c) == compose(c, b)
    G["G30"] = build("G30=S3xC5", 8, [a, b, c], 30)
    # G33 = C33, G35 = C35
    G["G33"] = build("G33=C33", 33, [cyc(33, list(range(33)))], 33)
    G["G35"] = build("G35=C35", 35, [cyc(35, list(range(35)))], 35)
    # G36 = S3 x S3 on disjoint supports
    a1 = (1, 2, 0, 3, 4, 5); b1 = (1, 0, 2, 3, 4, 5)
    a2 = (0, 1, 2, 4, 5, 3); b2 = (0, 1, 2, 4, 3, 5)
    G["G36"] = build("G36=S3xS3", 6, [a1, b1, a2, b2], 36)

    out = {}
    for k, D in G.items():
        out[k] = analyse(D)
        print(f"{k}: |Sub|={out[k]['num_subgroups']} normal={out[k]['num_normal']} "
              f"subcl={out[k]['subgroup_class_sizes']} elcl={out[k]['element_class_sizes']} "
              f"dlen={out[k]['derived_length']} dser={out[k]['derived_series_orders']} "
              f"Z={out[k]['centre_order']} nil={out[k]['nilpotent']} syl={out[k]['sylow_counts']}",
              flush=True)

    # ---- hard spot-checks (fail run on mismatch) ----
    assert out["G24"]["num_subgroups"] == 30 and out["G24"]["num_normal"] == 4
    assert out["G24"]["element_class_sizes"] == [1, 3, 6, 6, 8]
    assert out["G24"]["derived_series_orders"] == [24, 12, 4, 1]
    assert out["G24"]["centre_order"] == 1 and not out["G24"]["nilpotent"]
    assert out["G28"]["num_subgroups"] == 28  # tau(14)+sigma(14) = 4+24
    assert out["G30"]["num_subgroups"] == 12 and out["G30"]["num_normal"] == 6
    assert out["G33"]["num_subgroups"] == 4 and out["G35"]["num_subgroups"] == 4
    assert out["G33"]["element_class_sizes"] == [1] * 33
    assert out["G35"]["element_class_sizes"] == [1] * 35
    for k in ("G33", "G35"):
        assert out[k]["num_normal"] == out[k]["num_subgroups"] and out[k]["nilpotent"]

    # ---- G24 Hasse cover log ----
    D = G["G24"]
    subs = [frozenset(H) for H in out["G24"]["subgroups"]]
    covers = hasse(D, subs)
    with open("output/artifacts/hasse_G24.txt", "w") as f:
        f.write(f"# Hasse covers of Sub(S4): {len(covers)} cover relations\n")
        f.write("# each line: H < K with no intermediate, witness w with <H,w> = K\n")
        for H, K, w in covers:
            f.write(f"|H|={len(H)} < |K|={len(K)} witness w=elem{w}: "
                    f"H={H} K={K}\n")
    print(f"G24 Hasse covers: {len(covers)}", flush=True)

    # ---- G24 normality-failure certificate ----
    m, conj = D["m"], D["conj"]
    cert = None
    for H in subs:
        if not is_normal(D, H):
            for g in range(m):
                C = frozenset(conj[g][h] for h in H)
                if C != H:
                    cert = (sorted(H), g, sorted(C))
                    break
            break
    assert cert is not None
    H, g, C = cert
    with open("output/artifacts/normality_failure_G24.txt", "w") as f:
        f.write(f"H={H}\ng=elem{g} perm={D['perms'][g]}\ngHg^-1={C}\n"
                f"H != gHg^-1: {H != C}\n")
    print(f"G24 normality failure: H={H} g=elem{g} gHg^-1={C}", flush=True)
    out["G24"]["normality_failure"] = {"H": H, "g": g, "gHginv": C}

    # ---- G24 coset action on point-stabilizer S3 (order 6, index 4) ----
    stab = close_set({D["idx"][cyc(4, [0, 1, 2])], D["idx"][cyc(4, [0, 1])]}, D)
    assert len(stab) == 6
    mult = D["mult"]
    cosets, seen = [], set()
    for x in range(m):
        Cx = frozenset(mult[x][h] for h in stab)  # left cosets x*H
        if tuple(sorted(Cx)) not in seen:
            seen.add(tuple(sorted(Cx)))
            cosets.append(Cx)
    assert len(cosets) == 4 and sum(map(len, cosets)) == m
    rep = [min(C) for C in cosets]
    owner = {}
    for i, C in enumerate(cosets):
        for x in C:
            owner[x] = i
    # left action on left cosets: g . (xH) = (gx)H
    act = [[owner[mult[g][rep[i]]] for i in range(4)] for g in range(m)]
    for x in range(m):
        for y in range(m):
            assert act[mult[x][y]] == [act[x][act[y][i]] for i in range(4)], \
                "coset map is not a homomorphism"
    ker = frozenset(g for g in range(m) if act[g] == [0, 1, 2, 3])
    core = frozenset(h for h in stab
                     if all(frozenset(conj[g][q] for q in stab) == stab or True
                            for g in [0]) and all(conj[g][h] in stab for g in range(m)))
    core = frozenset(h for h in stab if all(conj[g][h] in stab for g in range(m)))
    assert ker == core, f"kernel {sorted(ker)} != core {sorted(core)}"
    assert len(core) == 1  # point stabilizer is core-free in S4
    assert len({tuple(a) for a in act}) > 1  # nontrivial image
    with open("output/artifacts/coset_action_G24.txt", "w") as f:
        f.write(f"# right-coset action of S4 on cosets of point-stabilizer S3 (index 4)\n")
        f.write(f"# coset reps (elem indices) = {rep}\n")
        for i, C in enumerate(cosets):
            f.write(f"coset{i}={sorted(C)}\n")
        f.write("# action images in S4 on {0,1,2,3} (one line per g):\n")
        for g in range(m):
            f.write(f"g{g} {D['perms'][g]} -> {act[g]}\n")
        f.write(f"kernel={sorted(ker)} core={sorted(core)} "
                f"equal={ker == core} faithful(core-free)={len(core) == 1}\n")
    out["G24"]["coset_action"] = {"reps": rep, "images": act, "kernel": sorted(ker),
                                  "core": sorted(core), "index": 4}
    out["G24"]["num_hasse_covers"] = len(covers)
    out["G24"]["hasse_covers"] = [[H, K, w] for H, K, w in covers]

    with open("output/artifacts/census_results.json", "w") as f:
        json.dump(out, f, indent=1)
    with open("output/artifacts/generators.json", "w") as f:
        json.dump({k: {"n": D["n"], "gens": [list(p) for p in D["gen_perms"]]}
                   for k, D in G.items()}, f, indent=1)
    print("CENSUS OK", flush=True)

if __name__ == "__main__":
    main()
