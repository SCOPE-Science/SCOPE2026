#!/usr/bin/env python3
"""Prove m2(2,5)=6: exhibit oval + exhaustive proof no 7-cap. Stdlib only."""
import itertools, time

def normalize(v):
    for x in v:
        if x != 0:
            inv = pow(x, -1, 5)
            return tuple((y*inv) % 5 for y in v)
    raise ValueError

def enum_pg2():
    pts, idx = [], {}
    for n in range(5**3):
        if n == 0: continue
        v, m = [], n
        for _ in range(3):
            v.append(m % 5); m //= 5
        w = normalize(tuple(v))
        if w not in idx:
            idx[w] = len(pts); pts.append(w)
    assert len(pts) == 31, len(pts)
    # lines: spans of pairs
    seen = set()
    for i in range(len(pts)):
        a = pts[i]
        for j in range(i+1, len(pts)):
            b = pts[j]
            lp = [j]
            for t in range(5):
                c = tuple((x+t*y) % 5 for x, y in zip(a, b))
                lp.append(idx[normalize(c)])
            key = tuple(sorted(lp))
            assert len(set(key)) == 6, key
            seen.add(key)
    lines = sorted(seen)
    assert len(lines) == 31, len(lines)
    return pts, idx, lines

def main():
    t0 = time.time()
    pts, idx, lines = enum_pg2()
    print(f"PG(2,5): {len(pts)} points, {len(lines)} lines ({1000*(time.time()-t0):.0f} ms)")
    # oval: conic X0*X2 - X1^2 = 0
    oval = []
    for t in range(5):
        oval.append(idx[normalize((1, t, (t*t) % 5))])
    oval.append(idx[normalize((0, 0, 1))])
    oval = sorted(oval)
    print("oval indices:", oval)
    print("oval coords:", [pts[i] for i in oval])
    # verify oval: each line <=2
    S = set(oval)
    assert len(oval) == 6
    for L in lines:
        assert sum(1 for p in L if p in S) <= 2, f"oval fails on {L}"
    print("oval (6-cap) VERIFIED")
    # prove no 7-cap: fix two points by 2-transitivity.
    # Choose canonical pair: P0 = idx[(1,0,0)], P1 = idx[(0,1,0)]? check distinct & arbitrary
    p0 = idx[normalize((1, 0, 0))]
    p1 = idx[normalize((0, 1, 0))]
    print(f"fixed pair: {p0} {pts[p0]}, {p1} {pts[p1]}")
    # line through p0,p1
    # find forbidden (other 4 on same line)
    lop = {}
    for li, L in enumerate(lines):
        for a in range(6):
            for b in range(a+1, 6):
                lop[(L[a], L[b])] = li
                lop[(L[b], L[a])] = li
    li01 = lop[(p0, p1)]
    forb = set(lines[li01]) - {p0, p1}
    print(f"line(p0,p1)={lines[li01]}, forbidden others={sorted(forb)}")
    cands = [i for i in range(31) if i not in set(lines[li01])]
    print(f"candidates after fixing pair: {len(cands)} (expect 25)")
    assert len(cands) == 25
    # need to check all 5-subsets of cands that together with {p0,p1} form cap
    # i.e., no three collinear among the 7, and none with p0/p1 (already ensured by removing line, but other lines through p0/p1 with 2 cands also forbidden)
    # brute force C(25,5)=53130
    total = 0
    # precompute line membership for fast check: for each pair in cands+fixed, line's other points
    # For each 5-set, check: (a) 5-set itself cap, (b) no line through p0 contains 2 of 5-set? Actually line through p0 and c contains no other of set; similarly p1.
    # Equivalent: full 7-set has max occupancy <=2
    # Use line sets for check
    line_sets = [set(L) for L in lines]
    # map point -> lines containing it
    from collections import defaultdict
    pt_lines = defaultdict(list)
    for li, L in enumerate(lines):
        for p in L:
            pt_lines[p].append(li)
    n_checked = 0
    t1 = time.time()
    for combo in itertools.combinations(cands, 5):
        n_checked += 1
        full = (p0, p1) + combo
        S7 = set(full)
        ok = True
        # check all lines: quick: for each pair in full, check line has no third in S7
        # 21 pairs
        for a in range(7):
            for b in range(a+1, 7):
                li = lop[(full[a], full[b])]
                # count: if any third point of lines[li] in S7 -> fail
                # since line has 6 points, check other 4
                for p in lines[li]:
                    if p != full[a] and p != full[b] and p in S7:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            print(f"FOUND 7-cap containing fixed pair: {full}")
            raise SystemExit("7-cap exists! bound fails")
    print(f"checked {n_checked} 5-subsets (C(25,5)=53130), none extends to 7-cap")
    print(f"search time {1000*(time.time()-t1):.0f} ms")
    print("CONCLUSION: no 7-cap in PG(2,5) (by 2-transitivity reduction). Hence m2(2,5)=6.")
    print(f"total time {1000*(time.time()-t0):.0f} ms")

if __name__ == "__main__":
    main()
