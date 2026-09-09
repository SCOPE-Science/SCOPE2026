"""Step J: per-height Lee matrices (d+Phi, no q split) + ranks + Lee dim for 10_124."""
import json, sys
sys.path.insert(0, 'output/artifacts')
from kh_stepD import parse_pd, smoothing_data
from collections import defaultdict

P = 1000000007

def lee_height_matrices(pd, P):
    n = len(pd)
    # global per-height index
    g = {}
    for h in range(n + 1):
        dct = {}
        for mask in range(1 << n):
            if bin(mask).count('1') == h:
                roots, lab = smoothing_data(pd, mask)
                for word in range(1 << len(roots)):
                    dct[(mask, word)] = len(dct)
        g[h] = dct
    mats = {}
    for h in range(n):
        tgt = g[h + 1]
        D = defaultdict(list)  # col -> [(row, val)]
        for (mask, word), col in g[h].items():
            roots0, lab0 = smoothing_data(pd, mask)
            c0 = len(roots0)
            for k in range(n):
                if (mask >> k) & 1:
                    continue
                mask2 = mask | (1 << k)
                roots1, lab1 = smoothing_data(pd, mask2)
                c1 = len(roots1)
                if abs(c1 - c0) != 1:
                    continue
                sgn = -1 if (bin(mask & ((1 << k) - 1)).count('1') % 2) else 1
                if c1 == c0 - 1:
                    grp = defaultdict(set)
                    for x, r in lab1.items():
                        grp[r].add(lab0[x])
                    merged = [sorted(v) for v in grp.values() if len(v) == 2]
                    if len(merged) != 1:
                        continue
                    (i, j) = merged[0]
                    bi = (word >> i) & 1
                    bj = (word >> j) & 1
                    ni = lab1[next(x for x, r in lab0.items() if r == i)]
                    npos = max(lab1.values()) + 1
                    outs = []
                    # Kh part
                    if bi == 0 and bj == 0:
                        outs.append((0, 1, 'kh'))
                    elif bi != bj:
                        outs.append((1, 1, 'kh'))
                    # Phi part
                    if bi == 1 and bj == 1:
                        outs.append((0, 1, 'lee'))
                    for (b, cf, _) in outs:
                        w2 = 0
                        for jj in range(npos):
                            if jj == ni:
                                bit = b
                            else:
                                s0 = next(lab0[x] for x, rr in lab1.items() if rr == jj)
                                bit = (word >> s0) & 1
                            if bit:
                                w2 |= (1 << jj)
                        if (mask2, w2) in tgt:
                            D[col].append((tgt[(mask2, w2)], (sgn * cf) % P))
                else:
                    grp = defaultdict(set)
                    for x, r in lab0.items():
                        grp[r].add(lab1[x])
                    split = [(r, sorted(v)) for r, v in grp.items() if len(v) == 2]
                    if len(split) != 1:
                        continue
                    (i, (a, b)) = split[0]
                    bi = (word >> i) & 1
                    npos = max(lab1.values()) + 1
                    outs = []
                    if bi == 0:
                        outs += [({a: 0, b: 1}, 1), ({a: 1, b: 0}, 1)]
                    else:
                        outs += [({a: 1, b: 1}, 1)]
                        outs += [({a: 0, b: 0}, 1)]  # Phi: - -> ++  (bits 0 = v+)
                    for (ab, cf) in outs:
                        w2 = 0
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
                        if (mask2, w2) in tgt:
                            D[col].append((tgt[(mask2, w2)], (sgn * cf) % P))
        mats[h] = (len(tgt), len(g[h]), D)
    dims = {h: len(g[h]) for h in g}
    return dims, mats

def sparse_rank(rows, cols, d, P):
    R = defaultdict(dict)
    for col, lst in d.items():
        for (r, v) in lst:
            R[r][col] = (R[r].get(col, 0) + v) % P
    piv = {}
    rank = 0
    for r in sorted(R):
        row = R[r]
        for pc in sorted(piv):
            if pc in row:
                f = row[pc] * pow(piv[pc][0], P - 2, P) % P
                if f:
                    for cc, vv in piv[pc][1].items():
                        row[cc] = (row.get(cc, 0) - f * vv) % P
                    row.pop(pc, None)
        row = {c: v % P for c, v in row.items() if v % P != 0}
        if not row:
            continue
        c0 = min(row)
        inv = pow(row[c0], P - 2, P)
        piv[c0] = (1, {c: v * inv % P for c, v in row.items()})
        rank += 1
    return rank

if __name__ == '__main__':
    d = json.load(open('output/artifacts/pd_codes.json'))
    pd = parse_pd(d['10_124']['pd'])
    dims, mats = lee_height_matrices(pd, P)
    print('dims:', dims)
    ranks = {}
    for h in sorted(mats):
        rows, cols, dd = mats[h]
        r = sparse_rank(rows, cols, dd, P)
        ranks[h] = r
        print('d_Lee h=%d: %d x %d rank %d' % (h, rows, cols, r))
    tot = sum((dims[h] - ranks.get(h - 1, 0) - ranks.get(h, 0)) for h in dims)
    print('Lee homology total dim =', tot)
    json.dump({'dims': dims, 'ranks': ranks, 'lee_dim': tot}, open('output/artifacts/lee_ranks_10_124.json', 'w'))
