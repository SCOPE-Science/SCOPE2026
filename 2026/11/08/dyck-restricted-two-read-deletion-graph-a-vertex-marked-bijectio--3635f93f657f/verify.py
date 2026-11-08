"""Finite cross-checks for two-read one-deletion ambiguity of Dyck words.
Standard library only.  Run: python3 verify.py
"""
from collections import Counter, defaultdict
from math import comb


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def dyck(n):
    def rec(s, ups, downs):
        if ups == downs == n:
            yield s
            return
        if ups < n:
            yield from rec(s + '1', ups + 1, downs)
        if downs < ups:
            yield from rec(s + '0', ups, downs + 1)
    yield from rec('', 0, 0)


def deletion_ball(w):
    return {w[:i] + w[i + 1:] for i in range(len(w))}


def formula(n):
    # Number of positive vertices summed over all Dyck paths of semilength m:
    # H_m = m(2m+1)/(m+2) * C_m.
    return sum(m * (2 * m + 1) * catalan(m) // (m + 2) for m in range(1, n))


def generated_edges(words):
    result = set()
    for w in words:
        # All oriented alternating phase flips, with positive initial height.
        height = 0
        for i in range(len(w)):
            if height > 0:
                for j in range(i + 2, len(w) + 1, 2):
                    b = w[i:j]
                    if all(b[t] != b[t - 1] for t in range(1, len(b))):
                        z = w[:i] + ''.join('1' if c == '0' else '0' for c in b) + w[j:]
                        assert z != w
                        result.add(tuple(sorted((w, z))))
                    else:
                        break
            height += (1 if w[i] == '1' else -1)
    return result


def brute_edges(words):
    by_read = defaultdict(set)
    for w in words:
        for z in deletion_ball(w):
            by_read[z].add(w)
    overlap = Counter()
    from itertools import combinations
    for parents in by_read.values():
        for e in combinations(sorted(parents), 2):
            overlap[e] += 1
    assert max(overlap.values(), default=0) <= 2
    return {e for e, d in overlap.items() if d == 2}


def main():
    values = []
    for n in range(1, 11):
        words = list(dyck(n))
        assert len(words) == catalan(n)
        edges = generated_edges(words)
        expected = formula(n)
        assert len(edges) == expected, (n, len(edges), expected)
        degrees = {u: 0 for u in words}
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
        assert max(degrees.values()) == (n - 1) ** 2
        if n >= 3:
            assert [u for u in words if degrees[u] == (n - 1) ** 2] == ['1' + '10' * (n - 1) + '0']
        if n <= 8:
            brute = brute_edges(words)
            assert edges == brute, (n, edges - brute, brute - edges)
        values.append((n, len(words), len(edges)))
    # Formula for the total positive marked vertices, checked separately.
    for m in range(1, 11):
        total = 0
        for w in dyck(m):
            h = 0
            for ch in w:
                h += 1 if ch == '1' else -1
                total += h > 0
        assert total == m * (2 * m + 1) * catalan(m) // (m + 2)
    print('VERIFY_OK; (semilength, Catalan_count, two_read_ambiguity_edges):')
    for row in values:
        print(*row)


if __name__ == '__main__':
    main()
