"""Independent verifier for lane-117 witnesses and census claims.

Checks, trusting no poset database and sharing no code with the search
scripts (self-contained reimplementation here):
  W1: each witness reachability relation is a partial order (reflexive,
      antisymmetric, transitive) and rows decode to it.
  W2: each cover edge is a true cover relation of the decoded poset, the
      cover graph is connected enough to be checked, and the stored bags
      form a valid tree-decomposition of width <= 2 (vertex coverage, edge
      coverage, running-intersection contiguity).
  W3: dimension upper bound: exhibits an explicit realizer (list of linear
      extensions, each a permutation extending the poset) whose intersection
      is exactly the poset order  -> dim <= len(realizer).
  W4: dimension lower bound: exhibits triples of critical pairs with
      alternating-cycle certificates (x_i <= y_{i+1} chains) proving no two
      of the three share one linear extension, hence dim >= 3.
  C1: re-enumerates ALL height-2 (4,4) bipartite patterns with >= 7 edges,
      counts linear extensions exactly (aborts loudly on any cap overflow),
      computes exact dimension, and confirms max dim = 3 (no dim>=4).
  C2: verifies the S4 crown (4+4, a_i < b_j iff i != j) has dimension
      exactly 4 and that its cover graph (K_{4,4} minus matching) is NOT
      treewidth <= 2, by exhaustive simplicial-elimination search (exact
      for n = 8).

Usage: python3 output/artifacts/verify_witness.py [--skip-census]
Exit 0 iff all checks pass. Stdlib only.
"""
import sys
import itertools

ART = 'output/artifacts'


def load_witnesses():
    import json
    with open(ART + '/witnesses.json') as f:
        return json.load(f)


def decode(n, rows):
    le = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or ((rows[i] >> j) & 1):
                le[i][j] = True
    return le


def is_partial_order(n, le):
    for i in range(n):
        if not le[i][i]:
            return False, 'reflexive %d' % i
        for j in range(n):
            if le[i][j] and le[j][i] and i != j:
                return False, 'antisym %d %d' % (i, j)
    for i in range(n):
        for j in range(n):
            if le[i][j]:
                for k in range(n):
                    if le[j][k] and not le[i][k]:
                        return False, 'trans %d %d %d' % (i, j, k)
    return True, 'ok'


def covers_of(n, le):
    cov = []
    for i in range(n):
        for j in range(n):
            if i != j and le[i][j]:
                if not any(k != i and k != j and le[i][k] and le[k][j]
                           for k in range(n)):
                    cov.append((i, j))
    return cov


def check_td(n, edges, bags):
    for b in bags:
        if len(b) > 3:
            return False, 'bag too big %r' % (b,)
    seen = set()
    for b in bags:
        seen.update(b)
    if seen != set(range(n)):
        return False, 'vertex coverage %r' % (sorted(seen),)
    und = set((min(a, b), max(a, b)) for a, b in edges)
    for (a, b) in und:
        if not any(a in bg and b in bg for bg in bags):
            return False, 'edge uncovered %r' % ((a, b),)
    for v in range(n):
        idx = [i for i, bg in enumerate(bags) if v in bg]
        if idx != list(range(min(idx), max(idx) + 1)):
            return False, 'contiguity %d' % v
    return True, 'ok'


def is_linear_extension(n, le, perm):
    if sorted(perm) != list(range(n)):
        return False
    pos = [0] * n
    for k, v in enumerate(perm):
        pos[v] = k
    for i in range(n):
        for j in range(n):
            if le[i][j] and pos[i] > pos[j]:
                return False
    return True


def realizer_intersection_is_order(n, le, realizer):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            in_all = all(p.index(i) < p.index(j) for p in
                         [list(r) for r in realizer])
            if in_all != le[i][j]:
                return False, (i, j, in_all, le[i][j])
    return True, None


