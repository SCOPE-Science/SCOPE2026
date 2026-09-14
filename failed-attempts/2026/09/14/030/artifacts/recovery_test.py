"""Recovery test for lane-1891 target.

Enumerates transitive (H,G)-bisets via Goursat subgroups L <= HxG for small
groups, and checks what the target's listed parameters determine:
  - full L (up to conjugacy) determines the biset/bimodule;
  - abstract stabilizer type + |M| + modular data does NOT (collisions);
  - corner reduction (finite type => both kG,kH finite => cyclic Sylows);
  - Kronecker-quotient lemma: if top dim c of kM as (kH,kG)-bimodule is >= 2,
    Lambda surjects onto c-arrow Kronecker => infinite type (rigorous).
  - c == 1 local-local cases stay ambiguous: full Tits form needs the complete
    relation ideal (Brauer-tree relations + gluing), which is not a function of
    any coarse listed parameter. This is the blocking core.
Pure Python, no network.
"""
import json
import itertools

def cyclic_group(n, name):
    els = list(range(n))
    mult = {(a, b): (a + b) % n for a in els for b in els}
    return {"name": name, "els": els, "mult": mult, "eid": 0,
            "inv": {a: (-a) % n for a in els}}

def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def sym_group():
    from functools import reduce
    e = (0, 1, 2)
    gens = [(1, 0, 2), (1, 2, 0)]
    seen, stack = {e}, [e]
    while stack:
        g = stack.pop()
        for h in gens:
            for c in (compose(g, h), compose(h, g)):
                if c not in seen:
                    seen.add(c)
                    stack.append(c)
    els = sorted(seen)
    idx = {g: i for i, g in enumerate(els)}
    mult = {(idx[a], idx[b]): idx[compose(a, b)] for a in els for b in els}
    inv = {}
    for a in els:
        for b in els:
            if compose(a, b) == e and compose(b, a) == e:
                inv[idx[a]] = idx[b]
    return {"name": "S3", "els": list(range(6)), "mult": mult,
            "eid": idx[e], "inv": inv}

def direct_product(H, G):
    els = [(h, g) for h in H["els"] for g in G["els"]]
    idx = {e: i for i, e in enumerate(els)}
    mult = {}
    for a in els:
        for b in els:
            c = (H["mult"][(a[0], b[0])], G["mult"][(a[1], b[1])])
            mult[(idx[a], idx[b])] = idx[c]
    inv = {idx[e]: idx[(H["inv"][e[0]], G["inv"][e[1]])] for e in els}
    eid = idx[(H["eid"], G["eid"])]
    return {"els": list(range(len(els))), "mult": mult, "inv": inv,
            "eid": eid, "decode": els, "H": H, "G": G}

def all_subgroups(P):
    n = len(P["els"])
    e, mult, inv = P["eid"], P["mult"], P["inv"]
    subs = []
    for mask in range(1 << n):
        if not (mask & (1 << e)):
            continue
        S = [i for i in range(n) if mask & (1 << i)]
        Sset = set(S)
        ok = all(mult[(a, b)] in Sset for a in S for b in S)
        ok = ok and all(inv[a] in Sset for a in S)
        if ok:
            subs.append(frozenset(S))
    return subs

def conj_subgroups(P, subs):
    els, mult, inv = P["els"], P["mult"], P["inv"]
    def conj(g, S):
        gi = inv[g]
        return frozenset(mult[(mult[(g, s)], gi)] for s in S)
    seen, classes = set(), []
    for S in subs:
        if S in seen:
            continue
        cls = set()
        for g in els:
            cls.add(conj(g, S))
        cls = [c for c in cls if c in set(subs)]
        for c in cls:
            seen.add(c)
        classes.append(cls)
    return classes

def group_abstract(P, S):
    S = list(S)
    mult, e = P["mult"], P["eid"]
    ab = all(mult[(a, b)] == mult[(b, a)] for a in S for b in S)
    def order(a):
        x, k = a, 1
        while x != e:
            x = mult[(x, a)]
            k += 1
        return k
    ords = sorted(order(a) for a in S)
    cyc = any(o == len(S) for o in ords)
    return {"order": len(S), "abelian": ab, "cyclic": cyc,
            "exponent": max(ords)}

