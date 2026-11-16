"""Exact finite Fourier-sampling rank certificate for order-five alternating-sign matrices.

Requires Python 3 and NumPy. All linear algebra is over integers or F_101;
no floating-point rank tests are used.
"""
import json
from itertools import combinations
from math import comb
from pathlib import Path
import numpy as np

N = 5
PRIME = 101
HERE = Path(__file__).resolve().parent

def enumerate_asm(n):
    row_patterns = []
    for weight in range(1, n + 1, 2):
        for locations in combinations(range(n), weight):
            row = [0] * n
            for k, pos in enumerate(locations):
                row[pos] = 1 if k % 2 == 0 else -1
            row_patterns.append(tuple(row))
    output = []
    def rec(matrix, column_prefix):
        if len(matrix) == n:
            if all(v == 1 for v in column_prefix):
                output.append(tuple(v for row in matrix for v in row))
            return
        for row in row_patterns:
            next_prefix = tuple(a + b for a, b in zip(column_prefix, row))
            if all(v in (0, 1) for v in next_prefix):
                rec(matrix + [row], next_prefix)
    rec([], (0,) * n)
    return output

def modular_rank(mat, p):
    a = np.array(mat, dtype=np.int64, copy=True) % p
    nr, nc = a.shape
    row = 0
    for col in range(nc):
        choices = np.flatnonzero(a[row:, col])
        if choices.size == 0:
            continue
        pivot_row = row + int(choices[0])
        a[[row, pivot_row]] = a[[pivot_row, row]]
        inverse = pow(int(a[row, col]), -1, p)
        a[row, col:] = (a[row, col:] * inverse) % p
        targets = np.flatnonzero(a[row+1:, col]) + row + 1
        if targets.size:
            a[targets, col:] = (a[targets, col:] - a[targets, col, None] * a[row, col:]) % p
        row += 1
        if row == nr:
            break
    return row

def agreement_grams(matrices):
    arr = np.asarray(matrices, dtype=np.int8)
    same = np.sum(arr[:, None, :] == arr[None, :, :], axis=2)
    g3 = np.zeros_like(same, dtype=np.int64)
    for k in range(4):
        g3 += np.frompyfunc(lambda v: comb(int(v), k), 1, 1)(same).astype(np.int64)
    g4 = g3 + np.frompyfunc(lambda v: comb(int(v), 4), 1, 1)(same).astype(np.int64)
    return g3, g4

def main():
    for n, count in [(2, 2), (3, 7), (4, 42), (5, 429)]:
        data = enumerate_asm(n)
        assert len(data) == len(set(data)) == count, (n, len(data))
    for small_n in (2, 3, 4):
        small = enumerate_asm(small_n)
        small_a = np.asarray(small, dtype=np.int8)
        agreements = np.sum(small_a[:, None, :] == small_a[None, :, :], axis=2)
        small_g3 = np.zeros((len(small), len(small)), dtype=np.int64)
        for kk in range(4):
            small_g3 += np.frompyfunc(lambda z: comb(int(z), kk), 1, 1)(agreements).astype(np.int64)
        assert modular_rank(small_g3, PRIME) == len(small)
    sample = enumerate_asm(N)
    assert len(sample) == 429
    g3, g4 = agreement_grams(sample)
    assert np.array_equal(g3, g3.T)
    assert np.array_equal(g4, g4.T)
    assert modular_rank(g3, PRIME) == 425
    assert modular_rank(g4, PRIME) == 429
    cert = json.loads((HERE / 'kernel_certificate.json').read_text(encoding='utf-8'))
    assert cert['ordering'] == 'row-patterns by increasing odd weight, then combinations, recursing top to bottom'
    vectors = []
    for sparse in cert['vectors']:
        v = np.zeros(429, dtype=np.int64)
        for i, sign in sparse:
            assert v[i] == 0 and sign in (-1, 1)
            v[i] = sign
        assert int(v.sum()) == 0
        assert np.array_equal(g3 @ v, np.zeros(429, dtype=np.int64))
        vectors.append(v)
    assert len(vectors) == 4
    anchor = np.stack(vectors)[:, cert['anchor_indices']]
    assert np.array_equal(anchor, np.eye(4, dtype=np.int64)), anchor
    assert [int(np.count_nonzero(v)) for v in vectors] == [16,16,134,120]
    # Rank over R is at least rank over F_101; four Q-independent null
    # vectors bound it above by 425. Full rank modulo 101 proves quartic
    # identifiability in characteristic zero.
    print(json.dumps({'asm_count':len(sample), 'degree3_rank':425,
                      'degree3_kernel_dimension':4, 'degree4_rank':429,
                      'certificate_supports':[16,16,134,120],
                      'field':'F_101', 'status':'PASS'}))

if __name__ == '__main__':
    main()