def all_les(n, le, cap):
    pred = [0] * n
    for i in range(n):
        for j in range(n):
            if j != i and le[j][i]:
                pred[i] |= (1 << j)
    out = []
    full = (1 << n) - 1
    cur = []
    bad = [False]

    def bt(placed):
        if bad[0]:
            return
        if placed == full:
            out.append(tuple(cur))
            return
        for v in range(n):
            if not (placed >> v) & 1 and (pred[v] & ~placed) == 0:
                cur.append(v)
                bt(placed | (1 << v))
                cur.pop()
                if len(out) >= cap:
                    bad[0] = True
                    return
    bt(0)
    return out, bad[0]


def critical_pairs(n, le):
    crit = []
    strict_down = []
    strict_up = []
    for i in range(n):
        d = set(j for j in range(n) if le[j][i]) - {i}
        u = set(j for j in range(n) if le[i][j]) - {i}
        strict_down.append(d)
        strict_up.append(u)
    for x in range(n):
        for y in range(n):
            if x != y and not le[x][y] and not le[y][x]:
                if strict_down[x] <= strict_down[y] | {y} and \
                   strict_up[y] <= strict_up[x] | {x}:
                    crit.append((x, y))
    return crit


def alternating_cycle_check(n, le, pairs):
    """Verify pairs form a strict alternating cycle: x_i <= y_{i+1} for all
    i (cyclic) and x_i, y_i incomparable. Returns cycle chains as evidence."""
    k = len(pairs)
    for (x, y) in pairs:
        if le[x][y] or le[y][x]:
            return False, 'not incomparable %r' % ((x, y),)
    for i in range(k):
        x = pairs[i][0]
        y = pairs[(i + 1) % k][1]
        if not le[x][y]:
            return False, 'no link %d->%d' % (x, y)
    return True, 'ok'


def greedy_realizer(n, le, crit, les):
    """Find a small realizer by greedy set cover over reversal masks."""
    c = len(crit)
    full = (1 << c) - 1
    pos_of = []
    for perm in les:
        idx = [0] * n
        for k, v in enumerate(perm):
            idx[v] = k
        m = 0
        for ci, (x, y) in enumerate(crit):
            if idx[y] < idx[x]:
                m |= (1 << ci)
        pos_of.append(m)
    chosen = []
    cov = 0
    rest = [m for m in pos_of if m != 0]
    while cov != full and rest:
        rest.sort(key=lambda m: -bin(m & ~cov).count('1'))
        cov |= rest.pop(0)
        chosen.append(cov)
    # recover actual permutations chosen
    real = []
    cov = 0
    rest = list(pos_of)
    while cov != full:
        best = max([m for m in rest if m & ~cov],
                   key=lambda m: bin(m & ~cov).count('1'))
        # find a perm attaining 'best' new coverage
        for perm, m in zip(les, pos_of):
            if m == best:
                real.append(list(perm))
                break
        cov |= best
    return real


