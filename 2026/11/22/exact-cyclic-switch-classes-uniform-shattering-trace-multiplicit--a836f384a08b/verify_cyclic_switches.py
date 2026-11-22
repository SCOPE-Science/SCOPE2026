#!/usr/bin/env python3
"""Finite independent checks for cyclic exact-transition Boolean concept families.

No finite computation substitutes for the general proof.
"""
from itertools import combinations, product
from math import comb


def circle_switch_count(w):
    return sum(w[i] != w[(i + 1) % len(w)] for i in range(len(w)))


def test_direct(n):
    universe = list(product((0, 1), repeat=n))
    tested = 0
    for k in range(0, n + 1, 2):
        H = [w for w in universe if circle_switch_count(w) == k]
        assert len(H) == 2 * comb(n, k)
        rank = min(k + 1, n - k + 1)
        face_counts = [0] * (n + 1)
        for size in range(n + 1):
            for S in combinations(range(n), size):
                traces = {tuple(w[i] for i in S) for w in H}
                shattered = len(traces) == 2**size
                assert shattered == (size <= rank), (n, k, S, traces)
                if shattered:
                    face_counts[size] += 1
                tested += 1
        assert face_counts == [comb(n, j) if j <= rank else 0
                               for j in range(n + 1)]
        # Independently check the gap-polynomial multiplicity for every
        # nonempty support of size at most three and every trace.
        for size in range(1, min(3, n) + 1):
            for S in combinations(range(n), size):
                gaps = [((S[(i + 1) % size] - S[i]) % n) if size > 1
                        else n for i in range(size)]
                for y in product((0, 1), repeat=size):
                    p = [1]  # polynomial product of allowed edge-switch counts
                    for i, gap in enumerate(gaps):
                        parity = y[i] ^ y[(i + 1) % size]
                        q = [comb(gap, t) if (t % 2) == parity else 0
                             for t in range(gap + 1)]
                        nextp = [0] * (len(p) + len(q) - 1)
                        for a, v in enumerate(p):
                            for b, w in enumerate(q):
                                nextp[a + b] += v * w
                        p = nextp
                    exact = sum(tuple(w[i] for i in S) == y for w in H)
                    predicted = p[k]
                    assert exact == predicted, (n, k, S, y, exact, predicted)
    return tested


def check_online(n, k):
    from functools import lru_cache
    H = []
    for word in product((0, 1), repeat=n):
        if circle_switch_count(word) == k:
            H.append(word)
    qbits = [sum((h[i] << j) for j, h in enumerate(H)) for i in range(n)]
    @lru_cache(maxsize=None)
    def dim(mask):
        best = 0
        for q in qbits:
            a = mask & q
            b = mask & ~q
            if a and b:
                best = max(best, 1 + min(dim(a), dim(b)))
        return best
    d = dim((1 << len(H)) - 1)
    low = k * (((n - 1) // k).bit_length() - 1) if k else 1
    high = len(H).bit_length() - 1
    assert low <= d <= high, (n, k, low, d, high)
    return d


def test_depth4_certificate():
    """Replay all paths in the supplied five-vertex online witness."""
    import json
    from pathlib import Path
    path = Path(__file__).with_name('depth4_certificate.json')
    cert = json.loads(path.read_text(encoding='utf-8'))
    leaves = []
    def visit(node, history, depth):
        if isinstance(node, str):
            assert depth == 4
            assert len(node) == 5 and set(node) <= {'0','1'}
            assert sum(node[i] != node[(i + 1) % 5] for i in range(5)) == 2
            assert all(node[i - 1] == str(bit) for i, bit in history)
            leaves.append(node)
            return
        pos = node['position']
        assert 1 <= pos <= 5
        visit(node['zero'], history + [(pos, 0)], depth + 1)
        visit(node['one'], history + [(pos, 1)], depth + 1)
    visit(cert, [], 0)
    assert len(leaves) == 16 and len(set(leaves)) == 16
    print('DEPTH4_CERTIFICATE_PASS leaves=16')


def main():
    count = 0
    for n in range(3, 12):
        total = test_direct(n)
        count += total
        print(f'n={n}: {total} direct supports checked')
    for n in range(3, 11):
        print(f'n={n}, k=2: exact finite online dimension {check_online(n,2)}')
    test_depth4_certificate()
    print(f'CYCLIC_SWITCH_CHECKS_PASS supports={count}')


if __name__ == '__main__':
    main()
