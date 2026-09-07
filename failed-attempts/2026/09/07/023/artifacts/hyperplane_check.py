#!/usr/bin/env python3
"""Verify hyperplane incidences in PG(4,5) and plane incidences in PG(3,5). Stdlib only."""
import json, os, time
BASE = os.path.dirname(os.path.abspath(__file__))

def normalize(v):
    for x in v:
        if x != 0:
            inv = pow(x, -1, 5)
            return tuple((y*inv) % 5 for y in v)
    raise ValueError

def main():
    t0 = time.time()
    with open(os.path.join(BASE, "points.json")) as f:
        pts4 = [tuple(p) for p in json.load(f)]
    with open(os.path.join(BASE, "lines.json")) as f:
        lines4 = [tuple(L) for L in json.load(f)]
    assert len(pts4) == 781 and len(lines4) == 20306
    # hyperplanes: a.x = 0 for each dual point a (781 equations, each gives 156 points)
    # enumerate distinct hyperplanes as frozensets? 781*781 dot products = 610k, fine
    n = 781
    # map point index -> list? compute incidence via dot products
    # hyperplanes indexed by same 781 (dual point a)
    # count points per hyperplane
    import collections
    hsize = []
    pt_on_h = [0]*n
    for a in pts4:
        c = 0
        for i, p in enumerate(pts4):
            if sum(x*y for x, y in zip(a, p)) % 5 == 0:
                c += 1
                pt_on_h[i] += 1
        hsize.append(c)
    print("hyperplane sizes: set =", set(hsize), "(expect {156})")
    assert set(hsize) == {156}
    print("hyperplanes per point: set =", set(pt_on_h), "(expect {156})")
    assert set(pt_on_h) == {156}
    # hyperplanes per pair (line): for each line, count a with a.p=0 for all p in line (i.e., a orthogonal to 2-dim span)
    # equivalently a orthogonal to first two points of line (since they span)
    # sample all 20306 lines: for each, count
    vals = set()
    for L in lines4:
        p, q = pts4[L[0]], pts4[L[1]]
        c = sum(1 for a in pts4 if sum(x*y for x, y in zip(a, p)) % 5 == 0 and sum(x*y for x, y in zip(a, q)) % 5 == 0)
        vals.add(c)
    print("hyperplanes per line (pair): set =", vals, "(expect {31})")
    assert vals == {31}
    print(f"PG(4,5) hyperplane incidences VERIFIED ({1000*(time.time()-t0):.0f} ms)")
    # PG(3,5) check: enumerate points (156) and planes (156)
    t1 = time.time()
    pts3, idx3 = [], {}
    for nn in range(5**4):
        if nn == 0: continue
        v, m = [], nn
        for _ in range(4):
            v.append(m % 5); m //= 5
        w = normalize(tuple(v))
        if w not in idx3:
            idx3[w] = len(pts3); pts3.append(w)
    assert len(pts3) == 156, len(pts3)
    # planes: a.x=0
    psize = []
    pt_on_p = [0]*156
    for a in pts3:
        c = 0
        for i, p in enumerate(pts3):
            if sum(x*y for x, y in zip(a, p)) % 5 == 0:
                c += 1; pt_on_p[i] += 1
        psize.append(c)
    print("PG(3,5) plane sizes: set =", set(psize), "(expect {31})")
    assert set(psize) == {31}
    print("PG(3,5) planes per point: set =", set(pt_on_p), "(expect {31})")
    assert set(pt_on_p) == {31}
    # lines in PG(3,5): enumerate to check planes per line = 6
    seen = set()
    for i in range(156):
        a = pts3[i]
        for j in range(i+1, 156):
            b = pts3[j]
            lp = [j]
            for t in range(5):
                c = tuple((x+t*y) % 5 for x, y in zip(a, b))
                # skip zero (same point case already excluded)
                import math
                if all(v == 0 for v in c):
                    lp = None; break
                lp.append(idx3[normalize(c)])
            if lp is None: continue
            key = tuple(sorted(set(lp)))
            if len(key) == 6:
                seen.add(key)
    lines3 = sorted(seen)
    print(f"PG(3,5) lines: {len(lines3)} (expect 806? check: 156*31/6=806)")
    assert len(lines3) == 806, len(lines3)
    vals3 = set()
    for L in lines3:
        p, q = pts3[L[0]], pts3[L[1]]
        c = sum(1 for a in pts3 if sum(x*y for x, y in zip(a, p)) % 5 == 0 and sum(x*y for x, y in zip(a, q)) % 5 == 0)
        vals3.add(c)
    print("PG(3,5) planes per line: set =", vals3, "(expect {6})")
    assert vals3 == {6}
    print(f"PG(3,5) incidences VERIFIED ({1000*(time.time()-t1):.0f} ms)")
    print("ALL INCIDENCE LEMMAS VERIFIED")

if __name__ == "__main__":
    main()
