"""Exact finite checks of the set-partition crossing--nesting covariance contrast.
The proof for arbitrary sizes is in RESULT.md; this script checks finite instances.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def bell_numbers(limit):
    b = [1]
    for m in range(limit):
        b.append(sum(comb(m, k) * b[k] for k in range(m + 1)))
    return b


def partitions(n):
    blocks = []
    def recurse(i):
        if i > n:
            yield tuple(tuple(block) for block in blocks)
            return
        for block in blocks:
            block.append(i)
            yield from recurse(i + 1)
            block.pop()
        blocks.append([i])
        yield from recurse(i + 1)
        blocks.pop()
    yield from recurse(1)


def statistics(part):
    arcs = [(a, b) for block in part for a, b in zip(block, block[1:])]
    levels = sum(b == a + 1 for a, b in arcs)
    crossings = sum(a < c < b < d or c < a < d < b
                    for (a,b),(c,d) in combinations(arcs,2))
    nestings = sum(a < c < d < b or c < a < b < d
                   for (a,b),(c,d) in combinations(arcs,2))
    dimension = sum(b - a - 1 for a,b in arcs)
    return levels, crossings, nestings, dimension


B = bell_numbers(80)
checks = 0
for n in range(2, 9):
    tot_l = tot_c = tot_ne = tot_lc = tot_ln = 0
    for p in partitions(n):
        lev, cr, ne, _ = statistics(p)
        tot_l += lev
        tot_c += cr
        tot_ne += ne
        tot_lc += lev * cr
        tot_ln += lev * ne
    assert tot_c == tot_ne, (n, tot_c, tot_ne)
    checks += 1
    difference = Fraction(tot_ln - tot_lc, B[n])
    target = Fraction(n + 3) - Fraction(2 * B[n+1], B[n])
    assert difference == target, (n, difference, target)
    checks += 1
    if n >= 4:
        assert difference > 0
    else:
        assert difference == 0
    checks += 1

for m in range(1, 9):
    dim = sum(statistics(p)[3] for p in partitions(m))
    formula = (m+4)*B[m+1]-2*B[m+2]
    assert dim == formula, (m, dim, formula)
    checks += 1

# Check the local contraction mechanism for each actual level arc.
for n in range(2, 9):
    for part in partitions(n):
        lev, cr, ne, _ = statistics(part)
        for i in range(1, n):
            if not any(i in block and i+1 in block for block in part):
                continue
            contracted = tuple(tuple(x if x <= i else x-1 for x in block if x != i+1)
                               for block in part)
            _, cc, nn, _ = statistics(contracted)
            h = sum(a < i < b for block in contracted
                    for a,b in zip(block,block[1:]))
            assert ne-cr == nn-cc+h, (n, i, part, contracted)
            checks += 1

for m in range(1, 9):
    for part in partitions(m):
        _,_,_,d = statistics(part)
        summed_h = sum(sum(a < i < b for block in part
                           for a,b in zip(block,block[1:]))
                       for i in range(1, m+1))
        assert summed_h == d
        checks += 1

for m in range(1, 61):
    marked_block_rec = sum(comb(m, j) * B[m-j+1] for j in range(m))
    assert marked_block_rec == B[m+2]-B[m+1]-B[1]
    checks += 1
    cut_formula = m * B[m+1] - 2*m*B[m] - 2 * sum(
        comb(m, s+1)*B[m-s] for s in range(1,m))
    assert cut_formula == (m+4)*B[m+1]-2*B[m+2]
    checks += 1

print('PASS', checks, 'exact checks, exhaustive partitions through n=8')
