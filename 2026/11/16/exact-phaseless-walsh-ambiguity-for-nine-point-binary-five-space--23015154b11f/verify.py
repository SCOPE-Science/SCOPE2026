"""Exact census of nine-point Walsh magnitudes in binary five-space.

Standard-library only. All arithmetic is integer; no floating-point comparisons.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, factorial, prod


def bitrank(vectors):
    piv = {}
    for v in vectors:
        w = v
        while w:
            j = w.bit_length()-1
            if j in piv:
                w ^= piv[j]
            else:
                piv[j] = w
                break
    return len(piv)


def gl_maps(n):
    ans = []
    for columns in product(range(1 << n), repeat=n):
        if bitrank(columns) != n:
            continue
        ans.append(tuple(
            __import__('functools').reduce(
                lambda a, b: a ^ b,
                (columns[j] for j in range(n) if (x >> j) & 1), 0)
            for x in range(1 << n)))
    return ans


def compositions(k, n):
    for bars in combinations(range(k + n - 1), n - 1):
        b = (-1,) + bars + (k + n - 1,)
        yield tuple(b[i+1] - b[i] - 1 for i in range(n))


def weights(columns):
    return tuple(sorted(sum(columns[c] for c in range(8)
                            if (c & u).bit_count() % 2) for u in range(1, 8)))


def canonical(v, gl):
    return min(tuple(sum(v[i] for i in range(8) if g[i] == j)
                     for j in range(8)) for g in gl)


def relation_rows(v):
    cols = [j for j in range(8) for _ in range(v[j])]
    assert len(cols) == 9
    return tuple(sum(1 << k for k, c in enumerate(cols) if (c >> bit) & 1)
                 for bit in range(3))


def make_points(v):
    R = relation_rows(v)
    orth = [s for s in range(1 << 9)
            if all((s & r).bit_count() % 2 == 0 for r in R)]
    assert len(orth) == 64 and 0x1ff in orth
    basis = [0x1ff]
    for s in orth:
        if bitrank(basis + [s]) > len(basis):
            basis.append(s)
        if len(basis) == 6:
            break
    assert len(basis) == 6
    rows = [s ^ (0x1ff if (s & 1) else 0) for s in basis[1:]]
    points = tuple(sum(((row >> j) & 1) << k
                       for k, row in enumerate(rows)) for j in range(9))
    assert len(set(points)) == 9
    assert bitrank([points[j] ^ points[0] for j in range(1,9)]) == 5
    return points


def walsh_hist(points, dimension):
    freq = [abs(sum(1 if ((u & x).bit_count() % 2 == 0) else -1
                    for x in points)) for u in range(1 << dimension)]
    return tuple(freq.count(a) for a in (1,3,5,7,9))


def code_hist(v):
    R = relation_rows(v)
    hist = Counter()
    for s in range(1 << 9):
        if all((s & r).bit_count() % 2 == 0 for r in R):
            hist[abs(9 - 2 * s.bit_count())] += 1
    assert all(hist[a] % 2 == 0 for a in hist)
    return tuple(hist[a] // 2 for a in (1,3,5,7,9))


def affine_generators(n):
    out = []
    for i in range(n):
        out.append(tuple(x ^ (1 << i) for x in range(1 << n)))
    for i in range(n-1):
        out.append(tuple(x ^ ((((x >> i) & 1) ^ ((x >> (i+1)) & 1))
                              * ((1 << i) | (1 << (i+1)))) for x in range(1 << n)))
    for i in range(n):
        for j in range(n):
            if i != j:
                out.append(tuple(x ^ ((((x >> j) & 1)) << i)
                                 for x in range(1 << n)))
    return out


def image_mask(mask, permutation):
    out = 0
    while mask:
        b = mask & -mask
        out |= 1 << permutation[b.bit_length() - 1]
        mask ^= b
    return out


def rank_four_classes():
    all_masks = {sum(1 << x for x in X)
                 for X in combinations(range(16), 9)}
    generators = affine_generators(4)
    result = []
    while all_masks:
        rep = min(all_masks)
        found = {rep}
        frontier = [rep]
        for m in frontier:
            for perm in generators:
                im = image_mask(m, perm)
                if im not in found:
                    found.add(im)
                    frontier.append(im)
        assert found <= all_masks
        all_masks -= found
        points = [x for x in range(16) if rep & (1 << x)]
        assert bitrank([x ^ points[0] for x in points[1:]]) == 4
        result.append((rep, len(found), tuple(2*h for h in walsh_hist(points,4))))
    return sorted(result)


def main():
    gl = gl_maps(3)
    assert len(gl) == 168
    valid = []
    for v in compositions(9,8):
        if any(sum(v[c] for c in range(8) if (c & u).bit_count() % 2) % 2
               for u in range(1,8)):
            continue
        ws = weights(v)
        if min(ws) < 4:
            continue
        valid.append(v)
    assert len(valid) == 148
    classes = {canonical(v,gl) for v in valid}
    assert len(classes) == 6
    group_size = 32 * prod(32 - (1 << i) for i in range(5))
    result = []
    for v in sorted(classes):
        p = weights(v)
        stab = sum(canonical(v, [g]) == v for g in gl)
        aut = stab * prod(factorial(a) for a in v)
        assert group_size % aut == 0
        orbit = group_size // aut
        hist = code_hist(v)
        direct = walsh_hist(make_points(v), 5)
        assert hist == direct
        assert sum(hist) == 32
        result.append((v,p,orbit,hist))
    assert sum(x[2] for x in result) == comb(32,9)-62*comb(16,9)
    prof = defaultdict(list)
    for v,p,orbit,hist in result:
        prof[hist].append(v)
    assert sorted(len(v) for v in prof.values()) == [1,1,1,1,2]
    assert sorted([sum(1 for t in p if t == 4) for v,p,orbit,h in result]) == [3,3,4,5,6,7]
    print('RANK5_CLASSES',len(result),'valid_multiplicities',len(valid),
          'GL3_order',len(gl))
    for rec in result:
        print('RANK5',rec)
    rank4 = rank_four_classes()
    assert len(rank4) == 3
    assert sum(o for rep,o,h in rank4) == comb(16,9)
    print('RANK4_CLASSES',len(rank4))
    for rep,orbit,hist in rank4:
        print('RANK4',hex(rep),62*orbit,hist)
    hist_total = defaultdict(list)
    for v,p,orbit,h in result:
        hist_total[h].append(('rank5',orbit))
    for rep,orbit,h in rank4:
        hist_total[h].append(('rank4',62*orbit))
    assert len(hist_total) == 8
    assert sum(len(v) for v in hist_total.values()) == 9
    assert sorted(len(v) for v in hist_total.values()) == [1]*7 + [2]
    assert sum(sum(cnt for _,cnt in v) for v in hist_total.values()) == comb(32,9)
    print('CHECK_OK nine_affine_orbits=9 distinct_walsh_histograms=8',
          'nine_point_subsets=',comb(32,9),
          'exact_double_histogram=',[k for k,v in hist_total.items() if len(v)==2])

if __name__ == '__main__':
    main()
