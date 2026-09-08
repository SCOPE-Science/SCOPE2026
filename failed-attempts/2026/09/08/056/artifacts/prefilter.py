"""Fast prefilter: for each of 112 connected graph reps, count ordered triples of H-slots with both cups exact (ns[0] reps)."""
import sys, json, itertools, sympy
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-162/output/artifacts")
from rmodel import faces_of, basis_J, deg_of, diff_mat
from cup import prod_on_basis
from massey import cup_vecs

reps = json.load(open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-162/output/artifacts/iso_reps.json"))["reps"]
ED = [(i, j) for i in range(6) for j in range(i + 1, 6)]


def conn(g):
    p = list(range(6))

    def f(a):
        while p[a] != a:
            p[a] = p[p[a]]
            a = p[a]
        return a

    for e, (a, b) in enumerate(ED):
        if (g >> e) & 1:
            ra, rb = f(a), f(b)
            if ra != rb:
                p[ra] = rb
    return len(set(f(i) for i in range(6))) == 1


out = []
for code, g in reps.items():
    if not conn(g):
        continue
    F = faces_of(g, 0)
    BB = {J: basis_J(J, F) for J in range(64)}
    slots = []
    for J in range(1, 64):
        B = BB[J]
        by = {}
        for b in B:
            by.setdefault(deg_of(*b), []).append(b)
        for d, Bd in by.items():
            BdN = by.get(d + 1, [])
            BdP = by.get(d - 1, [])
            Do = diff_mat(J, Bd, F, BdN) if BdN else sympy.zeros(0, len(Bd))
            Di = diff_mat(J, BdP, F, Bd) if BdP else sympy.zeros(len(Bd), 0)
            ns = Do.nullspace()
            if len(ns) - Di.rank() > 0:
                slots.append((J, d, Bd, ns[0]))
    nv = 0
    triples = 0
    for (Ja, da, Ba, va) in slots:
        for (Jb, db, Bb, vb) in slots:
            v, _ = cup_vecs(va, Ba, vb, Bb, BB[Ja | Jb], F)
            # exact in deg da+db?
            B = BB[Ja | Jb]
            by = {}
            for b in B:
                by.setdefault(deg_of(*b), []).append(b)
            Bd = by.get(da + db, [])
            if not Bd:
                e_ab = all(x == 0 for x in v)
            else:
                BdP = by.get(da + db - 1, [])
                Di = diff_mat(Ja | Jb, BdP, F, Bd) if BdP else sympy.zeros(len(Bd), 0)
                vv = sympy.Matrix([0] * len(Bd))
                i2 = {b: k for k, b in enumerate(Bd)}
                idx = {b: k for k, b in enumerate(B)}
                for b, k in i2.items():
                    vv[k] = v[idx[b]]
                from cup import is_coboundary
                e_ab = is_coboundary(vv, Di)
            if e_ab:
                nv += 1
    out.append((g, len(slots), nv))
    print(g, "slots:", len(slots), "exact-cup pairs:", nv, flush=True)

json.dump(out, open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-162/output/artifacts/prefilter.json", "w"))
