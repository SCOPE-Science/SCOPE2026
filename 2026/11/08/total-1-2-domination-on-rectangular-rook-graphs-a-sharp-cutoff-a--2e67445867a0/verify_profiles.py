"""Independent exact integer DP by target row degrees and column subsets.
Run: python3 verify_profiles.py
"""
from collections import defaultdict, Counter
from itertools import product
from math import comb

def expected(m, n):
    a, b = sorted([m, n])
    if a == 2:
        return {k: v for k, v in [(2, b + 2 * int(b == 2)),
                                  (3, 2 * b * (b - 1) + 2 * int(b == 3)),
                                  (4, comb(b, 2))] if v}
    if a == 3:
        return {3: b + 3 * int(b == 3)}
    return {}

def count_by_profile(m, n):
    # Each selected vertex has at most two neighbors in the selection.
    # Therefore each row has at most 3 members: if it contained >=4,
    # a selected vertex would have at least 3 selected row neighbors.
    ans = Counter()
    masks = list(range(1 << m))
    bits = [tuple((q >> i) & 1 for i in range(m)) for q in masks]
    for target in product(range(min(3, n) + 1), repeat=m):
        options = []
        for q, b in zip(masks, bits):
            degree = q.bit_count()
            if all(1 <= target[i] + degree - 2 * b[i] <= 2 for i in range(m)):
                options.append((q, b))
        if not options:
            continue
        zero = (0,) * m
        states = {zero: 1}
        for col in range(n):
            new = defaultdict(int)
            for v, weight in states.items():
                for _, b in options:
                    nxt = tuple(v[i] + b[i] for i in range(m))
                    if all(nxt[i] <= target[i] for i in range(m)):
                        new[nxt] += weight
            states = new
            if not states:
                break
        ans[sum(target)] += states.get(target, 0)
    return {k: v for k, v in ans.items() if v}

def main():
    boards = [(2, n) for n in [2, 3, 4, 5, 8, 12, 20]]
    boards += [(3, n) for n in [3, 4, 5, 8, 12]]
    boards += [(4, n) for n in [4, 5, 6, 8]]
    boards += [(5, 5), (5, 6), (6, 6)]
    for m, n in boards:
        got = count_by_profile(m, n)
        want = expected(m, n)
        assert got == want, (m, n, got, want)
        print(f'({m},{n}) {dict(sorted(got.items()))} PASS')
    print('PROFILE_DP_PASS', len(boards))
if __name__ == '__main__':
    main()
