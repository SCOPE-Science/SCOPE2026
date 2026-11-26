"""Standalone ordered-block verification for the bipartite acyclic-orientation flip-degree theorem."""
from collections import Counter, defaultdict
from itertools import permutations
from math import factorial


def ordered_partitions(elements):
    """Enumerate every ordered set partition exactly once (blocks are nonempty)."""
    items = tuple(elements)
    def rec(i, blocks):
        if i == len(items):
            for p in permutations(blocks):
                yield tuple(tuple(block) for block in p)
            return
        for b in range(len(blocks)):
            blocks[b].append(items[i])
            yield from rec(i + 1, blocks)
            blocks[b].pop()
        blocks.append([items[i]])
        yield from rec(i + 1, blocks)
        blocks.pop()
    yield from rec(0, [])


def degree_histogram(m, n):
    by_a = defaultdict(list)
    by_b = defaultdict(list)
    for p in ordered_partitions(range(m)):
        by_a[len(p)].append(p)
    for p in ordered_partitions(range(m, m + n)):
        by_b[len(p)].append(p)
    ans = Counter()
    for start in (0, 1):
        for ka, a_parts in by_a.items():
            for kb, b_parts in by_b.items():
                if not (ka == kb or (start == 0 and ka == kb + 1)
                        or (start == 1 and kb == ka + 1)):
                    continue
                for a in a_parts:
                    for b in b_parts:
                        blocks = []
                        for j in range(max(ka, kb)):
                            if start == 0:
                                if j < ka:
                                    blocks.append(a[j])
                                if j < kb:
                                    blocks.append(b[j])
                            else:
                                if j < kb:
                                    blocks.append(b[j])
                                if j < ka:
                                    blocks.append(a[j])
                        d = sum(len(u) * len(v) for u, v in zip(blocks, blocks[1:]))
                        ans[d] += 1
    return ans


def fall(n, k):
    return factorial(n) // factorial(n - k)


def predicted_simple(m, n):
    if min(m, n) == 1:
        return 2 ** max(m, n)
    p, q = min(m, n), max(m, n)
    return (2 * sum(fall(m, k) * fall(n, k) for k in range(1, p))
            + factorial(p) * fall(q, p - 1) * (2 ** (q - p + 1) - 2))


def main():
    expected = {
        (2, 2): {3: 8, 4: 6},
        (2, 3): {4: 24, 5: 12, 6: 10},
        (2, 4): {5: 64, 6: 48, 7: 16, 8: 18},
        (3, 3): {5: 90, 6: 72, 7: 36, 8: 18, 9: 14},
        (3, 4): {6: 312, 7: 360, 8: 192, 9: 96, 10: 60, 11: 24, 12: 22},
        (4, 4): {7: 1472, 8: 2304, 9: 1056, 10: 1248, 11: 192,
                 12: 408, 13: 64, 14: 96, 15: 32, 16: 30},
    }
    for m, n in [(1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]:
        h = degree_histogram(m, n)
        assert h[min(h)] == predicted_simple(m, n), (m, n, h)
        assert min(h) == m + n - 1
        assert max(h) == m * n
        assert h[m * n] == 2 ** m + 2 ** n - 2
        if (m, n) in expected:
            assert h == Counter(expected[m, n]), (m, n, h)
        print(f'K_{m},{n}: {sum(h.values())} orientations, {h[m+n-1]} simple vertices')
    print('ORDERED_BLOCKS_CERTIFICATE_PASS')


if __name__ == '__main__':
    main()
