"""Finite checks for pair-equality concepts of size-capped set partitions.

Run with Python 3 and the standard library. This verifies finite examples only.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


def partitions(n):
    if n == 0:
        yield ()
        return
    def visit(word, used):
        if len(word) == n:
            yield tuple(word)
            return
        for label in range(used + 1):
            word.append(label)
            yield from visit(word, max(used, label + 1))
            word.pop()
    yield from visit([0], 1)


def concepts(n, cap):
    edges = list(combinations(range(n), 2))
    answers = []
    for assignment in partitions(n):
        counts = Counter(assignment)
        if max(counts.values(), default=0) > cap:
            continue
        answers.append(sum((1 << i) for i, (u, v) in enumerate(edges)
                           if assignment[u] == assignment[v]))
    return edges, answers


def admissible(n, cap, edge_subset):
    parent = list(range(n))
    size = [1] * n
    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for u, v in edge_subset:
        x, y = find(u), find(v)
        if x == y:
            return False
        parent[y] = x
        size[x] += size[y]
        if size[x] > cap:
            return False
    return True


def polynomial(n, cap):
    # Root-component decomposition using Cayley's labeled-tree count.
    polys = [[1]]
    for size in range(1, n + 1):
        out = [0] * (size + 1)
        for j in range(1, min(size, cap) + 1):
            tree_count = 1 if j == 1 else j ** (j - 2)
            factor = comb(size - 1, j - 1) * tree_count
            for e, count in enumerate(polys[size - j]):
                out[e + j - 1] += factor * count
        polys.append(out)
    return polys[n]


def exact_ld(n, cap):
    edges, answer_masks = concepts(n, cap)
    num_concepts = len(answer_masks)
    queries = []
    for e in range(len(edges)):
        mask = sum((1 << i) for i, answers in enumerate(answer_masks)
                   if answers & (1 << e))
        if mask:
            queries.append(mask)
    @lru_cache(None)
    def rank(available):
        best = 0
        for mask in queries:
            yes = available & mask
            no = available ^ yes
            if yes and no:
                best = max(best, 1 + min(rank(yes), rank(no)))
        return best
    return rank((1 << num_concepts) - 1)


def facet_components(n, cap):
    if n == 0:
        return {0}
    counts = set()
    def rec(total, last, sizes):
        if total == n:
            if len(sizes) < 2 or sizes[0] + sizes[1] > cap:
                counts.add(len(sizes))
            return
        for j in range(last, min(cap, n - total) + 1):
            rec(total + j, j, sizes + (j,))
    rec(0, 1, ())
    return counts


def main():
    cases = supports = 0
    for n in range(0, 7):
        edges = list(combinations(range(n), 2))
        for cap in range(1, max(2, n + 1)):
            _, answers = concepts(n, cap)
            expected = polynomial(n, cap)
            observed = [0] * len(expected)
            max_dimension = n - (n + cap - 1) // cap if n else 0
            for k in range(len(edges) + 1):
                for subset in combinations(range(len(edges)), k):
                    graph_test = admissible(n, cap, [edges[i] for i in subset])
                    if k > max_dimension:
                        trace_test = False
                    else:
                        traces = {sum(((mask >> i) & 1) << j
                                      for j, i in enumerate(subset))
                                  for mask in answers}
                        trace_test = len(traces) == (1 << k)
                    if trace_test != graph_test:
                        raise AssertionError((n, cap, subset, graph_test, trace_test))
                    if trace_test:
                        observed[k] += 1
                    supports += 1
            if observed != expected:
                raise AssertionError((n, cap, observed, expected))
            if max(i for i, v in enumerate(observed) if v) != max_dimension:
                raise AssertionError((n, cap, observed))
            cases += 1
    online_cases = 0
    for n in range(0, 6):
        for cap in range(1, max(2, n + 1)):
            dim = n - (n + cap - 1) // cap if n else 0
            if exact_ld(n, cap) != dim:
                raise AssertionError(('online', n, cap))
            online_cases += 1
    facet_cases = 0
    for n in range(1, 17):
        for cap in range(1, min(n + 3, 12)):
            a = cap // 2 + 1
            delta = 1 if cap % 2 == 0 else 0
            bound = max(1, (n + delta) // a)
            expected = set(range((n + cap - 1) // cap, bound + 1))
            actual = facet_components(n, cap)
            if actual != expected:
                raise AssertionError(('facet_counts', n, cap, actual, expected))
            facet_cases += 1
    if not admissible(6, 3, [(0,1),(2,3),(4,5)]):
        raise AssertionError('matching facet')
    if not admissible(6, 3, [(0,1),(1,2),(3,4),(4,5)]):
        raise AssertionError('two-tree facet')
    print('BOUNDED_PARTITION_SHATTERING_PASS', cases, supports, online_cases, facet_cases)


if __name__ == '__main__':
    main()
