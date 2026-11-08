"""Independent finite checks for cyclic fixed-window shattering and online dimension.

Run with Python 3; only the standard library is needed.
"""
from functools import lru_cache
from itertools import combinations


def window(n, ell, start):
    return frozenset((start + t) % n for t in range(ell))


def traces(n, ell, support):
    return {tuple(p in window(n, ell, start) for p in support)
            for start in range(n)}


def direct_ldim(n, ell):
    """Exact recursive decision-tree rank, without using the proposed formula."""
    columns = [sum(1 << start for start in range(n)
                   if point in window(n, ell, start))
               for point in range(n)]

    @lru_cache(None)
    def rank(family):
        best = 0
        for col in columns:
            yes, no = family & col, family & ~col
            if yes and no:
                best = max(best, 1 + min(rank(yes), rank(no)))
        return best

    return rank((1 << n) - 1)


def verify_witness_tree(n, ell):
    """Explicit adaptive complete tree of the stated depth."""
    w = min(ell, n - ell)
    depth = w.bit_length()  # equals 1 + floor(log2 w)
    width = 1 << (depth - 1)
    positive = list(range(width))
    negative = list(range(ell, ell + width))
    assert max(negative) < n

    def certify_block(starts):
        if len(starts) == 1:
            return 1
        mid = len(starts) // 2
        query = starts[mid - 1] % n
        yes = [s for s in starts if query in window(n, ell, s)]
        no = [s for s in starts if query not in window(n, ell, s)]
        assert yes == starts[:mid], (n, ell, starts, query, yes)
        assert no == starts[mid:], (n, ell, starts, query, no)
        return certify_block(yes) + certify_block(no)

    root_query = ell - 1
    assert all(root_query in window(n, ell, s) for s in positive)
    assert all(root_query not in window(n, ell, s) for s in negative)
    assert certify_block(positive) == width
    assert certify_block(negative) == width
    return depth


def main():
    nparams = 0
    supports_checked = 0
    for n in range(2, 18):
        for ell in range(1, n):
            w = min(ell, n - ell)
            expected_ldim = w.bit_length()
            assert direct_ldim(n, ell) == expected_ldim, (n, ell)
            assert verify_witness_tree(n, ell) == expected_ldim
            nparams += 1
            concepts = [window(n, ell, start) for start in range(n)]
            for size in (1, 2):
                observed = 0
                for support in combinations(range(n), size):
                    yes = len({tuple(p in c for p in support) for c in concepts}) == (1 << size)
                    if size == 2:
                        a, b = support
                        circular_distance = min((b - a) % n, (a - b) % n)
                        assert yes == (circular_distance < w), (n, ell, support)
                    observed += yes
                    supports_checked += 1
                expected = n if size == 1 else n * (w - 1)
                assert observed == expected, (n, ell, size, observed, expected)
            if n <= 11:
                for support in combinations(range(n), 3):
                    assert len({tuple(p in c for p in support) for c in concepts}) < 8, (n, ell, support)
                    supports_checked += 1
    for n, ell in ((32, 16), (101, 50), (1024, 512), (57, 2), (57, 55)):
        assert verify_witness_tree(n, ell) == min(ell, n-ell).bit_length()
    print(f'ALL_CYCLIC_WINDOW_CHECKS_PASS {nparams} parameter_pairs {supports_checked} supports')


if __name__ == '__main__':
    main()
