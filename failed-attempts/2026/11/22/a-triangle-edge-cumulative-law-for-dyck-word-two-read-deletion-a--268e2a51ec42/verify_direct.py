"""Independent finite check of Dyck two-read triangle counts using deletion sets.
Python 3 standard library. The mathematical proof is in RESULT.md.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
from math import comb

@lru_cache(None)
def dyck(n):
    if n == 0:
        return ('',)
    return tuple('1' + a + '0' + b
                 for i in range(n) for a in dyck(i) for b in dyck(n-i-1))

def exact(n):
    return sum(2 * (k - 1) * comb(2 * (n-k) + 1, n-k-1)
               for k in range(2, n))

def count_triangles(n):
    words = dyck(n)
    by_read = defaultdict(list)
    for i, w in enumerate(words):
        for v in {w[:j] + w[j+1:] for j in range(len(w))}:
            by_read[v].append(i)
    overlap = defaultdict(int)
    for origins in by_read.values():
        for i,j in combinations(origins,2):
            overlap[i,j] += 1
    assert max(overlap.values(), default=0) <= 2
    adjacency = [set() for _ in words]
    for (i,j), count in overlap.items():
        if count == 2:
            adjacency[i].add(j)
            adjacency[j].add(i)
    three = sum(len({w for w in adjacency[i] & adjacency[j] if w > j})
                for i in range(len(words)) for j in adjacency[i] if j > i)
    return three, sum(map(len, adjacency))//2

if __name__ == '__main__':
    expected_edges = {1:0, 2:1, 3:6, 4:27, 5:111, 6:441, 7:1728, 8:6733}
    for n in range(1,9):
        got, edge_count = count_triangles(n)
        assert got == exact(n), (n,got,exact(n))
        assert edge_count == expected_edges[n], (n,edge_count)
        print(f'n={n} triangles={got} edges={edge_count}')
    print('DIRECT_VERIFICATION_OK')
