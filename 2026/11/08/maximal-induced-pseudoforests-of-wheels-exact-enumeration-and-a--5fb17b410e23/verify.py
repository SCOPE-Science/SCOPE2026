"""Exact checks for inclusion-maximal induced pseudoforests in wheel graphs.

Usage: python verify.py. Standard library only. The finite test is not an
infinite proof; the accompanying text supplies the unrestricted argument.
"""
from collections import Counter
from math import comb


def proposed(n):
    counts = Counter({n: 1})
    if n % 2 == 0:
        counts[n // 2 + 1] += 2
    for k in range((n + 4) // 3, (n + 1) // 2 + 1):
        t = n - 2 * k + 1
        if 0 <= t <= k - 1:
            counts[k + 1] += n * comb(k - 1, t)
    return counts


def graph_edges(n):
    return [(i, (i + 1) % n) for i in range(n)] + [(i, n) for i in range(n)]


def is_pseudoforest(n, selected, edges):
    # Independent criterion: every connected component has edge count <= vertex count.
    seen = 0
    adj = [0] * (n + 1)
    for a, b in edges:
        if (selected >> a) & 1 and (selected >> b) & 1:
            adj[a] |= 1 << b
            adj[b] |= 1 << a
    for v in range(n + 1):
        if not ((selected >> v) & 1) or (seen >> v) & 1:
            continue
        todo = [v]
        seen |= 1 << v
        vcount, twice_edges = 0, 0
        while todo:
            u = todo.pop()
            vcount += 1
            twice_edges += adj[u].bit_count()
            free = adj[u] & ~seen
            while free:
                least = free & -free
                free -= least
                seen |= least
                todo.append(least.bit_length() - 1)
        if twice_edges // 2 > vcount:
            return False
    return True


def brute(n):
    counts = Counter()
    edges = graph_edges(n)
    limit = 1 << (n + 1)
    for chosen in range(1, limit):
        if not is_pseudoforest(n, chosen, edges):
            continue
        missing = (limit - 1) ^ chosen
        maximal = True
        while missing:
            least = missing & -missing
            missing -= least
            if is_pseudoforest(n, chosen | least, edges):
                maximal = False
                break
        if maximal:
            counts[chosen.bit_count()] += 1
    return counts


def rational_coefficients(nmax):
    # Coefficients of z^3 x^3(1+x)/(1-z x^2-z x^3).
    c = [Counter() for _ in range(nmax + 1)]
    c[3][3] = 1
    c[4][3] = 1
    for n in range(5, nmax + 1):
        for k, number in c[n - 2].items():
            c[n][k + 1] += number
        for k, number in c[n - 3].items():
            c[n][k + 1] += number
    outputs = []
    for n in range(3, nmax + 1):
        out = Counter({n: 1})
        if n % 2 == 0:
            out[n // 2 + 1] += 2
        for k, number in c[n].items():
            out[k] += n * number
        outputs.append(out)
    return outputs


def main():
    examined, maximal = 0, 0
    for n in range(3, 17):
        result = brute(n)
        assert result == proposed(n), (n, result, proposed(n))
        examined += (1 << (n + 1)) - 1
        maximal += sum(result.values())
    for n, from_ogf in enumerate(rational_coefficients(180), 3):
        prediction = proposed(n)
        assert from_ogf == prediction, (n, from_ogf, prediction)
        actual_deletion_sizes = sorted(n + 1 - k for k in prediction)
        expected = sorted(set([1] + list(range(n // 2, n - (n + 4) // 3 + 1))))
        assert actual_deletion_sizes == expected, (n, actual_deletion_sizes, expected)
        expected_largest_count = n if n % 2 else n * (n - 2) // 2 + 2
        assert prediction[1 + (n + 1) // 2] == expected_largest_count + (n == 3)
    print(f'VERIFY_OK wheels_n=3..16 direct_nonempty_vertex_subsets={examined} '
          f'maximal_induced_pseudoforests={maximal} rational_and_gap_n=3..180 PASS')


if __name__ == '__main__':
    main()
