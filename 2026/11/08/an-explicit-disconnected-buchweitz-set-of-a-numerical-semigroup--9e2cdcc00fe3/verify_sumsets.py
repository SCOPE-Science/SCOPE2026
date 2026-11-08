#!/usr/bin/env python3
"""Exact interval-union certificate for a disconnected Buchweitz set."""

H = [(0, 58), (73, 73), (111, 112), (118, 118)]
EXPECTED = {
    2: (186, 0), 3: (311, 1), 4: (434, 0),
    5: (558, 0), 6: (683, 1), 7: (807, 1), 8: (930, 0),
}
BASE8 = [(0, 914), (916, 920), (923, 926),
         (930, 932), (937, 938), (944, 944)]
E = {1, 2, 3, 4, 5, 8, 9, 10, 11, 15, 16, 17, 22, 23, 29}


def merge(intervals):
    ans = []
    for lo, hi in sorted(intervals):
        if ans and lo <= ans[-1][1] + 1:
            ans[-1] = (ans[-1][0], max(ans[-1][1], hi))
        else:
            ans.append((lo, hi))
    return ans


def add_intervals(a, b):
    return merge([(x + u, y + v) for x, y in a for u, v in b])


assert merge(H) == H
assert len(E) == 15
# Independent arithmetic characterization of the 6,7 semigroup gaps.
assert E == {d for d in range(30)
             if not any(6 * u + 7 * v == d
                        for u in range(6) for v in range(6))}
assert all(any(6 * u + 7 * v == d for u in range(d // 6 + 1)
               for v in range(d // 7 + 1)) for d in range(30, 60))

intervals = H
print('n\tcardinality\tbeta\tintervals')
for n in range(2, 9):
    intervals = add_intervals(intervals, H)
    c = sum(b - a + 1 for a, b in intervals)
    beta = c - (2 * n - 1) * 62
    assert (c, beta) == EXPECTED[n]
    print(f'{n}\t{c}\t{beta}\t' + ';'.join(f'{a}-{b}' for a,b in intervals))
assert intervals == BASE8
assert sum(b-a+1 for a,b in BASE8) == 118*8 + 1 - len(E)
assert set(range(118*8+1)) - {x for lo,hi in BASE8
                                 for x in range(lo,hi+1)} == {118*8-d for d in E}
# Infinite step checked symbolically in the mathematical argument:
# (nH+[0,58]) union (nH+{118}) fills [0,118(n+1)-30],
# and the top 30 positions are resolved by deficits 6 and 7.
print('BASE8_OK; DEFICIT_GAPS_OK; RECURSION_CERTIFICATE_OK')
