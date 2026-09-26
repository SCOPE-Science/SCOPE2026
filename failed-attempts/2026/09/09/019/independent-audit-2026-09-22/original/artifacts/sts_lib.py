"""Shared stdlib-only library for STS(13)/STS(15) Pasch census (lane-300)."""
import hashlib
import itertools
import json


def canon_block(b):
    return tuple(sorted(b))


def canon_system(blocks):
    return tuple(sorted(tuple(sorted(b)) for b in blocks))


def sha_of_system(blocks):
    return hashlib.sha256(repr(canon_system(blocks)).encode()).hexdigest()[:16]


def verify_sts(blocks, v):
    """Return (ok, msg). Checks block count, triple size, each pair exactly once."""
    b = v * (v - 1) // 6
    if len(blocks) != b:
        return False, "wrong block count %d != %d" % (len(blocks), b)
    seen = set()
    for B in blocks:
        if len(set(B)) != 3:
            return False, "bad block %r" % (B,)
        for x, y in itertools.combinations(sorted(set(B)), 2):
            if (x, y) in seen:
                return False, "pair repeated %r" % ((x, y),)
            seen.add((x, y))
    if len(seen) != v * (v - 1) // 2:
        return False, "pairs covered %d" % len(seen)
    return True, "ok"


def third_table(blocks, v):
    t = [[-1] * v for _ in range(v)]
    for B in blocks:
        a, b, c = sorted(set(B))
        t[a][b] = t[b][a] = c
        t[a][c] = t[c][a] = b
        t[b][c] = t[c][b] = a
    return t


def block_masks(blocks):
    ms = []
    for B in blocks:
        m = 0
        for x in B:
            m |= 1 << x
        ms.append(m)
    return ms


def pasch_fast(blocks, v):
    """Count Pasch configurations via intersecting-pair completion.

    In an STS, 4 blocks form a Pasch iff every pair meets in exactly one
    point and the union has 6 points. For an intersecting pair B1,B2 with
    B1 cap B2 = {p}, B1={p,a,b}, B2={p,c,d}, a Pasch completion exists iff
    block(a,c)={a,c,z} and block(b,z) contains d (pairing (a,c)|(b,d)), or
    the (a,d)|(b,c) analogue. Each Pasch is found exactly 6 times.
    """
    t = third_table(blocks, v)
    ms = block_masks(blocks)
    n = len(blocks)
    pts = [None] * n
    for i, B in enumerate(blocks):
        pts[i] = sorted(set(B))
    cnt = 0
    for i in range(n):
        mi = ms[i]
        for j in range(i + 1, n):
            inter = mi & ms[j]
            if inter == 0 or (inter & (inter - 1)):
                continue  # disjoint or share 2 (latter impossible in STS)
            p = inter.bit_length() - 1
            a, b = [x for x in pts[i] if x != p]
            c, d = [x for x in pts[j] if x != p]
            z1 = t[a][c]
            if t[b][z1] == d:
                cnt += 1
            z2 = t[a][d]
            if t[b][z2] == c:
                cnt += 1
    assert cnt % 6 == 0, "pasch completion count not divisible by 6: %d" % cnt
    return cnt // 6


def pasch_bruteforce(blocks):
    """Independent definition-level counter: 4-subsets whose union is 6 points.

    Lemma: in an STS any 4 distinct blocks with 6-point union form a Pasch
    (3 blocks through one point already cover 7 points, so max degree <= 2,
    hence every degree == 2 since 4*3 = 2*6).
    """
    ms = block_masks(blocks)
    n = len(blocks)
    cnt = 0
    for q in itertools.combinations(range(n), 4):
        u = ms[q[0]] | ms[q[1]] | ms[q[2]] | ms[q[3]]
        if bin(u).count("1") == 6:
            cnt += 1
    return cnt


def find_one_pasch(blocks):
    """Return 4 block indices forming a Pasch, or None (brute force)."""
    ms = block_masks(blocks)
    n = len(blocks)
    for q in itertools.combinations(range(n), 4):
        u = ms[q[0]] | ms[q[1]] | ms[q[2]] | ms[q[3]]
        if bin(u).count("1") == 6:
            return list(q)
    return None


def apply_perm(blocks, p):
    return canon_system(tuple(p[x] for x in B) for B in blocks)


def find_iso(A, B, v, limit=1):
    """Backtracking isomorphisms A -> B. Returns list of perms (<= limit; None = all)."""
    tA = third_table(A, v)
    tB = third_table(B, v)
    Asets = [set(B_) for B_ in A]
    Bsets = [set(B_) for B_ in B]
    f = [-1] * v
    used = [False] * v
    mapped = [False] * v
    out = []

    def consistent(x, y):
        for z in range(v):
            if mapped[z]:
                w = tA[x][z]
                if w == -1:
                    return False
                if mapped[w]:
                    if f[w] != tB[y][f[z]]:
                        return False
        return True

    def rec(nmapped):
        if limit is not None and len(out) >= limit:
            return True
        if nmapped == v:
            out.append(list(f))
            return limit is not None and len(out) >= limit
        # prefer a forced point (third of two mapped), else smallest unmapped
        forced = None
        for a in range(v):
            if not mapped[a]:
                continue
            for b in range(a + 1, v):
                if not mapped[b]:
                    continue
                w = tA[a][b]
                if not mapped[w]:
                    forced = (w, tB[f[a]][f[b]])
                    break
            if forced:
                break
        if forced is not None:
            x, y = forced
            if not used[y] and consistent(x, y):
                f[x] = y
                used[y] = True
                mapped[x] = True
                if rec(nmapped + 1):
                    pass
                mapped[x] = False
                used[y] = False
                f[x] = -1
            return False
        x = next(i for i in range(v) if not mapped[i])
        for y in range(v):
            if used[y]:
                continue
            if consistent(x, y):
                f[x] = y
                used[y] = True
                mapped[x] = True
                stop = rec(nmapped + 1)
                mapped[x] = False
                used[y] = False
                f[x] = -1
                if stop:
                    return True
        return False

    rec(0)
    return out


def aut_order(blocks, v):
    return len(find_iso(blocks, blocks, v, limit=None))


def cyclic_sts(v, base_blocks):
    blks = set()
    for B in base_blocks:
        for s in range(v):
            blks.add(canon_block([(x + s) % v for x in B]))
    return sorted(blks)


def pg32():
    """PG(3,2): 15 nonzero vectors of F2^4, blocks = lines {x,y,x+y}."""
    pts = list(range(1, 16))
    blks = set()
    for x in pts:
        for y in pts:
            if y <= x:
                continue
            z = x ^ y
            if z == 0 or z == x or z == y:
                continue
            blks.add(canon_block([x - 1, y - 1, z - 1]))
    return sorted(blks)