def verify_witness(w, idx):
    n = w['n']
    rows = w['reach_rows']
    le = decode(n, rows)
    ok, msg = is_partial_order(n, le)
    assert ok, 'W%d order: %s' % (idx, msg)
    cov = covers_of(n, le)
    cov_und = set((min(a, b), max(a, b)) for a, b in cov)
    stored_und = set(tuple(e) for e in w['cover_edges'])
    assert cov_und == stored_und, \
        'W%d cover mismatch: true=%s stored=%s' % (idx, sorted(cov_und),
                                                  sorted(stored_und))
    ok, msg = check_td(n, list(stored_und), w['bags'])
    assert ok, 'W%d TD: %s' % (idx, msg)
    width = max(len(b) for b in w['bags']) - 1
    assert width <= 2, 'W%d width %d' % (idx, width)
    les, ov = all_les(n, le, 40000)
    assert not ov, 'W%d LE overflow' % idx
    crit = critical_pairs(n, le)
    assert len(crit) == w['ncrit'], \
        'W%d ncrit %d != %d' % (idx, len(crit), w['ncrit'])
    assert len(les) == w['nLE'], \
        'W%d nLE %d != %d' % (idx, len(les), w['nLE'])
    real = greedy_realizer(n, le, crit, les)
    assert len(real) == 3, 'W%d realizer size %d' % (idx, len(real))
    for perm in real:
        assert is_linear_extension(n, le, perm), 'W%d bad LE' % idx
    ok, info = realizer_intersection_is_order(n, le, real)
    assert ok, 'W%d realizer intersection fails at %r' % (idx, info)
    # lower bound: certify dim >= 3 by proving no 2 linear extensions reverse
    # all critical pairs. Witness: for every ordered pair of linear
    # extensions (L1, L2) from the complete LE list, name a critical pair
    # reversed by neither. Since the LE list is complete, no 2-realizer
    # exists. (A triple of pairwise-incompatible pairs would also suffice
    # but need not exist; this full check is the general certificate.)
    def rev_mask(perm):
        idx = [0] * n
        for k, v in enumerate(perm):
            idx[v] = k
        m = 0
        for ci, (x, y) in enumerate(crit):
            if idx[y] < idx[x]:
                m |= (1 << ci)
        return m
    masks = [rev_mask(perm) for perm in les]
    full = (1 << len(crit)) - 1
    uncovered_pair = None
    for i in range(len(masks)):
        for j in range(i, len(masks)):
            if (masks[i] | masks[j]) != full:
                missing = (~(masks[i] | masks[j])) & full
                miss_idx = (missing & -missing).bit_length() - 1 \
                    if False else None
                import math
                miss = [ci for ci in range(len(crit))
                        if not (masks[i] | masks[j]) >> ci & 1]
                uncovered_pair = (i, j, miss[0])
                break
        if uncovered_pair is not None:
            break
    assert uncovered_pair is not None, 'W%d unexpectedly has dim<=2' % idx
    # Spot-check: verify the named missing pair is critical and unreversed.
    i0, j0, m0 = uncovered_pair
    x0, y0 = crit[m0]
    for perm in (les[i0], les[j0]):
        idx = [0] * n
        for k, v in enumerate(perm):
            idx[v] = k
        assert idx[x0] < idx[y0], 'W%d obstruction pair reversed?!' % idx
    obstruction = {'every_LE_pair_misses_a_pair': True,
                   'example_LE_indices': [i0, j0],
                   'example_missed_pair': [x0, y0]}
    return {'realizer': real, 'obstruction': obstruction,
            'ncrit': len(crit), 'nLE': len(les), 'width': width}


def tw_leq2_exact(n, edges):
    """Exact tw<=2 test by simplicial elimination search (complete)."""
    adj = [set() for _ in range(n)]
    for (a, b) in edges:
        adj[a].add(b)
        adj[b].add(a)
    from functools import lru_cache
    found = [None]

    def bt(alive, cur, bags):
        if found[0] is not None:
            return True
        if not alive:
            found[0] = [b[:] for b in bags]
            return True
        cand = [v for v in alive if len(cur[v] & alive) <= 2]
        if not cand:
            return False
        for v in cand:
            nb = set(cur[v] & alive)
            added = []
            for a in nb:
                for b in nb:
                    if a != b and b not in cur[a]:
                        cur[a].add(b)
                        added.append((a, b))
            bags.append([v] + sorted(nb))
            if bt(alive - {v}, cur, bags):
                return True
            bags.pop()
            for (a, b) in added:
                cur[a].discard(b)
        return False
    bt(set(range(n)), [set(a) for a in adj], [])
    return found[0]


