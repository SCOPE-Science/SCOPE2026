"""Finite checks for alternating box-diamond modal convergence.

Run with Python 3.9+; uses no third-party libraries. This is a finite
consistency check, not a substitute for the all-size mathematical proof.
"""
from itertools import product
from random import Random


def ranks_of_frame(rows):
    n = len(rows)
    bits = (1 << n) - 1
    bad = 0
    ranks = [0] * n  # 0 denotes non-failure at any finite iterate.
    for depth in range(1, n + 2):
        new = 0
        for x in range(n):
            for y in range(n):
                if ((rows[x] >> y) & 1) and rows[y] & ~bad == 0:
                    new |= 1 << x
                    break
        assert (new | bad) == new
        for x in range(n):
            if ((new >> x) & 1) and not ((bad >> x) & 1):
                ranks[x] = depth
        if new == bad:
            break
        bad = new
    else:
        raise AssertionError("Iteration did not stabilize")
    return ranks


def certificate(rows, ranks, start):
    t = ranks[start]
    assert t > 0
    path = []
    x = start
    for j in range(t, 0, -1):
        assert ranks[x] == j
        path.append(x)
        witnesses = []
        for y in range(len(rows)):
            if not ((rows[x] >> y) & 1):
                continue
            successor_ranks = [ranks[z] for z in range(len(rows))
                               if (rows[y] >> z) & 1]
            if (not successor_ranks and j == 1) or (
                successor_ranks and all(0 < k <= j-1 for k in successor_ranks)
                and max(successor_ranks) == j-1):
                witnesses.append(y)
        assert witnesses
        y = witnesses[0]
        assert ranks[y] == 0
        path.append(y)
        if j > 1:
            x = next(z for z in range(len(rows))
                     if ((rows[y] >> z) & 1) and ranks[z] == j-1)
        else:
            assert rows[y] == 0
    assert len(path) == 2*t and len(set(path)) == 2*t
    assert all((rows[a] >> b) & 1 for a,b in zip(path,path[1:]))
    return path


def verify(rows):
    n = len(rows)
    ranks = ranks_of_frame(rows)
    assert max(ranks, default=0) <= n // 2
    for x in range(n):
        if ranks[x]:
            certificate(rows, ranks, x)


def run():
    total = 0
    for n in range(1,5):
        rowmask = (1 << n)-1
        for mask in range(1 << (n*n)):
            rows = [(mask >> (i*n)) & rowmask for i in range(n)]
            verify(rows)
            total += 1
    rng = Random(20260613)
    samples = 0
    for n in (5,6,7,8):
        for _ in range(2500):
            rows = [rng.getrandbits(n) for _ in range(n)]
            verify(rows)
            samples += 1
    for t in range(1,31):
        n = 2*t
        rows = [1 << (i+1) if i+1<n else 0 for i in range(n)]
        ranks = ranks_of_frame(rows)
        assert ranks[0] == t
        assert max(ranks) == t
        assert certificate(rows,ranks,0) == list(range(n))
    print('ALTERNATING_MODAL_HALF_SIZE_OK exhaustive_frames=',total,
          'sampled_frames=',samples,'sharp_path_sizes=2..60')


if __name__ == '__main__':
    run()
