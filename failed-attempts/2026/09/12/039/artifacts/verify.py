"""Independent verifier for lane-1133 claimed partitions and bounds.
Checks: STS pair coverage of A1-A4; partition10_A1 (10 classes, disjoint, covers);
partition12_A4 (12 classes, disjoint, covers); max-PPC bound for A4 (no 6 disjoint
blocks -> chi>=12); 6-matching census quick check on A4 only (bounded).
Usage: python3 verify.py
"""
import itertools

A = [
    ((0, 1, 4), (0, 2, 9), (0, 5, 11)),
    ((0, 1, 4), (0, 2, 12), (0, 5, 13)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 10)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 13)),
]
V = 19


def develop(fam):
    B = set()
    for t in fam:
        for s in range(V):
            B.add(frozenset((x + s) % V for x in t))
    return sorted(B)


def readpart(fn):
    txt = open(fn).read().strip().splitlines()
    cs = []
    cur = None
    for ln in txt:
        ln = ln.strip()
        if ln.startswith("class"):
            cur = []
            cs.append(cur)
        else:
            cur.append(frozenset(eval(ln)))
    return cs


def check_sts(w):
    B = develop(A[w])
    assert len(B) == 57, (w, len(B))
    pairs = set()
    for b in B:
        for e in itertools.combinations(sorted(b), 2):
            assert e not in pairs, (w, e)
            pairs.add(e)
    assert len(pairs) == 171, (w, len(pairs))
    print(f"A{w+1}: STS(19) OK (57 blocks, 171 pairs)")


def check_partition(w, fn, expect):
    blocks = develop(A[w])
    B = set(map(frozenset, blocks))
    cs = readpart(fn)
    assert len(cs) == expect, (fn, len(cs), expect)
    seen = set()
    for ci, c in enumerate(cs):
        pts = set()
        for b in c:
            assert b not in seen, (fn, ci, "dup")
            seen.add(b)
            assert not (set(b) & pts), (fn, ci, "clash")
            pts |= set(b)
            assert b in B, (fn, ci, "foreign")
    assert seen == B, (fn, "incomplete cover")
    print(f"{fn}: {expect}-partition of A{w+1} OK sizes={sorted(len(c) for c in cs)}")


def check_A4_bound():
    blocks = develop(A[3])
    bs = [set(b) for b in blocks]
    # exhaustive 6-disjoint search (bounded backtrack over 57 blocks)
    found = [False]

    def rec(cand, depth):
        if found[0]:
            return
        if depth == 6:
            found[0] = True
            return
        if len(cand) < 6 - depth:
            return
        v = cand[0]
        rest = cand[1:]
        rec([u for u in rest if not (bs[u] & bs[v])], depth + 1)
        rec(rest, depth)
    rec(list(range(len(blocks))), 0)
    assert not found[0], "A4 has a 6-matching?!"
    print("A4: max PPC <= 5 confirmed (no 6 disjoint blocks) => 11 classes cover <= 55 < 57 => chi(A4) >= 12")


for w in range(4):
    check_sts(w)
check_partition(0, "partition10_A1.txt", 10)
check_partition(3, "partition12_A4.txt", 12)
check_A4_bound()
print("chi(A1) <= 10 and chi(A4) = 12 (upper via partitions, lower via counting) ALL CHECKS PASSED")
