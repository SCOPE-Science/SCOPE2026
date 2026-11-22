"""Exhaustive small-order checks for parity-filtered permutation incidence."""
from itertools import permutations, combinations
from math import comb, factorial


def sign(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2


def is_matching(s):
    return len({x for x, y in s}) == len(s) and len({y for x, y in s}) == len(s)


def check(n):
    board = tuple((a, b) for a in range(n) for b in range(n))
    pp = [(p, sign(p)) for p in permutations(range(n))]
    assert len(pp) == factorial(n)
    total_checked = 0
    balanced = 0
    matched_checked = 0
    leakage_checked = 0
    for k in range(n):
        for s in combinations(board, k):
            if k <= n - 2:
                traces = [[0] * (1 << k), [0] * (1 << k)]
                for p, sg in pp:
                    mask = sum(1 << i for i, (a, b) in enumerate(s) if p[a] == b)
                    traces[sg][mask] += 1
                assert traces[0] == traces[1], (n, s, traces)
                balanced += 1
                if is_matching(s):
                    assert all(x > 0 for x in traces[0]), (n, s)
                    for mask in range(1 << k):
                        t = mask.bit_count()
                        r = k - t
                        expected = sum((-1)**j * comb(r,j) * factorial(n-t-j) for j in range(r+1)) // 2
                        assert traces[0][mask] == expected, (n, s, mask)
                    matched_checked += 1
            elif k == n - 1 and is_matching(s):
                count = [[0] * (1 << k), [0] * (1 << k)]
                for p, sg in pp:
                    mask = sum(1 << i for i, (a, b) in enumerate(s) if p[a] == b)
                    count[sg][mask] += 1
                remaining_row = next(i for i in range(n) if i not in {a for a, b in s})
                remaining_col = next(i for i in range(n) if i not in {b for a, b in s})
                completion = [None] * n
                for a, b in s:
                    completion[a] = b
                completion[remaining_row] = remaining_col
                completion_sign = 1 if sign(completion) == 0 else -1
                for mask in range(1 << k):
                    expected = completion_sign * (-1)**(k - mask.bit_count())
                    assert count[0][mask] - count[1][mask] == expected, (n, s, mask)
                assert sum(abs(a-b) for a,b in zip(count[0],count[1])) == (1 << k)
                assert sum(1 for x in count[0] if x) < (1 << k)
                assert sum(1 for x in count[1] if x) < (1 << k)
                matched_checked += 1
                leakage_checked += 1
            total_checked += 1
    # All size-n matching supports are automatically unshattered: positivity of n-1 edges forces the nth.
    assert sum(comb(n,k)**2*factorial(k) for k in range(n-1)) == matched_checked - (comb(n,n-1)**2*factorial(n-1))
    print(f'n={n} all-permutations={len(pp)} parity-balanced-supports={balanced} tested-matching-supports={matched_checked} leakage-matching-supports={leakage_checked} PASS')

for n in range(2,6):
    check(n)
print('PYTHON_ALL_PASS')
