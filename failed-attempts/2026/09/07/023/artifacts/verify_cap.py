#!/usr/bin/env python3
"""Independent verifier: re-enumerates PG(4,5) lines from scratch, checks cap, completeness, hyperplane spectrum. Stdlib only."""
import json, os, sys, time, hashlib, struct

BASE = os.path.dirname(os.path.abspath(__file__))

def normalize(v):
    for x in v:
        if x != 0:
            inv = pow(x, -1, 5)
            return tuple((y*inv) % 5 for y in v)
    raise ValueError

def enum_points():
    pts, idx = [], {}
    for n in range(5**5):
        if n == 0: continue
        v, m = [], n
        for _ in range(5):
            v.append(m % 5); m //= 5
        w = normalize(tuple(v))
        if w not in idx:
            idx[w] = len(pts); pts.append(w)
    return pts, idx

def enum_lines(pts, idx):
    seen = set()
    n = len(pts)
    for i in range(n):
        a = pts[i]
        for j in range(i+1, n):
            b = pts[j]
            lp = [j]
            for t in range(5):
                c = tuple((x+t*y) % 5 for x, y in zip(a, b))
                lp.append(idx[normalize(c)])
            key = tuple(sorted(lp))
            assert len(set(key)) == 6
            seen.add(key)
    return sorted(seen)

def main():
    t0 = time.time()
    capfile = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "best_cap.json")
    with open(capfile) as f:
        d = json.load(f)
    cap_idx = sorted(d["indices"])
    cap_coords = [tuple(c) for c in d["coords"]]
    print(f"cap size claimed: {d['size']}, indices {len(cap_idx)}")
    pts, idx = enum_points()
    print(f"re-enumerated points: {len(pts)} ({1000*(time.time()-t0):.0f} ms)")
    assert len(pts) == 781
    # verify coords match indices
    for i, c in zip(cap_idx, cap_coords):
        assert tuple(pts[i]) == c, f"coord mismatch at {i}"
    print("coordinate-index consistency: OK")
    t1 = time.time()
    lines = enum_lines(pts, idx)
    print(f"re-enumerated lines: {len(lines)} ({1000*(time.time()-t1):.0f} ms)")
    assert len(lines) == 20306
    h = hashlib.sha256()
    for L in lines:
        for p in L:
            h.update(struct.pack("<H", p))
    print("lines sha256:", h.hexdigest())
    S = set(cap_idx)
    mx = 0
    bad = 0
    for L in lines:
        c = sum(1 for p in L if p in S)
        if c > mx: mx = c
        if c >= 3: bad += 1
    print(f"max line occupancy: {mx}")
    print(f"lines with >=3 cap points: {bad}")
    assert mx <= 2, "NOT A CAP"
    print("CAP PROPERTY: VERIFIED (no three collinear)")
    # completeness: every outside point on a secant (line with exactly 2 cap points)
    secants = set()
    sec_lines = []
    for L in lines:
        c = [p for p in L if p in S]
        if len(c) == 2:
            sec_lines.append(L)
            for p in L:
                if p not in S:
                    secants.add(p)
    outside = [p for p in range(781) if p not in S]
    uncovered = [p for p in outside if p not in secants]
    print(f"secant lines (exactly 2 cap pts): {len(sec_lines)}")
    print(f"outside points: {len(outside)}, covered by secant: {len(secants)}, uncovered: {len(uncovered)}")
    if uncovered:
        print("INCOMPLETE cap (extendable); example uncovered:", uncovered[:5])
    else:
        print("COMPLETENESS: VERIFIED (every outside point on a secant -> maximal, complete cap)")
    # hyperplane spectrum: hyperplanes a.x=0 for a in pts (781 hyperplanes)
    import collections
    spec = collections.Counter()
    for a in pts:
        c = sum(1 for i in cap_idx if sum(x*y for x, y in zip(a, pts[i])) % 5 == 0)
        spec[c] += 1
    print("hyperplane-section spectrum {size: count}:", dict(sorted(spec.items())))
    # secant distribution? weight: number of secants through each cap point
    print(f"total time {1000*(time.time()-t0):.0f} ms")

if __name__ == "__main__":
    main()
