"""Direct enumeration of the reversible binary wave on dyadic open ladders.

Python standard library only; no symbolic matrix package is used.
"""
from collections import Counter


def ladder_neighbors(n):
    adj = [0] * (2 * n)
    for i in range(n):
        for side in range(2):
            j = 2 * i + side
            adj[j] |= 1 << (2 * i + 1 - side)
            for other in (i - 1, i + 1):
                if 0 <= other < n:
                    adj[j] |= 1 << (2 * other + side)
    return adj


def apply_adj(u, neighbors):
    out = 0
    for i, nbrs in enumerate(neighbors):
        out |= (((u & nbrs).bit_count() & 1) << i)
    return out


def step(state, adj):
    size = len(adj)
    mask = (1 << size) - 1
    u = state & mask
    v = state >> size
    return (u << size) | (apply_adj(u, adj) ^ v)


def predicted_counts(n):
    assert n >= 3 and (n + 1).bit_count() == 1
    a = (n + 1).bit_length() - 1
    prev = 1
    counts = {}
    for j in range(a + 1):
        h = 1 << j
        exponent = 2 * (min(n - 1, h) + min(n + 1, h))
        current = 1 << exponent
        counts[3 * h] = current - prev
        prev = current
    assert sum(counts.values()) == (1 << (4 * n)) - 1
    counts[1] = 1
    return counts


def main():
    for n in (3,):
        adj = ladder_neighbors(n)
        bound = 3 * (n + 1)
        census = Counter()
        for state in range(1 << (4 * n)):
            x = step(state, adj)
            period = 1
            while x != state:
                x = step(x, adj)
                period += 1
                assert period <= bound, (n, state, period)
            census[period] += 1
        predicted = predicted_counts(n)
        assert dict(census) == predicted, (census, predicted)
        print('open ladder vertices:', 2 * n)
        print('exhaustively enumerated initial pairs:', 1 << (4 * n))
        print('primitive populations:', sorted(census.items()))
    print('PASS')


if __name__ == '__main__':
    main()
