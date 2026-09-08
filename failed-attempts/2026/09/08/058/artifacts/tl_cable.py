"""Transfer-matrix Kauffman bracket for braid closures (any crossings count).
Connectivity states = set partitions of 2m boundary points (m = strands), stored canonically.
Processes braid word crossing-by-crossing from top; active points = current strand positions.
State = partition of the 2m endpoints (m top-fixed + m current). Each crossing on positions (a,a+1):
  A-smoothing: keep connectivity, weight A^{+1} (calibrate which smoothing is A per sign).
  B-smoothing: rewire: join the blocks of the two wires... standard: if the two active points are in the
    same block -> B-smoothing splits off a loop (loops+1, connectivity unchanged); else merge blocks.
Circles counted incrementally via loop events; final closure: merge current points with top points pairwise
  (closure caps) and count remaining components: result circles = loops + components(final partition).
Weights: each loop contributes factor d = -A^2 - A^-2. Bracket = sum_states A^{#A-#B} d^{circles-1}... standard:
  <D> = sum A^{a-b} d^{|S|-1} over states (unnormalized bracket, |S| = #circles).
Calibrated against kauffman_check (exact, verified vs Atlas) on trefoil/K11n34/K11n42.
"""
from copy import deepcopy

ONE = {0: 1}
def padd(a, b):
    c = dict(a)
    for e, v in b.items():
        c[e] = c.get(e, 0) + v
        if c[e] == 0: del c[e]
    return c

def canon(part):
    return tuple(sorted(tuple(sorted(b)) for b in part))

