#!/usr/bin/env python3
"""Exact Mahler spectrum over the 16 reflexive lattice polygon classes.

Stdlib only (fractions, itertools, math). Exact integer/rational arithmetic.
Replay: `python3 mahler_reflexive.py` (~1-3 min) -> prints 16-row table, gap data,
writes mahler_table.json / mahler_table.csv next to itself.

Completeness (proved in DRAFT.md):
  * Cited background: Twelve-Point Theorem B(P)+B(P*)=12 for reflexive P;
    hence V(P)<=6 (via 12>=2V), B(P)<=9, A(P)<=9/2 (Pick's, I=1).
  * Width lemma (proved): every vertex coordinate lies in [-3,3].
    Hence every reflexive polygon has a vertex set among the 32 primitive
    points of [-3,3]^2, and subset enumeration over sizes 3..6 is exhaustive.
  * GL(2,Z)-classification by exact equivalence search; expect exactly 16.
"""
import json
import math
import os
import time
from fractions import Fraction
from itertools import combinations

t0 = time.time()

def cross(ax, ay, bx, by):
    return ax * by - ay * bx

def hull(pts):
    P = sorted(set(pts))
    if len(P) <= 1:
        return P
    def build(Q):
        h = []
        for p in Q:
            while len(h) >= 2 and cross(h[-1][0]-h[-2][0], h[-1][1]-h[-2][1],
                                        p[0]-h[-1][0], p[1]-h[-1][1]) <= 0:
                h.pop()
            h.append(p)
        return h
    lo = build(P)
    hi = build(P[::-1])
    return lo[:-1] + hi[:-1]

def signed2A(H):
    s = 0
    n = len(H)
    for i in range(n):
        x1, y1 = H[i]
        x2, y2 = H[(i+1) % n]
        s += x1 * y2 - x2 * y1
    return s

def origin_strict_inside(H):
    n = len(H)
    for i in range(n):
        ax, ay = H[i]
        bx, by = H[(i+1) % n]
        if ax * by - ay * bx <= 0:
            return False
    return True

def on_seg(a, b, p):
    if (b[0]-a[0])*(p[1]-a[1]) != (b[1]-a[1])*(p[0]-a[0]):
        return False
    return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and \
        min(a[1], b[1]) <= p[1] <= max(a[1], b[1])

def point_status(H, p):
    n = len(H)
    touch = False
    for i in range(n):
        a, b = H[i], H[(i+1) % n]
        c = (b[0]-a[0])*(p[1]-a[1]) - (b[1]-a[1])*(p[0]-a[0])
        if c < 0:
            return 'out'
        if c == 0:
            touch = True
    if touch:
        for i in range(n):
            if on_seg(H[i], H[(i+1) % n], p):
                return 'bd'
        return 'out'
    return 'in'

