"""Independent finite tests for resolving-set enumeration in matching-deleted bicliques.

Run with Python 3.9+ and no third-party packages.
"""
from collections import Counter, deque


def distance_matrix(a, b, t):
    n = a + b
    adjacency = [[] for _ in range(n)]
    for i in range(a):
        for j in range(b):
            if i == j and i < t:
                continue
            adjacency[i].append(a + j)
            adjacency[a + j].append(i)
    result = []
    for origin in range(n):
        dist = [-1] * n
        dist[origin] = 0
        todo = deque([origin])
        while todo:
            u = todo.popleft()
            for v in adjacency[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    todo.append(v)
        assert all(d >= 0 for d in dist)
        result.append(dist)
    return result


def coefficient_prediction(a, b, t):
    p, q = a - t, b - t
    unmatched_left = Counter({p: 1})
    unmatched_right = Counter({q: 1})
    if p:
        unmatched_left[p - 1] += p
    if q:
        unmatched_right[q - 1] += q

    def matched_factor(k):
        f = Counter({0: 1})
        for _ in range(k):
            g = Counter()
            for degree, coefficient in f.items():
                g[degree + 1] += 2 * coefficient
                g[degree + 2] += coefficient
            f = g
        return f

    result = Counter()
    for degree, count in matched_factor(t).items():
        for i, li in unmatched_left.items():
            for j, rj in unmatched_right.items():
                result[degree + i + j] += count * li * rj
    if t:
        for degree, count in matched_factor(t - 1).items():
            result[degree + p + q] += t * count
    return result


def minimal_prediction(a, b, t):
    p, q = a - t, b - t
    result = Counter()
    if p and q:
        result[t + p + q - 2] += p * q * (2 ** t)
    if p and not q:
        result[t + p - 1] += p * (2 ** t)
    if q and not p:
        result[t + q - 1] += q * (2 ** t)
    if t:
        result[t + p + q - 1] += t * (2 ** (t - 1))
    return result


def independent_structural_test(a, b, t, mask):
    p = sum(((mask >> i) & 1) == 0 for i in range(t, a))
    q = sum(((mask >> (a + j)) & 1) == 0 for j in range(t, b))
    empty_pairs = sum(
        ((mask >> i) & 1) == 0 and ((mask >> (a + i)) & 1) == 0
        for i in range(t)
    )
    return empty_pairs + p <= 1 and empty_pairs + q <= 1


def run():
    cases = 0
    subsets = 0
    resolving_sets = 0
    minimal_sets = 0
    for a in range(3, 6):
        for b in range(3, 6):
            if a + b > 10:
                continue
            for t in range(min(a, b) + 1):
                distance = distance_matrix(a, b, t)
                n = a + b
                is_resolving = []
                observed = Counter()
                for mask in range(1 << n):
                    chosen = [s for s in range(n) if mask & (1 << s)]
                    resolves = all(
                        any(distance[u][s] != distance[v][s] for s in chosen)
                        for u in range(n)
                        for v in range(u + 1, n)
                    )
                    assert resolves == independent_structural_test(a, b, t, mask), (
                        "classification", a, b, t, mask
                    )
                    is_resolving.append(resolves)
                    if resolves:
                        observed[len(chosen)] += 1
                assert observed == coefficient_prediction(a, b, t), (
                    "polynomial", a, b, t, observed, coefficient_prediction(a, b, t)
                )
                minimal = Counter()
                for mask, resolves in enumerate(is_resolving):
                    if resolves and all(
                        not is_resolving[mask ^ (1 << vertex)]
                        for vertex in range(n)
                        if mask & (1 << vertex)
                    ):
                        minimal[mask.bit_count()] += 1
                assert minimal == minimal_prediction(a, b, t), (
                    "minimal", a, b, t, minimal, minimal_prediction(a, b, t)
                )
                cases += 1
                subsets += 1 << n
                resolving_sets += sum(observed.values())
                minimal_sets += sum(minimal.values())
    assert (cases, subsets, resolving_sets, minimal_sets) == (41, 15872, 4473, 979)
    print(
        f"VERIFY_OK instances={cases} vertex_subsets={subsets} "
        f"resolving_sets={resolving_sets} minimal_resolving_sets={minimal_sets} "
        "distance_BFS=PASS iff_characterization=PASS "
        "all_set_polynomial=PASS minimal_polynomial=PASS"
    )


if __name__ == "__main__":
    run()