def transfer_bracket(m, word, Across_sign=+1):
    """word: list of signed generator indices (1-based). Returns ({Aexp:coef}, writhe).
    Across_sign: +1 means positive crossing's A-smoothing is the 'through' (identity) one.
    We calibrate: for positive crossing, A-smoothing = through; B = turn (standard Kauffman for
    braid orientation? verify numerically)."""
    # endpoints: top points T_j (j=0..m-1), current points C_j.
    # partition blocks over 2m labels: T_j = j, C_j = m+j. But crossings permute STRANDS: track pos->strand?
    # Connectivity only needs positions: active points are spatial positions; crossing acts on positions.
    # Initial: T_j connected to C_j (straight wires): blocks {T_j, C_j}.
    init = canon([[j, m+j] for j in range(m)])
    # states: dict partition -> [poly(A-exp->coef WITHOUT loop factors... include d powers at end), loops]
    # Simpler: states: partition -> poly where loops already multiplied as d-powers when they occur.
    d = {2: -1, -2: -1}  # d = -A^2 - A^-2
    states = {init: dict(ONE)}
    for g in word:
        a = abs(g) - 1
        pos = g > 0
        ns = {}
        for part, poly in states.items():
            # find blocks containing C_a, C_{a+1}
            blocks = [set(b) for b in part]
            ia = next(k for k,b in enumerate(blocks) if (m+a) in b)
            ib = next(k for k,b in enumerate(blocks) if (m+a+1) in b)
            # through (identity connectivity): A-smoothing if (pos and Across_sign>0) etc.
            # Convention choice: through-weight A^{+1} for positive crossing, A^{-1} for negative.
            if pos:
                wthru, wturn = {1: 1}, {-1: 1}
            else:
                wthru, wturn = {-1: 1}, {1: 1}
            # THROUGH option: connectivity unchanged
            key = part
            add = {e+ (1 if pos else -1): c for e, c in poly.items()}
            ns[key] = padd(ns.get(key, {}), add)
            # TURN option: rewire C_a-C_{a+1} locally
            if ia == ib:
                # same block: turn splits off a loop; connectivity of remaining unchanged
                # (for planar states; in general partition frameworks this needs care, but for
                # single-row braid transfer the loop count is: loop closed, partition unchanged)
                add2 = {e + (-1 if pos else 1): c for e, c in poly.items()}
                # multiply by d
                from itertools import product as _p
                nd = {}
                for e1, v1 in add2.items():
                    for e2, v2 in d.items():
                        nd[e1+e2] = nd.get(e1+e2, 0) + v1*v2
                nd = {e: v for e, v in nd.items() if v != 0}
                ns[key] = padd(ns.get(key, {}), nd)
            else:
                # merge blocks ia, ib, then the turn reconnects: new blocks: (Ba ∪ Bb ∪ {Ca,Ca+1} minus...)—
                # precise: turn pairs Ca-Ca+1 directly; the OTHER ends of their wires join:
                # find partners: in block ia, the element connected "through" Ca... general partition:
                # new partition: remove Ca from ia, remove Ca+1 from ib, merge (ia\{Ca}) ∪ (ib\{Ca+1}), add {Ca,Ca+1}.
                Bi, Bj = blocks[ia], blocks[ib]
                ni = set(Bi); ni.discard(m+a)
                nj = set(Bj); nj.discard(m+a+1)
                rest = [b for k, b in enumerate(blocks) if k not in (ia, ib)]
                newb = rest + [ni | nj, {m+a, m+a+1}]
                newb = [b for b in newb if b]
                key2 = canon(newb)
                add2 = {e + (-1 if pos else 1): c for e, c in poly.items()}
                ns[key2] = padd(ns.get(key2, {}), add2)
        states = ns
    # closure: caps join C_j to T_j. Count components: union partition with {T_j,C_j} pairs, #blocks = #circles
    # (all points paired up; each block with 2k points = ... for a 1-manifold closure, #circles = #blocks after
    # capping? Each resulting block corresponds to one circle. Yes since everything is closed loops.)
    # bracket = sum_states A^{a-b} d^{circles-1}.
    from collections import defaultdict
    tot = defaultdict(int)
    parent = {}
    for part, poly in states.items():
        blocks = [set(b) for b in part]
        # union-find over 2m points + closure pairs
        par = list(range(2*m))
        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]; x = par[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry: par[rx] = ry
        for b in blocks:
            b = list(b)
            for x in b[1:]: union(b[0], x)
        for j in range(m): union(j, m+j)
        nblocks = len(set(find(x) for x in range(2*m)))
        # multiply poly by d^{nblocks-1}
        pw = {0: 1}
        for _ in range(nblocks-1):
            nd = defaultdict(int)
            for e1, v1 in pw.items():
                for e2, v2 in d.items():
                    nd[e1+e2] += v1*v2
            pw = dict(nd)
        for e1, v1 in poly.items():
            for e2, v2 in pw.items():
                tot[e1+e2] += v1*v2
    tot = {e: v for e, v in tot.items() if v != 0}
    writhe = sum(1 if g > 0 else -1 for g in word)
    return tot, writhe

def jones_from_bracket(br, m, word):
    """Reduced Jones as {qexp_int: coef} with q = A^-4."""
    from collections import defaultdict
    # f = (-A^3)^{-w} <K>
    f = defaultdict(int)
    for e, c in br.items():
        f[e - 3*writhe_of(word)] += c * ((-1) ** (-writhe_of(word)))
    # careful: (-A^3)^{-w} = (-1)^{-w} A^{-3w}
    q = defaultdict(int)
    for e, c in f.items():
        if e % 4 != 0: return None  # non-integral -> convention wrong
        q[-e//4] += c
    return dict(q)

def writhe_of(word):
    return sum(1 if g > 0 else -1 for g in word)

if __name__ == "__main__":
    import sys
    tests = [("trefoil", 2, [-1,-1,-1], {-4:-1,-3:1,-1:1}),
             ("K11n34", 4, [1,1,2,-3,2,1,-3,-2,-2,-3,-3], None),
             ("K11n42", 4, [1,-2,3,-2,3,-2,-2,-1,2,-3,-3,2,2], None)]
    for name, m, w, exp in tests:
        br, wr = transfer_bracket(m, w)
        q = jones_from_bracket(br, m, w)
        print(name, "w=", wr, "Jones:", sorted(q.items()) if q else "NON-INTEGRAL")
        if exp: print("  expected:", sorted(exp.items()), "MATCH" if q == exp else "MISMATCH")
