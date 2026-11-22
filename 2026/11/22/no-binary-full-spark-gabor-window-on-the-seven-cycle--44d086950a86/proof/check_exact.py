"""Exact integer proof of binary seven-cycle Gabor spark deficiency.

Run: python proof/check_exact.py
"""
from itertools import permutations
import json
from pathlib import Path

DATA = json.loads(Path(__file__).with_name('witnesses.json').read_text(encoding='utf-8'))
WITNESSES = DATA['witnesses']
N = 7


def binary_window(mask):
    return (1,) + tuple(-1 if mask & (1 << (x - 1)) else 1 for x in range(1, N))


def normalized_mask(seq):
    if seq[0] == -1:
        seq = tuple(-v for v in seq)
    assert seq[0] == 1
    return sum((1 << (j - 1)) for j in range(1, N) if seq[j] == -1)


def orbit(mask):
    g = binary_window(mask)
    out = set()
    for shift in range(N):
        for direction in (-1, 1):
            out.add(normalized_mask(tuple(g[(shift + direction*x) % N] for x in range(N))))
    return out


def coefficient_vector(g, cols):
    # Determinant expansion into the group algebra of C_7:
    # det = sum_{r=0}^6 c[r] omega^r, omega^7=1.
    c = [0]*N
    for sigma in permutations(range(N)):
        inversions = sum(sigma[i] > sigma[j] for i in range(N) for j in range(i+1,N))
        sgn = -1 if inversions % 2 else 1
        power = 0
        for x, k in enumerate(sigma):
            a,b = divmod(cols[k], N)
            sgn *= g[(x-a) % N]
            power += b*x
        c[power % N] += sgn
    return c


def main():
    expected = {r['mask']:r['normalized_class_size'] for r in WITNESSES}
    assert len(expected) == N+2 == 9
    assert sum(expected.values()) == 64
    covered = set()
    for mask, count in expected.items():
        this = orbit(mask)
        assert len(this) == count
        assert min(this) == mask
        assert not (covered & this)
        covered.update(this)
    assert covered == set(range(64))
    print('Nine symmetry classes partition all 64 normalized sign windows.')
    for row in WITNESSES:
        mask, cols = row['mask'], row['columns']
        assert len(cols) == N == len(set(cols))
        assert all(0 <= k < N*N for k in cols)
        coeff = coefficient_vector(binary_window(mask), cols)
        assert coeff == [0]*N, (mask, coeff)
        print(f'mask={mask:2d}: seven integer determinant coefficients {coeff}')
    print('PASS: each binary seven-cycle Gabor system has a singular seven-column selection.')

if __name__ == '__main__':
    main()
