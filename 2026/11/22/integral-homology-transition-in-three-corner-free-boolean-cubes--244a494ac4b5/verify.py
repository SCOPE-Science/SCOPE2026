#!/usr/bin/env python3
"""Recompute integral homology of cube-square three-corner avoidance complexes."""
import pathlib
import subprocess
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
EXPECTED = {
    2: {1: 3},
    3: {2: 3},
    4: {3: 16, 4: 1},
    5: {7: 681},
}
EXPECTED_FACES = {2: 11, 3: 77, 4: 3055, 5: 3302633}
EXPECTED_RANKS = {2: {}, 3: {}, 4: {4: 1, 5: 4},
                  5: {6: 1, 7: 15, 8: 61, 9: 12, 10: 0, 11: 1}}

def unit_smith(a, r, c):
    # Explicit elementary integer row and column operations by unit pivots.
    m = [row[:] for row in a]
    p = 0
    while p < min(r, c):
        candidate = next(((i, j) for i in range(p, r)
                          for j in range(p, c) if abs(m[i][j]) == 1), None)
        if candidate is None:
            break
        i, j = candidate
        m[p], m[i] = m[i], m[p]
        for row in m:
            row[p], row[j] = row[j], row[p]
        if m[p][p] < 0:
            m[p] = [-x for x in m[p]]
        for i in range(p + 1, r):
            t = m[i][p]
            if t:
                m[i] = [x - t * y for x, y in zip(m[i], m[p])]
        for j in range(p + 1, c):
            t = m[p][j]
            if t:
                for row in m:
                    row[j] -= t * row[p]
        p += 1
    assert all(m[i][j] == 0 for i in range(p, r) for j in range(p, c)), \
        'Nonunit residual requires further Smith reduction'
    return p

def read_boundary(p):
    with p.open() as fh:
        r, c = map(int, fh.readline().split())
        cols = []
        for _ in range(c):
            line = fh.readline()
            assert line, (p, 'missing column')
            col = list(map(int, line.split()))
            assert len(col) == r
            cols.append(col)
        assert not fh.read().strip()
    return (r, c, [[cols[j][i] for j in range(c)] for i in range(r)])

def matrix_product_zero(a, b):
    r, m, A = a
    m2, c, B = b
    assert m == m2
    for i in range(r):
        for j in range(c):
            assert sum(A[i][k] * B[k][j] for k in range(m)) == 0, (i, j)

def check(n, work):
    subprocess.run([str(work / 'corner_morse'), str(n)], check=True,
                   cwd=work, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    lines = (work / f'summary_n{n}.txt').read_text().splitlines()
    f = {}
    crit = {}
    for line in lines:
        parts = line.split()
        if parts[0] == 'face_size':
            f[int(parts[1])] = int(parts[2])
        if parts[0] == 'critical':
            crit[int(parts[1])] = int(parts[2])
    assert sum(f.values()) == EXPECTED_FACES[n]
    assert f[0] == 1
    assert sum((-1) ** (k - 1) * v for k, v in f.items()) == \
           sum((-1) ** d * b for d, b in EXPECTED[n].items())
    matrices = {d: read_boundary(work / f'boundary_n{n}_d{d}.txt')
                for d in crit if d >= 1}
    ranks = {}
    for d, (r, c, mat) in matrices.items():
        assert r == crit.get(d - 1, 0) and c == crit[d]
        ranks[d] = unit_smith(mat, r, c)
    assert all(ranks.get(d, 0) == rank for d, rank in EXPECTED_RANKS[n].items())
    assert set(ranks) == set(matrices)
    for d in matrices:
        if d - 1 in matrices:
            matrix_product_zero(matrices[d - 1], matrices[d])
    betti = {d: count - ranks.get(d, 0) - ranks.get(d + 1, 0)
             for d, count in crit.items()}
    betti = {d: b for d, b in betti.items() if b}
    assert betti == EXPECTED[n], (n, betti)
    print('n=', n, 'faces=', sum(f.values()), 'critical=', crit,
          'unit_Smith_ranks=', ranks, 'reduced_homology=', betti, flush=True)

with tempfile.TemporaryDirectory(prefix='corner-check-') as tmp:
    p = pathlib.Path(tmp)
    subprocess.run(['g++', '-O3', '-std=c++17', str(HERE / 'corner_morse.cpp'),
                    '-o', str(p / 'corner_morse')], check=True)
    for n in range(2, 6):
        check(n, p)
print('CUBE_THREE_CORNER_INTEGRAL_HOMOLOGY_OK')
