"""Independent finite checks for online shattering by nonempty intervals.

Run with: python3 verify_intervals.py
Uses only the Python standard library.
"""
from functools import lru_cache
from math import comb


def log2_floor(m):
    assert m > 0
    return m.bit_length() - 1


def normalize(parts):
    return tuple(sorted((p for p in parts if p > 0), reverse=True))


@lru_cache(None)
def rank_partition(parts):
    """Exact online rank after negative-only observations.

    parts lists the nonzero lengths of available runs. The empty tuple
    describes an empty version space and has rank -1 as a sentinel.
    """
    if not parts:
        return -1
    best = 0
    for index, length in enumerate(parts):
        for offset in range(1, length + 1):
            positive = log2_floor(offset) + log2_floor(length - offset + 1)
            rest = list(parts)
            rest.pop(index)
            rest.extend((offset - 1, length - offset))
            negative = rank_partition(normalize(rest))
            best = max(best, 1 + min(positive, negative))
    return best


def rank_bruteforce(n):
    """Independent general version-space recursion using an explicit bitmask."""
    intervals = [sum(1 << j for j in range(a, b + 1))
                 for a in range(n) for b in range(a, n)]
    query_masks = [sum(1 << h for h, bits in enumerate(intervals)
                       if bits & (1 << site)) for site in range(n)]

    @lru_cache(None)
    def rank(state):
        if state == 0:
            return -1
        best = 0
        for q in query_masks:
            yes = state & q
            no = state & ~q
            if yes and no:
                best = max(best, 1 + min(rank(yes), rank(no)))
        return best
    return rank((1 << len(intervals)) - 1)


def assert_vc(n):
    ivs = [sum(1 << j for j in range(a, b + 1))
           for a in range(n) for b in range(a, n)]
    result = 0
    for mask in range(1 << n):
        traces = {hyp & mask for hyp in ivs}
        if len(traces) == (1 << mask.bit_count()):
            result = max(result, mask.bit_count())
    return result


def check_all_histories(n):
    """Check every realizable three-valued query history on n sites."""
    intervals = [sum(1 << j for j in range(a, b + 1))
                 for a in range(n) for b in range(a, n)]
    query_masks = [sum(1 << h for h, bits in enumerate(intervals)
                       if bits & (1 << site)) for site in range(n)]

    @lru_cache(None)
    def rank(state):
        if state == 0: return -1
        best = 0
        for qm in query_masks:
            yes, no = state & qm, state & ~qm
            if yes and no:
                best = max(best, 1 + min(rank(yes), rank(no)))
        return best

    checked = 0
    for encoding in range(3 ** n):
        labels = []
        x = encoding
        for _ in range(n):
            labels.append(x % 3)  # 0 unknown, 1 positive, 2 negative
            x //= 3
        present = [i for i, z in enumerate(labels) if z == 1]
        absent = [i for i, z in enumerate(labels) if z == 2]
        state = (1 << len(intervals)) - 1
        for i in present: state &= query_masks[i]
        for i in absent: state &= ~query_masks[i]
        if not state: continue
        if present:
            first, last = min(present), max(present)
            assert all(not first <= i <= last for i in absent)
            left_bound = max([i for i in absent if i < first] + [-1])
            right_bound = min([i for i in absent if i > last] + [n])
            L, R = first - left_bound, right_bound - last
            prediction = log2_floor(L) + log2_floor(R)
        else:
            runs, current = [], 0
            for val in labels:
                if val != 2: current += 1
                elif current:
                    runs.append(current)
                    current = 0
            if current: runs.append(current)
            prediction = rank_partition(normalize(runs))
        assert prediction == rank(state), (n, encoding, prediction, rank(state))
        checked += 1
    return checked


def main():
    expected = [0, 1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6,
                7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8,
                8, 8, 8, 9, 9]
    for n, target in enumerate(expected, 1):
        computed = rank_partition((n,))
        assert computed == target, (n, computed, target)
    for n in range(1, 11):
        assert rank_partition((n,)) == rank_bruteforce(n), n
        assert assert_vc(n) == min(2, n - 1), n
    history_checks = sum(check_all_histories(n) for n in range(1, 9))
    for k in range(0, 6):
        n = (1 << (k + 1)) - 1
        if n <= 40:
            computed = rank_partition((n,))
            assert computed == 2 * k, (n, computed)
        total = n * (n + 1) // 2
        assert total < (1 << (2*k + 1))
    print('INTERVAL_ONLINE_PASS dp_n=1..40 brute_n=1..10 vc_n=1..10 all_histories_n=1..8 checked=%d dyadic_k=0..5' % history_checks)


if __name__ == '__main__':
    main()
