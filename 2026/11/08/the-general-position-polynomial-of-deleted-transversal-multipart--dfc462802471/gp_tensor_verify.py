"""Direct finite checks for general-position sets in products of complete graphs.

Run: python3 gp_tensor_verify.py
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted(a, r):
    result = [1, a*r, choose(a*r, 2)]
    for k in range(3, max(a, r, 4) + 1):
        count = a*choose(r, k) + r*choose(a, k)
        count += factorial(k)*choose(a, k)*choose(r, k)
        if k == 3:
            count += 4*choose(a, 2)*choose(r, 2)
        if k == 4:
            count += choose(a, 2)*choose(r, 2)
        result.append(count)
    while result[-1] == 0:
        result.pop()
    return result


def brute(a, r):
    vertices = [(i, j) for i in range(a) for j in range(r)]
    n = len(vertices)
    infinity = n + 1
    distances = [[0 if i == j else (1 if vertices[i][0] != vertices[j][0] and vertices[i][1] != vertices[j][1] else infinity)
                  for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    bad = []
    for i, j, k in combinations(range(n), 3):
        if (distances[i][j] + distances[j][k] == distances[i][k]
                or distances[i][k] + distances[k][j] == distances[i][j]
                or distances[j][i] + distances[i][k] == distances[j][k]):
            bad.append((1 << i) | (1 << j) | (1 << k))
    counts = Counter()
    for mask in range(1 << n):
        if all((mask & t) != t for t in bad):
            counts[mask.bit_count()] += 1
    return [counts[k] for k in range(max(counts) + 1)], 1 << n


def unimodal(coeff):
    i = 0
    while i + 1 < len(coeff) and coeff[i] <= coeff[i+1]:
        i += 1
    return all(coeff[j] >= coeff[j+1] for j in range(i, len(coeff)-1))


def main():
    checked = 0
    subsets = 0
    for a, r in [(3,3),(3,4),(4,3),(3,5),(5,3),(4,4)]:
        actual, total = brute(a, r)
        formula = predicted(a, r)
        assert actual == formula, (a, r, actual, formula)
        checked += 1
        subsets += total
    assert predicted(3,3) == [1,9,36,48,9]
    assert predicted(4,3) == [1,12,66,112,21]
    assert predicted(4,4) == [1,16,120,272,68]
    # Published coefficient formula (arXiv:2401.05696, Section 4)
    # predicts 66 for the cubic coefficient at a=r=3,
    # in contrast to the direct graph test and structural count 48.
    source_cubic_at_3_3 = 2*3*(3-1)*choose(3,2) + 3*choose(3,3) + 3**3*choose(3,3)
    assert source_cubic_at_3_3 == 66
    assert predicted(3,3)[3] == 48
    for r in range(3, 1001):
        coeff = predicted(4, r)
        expected = (r <= 11 or r >= 40)
        assert unimodal(coeff) == expected, r
        if 12 <= r <= 39:
            assert coeff[4] > coeff[5] < coeff[6]
        if r >= 40:
            assert coeff[0] <= coeff[1] <= coeff[2] <= coeff[3] <= coeff[4] <= coeff[5]
    print('VERIFY_OK direct_graph_instances={} tested_vertex_subsets={} a4_unimodality_r=3..1000 source_discrepancy_a=r=3_48_vs_66=PASS'.format(checked,subsets))


if __name__ == '__main__':
    main()
