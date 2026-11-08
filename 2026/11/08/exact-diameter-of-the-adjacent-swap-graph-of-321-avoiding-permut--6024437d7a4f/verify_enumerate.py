"""Exhaustive check of pattern-avoider adjacent-swap distances.

Requires only Python 3 standard library. Run: python3 verify_enumerate.py
This program supplies finite checks, not a proof of the all-order theorem.
"""
from collections import deque
from itertools import permutations


def avoids_321(p):
    n = len(p)
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] <= p[j]:
                continue
            for k in range(j + 1, n):
                if p[j] > p[k]:
                    return False
    return True


def inversions(p):
    return sum(p[i] > p[j]
               for i in range(len(p))
               for j in range(i + 1, len(p)))


def extreme_pair(n):
    h = n // 2
    ell = (n - 1) // 2
    c = ell + 1
    high = tuple(range(c + 1, n + 1))
    low = tuple(range(1, c))
    assert len(high) == h and len(low) == ell
    return (c,) + high + low, high + low + (c,)


def main():
    expected_counts = [1, 2, 5, 14, 42, 132, 429, 1430]
    expected_diameters = [0, 1, 4, 7, 12, 17, 24, 31]
    for n in range(1, 9):
        states = [p for p in permutations(range(1, n+1)) if avoids_321(p)]
        id_of = {p: i for i, p in enumerate(states)}
        assert len(states) == expected_counts[n - 1]
        adjacent = []
        for p in states:
            row = []
            for i in range(n-1):
                q = list(p)
                q[i], q[i+1] = q[i+1], q[i]
                if tuple(q) in id_of:
                    row.append(id_of[tuple(q)])
            adjacent.append(row)
        assert sum(len(row) for row in adjacent) % 2 == 0
        assert all(i in adjacent[j] for i, row in enumerate(adjacent) for j in row)
        hi = (n*n)//4
        assert max(map(inversions, states)) == hi
        assert sum(inversions(p) == hi for p in states) == (1 if n % 2 == 0 or n == 1 else 2)
        diameter = 0
        count_diam_pairs = 0
        witness_a, witness_b = extreme_pair(n)
        witness_distance = -1
        for start, p in enumerate(states):
            ds = [-1] * len(states)
            ds[start] = 0
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adjacent[u]:
                    if ds[v] == -1:
                        ds[v] = ds[u] + 1
                        q.append(v)
            assert -1 not in ds
            assert all(d <= inversions(p) + inversions(states[j]) for j, d in enumerate(ds))
            diameter = max(diameter, max(ds))
            if p == witness_a:
                witness_distance = ds[id_of[witness_b]]
            for j in range(start):
                if ds[j] == expected_diameters[n - 1]:
                    count_diam_pairs += 1
        assert diameter == expected_diameters[n - 1], (n, diameter)
        assert witness_distance == diameter, (n, witness_distance, diameter)
        assert diameter == (n*n-1)//2 if n%2 else diameter == n*n//2-1
        print('n=%d Catalan=%d edges=%d diameter=%d witness=%d diameter_pairs=%d' %
              (n,len(states),sum(map(len,adjacent))//2,diameter,witness_distance,count_diam_pairs))
    print('EXHAUSTIVE_321_ADJACENT_SWAP_DIAMETERS_PASS')

if __name__ == '__main__':
    main()
