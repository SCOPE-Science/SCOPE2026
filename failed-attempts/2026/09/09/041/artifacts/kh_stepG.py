"""Step G: differentials + homology ranks per (h,q) block for 10_124 mod p.
Full implementation. Circle maps with explicit indexing.
"""
import json, sys
sys.path.insert(0, 'output/artifacts')
from kh_stepD import parse_pd, smoothing_data
from collections import defaultdict

def build_differentials(pd, nplus, nminus, P):
    n = len(pd)
    shift = nplus - nminus
    # basis index per (h,q)
    index = {}
    members = defaultdict(list)
    for mask in range(1 << n):
        h = bin(mask).count('1')
        roots, lab = smoothing_data(pd, mask)
        c = len(roots)
        for word in range(1 << c):
            pw = c - bin(word).count('1')
            mw = bin(word).count('1')
            q = (pw - mw) + h + shift
            members[(h, q)].append((mask, word))
    for k, v in members.items():
        index[k] = {bw: j for j, bw in enumerate(v)}
    # differentials d_h: C^h -> C^{h+1}, per q; store as list of (row, col, val)
    diffs = {}
    for (h, q), lst in members.items():
        if (h + 1, q) not in members:
            continue
        tgt = index[(h + 1, q)]
        rows = len(members[(h + 1, q)])
        cols = len(lst)
        # sparse columns
        d = defaultdict(list)  # col -> [(row, val)]
        for col, (mask, word) in enumerate(lst):
            roots0, lab0 = smoothing_data(pd, mask)
            c0 = len(roots0)
            for k in range(n):
                if (mask >> k) & 1:
                    continue
                mask2 = mask | (1 << k)
                roots1, lab1 = smoothing_data(pd, mask2)
                c1 = len(roots1)
                sgn = -1 if (bin(mask & ((1 << k) - 1)).count('1') % 2) else 1
                if abs(c1 - c0) != 1:
                    continue
                # determine circle mapping
                if c1 == c0 - 1:
                    # merge: find the two circles in mask mapping to one in mask2
                    # group labels by lab1 root; the merged root contains labels from 2 distinct lab0 roots
                    from collections import defaultdict as dd
                    grp = dd(set)
                    for x, r in lab1.items():
                        grp[r].add(lab0[x])
                    merged = [sorted(v) for v in grp.values() if len(v) == 2]
                    if len(merged) != 1:
                        continue
                    (i, j) = merged[0]
                    bi = (word >> i) & 1
                    bj = (word >> j) & 1
                    # merge output bit at new circle: index = position of merged root in roots1 order
                    # find new circle idx: the lab1 root containing labels of i
                    # locate: pick a label x with lab0[x]==i, new idx = idx of lab1[x] in roots1
                    xi = next(x for x, r in lab0.items() if r == i)
                    newroot = lab1[xi]
                    # smoothing_data returns (roots=list-of-root-ids, lab dict label->position-index).
                    # lab values are already 0..c-1 positions; merged new-circle position:
                    ni = lab1[xi]
                    # output word: bits of word except i,j plus merged bit at ni
                    if bi == 0 and bj == 0:
                        out = {(0, 1)}  # + with coeff 1
                    elif bi == 1 and bj == 1:
                        out = {}
                    else:
                        out = {(1, 1)}
                    for (b, cf) in out:
                        w2 = 0
                        # new-circle positions jj run 0..c1-1; lab1 values are those positions.
                        # merged circle is at position ni; other new circle at position r' carries old bit.
                        npos = max(lab1.values()) + 1
                        for jj in range(npos):
                            if jj == ni:
                                bit = b
                            else:
                                # find old circle mapping into jj
                                s0 = next(lab0[x] for x, rr in lab1.items() if rr == jj)
                                bit = (word >> s0) & 1
                            if bit:
                                w2 |= (1 << jj)
                        key = (mask2, w2)
                        if key in tgt:
                            d[col].append((tgt[key], (sgn * cf) % P))
                else:
                    # split: circle i in mask splits into (a,b) in mask2
                    grp = dd2 = defaultdict(set)
                    for x, r in lab0.items():
                        grp[r].add(lab1[x])
                    split = [(r, sorted(v)) for r, v in grp.items() if len(v) == 2]
                    if len(split) != 1:
                        continue
                    (i, (a, b)) = split[0]
                    bi = (word >> i) & 1
                    roots1s, _ = smoothing_data(pd, mask2)
                    # note: smoothing_data called 3x per edge; slow but ok for 5120 edges? each call is union-find over 20 labels: fine.
                    outs = []
                    if bi == 0:
                        outs = [({a: 0, b: 1}, 1), ({a: 1, b: 0}, 1)]
                    else:
                        outs = [({a: 1, b: 1}, 1)]
                    for (ab, cf) in outs:
                        w2 = 0
                        npos = max(lab1.values()) + 1
                        for jj in range(npos):
                            if jj == a:
                                bit = ab[a]
                            elif jj == b:
                                bit = ab[b]
                            else:
                                s0 = next(lab0[x] for x, rr in lab1.items() if rr == jj)
                                bit = (word >> s0) & 1
                            if bit:
                                w2 |= (1 << jj)
                        key = (mask2, w2)
                        if key in tgt:
                            d[col].append((tgt[key], (sgn * cf) % P))
        diffs[(h, q)] = (rows, cols, d)
    return members, diffs

def sparse_rank(rows, cols, d, P):
    # d: dict col -> [(row, val)]; rank via row elimination with dict rows
    # transpose to row ops: build row list
    R = defaultdict(dict)
    for col, lst in d.items():
        for (r, v) in lst:
            R[r][col] = (R[r].get(col, 0) + v) % P
    pivots = {}
    rank = 0
    for r in sorted(R):
        row = R[r]
        # eliminate using existing pivots
        for pc, pr in sorted(pivots.items()):
            if pc in row:
                f = row[pc] * pow(pr[0], P - 2, P) % P
                if f:
                    for cc, vv in pr[1].items():
                        row[cc] = (row.get(cc, 0) - f * vv) % P
                    row.pop(pc, None)
        # normalize
        nz = [(c, v % P) for c, v in row.items() if v % P != 0]
        if not nz:
            continue
        c0 = min(nz)[0]
        inv = pow(dict(nz)[c0], P - 2, P)
        row = {c: v * inv % P for c, v in nz}
        pivots[c0] = (1, row)
        rank += 1
    return rank

if __name__ == '__main__':
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000007
    d = json.load(open('output/artifacts/pd_codes.json'))
    pd = parse_pd(d['10_124']['pd'])
    members, diffs = build_differentials(pd, 10, 0, P)
    print('blocks=', len(members), 'diffs=', len(diffs))
    import json as J
    ranks = {}
    tot_live = 0
    for (h, q) in sorted(diffs):
        rows, cols, dd = diffs[(h, q)]
        r = sparse_rank(rows, cols, dd, P)
        ranks['%d,%d' % (h, q)] = [rows, cols, r]
    # homology: dim H(h,q) = dimC(h,q) - rank(d_{h-1,q}) - rank(d_{h,q})
    print('computed ranks for', len(ranks), 'diffs')
    J.dump(ranks, open('output/artifacts/kh_ranks_%d.json' % P, 'w'))
    print('saved')