def facet_normals(H):
    ns = []
    ok = True
    n = len(H)
    for i in range(n):
        ax, ay = H[i]
        bx, by = H[(i+1) % n]
        c = ax*by - ay*bx
        assert c > 0
        dx, dy = bx-ax, by-ay
        if dy % c != 0 or (-dx) % c != 0:
            ok = False
            ns.append((Fraction(dy, c), Fraction(-dx, c)))
        else:
            ns.append((dy//c, -dx//c))
    return ns, ok

def gl_equiv(VP, VQ):
    if len(VP) != len(VQ):
        return False
    SQ = set(VQ)
    LP = list(VP)
    LQ = list(VQ)
    for i, j in combinations(range(len(LP)), 2):
        a, b = LP[i], LP[j]
        detV = a[0]*b[1]-a[1]*b[0]
        if detV == 0:
            continue
        for k, l in combinations(range(len(LQ)), 2):
            for (c, d) in ((LQ[k], LQ[l]), (LQ[l], LQ[k])):
                m11 = c[0]*b[1]-d[0]*a[1]
                m12 = -c[0]*b[0]+d[0]*a[0]
                m21 = c[1]*b[1]-d[1]*a[1]
                m22 = -c[1]*b[0]+d[1]*a[0]
                if m11 % detV or m12 % detV or m21 % detV or m22 % detV:
                    continue
                m11 //= detV; m12 //= detV; m21 //= detV; m22 //= detV
                if m11*m22-m12*m21 not in (1, -1):
                    continue
                if {(m11*x+m12*y, m21*x+m22*y) for (x, y) in LP} == SQ:
                    return True
    return False

def is_parallelogram(V):
    if len(V) != 4:
        return False
    for i, j in combinations(range(4), 2):
        mx = V[i][0]+V[j][0]
        my = V[i][1]+V[j][1]
        rest = [V[k] for k in range(4) if k != i and k != j]
        if rest[0][0]+rest[1][0] == mx and rest[0][1]+rest[1][1] == my:
            return True
    return False

# ---------- enumeration over [-3,3]^2 primitive points ----------
prims = [(x, y) for x in range(-3, 4) for y in range(-3, 4)
         if not (x == 0 and y == 0) and math.gcd(x, y) == 1]
print(f"primitive search points: {len(prims)}")
assert len(prims) == 32

found = []
nsub = 0
for r in (3, 4, 5, 6):
    for S in combinations(prims, r):
        nsub += 1
        H = hull(S)
        if len(H) != r or set(H) != set(S):
            continue
        if signed2A(H) <= 0:
            H = H[::-1]
        if signed2A(H) <= 0 or not origin_strict_inside(H):
            continue
        ns, ok = facet_normals(H)
        if not ok:
            continue
        xs = [p[0] for p in H]; ys = [p[1] for p in H]
        bad = False
        interior_count = 0
        for x in range(min(xs), max(xs)+1):
            for y in range(min(ys), max(ys)+1):
                st = point_status(H, (x, y))
                if st == 'in':
                    interior_count += 1
                    if (x, y) != (0, 0):
                        bad = True
                        break
            if bad:
                break
        if bad or interior_count != 1:
            continue
        found.append(H)

print(f"subsets scanned: {nsub}, reflexive vertex-sets in box: {len(found)}")

# ---------- classification ----------
reps = []
for H in found:
    for R in reps:
        if gl_equiv(H, R):
            break
    else:
        reps.append(H)
print(f"GL(2,Z)-classes: {len(reps)}")
assert len(reps) == 16, f"expected 16 classes, got {len(reps)}"

# ---------- per-class exact data ----------
def boundary_count(H):
    xs = [p[0] for p in H]; ys = [p[1] for p in H]
    B = 0
    for x in range(min(xs)-1, max(xs)+2):
        for y in range(min(ys)-1, max(ys)+2):
            if point_status(H, (x, y)) == 'bd':
                B += 1
    return B

rows = []
for H in reps:
    ns, ok = facet_normals(H)
    assert ok
    D = hull(ns)
    assert set(D) == set(ns)
    if signed2A(D) <= 0:
        D = D[::-1]
    A2 = signed2A(H)
    B2 = signed2A(D)
    assert A2 > 0 and B2 > 0
    vol = Fraction(A2, 2); vold = Fraction(B2, 2)
    M = vol * vold
    B = boundary_count(H)
    Bd = boundary_count(D)
    assert A2 == B, (H, A2, B)          # Pick's cross-check (I=1)
    assert B + Bd == 12, (H, B, Bd)     # Twelve-Point cross-check
    ns2, ok2 = facet_normals(D)
    assert ok2 and set(ns2) == set(H)   # duality involution
    sym = (set((-x, -y) for (x, y) in H) == set(H))
    rows.append(dict(verts=sorted(H), dual=sorted(D), n=len(H), b=B, bd=Bd,
                     vol=str(vol), vold=str(vold), mahler=str(M),
                     Mfrac=[M.numerator, M.denominator],
                     symmetric=sym, parallelogram=is_parallelogram(H)))

rows.sort(key=lambda r: (Fraction(r['Mfrac'][0], r['Mfrac'][1]), r['n'], r['verts']))
for i, r in enumerate(rows):
    r['id'] = i + 1

# duality-pairing consistency: each dual is GL(2,Z)-equivalent to some rep in table
for r in rows:
    hit = [q for q in rows if gl_equiv(r['dual'], q['verts'])]
    assert hit, r
    assert hit[0]['mahler'] == r['mahler'], (r, hit[0])

sym_rows = [r for r in rows if r['symmetric']]
hex_rows = [r for r in sym_rows if not r['parallelogram']]
print(f"symmetric classes: {len(sym_rows)}, parallelograms: "
      f"{sum(1 for r in sym_rows if r['parallelogram'])}, "
      f"symmetric non-parallelograms: {len(hex_rows)}")
for r in rows:
    print(r['id'], r['verts'], 'n=%d b=%d bd*=%d' % (r['n'], r['b'], r['bd']),
          'vol=%s vol*=%s M=%s' % (r['vol'], r['vold'], r['mahler']),
          'SYM' if r['symmetric'] else '', 'PARA' if r['parallelogram'] else '')

Ms = [Fraction(*r['Mfrac']) for r in rows]
print("global min:", min(Ms), "global max:", max(Ms))
if hex_rows:
    hmin = min(Fraction(*r['Mfrac']) for r in hex_rows)
    print("min symmetric-nonparallelogram Mahler:", hmin, " gap G =", hmin - 8)

out = dict(n_classes=len(rows), table=rows,
           global_min=str(min(Ms)), global_max=str(max(Ms)),
           elapsed_s=round(time.time()-t0, 1))
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'mahler_table.json'), 'w') as f:
    json.dump(out, f, indent=2)
with open(os.path.join(here, 'mahler_table.csv'), 'w') as f:
    f.write('id,n,boundary,boundary_dual,vol,vol_dual,mahler,symmetric,parallelogram,vertices\n')
    for r in rows:
        f.write(f"{r['id']},{r['n']},{r['b']},{r['bd']},{r['vol']},{r['vold']},{r['mahler']},{r['symmetric']},{r['parallelogram']},\"{r['verts']}\"\n")
print("wrote mahler_table.json / mahler_table.csv in %.1fs" % (time.time()-t0,))
