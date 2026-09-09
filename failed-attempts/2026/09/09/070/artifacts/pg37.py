"""PG(3,7) exact model; line-stabilizer H orbit partition and tactical matrix.

All arithmetic exact over F7 with stdlib only.
l* = span(e1, e2). Every point classified on/off l*; every line classified as
l* / concurrent-with-l* / skew-to-l*. Counts and per-type meeting numbers are
computed by exhaustive enumeration (all 400 points, 2850 lines).
Uniformity of meeting numbers within a type is verified for EVERY line
(no transitivity assumption needed for the numbers themselves).
"""
import itertools, json

Q = 7

def norm_point(v):
    # canonical rep of 1-space: first nonzero coord scaled to 1
    for i, c in enumerate(v):
        if c % Q != 0:
            inv = pow(c, -1, Q)
            return tuple((x * inv) % Q for x in v)
    raise ValueError

def all_points():
    pts = set()
    for v in itertools.product(range(Q), repeat=4):
        if all(c == 0 for c in v):
            continue
        pts.add(norm_point(v))
    return sorted(pts)

def line_key(a, b):
    # canonical rep of 2-space span(a,b): sorted tuple of its 8 points
    pts = set()
    for s in range(Q):
        for t in range(Q):
            if s == 0 and t == 0:
                continue
            v = tuple((s * x + t * y) % Q for x, y in zip(a, b))
            pts.add(norm_point(v))
    assert len(pts) == Q + 1
    return tuple(sorted(pts))

def all_lines(points):
    lines = set()
    P = list(points)
    n = len(P)
    for i in range(n):
        for j in range(i + 1, n):
            # check independent
            a, b = P[i], P[j]
            # dependent iff scalar multiples; normalized so equal iff same point
            lines.add(line_key(a, b))
    return sorted(lines)

def main():
    points = all_points()
    assert len(points) == Q**3 + Q**2 + Q + 1 == 400, len(points)
    lines = all_lines(points)
    nlines_expected = (Q**2 + 1) * (Q**2 + Q + 1)
    assert len(lines) == nlines_expected == 2850, len(lines)

    e1 = (1, 0, 0, 0); e2 = (0, 1, 0, 0)
    e3 = (0, 0, 1, 0); e4 = (0, 0, 0, 1)
    lstar = line_key(e1, e2)
    lstar_set = set(lstar)
    assert len(lstar_set) == 8

    on = [p for p in points if p in lstar_set]
    off = [p for p in points if p not in lstar_set]
    assert len(on) == 8 and len(off) == 392

    # classify lines
    O0, O1, O2 = [], [], []
    for L in lines:
        s = set(L)
        if L == lstar:
            O0.append(L)
        elif s & lstar_set:
            O1.append(L)
        else:
            O2.append(L)
    assert len(O0) == 1 and len(O1) == 448 and len(O2) == 2401, \
        (len(O0), len(O1), len(O2))

    # incidence: point -> lines through it
    pt_lines = {p: [] for p in points}
    for idx, L in enumerate(lines):
        for p in L:
            pt_lines[p].append(idx)
    # every point on 57 lines
    assert all(len(v) == Q**2 + Q + 1 for v in pt_lines.values())

    line_index = {L: i for i, L in enumerate(lines)}
    O0i = {line_index[L] for L in O0}
    O1i = {line_index[L] for L in O1}
    O2i = {line_index[L] for L in O2}

    def meet_counts(li):
        L = lines[li]
        seen = set()
        for p in L:
            seen.update(pt_lines[p])
        seen.discard(li)
        c0 = len(seen & O0i); c1 = len(seen & O1i); c2 = len(seen & O2i)
        assert c0 + c1 + c2 == 448, (c0, c1, c2)
        return (c0, c1, c2)

    # verify uniformity over EVERY line in each orbit
    from collections import Counter
    for name, orb in (("O0", O0), ("O1", O1), ("O2", O2)):
        cnt = Counter()
        for L in orb:
            cnt[meet_counts(line_index[L])] += 1
        print(name, "size", len(orb), "meeting-type histogram:", dict(cnt))
        assert len(cnt) == 1, (name, cnt)

    print("POINTS:", len(points), "on:", len(on), "off:", len(off))
    print("LINES:", len(lines), "O0:", len(O0), "O1:", len(O1), "O2:", len(O2))
    print("ALL CHECKS PASSED")

if __name__ == "__main__":
    main()
