"""Independent matrix-power checks for a triangular-graph chorded XOR map.
Run: python verify_rank.py
"""
from itertools import combinations
from functools import reduce


def graph(n, chord=True):
    pairs = list(combinations(range(n), 2))
    rows = []
    for e in pairs:
        rows.append(sum(1 << j for j, f in enumerate(pairs)
                        if len(set(e) & set(f)) == 1))
    if chord:
        i, j = pairs.index((0, 1)), pairs.index((2, 3))
        rows[i] ^= 1 << j
        rows[j] ^= 1 << i
    return rows


def mul(A, B):
    rows = []
    for x in A:
        s = 0
        while x:
            lsb = x & -x
            s ^= B[lsb.bit_length() - 1]
            x ^= lsb
        rows.append(s)
    return rows


def rank(rows):
    pivots = {}
    for x in rows:
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def addI(A):
    return [x ^ (1 << i) for i, x in enumerate(A)]


def run():
    cases = 0
    for n in range(4, 17):
        A = graph(n)
        N = len(A)
        orig = graph(n, False)
        I = [1 << j for j in range(N)]
        assert mul(orig, orig) == (orig if n % 2 else [0] * N)
        powers = [I]
        for i in range(6):
            powers.append(mul(powers[-1], A))
        expect = ((n + 1, n + 1, n + 1) if n % 2
                  else (n, 2 if n == 4 else 4, 2))
        assert tuple(rank(powers[i]) for i in range(1, 4)) == expect, n
        if n % 2:
            assert powers[5] == powers[1], n
            dims = (n - 3, n - 1, n + 1)
            assert tuple(N - rank(addI(powers[i])) for i in (1, 2, 4)) == dims, n
            assert powers[3] != powers[1] and powers[2] != powers[1]
        else:
            assert powers[5] == powers[3], n
            assert tuple(N - rank(addI(powers[i])) for i in (1, 2)) == (1, 2), n
            assert powers[2] == powers[4] if n == 4 else powers[2] != powers[4]
        cases += 1
    print('PASS rank-power check: %d dimensions (4..16), original and edited.' % cases)

if __name__ == '__main__':
    run()
