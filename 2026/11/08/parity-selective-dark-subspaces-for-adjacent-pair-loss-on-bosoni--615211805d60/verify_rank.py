#!/usr/bin/env python3
"""Finite-field observability checks for two freely hopping bosons with adjacent-pair loss.

This checker uses an integer, unnormalised symmetric-tensor basis and does not
construct the Fourier projector. It corroborates the separate all-n proof.
"""


def h_transpose_columns(n):
    pairs = [(a, b) for a in range(n) for b in range(a, n)]
    idx = {p: i for i, p in enumerate(pairs)}
    size = len(pairs)
    columns = []
    for a, b in pairs:
        ordered = [(a, b)] if a == b else [(a, b), (b, a)]
        acc = {}
        for x, y in ordered:
            for xp, yp in (((x + 1) % n, y), ((x - 1) % n, y),
                           (x, (y + 1) % n), (x, (y - 1) % n)):
                acc[(xp, yp)] = acc.get((xp, yp), 0) + 1
        col = [0] * size
        for (u, v), c in acc.items():
            if u <= v:
                col[idx[(u, v)]] = c
        columns.append(col)
    # H[column_target, column_source].  The transpose maps row observables.
    return pairs, columns


def rank_observable(n, p):
    pairs, columns = h_transpose_columns(n)
    size = len(pairs)
    adj = [i for i, (a, b) in enumerate(pairs)
           if a != b and (a - b) % n in (1, n - 1)]
    pivots = {}
    queue = []

    def insert(v):
        v = [x % p for x in v]
        for pivot in sorted(pivots):
            c = v[pivot]
            if c:
                b = pivots[pivot]
                v = [(x - c * y) % p for x, y in zip(v, b)]
        first = next((j for j, x in enumerate(v) if x), None)
        if first is None:
            return False
        inv = pow(v[first], -1, p)
        v = [(x * inv) % p for x in v]
        pivots[first] = v
        queue.append(v)
        return True

    for i in adj:
        v = [0] * size
        v[i] = 1
        insert(v)
    head = 0
    while head < len(queue):
        v = queue[head]
        head += 1
        # H.T*v has i-th coefficient dot(H[:,i],v)
        out = [sum(cj * v[j] for j, cj in enumerate(col)) % p
               for col in columns]
        insert(out)
    return size - len(pivots)


def predicted(n):
    return 0 if n % 2 else (n - 1 if n % 4 == 0 else n - 2)


if __name__ == '__main__':
    for n in range(3, 17):
        vals = [rank_observable(n, p) for p in (1000003, 1000033)]
        want = predicted(n)
        assert vals == [want, want], (n, vals, want)
        print('n=%2d dark_rank=%3d moduli_agree=yes' % (n, want))
    print('PASS: all modular observability ranks agree with closed formula')