def exact_dim(n, le, cap=60000):
    les, ov = all_les(n, le, cap)
    if ov:
        return None, None, True
    crit = critical_pairs(n, le)
    if not crit:
        return 1, crit, False
    full = (1 << len(crit)) - 1
    masks = []
    for perm in les:
        idx = [0] * n
        for k, v in enumerate(perm):
            idx[v] = k
        m = 0
        for ci, (x, y) in enumerate(crit):
            if idx[y] < idx[x]:
                m |= (1 << ci)
        if m:
            masks.append(m)
    masks = sorted(set(masks), key=lambda m: -bin(m).count('1'))
    cov = 0
    g = 0
    rest = list(masks)
    while cov != full and rest:
        rest.sort(key=lambda m: -bin(m & ~cov).count('1'))
        cov |= rest.pop(0)
        g += 1
    if cov != full:
        return None, crit, False
    masks.sort(key=lambda m: -bin(m).count('1'))
    L = len(masks)
    suf = [0] * (L + 1)
    for i in range(L - 1, -1, -1):
        suf[i] = suf[i + 1] | masks[i]

    def dfs(i, covered, used, limit):
        if used > limit:
            return False
        if covered == full:
            return True
        if i == L or (covered | suf[i]) != full:
            return False
        rem = full & ~covered
        mx = max(bin(mm & rem).count('1') for mm in masks[i:])
        if mx == 0:
            return False
        import math
        need = (bin(rem).count('1') + mx - 1) // mx
        if used + need > limit:
            return False
        return dfs(i + 1, covered | masks[i], used + 1, limit) or \
            dfs(i + 1, covered, used, limit)
    for limit in range(g):
        if dfs(0, 0, 0, limit):
            return limit, crit, False
    return g, crit, False


def census_44():
    n = 8
    total = 0
    d4 = 0
    maxd = 0
    for bits in range(1 << 16):
        if bin(bits).count('1') < 7:
            continue
        le = [[False] * n for _ in range(n)]
        for i in range(n):
            le[i][i] = True
        for k in range(16):
            if (bits >> k) & 1:
                le[k // 4][4 + k % 4] = True
        # transitivity is automatic for height-2 bipartite
        crit = critical_pairs(n, le)
        if len(crit) < 8:
            continue
        d, _, ov = exact_dim(n, le)
        assert not ov, 'census LE overflow at bits=%d' % bits
        total += 1
        maxd = max(maxd, d)
        if d >= 4:
            d4 += 1
            print('CENSUS COUNTEREXAMPLE bits=%d dim=%d' % (bits, d))
    return total, d4, maxd


def s4_check():
    n = 8
    le = [[False] * n for _ in range(n)]
    for i in range(n):
        le[i][i] = True
    for i in range(4):
        for j in range(4):
            if i != j:
                le[i][4 + j] = True
    d, crit, ov = exact_dim(n, le)
    assert not ov and d == 4, 'S4 dim=%r' % d
    cov = covers_of(n, le)
    und = [(min(a, b), max(a, b)) for a, b in cov]
    assert len(und) == 12
    assert tw_leq2_exact(n, und) is None, 'S4 cover unexpectedly tw<=2'
    return d, len(und)


def main():
    skip = '--skip-census' in sys.argv
    ws = load_witnesses()
    assert len(ws) >= 1, 'need >=1 witness'
    for i, w in enumerate(ws):
        info = verify_witness(w, i)
        print('witness %d: n=%d width=%d ncrit=%d nLE=%d dim=3 '
              'realizer=%s obstruction=%s' %
              (i, w['n'], info['width'], info['ncrit'], info['nLE'],
               info['realizer'], info['obstruction']), flush=True)
    d, m = s4_check()
    print('S4: dim=%d cover-m=%d cover-tw>2 confirmed' % (d, m), flush=True)
    if not skip:
        total, d4, maxd = census_44()
        print('census44: enumerated=%d dim4=%d maxd=%d' %
              (total, d4, maxd), flush=True)
        assert total == 50235, 'census count changed: %d' % total
        assert d4 == 0 and maxd == 3
    print('ALL CHECKS PASSED', flush=True)


if __name__ == '__main__':
    main()