def elt_order(P, a):
    x, k, e = a, 1, P["eid"]
    while x != e:
        x = P["mult"][(x, a)]
        k += 1
    return k

def conjugacy_classes(G):
    els, mult, inv = G["els"], G["mult"], G["inv"]
    seen, out = set(), []
    for a in els:
        if a in seen:
            continue
        cl = set(mult[(mult[(g, a)], inv[g])] for g in els)
        seen |= cl
        out.append(sorted(cl))
    return out

def modular_data(G, p):
    pprime = sum(1 for cl in conjugacy_classes(G)
                 if all(elt_order(G, a) % p != 0 for a in cl))
    subs = all_subgroups({"els": G["els"], "mult": G["mult"],
                          "inv": G["inv"], "eid": G["eid"]})
    import math
    pk = 1
    while len(G["els"]) % (pk * p) == 0:
        pk *= p
    syl = [S for S in subs if len(S) == pk]
    cyc = any(group_abstract(
        {"els": G["els"], "mult": G["mult"],
         "inv": G["inv"], "eid": G["eid"]}, S)["cyclic"] for S in syl)
    return {"nsimples": pprime, "sylow_order": pk,
            "sylow_cyclic": cyc, "group_order": len(G["els"])}

def cosets_and_actions(P, H, G, L):
    N = len(P["els"])
    mult, eid = P["mult"], P["eid"]
    # cosets of L: greedy
    reps, covered = [], set()
    for a in P["els"]:
        if a in covered:
            continue
        C = set(mult[(a, s)] for s in L)
        covered |= C
        reps.append(a)
    m = len(reps)
    coset_of = {}
    for i, r in enumerate(reps):
        for s in L:
            coset_of[mult[(r, s)]] = i
    Hid = [(h, H["eid"]) for h in H["els"]]
    # left H action: h.(a,b)L = (ha,b)L ; right G action similarly
    def pelem(h, g):
        return P["decode"].index((h, g))
    left = {}
    for h in H["els"]:
        perm = []
        for r in reps:
            a, b = P["decode"][r]
            na = H["mult"][(h, a)]
            perm.append(coset_of[mult[(pelem(h, H["eid"]) if False else pelem(na, b), eid)]] if False else coset_of[mult[(pelem(na, b), eid)]])
        left[h] = perm
    right = {}
    for g in G["els"]:
        perm = []
        for r in reps:
            a, b = P["decode"][r]
            nb = G["mult"][(b, g)]
            perm.append(coset_of[mult[(pelem(a, nb), eid)]])
        right[g] = perm
    # orbits + point stabilizers of coset 0
    def orbits(perms, n):
        seen, out = set(), []
        acts = list(perms.values())
        for i in range(n):
            if i in seen:
                continue
            orb, stack = set(), [i]
            while stack:
                x = stack.pop()
                if x in orb:
                    continue
                orb.add(x)
                for q in acts:
                    stack.append(q[x])
            seen |= orb
            out.append(sorted(orb))
        return out
    Horb = orbits(left, m)
    Gorb = orbits(right, m)
    hstab0 = sorted(h for h in H["els"] if left[h][0] == 0)
    gstab0 = sorted(g for g in G["els"] if right[g][0] == 0)
    projH = sorted(set(a for (a, b) in (P["decode"][s] for s in L)))
    projG = sorted(set(b for (a, b) in (P["decode"][s] for s in L)))
    return {"Msize": m, "Horbits": Horb, "Gorbits": Gorb,
            "left_point_stab_order": len(hstab0),
            "right_point_stab_order": len(gstab0),
            "projH_size": len(projH), "projG_size": len(projG),
            "left_perm": {str(k): v for k, v in left.items()},
            "right_perm": {str(k): v for k, v in right.items()}}

