#!/usr/bin/env python3
"""Enumerate PG(4,5): 781 normalized points, 20306 lines. Stdlib only."""
import hashlib, json, time, os
BASE = os.path.dirname(os.path.abspath(__file__))

Q = 5
N = 5  # dimension of vector space GF(5)^5; projective dim 4

def normalize(v):
    # v: tuple len 5 over GF5, nonzero; scale so first nonzero == 1
    for x in v:
        if x != 0:
            inv = pow(x, -1, 5)
            return tuple((y * inv) % 5 for y in v)
    raise ValueError("zero vector")

def main():
    t0 = time.time()
    # enumerate points
    points = []
    index = {}
    # iterate over all 5^5-1 = 3124 nonzero vectors, keep normalized
    # direct product loop
    for n in range(5**5):
        if n == 0:
            continue
        v = []
        m = n
        for _ in range(5):
            v.append(m % 5)
            m //= 5
        v = tuple(v)
        # normalize: first nonzero (in order v[0..4]) == 1
        # find first nonzero
        for x in v:
            if x != 0:
                if x == 1:
                    # check if already canonical? need full normalize check:
                    pass
                break
        w = normalize(v)
        if w not in index:
            index[w] = len(points)
            points.append(w)
    assert len(points) == 781, f"got {len(points)}"
    print(f"points: {len(points)}  ({time.time()-t0:.2f}s)")

    # enumerate lines: span of each pair
    # map point tuple -> idx already have
    lines_set = set()
    # for speed, store points as lists
    pts = points
    npts = len(pts)
    t1 = time.time()
    for i in range(npts):
        a = pts[i]
        for j in range(i+1, npts):
            b = pts[j]
            # compute 6 points on line: [b] + [a + t b]
            # a,b as tuples
            linepts = [j]  # [b]
            # unroll t=0..4
            for t in range(5):
                c = tuple((x + t*y) % 5 for x, y in zip(a, b))
                # c could be zero? a+tb=0 means a,b scalar multiples -> same projective point, but i!=j so never zero
                if all(v == 0 for v in c):
                    linepts = None
                    break
                cn = normalize(c)
                linepts.append(index[cn])
            if linepts is None:
                continue
            key = tuple(sorted(linepts))
            # key must have 6 distinct entries
            if len(set(key)) != 6:
                print("BAD line", i, j, key)
                raise SystemExit(1)
            lines_set.add(key)
    lines = sorted(lines_set)
    print(f"lines: {len(lines)}  ({time.time()-t1:.2f}s)")
    assert len(lines) == 20306, f"got {len(lines)}"
    # verify each line has 6 points
    # verify lines-per-point = 156
    from collections import Counter
    cnt = Counter()
    for L in lines:
        for p in L:
            cnt[p] += 1
    vals = set(cnt.values())
    print("lines-per-point values:", vals)
    assert vals == {156}, vals
    # checksum
    import struct
    h2 = hashlib.sha256()
    for L in lines:
        for p in L:
            h2.update(struct.pack("<H", p))
    print("sha256(lines, u16le):", h2.hexdigest())
    # save
    with open(os.path.join(BASE, "points.json"), "w") as f:
        json.dump(points, f)
    # save lines as list of lists
    with open(os.path.join(BASE, "lines.json"), "w") as f:
        json.dump(lines, f)
    print(f"total time {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
