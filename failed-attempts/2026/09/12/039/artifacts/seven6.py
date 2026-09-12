"""10-partition search via 7x6+3x5 decomposition.
Arithmetic: 57 blocks in 10 classes of size<=6 needs >=7 six-classes.
So 10-colorable <=> 7 pairwise-disjoint 6-matchings whose 15-block remainder
splits into 3 matchings. Modes: heur (randomized) | exact (Algorithm-X exhaustive).
"""
import sys, time, random

A = [
    ((0, 1, 4), (0, 2, 9), (0, 5, 11)),
    ((0, 1, 4), (0, 2, 12), (0, 5, 13)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 10)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 13)),
]
V = 19
which = int(sys.argv[1]) if len(sys.argv) > 1 else 0
mode = sys.argv[2] if len(sys.argv) > 2 else "heur"
BUDGET = float(sys.argv[3]) if len(sys.argv) > 3 else 300


def develop(fam):
    B = set()
    for t in fam:
        for s in range(V):
            B.add(frozenset((x + s) % V for x in t))
    return sorted(B)


blocks = develop(A[which])
m = len(blocks)
bmask = []
for b in blocks:
    mm = 0
    for x in b:
        mm |= 1 << x
    bmask.append(mm)
bidx = {b: i for i, b in enumerate(blocks)}

# all maximal matchings; six-matchings are maximal (cover 18 pts)
mmall = []
sys.setrecursionlimit(10000)


def rec(chosen, usedpts, cand):
    if not cand:
        mmall.append(tuple(chosen))
        return
    v = cand[0]
    rest = cand[1:]
    bv = bmask[v]
    rec(chosen + [v], usedpts | bv, [u for u in rest if not (bmask[u] & bv)])
    rec(chosen, usedpts, rest)


rec([], 0, list(range(m)))
six = [t for t in mmall if len(t) == 6]
print(f"A{which+1}: maximal={len(mmall)} six={len(six)}", flush=True)

# block-mask (57-bit) per six-matching + contain lists
smask = []
for t in six:
    q = 0
    for i in t:
        q |= 1 << i
    smask.append(q)
contain = [[] for _ in range(m)]
for mi, t in enumerate(six):
    for i in t:
        contain[i].append(mi)

# shift permutation on block indices
def shift_idx(s):
    out = [0] * m
    for i, b in enumerate(blocks):
        out[i] = bidx[frozenset((x + s) % V for x in b)]
    return out

sh = [shift_idx(s) for s in range(V)]


def mcanon(mi):
    t = six[mi]
    best = None
    for s in range(V):
        img = tuple(sorted(sh[s][i] for i in t))
        if best is None or img < best:
            best = img
    return best


seen = set()
reps = []
for mi in range(len(six)):
    c = mcanon(mi)
    if c not in seen:
        seen.add(c)
        reps.append(mi)
print(f"A{which+1}: cyc-orbit reps of six-matchings: {len(reps)}", flush=True)

FULL = (1 << m) - 1

# ---- remainder check: can block-set (int mask, popcount<=15) split into <=K matchings?
from functools import lru_cache

# maximal matchings restricted: use mmall as block masks
mm_blk = []
for t in mmall:
    q = 0
    for i in t:
        q |= 1 << i
    mm_blk.append(q)


def coverable(rem, K):
    # B&B: pick lowest set bit, branch over sub-matchings of rem covering it
    if rem == 0:
        return True
    if K == 0:
        return False
    # bound: popcount(rem) <= 6*K for maxsize-6 systems (A4: 5*K)
    import math
    cap = 5 if which == 3 else 6
    n = bin(rem).count("1")
    if n > cap * K:
        return False
    v = (rem & -rem).bit_length() - 1  # lowest set bit index
    # candidate sub-matchings: maximal matchings of rem containing v -> use subsets:
    # branch over maximal matchings M with M&rem covering v... simpler: branch over
    # choice of matching = maximal matching of rem containing v (from mm_blk with M<=rem)
    cands = [M for M in mm_blk if (M & rem) and (M | rem) == rem and (M & (1 << v))]
    # dedupe M&rem
    seenM = set()
    uniq = []
    for M in cands:
        Mr = M & rem
        if Mr not in seenM:
            seenM.add(Mr)
            uniq.append(Mr)
    uniq.sort(key=lambda M: -bin(M).count("1"))
    for Mr in uniq:
        if coverable(rem & ~Mr, K - 1):
            return True
    return False


