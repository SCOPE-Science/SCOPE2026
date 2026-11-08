#!/usr/bin/env python3
"""Finite independent checks of exact symbolic self-return probabilities."""
from itertools import product
from math import gcd


def graph_rank(k, times):
    vertices = set(range(k))
    for time in times:
        vertices.update(range(time, time + k))
    parent = {j: j for j in vertices}
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for time in times:
        for j in range(k):
            a, b = root(j), root(j + time)
            parent[a] = b
    components = len({root(j) for j in vertices})
    return k * len(times) - len(vertices) + components


def explicit_count(q, k, times):
    """Enumerate every q-ary word through the last compared coordinate."""
    n = max(times) + k
    count = 0
    for w in product(range(q), repeat=n):
        if all(all(w[i] == w[i + t] for i in range(k)) for t in times):
            count += 1
    return count, q ** n


def main():
    pair_cases = triple_cases = enumeration_cases = 0
    for k in range(1, 31):
        for a in range(1, 26):
            for b in range(1, 26):
                ts = [k + 2, k + 2 + a, k + 2 + a + b]
                want = max(0, k - a - b + gcd(a, b))
                got = graph_rank(k, ts)
                assert got == want, (k, a, b, got, want)
                triple_cases += 1
                if b == 1:
                    assert graph_rank(k, ts[:2]) == 0
                    assert graph_rank(k, [ts[0], ts[2]]) == 0
                    assert graph_rank(k, ts[1:]) == 0
                    pair_cases += 3
    # Truly independent, whole-sample-space string enumerations; no graph formula used.
    for q, k, times in [
        (2, 1, [1, 2, 3]), (2, 2, [2, 3, 4]),
        (2, 3, [3, 4, 5]), (2, 4, [4, 5, 6]),
        (2, 3, [3, 5, 7]), (2, 4, [4, 6, 8]),
        (2, 3, [3, 4]), (2, 4, [4, 6]),
        (3, 1, [1, 2, 3]), (3, 2, [2, 3, 4]),
        (3, 2, [2, 4, 6])]:
        count, total = explicit_count(q, k, times)
        want = total // (q ** (k * len(times) - graph_rank(k, times)))
        assert count == want, (q, k, times, count, want)
        enumeration_cases += 1
    assert graph_rank(3, [3, 4, 5]) == 2
    assert explicit_count(2, 3, [3, 4, 5]) == (2, 1 << 8)
    print(f'VERIFY_OK graph_triples={triple_cases} graph_pairs={pair_cases} '
          f'exhaustive_word_cases={enumeration_cases} fixed_example=2/256')


if __name__ == '__main__':
    main()
