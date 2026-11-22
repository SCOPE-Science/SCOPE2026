"""Finite regression tests for the directed radius-separated cycle reconfiguration theorem.
Uses direct enumeration, directed breadth-first search, and a separate edge-flow formula.
No external packages. Python 3.10+.
"""
from itertools import combinations
from collections import deque
from math import comb


def feasible(bitmask, n, k, r):
    positions = [v for v in range(n) if (bitmask >> v) & 1]
    if len(positions) != k:
        return False
    return all((positions[(i + 1) % k] - positions[i]) % n >= r
               for i in range(k))


def distance_formula(a, b, n):
    level = 0
    prefix = []
    for v in range(n):
        level += ((a >> v) & 1) - ((b >> v) & 1)
        prefix.append(level)
    assert level == 0
    return sum(prefix) - n * min(prefix)


def check(n, k, r):
    states = [sum(1 << v for v in c)
              for c in combinations(range(n), k)
              if all((c[(i + 1) % k] - c[i]) % n >= r
                     for i in range(k))]
    indices = {a: i for i, a in enumerate(states)}
    assert len(states) == n * comb(n - (r - 1)*k - 1, k - 1) // k
    edges = []
    for a in states:
        destinations = []
        for v in range(n):
            w = (v + 1) % n
            if (a >> v) & 1 and not ((a >> w) & 1):
                b = a ^ (1 << v) ^ (1 << w)
                if feasible(b, n, k, r):
                    destinations.append(indices[b])
        edges.append(destinations)
    bound = k * (n - r*(k - 1) - 1)
    maximum = 0
    diametral_pairs = 0
    pair_tests = 0
    for a_i, a in enumerate(states):
        distances = [-1] * len(states)
        distances[a_i] = 0
        queue = deque([a_i])
        while queue:
            i = queue.popleft()
            for j in edges[i]:
                if distances[j] == -1:
                    distances[j] = distances[i] + 1
                    queue.append(j)
        assert all(d >= 0 for d in distances), (n, k, r, 'unreachable')
        for j, b in enumerate(states):
            observed = distances[j]
            predicted = distance_formula(a, b, n)
            assert observed == predicted, (n, k, r, a, b, observed, predicted)
            maximum = max(maximum, observed)
            diametral_pairs += observed == bound
            pair_tests += 1
    assert maximum == bound, (n, k, r, maximum, bound)
    assert diametral_pairs == n, (n, k, r, diametral_pairs)
    return len(states), pair_tests


def main():
    cases = 0
    total_pairs = 0
    largest_state_space = 0
    for n in range(5, 17):
        for r in range(2, min(n//2, 6)):
            for k in range(2, min((n - 1)//r, 5) + 1):
                states, pairs = check(n, k, r)
                cases += 1
                total_pairs += pairs
                largest_state_space = max(largest_state_space, states)
                print(f'n={n} r={r} k={k}: {states} states, {pairs} BFS pairs, PASS')
    print(f'PASS: {cases} parameter cases, {total_pairs} ordered pairs, '
          f'largest state space {largest_state_space}')


if __name__ == '__main__':
    main()