t0 = time.time()

if mode == "heur":
    random.seed(1000 + which)
    tries = 0
    order = list(range(len(six)))
    sol = None
    while time.time() - t0 < BUDGET:
        tries += 1
        random.shuffle(order)
        used = 0
        chosen = []
        for mi in order:
            if not (smask[mi] & used):
                used |= smask[mi]
                chosen.append(mi)
                if len(chosen) == 7:
                    break
        if len(chosen) == 7 and coverable(FULL & ~used, 3):
            sol = (list(chosen), FULL & ~used)
            break
    print(f"heur tries={tries} t={time.time()-t0:.0f}s solved={sol is not None}", flush=True)
    if sol:
        # reconstruct full 10-partition: 7 six-classes + cover remainder in 3
        rem = sol[1]
        # greedy recover the 3 classes
        classes = [list(six[mi]) for mi in sol[0]]
        # find 3-cover explicitly
        def findcov(rem, K):
            if rem == 0:
                return []
            if K == 0:
                return None
            v = (rem & -rem).bit_length() - 1
            cands = [M for M in mm_blk if (M | rem) == rem and (M & (1 << v))]
            seenM = set()
            uniq = []
            for M in cands:
                Mr = M & rem
                if Mr not in seenM:
                    seenM.add(Mr)
                    uniq.append(Mr)
            uniq.sort(key=lambda M: -bin(M).count("1"))
            for Mr in uniq:
                out = findcov(rem & ~Mr, K - 1)
                if out is not None:
                    return [Mr] + out
            return None
        cov = findcov(rem, 3)
        for Mr in cov:
            classes.append([i for i in range(m) if (Mr >> i) & 1])
        with open(f"partition10_A{which+1}.txt", "w") as fh:
            for ci, cl in enumerate(classes):
                fh.write(f"class {ci} ({len(cl)} blocks):\n")
                for i in sorted(cl):
                    fh.write("  " + repr(sorted(blocks[i])) + "\n")
        print(f"WROTE partition10_A{which+1}.txt sizes={sorted(len(c) for c in classes)}", flush=True)
else:
    # exact: depth-0 restricted to orbit reps; Algorithm-X selection afterwards
    nodes = [0]
    timed = [False]
    solved = [None]

    def dfs(used, depth, chosen):
        nodes[0] += 1
        if solved[0] is not None or (time.time() - t0 > BUDGET):
            timed[0] = True
            return
        if depth == 7:
            if coverable(FULL & ~used, 3):
                solved[0] = list(chosen)
            return
        # select uncovered block with fewest live options
        bestv, bestopts = -1, None
        r = FULL & ~used
        rr = r
        while rr:
            lsb = rr & -rr
            v = lsb.bit_length() - 1
            rr ^= lsb
            opts = [mi for mi in contain[v] if not (smask[mi] & used)]
            if not opts:
                return  # dead: v in no six-matching -> this branch can't reach 7
            if bestopts is None or len(opts) < len(bestopts):
                bestv, bestopts = v, opts
                if len(bestopts) == 1:
                    break
        if depth == 0:
            bestopts = [mi for mi in bestopts if mi in set(reps)]
        for mi in bestopts:
            chosen.append(mi)
            dfs(used | smask[mi], depth + 1, chosen)
            chosen.pop()
            if solved[0] is not None or timed[0]:
                return

    dfs(0, 0, [])
    print(f"exact t={time.time()-t0:.0f}s nodes={nodes[0]} solved={solved[0] is not None} timedout={timed[0] and solved[0] is None}", flush=True)
    if solved[0] is not None:
        print("six-tuple found (10-partition EXISTS); run heur mode to write it", flush=True)
    elif not timed[0]:
        print("CERTIFIED: no 7 disjoint six-matchings with 3-coverable remainder => NO 10-PARTITION", flush=True)
