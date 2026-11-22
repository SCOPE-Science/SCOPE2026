"""Independent finite-field row reduction for closed-neighborhood parity equations."""
from collections import Counter


def masks(kind, n):
    N = 2 * n
    out = []
    for v in range(N):
        if kind == 'mobius':
            nbr = [(v - 1) % N, v, (v + 1) % N, (v + n) % N]
        else:
            layer, j = divmod(v, n)
            nbr = [v, layer * n + (j - 1) % n,
                   layer * n + (j + 1) % n, (1 - layer) * n + j]
        assert len(set(nbr)) == 4
        out.append(sum(1 << k for k in nbr))
    return out


def solutions(rows, t):
    N = len(rows)
    augmented = [r | (t << N) for r in rows]
    pivots = []
    k = 0
    for c in range(N):
        nxt = next((j for j in range(k, N) if augmented[j] >> c & 1), None)
        if nxt is None:
            continue
        augmented[k], augmented[nxt] = augmented[nxt], augmented[k]
        for j in range(N):
            if j != k and (augmented[j] >> c & 1):
                augmented[j] ^= augmented[k]
        pivots.append(c)
        k += 1
    assert all(not (a >> N & 1) or (a & ((1 << N) - 1)) for a in augmented[k:])
    free = [c for c in range(N) if c not in pivots]
    assert len(free) <= 6
    counter = Counter()
    for free_mask in range(1 << len(free)):
        x = 0
        for j, f in enumerate(free):
            if free_mask >> j & 1:
                x |= 1 << f
        for i in range(k - 1, -1, -1):
            p = pivots[i]
            x |= (((augmented[i] >> N & 1) ^ ((augmented[i] & x).bit_count() % 2)) << p)
        assert all(((r & x).bit_count() % 2) == t for r in rows)
        counter[x.bit_count()] += 1
    return dict(counter), 1 << len(free)


def expectation(kind, n, t):
    if n % 2:
        return ({0: 1, 2 * n: 1} if t == 0 else {n: 2})
    if kind == 'mobius':
        if n % 4 == 0:
            return ({0: 1, n: 2, 2 * n: 1} if t == 0 else {n: 4})
        return ({0: 1, n: 6, 2 * n: 1} if t == 0 else {n // 2: 4, 3 * n // 2: 4})
    if n % 4 == 2:
        return ({0: 1, n: 2, 2 * n: 1} if t == 0 else {n: 4})
    return ({0: 1, n: 14, 2 * n: 1} if t == 0 else {n // 2: 4, n: 8, 3 * n // 2: 4})


def main():
    tested = 0
    for n in range(3, 81):
        for kind in ('mobius', 'prism'):
            rows = masks(kind, n)
            for t in (0, 1):
                weights, size = solutions(rows, t)
                expected = expectation(kind, n, t)
                assert weights == expected, (kind, n, t, weights, expected)
                assert size == sum(expected.values())
                tested += 1
    print(f'PASS: {tested} direct binary-elimination cases on 3 <= n <= 80; both targets and graph families')

if __name__ == '__main__':
    main()