def gfrank(mat, p):
    M = [row[:] for row in mat]
    r = 0
    ncols = len(M[0]) if M else 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(M)) if M[i][c] % p != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c] % p, -1, p)
        M[r] = [(v * inv) % p for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p != 0:
                f = M[i][c] % p
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return r

def bimodule_top_dim(act, m, H, G, p):
    # V = k^M with permutation actions; S = J_H V + V J_G over GF(p).
    rows = []
    gensH = [h for h in H["els"] if h != H["eid"]]
    gensG = [g for g in G["els"] if g != G["eid"]]
    L = act["left_perm"]
    R = act["right_perm"]
    for h in gensH:
        q = L[str(h)]
        for j in range(m):
            row = [0] * m
            row[q[j]] = (row[q[j]] + 1) % p
            row[j] = (row[j] - 1) % p
            rows.append(row)
    for g in gensG:
        q = R[str(g)]
        for j in range(m):
            row = [0] * m
            row[q[j]] = (row[q[j]] + 1) % p
            row[j] = (row[j] - 1) % p
            rows.append(row)
    if not rows:
        return m
    return m - gfrank(rows, p)

def run_case(H, G, p):
    P = direct_product(H, G)
    subs = all_subgroups(P)
    classes = conj_subgroups(P, subs)
    modH, modG = modular_data(H, p), modular_data(G, p)
    bisets = []
    for cls in classes:
        L = sorted(cls, key=lambda S: (len(S), sorted(S)))[0]
        absL = group_abstract(P, L)
        act = cosets_and_actions(P, H, G, L)
        b = {"L_order": len(L), "abstract_L": absL,
             "Msize": act["Msize"],
             "left_ps_order": act["left_point_stab_order"],
             "right_ps_order": act["right_point_stab_order"],
             "projH": act["projH_size"], "projG": act["projG_size"],
             "H_orbit_sizes": sorted(map(len, act["Horbits"])),
             "G_orbit_sizes": sorted(map(len, act["Gorbits"])),
             "n_conjugate": len(cls)}
        # one-sided projectivity flags: summand k[H/K] projective iff p not | K|
        b["left_nonproj_summand"] = any(
            (len(H["els"]) // len(o)) % p == 0 for o in act["Horbits"])
        b["right_nonproj_summand"] = any(
            (len(G["els"]) // len(o)) % p == 0 for o in act["Gorbits"])
        if modH["nsimples"] == 1 and modG["nsimples"] == 1:
            b["topdim_c"] = bimodule_top_dim(act, act["Msize"], H, G, p)
            b["kronecker_quotient_forces_infinite"] = b["topdim_c"] >= 2
        bisets.append(b)
    # collisions: same coarse key, different fine data
    seen_keys = {}
    collisions = []
    for b in bisets:
        key = (b["abstract_L"]["order"], b["abstract_L"]["abelian"],
               b["abstract_L"]["cyclic"], b["Msize"])
        if key in seen_keys:
            o = seen_keys[key]
            if (o["projH"], o["projG"], o["left_ps_order"],
                    o["right_ps_order"], o["H_orbit_sizes"],
                    o["G_orbit_sizes"]) != (
                    b["projH"], b["projG"], b["left_ps_order"],
                    b["right_ps_order"], b["H_orbit_sizes"],
                    b["G_orbit_sizes"]):
                collisions.append({"coarse_key": str(key),
                                   "first": o, "second": b})
        else:
            seen_keys[key] = b
    return {"H": H["name"], "G": G["name"], "p": p,
            "modH": modH, "modG": modG,
            "n_subgroup_classes": len(classes),
            "n_transitive_bisets": len(classes),
            "bisets": bisets, "collisions": collisions}

C2 = cyclic_group(2, "C2")
C3 = cyclic_group(3, "C3")
C4 = cyclic_group(4, "C4")
S3 = sym_group()
out = [
    run_case(C2, C2, 2),
    run_case(C3, C3, 3),
    run_case(C4, C2, 2),
    run_case(C3, C2, 3),
    run_case(S3, C2, 2),
    run_case(S3, C2, 3),
]
with open("output/artifacts/recovery_results.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(
    [{"case": (c["H"], c["G"], c["p"]), "n_bisets": c["n_transitive_bisets"],
      "modH": c["modH"], "modG": c["modG"],
      "n_collisions": len(c["collisions"])} for c in out], indent=1))
for c in out:
    for b in c["bisets"]:
        print(c["H"], c["G"], "p=%d" % c["p"], b)
