"""Direct full-subset check of total [1,2]-domination in selected rook graphs.
Run: python3 verify_direct.py
"""
from collections import Counter
from math import comb

def expected(m, n):
    a, b = sorted((m, n))
    if a == 2:
        return {k: v for k, v in ((2, b + 2 * (b == 2)),
                                   (3, 2 * b * (b - 1) + 2 * (b == 3)),
                                   (4, comb(b, 2))) if v}
    if a == 3:
        return {3: b + 3 * (b == 3)}
    return {}

def count_direct(m, n):
    adj = []
    for i in range(m):
        for j in range(n):
            mask = 0
            for k in range(m):
                for ell in range(n):
                    if (i == k or j == ell) and (i, j) != (k, ell):
                        mask |= 1 << (k * n + ell)
            adj.append(mask)
    hist = Counter()
    for s in range(1 << (m * n)):
        if all(1 <= (s & a).bit_count() <= 2 for a in adj):
            hist[s.bit_count()] += 1
    return dict(hist)

def main():
    boards = [(2, j) for j in range(2, 9)] + [(3, j) for j in range(3, 7)] + [(4, 4), (4, 5)]
    for m, n in boards:
        got = count_direct(m, n)
        want = expected(m, n)
        assert got == want, (m, n, got, want)
        print(f'({m},{n}) {dict(sorted(got.items()))} PASS')
    print('DIRECT_CHECK_PASS', len(boards))
if __name__ == '__main__':
    main()
