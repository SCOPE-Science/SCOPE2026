"""Independent finite checks for exact two-hole reaching distances in Cerny automata.

No external packages; invoke: python checker.py
"""
from collections import deque
from itertools import combinations


def a(S, n):
    return frozenset((x + 1) % n for x in S)


def b(S, n):
    return frozenset((0 if x == n - 1 else x) for x in S)


def predicted(n, p, q):
    assert n >= 4 and 0 <= p < q < n
    if q == n - 1:
        return n + 2 if p == 0 else p + 3
    return n + p + 3 if q == p + 1 else q + 3


def witness(n, p, q):
    if q == n - 1 and p > 0:
        h, t = p + 1, 0
    elif q == n - 1 and p == 0:
        h, t = n - 1, 1
    elif q == p + 1:
        h, t = n - 1, p + 2
    else:
        h, t = q - p, p + 1
    return 'b' + 'a' * h + 'b' + 'a' * t


def potential(S, n):
    holes = sorted(set(range(n)) - set(S))
    if len(holes) == 0:
        return 0
    if len(holes) == 1:
        return 1 if holes[0] == n - 1 else holes[0] + 2
    if len(holes) == 2:
        return predicted(n, *holes)
    return None


def bfs_distances(n):
    Q = frozenset(range(n))
    dist = {Q: 0}
    todo = deque([Q])
    while todo:
        state = todo.popleft()
        for op in (a, b):
            nxt = op(state, n)
            if nxt not in dist:
                dist[nxt] = dist[state] + 1
                todo.append(nxt)
    return dist


def verify():
    bfs_cases = witness_cases = bellman_cases = histogram_cases = 0
    # Exhaustive subset-state BFS, independent of claimed proof/potential.
    for n in range(4, 15):
        d = bfs_distances(n)
        Q = frozenset(range(n))
        observed = {}
        for p, q in combinations(range(n), 2):
            target = Q - {p, q}
            value = predicted(n, p, q)
            assert d[target] == value, (n, p, q, d[target], value)
            bfs_cases += 1
            s = Q
            w = witness(n, p, q)
            assert len(w) == value
            for letter in w:
                s = a(s, n) if letter == 'a' else b(s, n)
            assert s == target, (n, p, q, w)
            witness_cases += 1
            observed[value] = observed.get(value, 0) + 1
        for t in range(0, 2*n + 2):
            expected = t - 3 if 4 <= t <= n + 1 else (1 if n + 2 <= t <= 2*n else 0)
            assert observed.get(t, 0) == expected, (n, t, observed)
            histogram_cases += 1
    # Independent local verification of lower-bound potential on all rank >= n-2 images.
    for n in range(4, 41):
        Q = frozenset(range(n))
        states = [Q]
        states += [Q - {p} for p in range(n)]
        states += [Q - {p, q} for p, q in combinations(range(n), 2)]
        for S in states:
            for op in (a, b):
                T = op(S, n)
                if len(T) >= n - 2:
                    assert potential(T, n) <= potential(S, n) + 1, (n, S, T)
                bellman_cases += 1
    print('VERIFY_OK')
    print('exact_BFS_pairs', bfs_cases)
    print('witness_pairs', witness_cases)
    print('histogram_entries', histogram_cases)
    print('potential_transitions', bellman_cases)


if __name__ == '__main__':
    verify()
