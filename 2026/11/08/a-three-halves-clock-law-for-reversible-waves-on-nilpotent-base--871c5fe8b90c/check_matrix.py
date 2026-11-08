"""Exact binary-matrix tests of the nilpotent-base prism wave census.

Requires Python 3 standard library only. All arithmetic is in GF(2).
"""
from itertools import combinations


def identity(n):
    return tuple(1 << i for i in range(n))


def matrix_mul(a, b):
    return tuple(xor_rows(row, b) for row in a)


def xor_rows(bits, b):
    v = 0
    while bits:
        low = bits & -bits
        v ^= b[low.bit_length() - 1]
        bits ^= low
    return v


def matrix_power(a, k):
    p = identity(len(a))
    while k:
        if k & 1:
            p = matrix_mul(p, a)
        a = matrix_mul(a, a)
        k >>= 1
    return p


def rank(a):
    basis = {}
    for row in a:
        x = row
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def nullity(a):
    return len(a) - rank(a)


def nilpotent_blocks(b):
    n = len(b)
    nulls = [0]
    power = identity(n)
    for j in range(1, n + 1):
        power = matrix_mul(power, b)
        nulls.append(nullity(power))
        if power == (0,) * n:
            break
    if power != (0,) * n:
        return None
    counts = []
    for j in range(1, len(nulls)):
        before = nulls[j] - nulls[j - 1]
        after = (nulls[j + 1] - nulls[j]) if j + 1 < len(nulls) else 0
        counts += [j] * (before - after)
    return sorted(counts)


def adjacency(n, mask):
    edges = list(combinations(range(n), 2))
    b = [0] * n
    for idx, (u, v) in enumerate(edges):
        if (mask >> idx) & 1:
            b[u] |= 1 << v
            b[v] |= 1 << u
    return tuple(b)


def prism_adjacency(b):
    n = len(b)
    a = [0] * (2 * n)
    for i in range(n):
        for side in range(2):
            j = 2 * i + side
            a[j] = 1 << (2 * i + (1 - side))
            for k in range(n):
                if b[i] >> k & 1:
                    a[j] |= 1 << (2 * k + side)
    return tuple(a)


def wave_matrix(a):
    m = len(a)
    return tuple((a[i] | (1 << (m + i))) for i in range(m)) + tuple(1 << i for i in range(m))


def predicted_blocks(blocks):
    out = []
    for s in blocks:
        if s % 2 == 0:
            out += [s, s]
        else:
            out += [s + 1]
            if s > 1:
                out += [s - 1]
    return sorted(out)


def predicted_fixed(t, blocks):
    if t % 3:
        return 0
    j = (t & -t).bit_length() - 1
    return 2 * sum(min(s, 1 << j) for s in blocks)


def check_one(b, checkpoints):
    blocks = nilpotent_blocks(b)
    if blocks is None:
        return False
    a = prism_adjacency(b)
    m = len(a)
    predicted = predicted_blocks(blocks)
    assert nilpotent_blocks(tuple(x ^ (1 << i) for i, x in enumerate(a))) == predicted, (b, blocks, predicted)
    wave = wave_matrix(a)
    total = 2 * m
    bound = 3 * (1 << ((max(predicted) - 1).bit_length()))
    base_wave = wave_matrix(b)
    base_bound = 2 * (1 << ((max(blocks) - 1).bit_length()))
    assert matrix_power(base_wave, base_bound) == identity(len(base_wave))
    assert matrix_power(base_wave, base_bound // 2) != identity(len(base_wave))
    assert 2 * bound == (6 if b == (0,) * len(b) else 3) * base_bound
    assert matrix_power(wave, bound) == identity(total)
    assert matrix_power(wave, bound // 2) != identity(total)
    assert matrix_power(wave, bound // 3) != identity(total)
    for t in (1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 18, 24, 36, 48):
        x = tuple(row ^ (1 << i) for i, row in enumerate(matrix_power(wave, t)))
        assert nullity(x) == predicted_fixed(t, predicted), (b, t, nullity(x), predicted_fixed(t, predicted))
        checkpoints[0] += 1
    return True


def main():
    tested = 0
    graphs = 0
    checkpoints = [0]
    for n in range(1, 6):
        for mask in range(1 << (n * (n - 1) // 2)):
            graphs += 1
            if check_one(adjacency(n, mask), checkpoints):
                tested += 1
    print('labelled simple graphs examined:', graphs)
    print('nilpotent-adjacency base graphs tested:', tested)
    print('wave fixed-space comparisons:', checkpoints[0])
    for r in range(2, 5):
        n = (1 << r) - 1
        p = [0] * n
        for j in range(n - 1):
            p[j] |= 1 << (j + 1)
            p[j + 1] |= 1 << j
        assert nilpotent_blocks(tuple(p)) == [n]
        a = prism_adjacency(tuple(p))
        assert nilpotent_blocks(tuple(x ^ (1 << i) for i, x in enumerate(a))) == [n - 1, n + 1]
        w = wave_matrix(a)
        assert matrix_power(w, 3 * (n + 1)) == identity(len(w))
        assert matrix_power(w, 3 * (n + 1) // 2) != identity(len(w))
        print('dyadic open ladder width=2, length=', n, 'wave order=', 3 * (n + 1))
    print('PASS')


if __name__ == '__main__':
    main()
