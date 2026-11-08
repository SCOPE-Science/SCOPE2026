"""Reproduce the exact DLDS-partition polynomial for labelled cycles C_n, n >= 5.
Run: python verify.py. Requires Python 3 and sympy for the characteristic-polynomial check.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from math import ceil

STATES = tuple(tuple(map(int, f'{i:04b}')) for i in range(16))
INDEX = {a: i for i, a in enumerate(STATES)}
EDGES = []
for i, a in enumerate(STATES):
    for t in (0, 1):
        v = a + (t,)
        if v[-3:] in ((0, 0, 0), (1, 1, 1)) or v == (0, 0, 1, 0, 0):
            continue
        EDGES.append((i, INDEX[v[1:]], t))

@lru_cache(None)
def transfer_polynomial(n):
    ans = Counter()
    by_source = [[] for _ in range(16)]
    for i, j, t in EDGES:
        by_source[i].append((j, t))
    for start in range(16):
        cur = {(start, 0): 1}
        for _ in range(n):
            nxt = defaultdict(int)
            for (i, k), val in cur.items():
                for j, t in by_source[i]:
                    nxt[(j, k + t)] += val
            cur = nxt
        for (j, k), val in cur.items():
            if j == start:
                ans[k] += val
    return {k: v for k, v in sorted(ans.items()) if v}

def original_graph_test(n, mask):
    # Independent definition on the graph; does not use local-word restrictions.
    membership = [(mask >> i) & 1 for i in range(n)]
    outside_signatures = set()
    for i in range(n):
        neighbors = ((i - 1) % n, (i + 1) % n)
        if membership[i]:
            if all(membership[j] for j in neighbors):
                return False  # The complement D fails to dominate L.
        else:
            sig = tuple(j for j in neighbors if membership[j])
            if not sig or sig in outside_signatures:
                return False  # L fails to dominate or locate a D vertex.
            outside_signatures.add(sig)
    return True

def forbidden_word_test(n, mask):
    b = [(mask >> i) & 1 for i in range(n)]
    for i in range(n):
        triple = tuple(b[(i + j) % n] for j in range(3))
        five = tuple(b[(i + j) % n] for j in range(5))
        if triple in ((0, 0, 0), (1, 1, 1)) or five == (0, 0, 1, 0, 0):
            return False
    return True

def add_shift(ans, poly, offset):
    for k, v in poly.items():
        ans[k + offset] += v

def main():
    from sympy import Matrix, symbols, factor
    x, z = symbols('x z')
    arr = [[0 for _ in range(16)] for _ in range(16)]
    for i, j, t in EDGES:
        arr[i][j] += z**t
    char = factor(Matrix(arr).charpoly(x).as_expr())
    target = x**10 * (x**6 - z*x**4 - z**2*x**3 - z**2*x**2 - z**2*x - z**3)
    assert factor(char - target) == 0
    print('EXACT_CHARACTERISTIC_POLYNOMIAL_OK')

    for n in range(5, 17):
        expected = Counter()
        for mask in range(1 << n):
            a = original_graph_test(n, mask)
            b = forbidden_word_test(n, mask)
            assert a == b, ('local characterisation', n, mask)
            if a:
                expected[mask.bit_count()] += 1
        poly = transfer_polynomial(n)
        assert dict(expected) == poly, ('graph vs transfer', n, expected, poly)
        assert min(poly) == (2*n+4)//5
        assert max(poly) == (2*n)//3
        print('GRAPH_AND_TRANSFER_EXHAUSTIVE_OK', n, sum(expected.values()))

    for n in range(11, 40):
        rec = Counter()
        for lag, power in ((2, 1), (3, 2), (4, 2), (5, 2), (6, 3)):
            add_shift(rec, transfer_polynomial(n-lag), power)
        assert dict(rec) == transfer_polynomial(n), ('recurrence', n)
        poly = transfer_polynomial(n)
        assert min(poly) == (2*n+4)//5 and max(poly) == 2*n//3
    print('WEIGHTED_RECURRENCE_AND_SUPPORT_OK 11..39')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
