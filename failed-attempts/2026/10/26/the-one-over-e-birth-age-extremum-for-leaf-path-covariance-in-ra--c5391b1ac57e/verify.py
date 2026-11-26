"""Exact checks for marked-leaf conditioning in uniform recursive trees."""
from itertools import product
from fractions import Fraction
from math import factorial


def harmonic(m):
    return sum((Fraction(1, j) for j in range(1, m + 1)), Fraction(0))


def tree_info(parents):
    # parents[j] is the parent of label j, where label 1 is the root.
    n = len(parents) - 1
    depths = [0] * (n + 1)
    leaf = [True] * (n + 1)
    for j in range(2, n + 1):
        v = parents[j]
        assert 1 <= v < j
        depths[j] = depths[v] + 1
        leaf[v] = False
    return depths, leaf, sum(depths)


def all_parent_arrays(n):
    for choices in product(*(range(1, j) for j in range(2, n + 1))):
        yield (0, 0, *choices)


def check_exact(n):
    raw_count = 0
    sum_path = 0
    sum_leaves = 0
    sum_leaf_path = 0
    count_marked = [0] * (n + 1)
    sum_marked_path = [0] * (n + 1)
    # Bijection from conditioned marked-leaf trees to an (n-1)-tree
    # and an insertion parent. Check each pair is produced exactly once.
    seen = [set() for _ in range(n + 1)]
    for parents in all_parent_arrays(n):
        depths, leaf, path = tree_info(parents)
        raw_count += 1
        sum_path += path
        sum_leaves += sum(leaf[2:])
        sum_leaf_path += sum(leaf[2:]) * path
        for i in range(2, n + 1):
            if leaf[i]:
                count_marked[i] += 1
                sum_marked_path[i] += path
                short = [0, 0]
                for j in range(2, n + 1):
                    if j == i:
                        continue
                    v = parents[j]
                    assert v != i
                    short.append(v - (v > i))
                short = tuple(short)
                assert len(short) == n
                assert tree_info(short)[2] + 1 + depths[parents[i]] == path
                key = (short, parents[i])
                assert key not in seen[i], (n, i, key)
                seen[i].add(key)
    assert raw_count == factorial(n - 1)
    assert Fraction(sum_path, raw_count) == n * (harmonic(n) - 1)
    assert Fraction(sum_leaf_path, raw_count) - Fraction(sum_leaves * sum_path, raw_count ** 2) == -Fraction(n - 2, 4)
    for i in range(2, n + 1):
        assert count_marked[i] == factorial(n - 2) * (i - 1)
        assert len(seen[i]) == count_marked[i]
        cond_mean = Fraction(sum_marked_path[i], count_marked[i])
        assert cond_mean == (n - 1) * (harmonic(n - 1) - 1) + harmonic(i - 1), (n,i,cond_mean)
        covariance = Fraction(sum_marked_path[i], raw_count) - Fraction(count_marked[i] * sum_path, raw_count ** 2)
        assert covariance == Fraction(i - 1, n - 1) * (harmonic(i - 1) - harmonic(n - 1))
    print('EXHAUSTIVE_MARKED_LEAF_BIJECTION_PASS', n, 'trees=', raw_count)


def check_optimum(n):
    H = [Fraction(0)]
    for j in range(1, n):
        H.append(H[-1] + Fraction(1, j))
    N = n - 1
    cv = [Fraction(k, N) * (H[k] - H[N]) for k in range(1, n)]
    imin = min(range(len(cv)), key=lambda j: cv[j]) + 2
    assert cv.count(min(cv)) == 1
    # Convexity / exact harmonic threshold for the unique minimizer.
    kstar = next(k for k in range(1, n) if H[N] - H[k] < 1)
    assert imin == kstar + 1, (n, imin, kstar)


for n in range(2, 10):
    check_exact(n)
for n in range(3, 301):
    check_optimum(n)
print('EXACT_UNIQUE_AGE_OPTIMUM_PASS n=3..300')
print('VERIFY_OK')
