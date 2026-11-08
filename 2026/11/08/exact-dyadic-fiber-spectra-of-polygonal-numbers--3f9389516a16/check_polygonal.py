"""Independent finite tests for dyadic polygonal-number fiber classification.

Run: python3 check_polygonal.py
Uses only the Python standard library. Finite tests do not prove the infinite theorem.
"""
from collections import Counter


def square_roots(k, w):
    m = 1 << k
    w %= m
    if w == 0:
        return 1 << (k // 2)
    v = (w & -w).bit_length() - 1
    if v % 2:
        return 0
    j, h = v // 2, k - v
    z = w >> v
    if h == 1:
        return 1 << j
    if h == 2:
        return (1 << (j + 1)) if z % 4 == 1 else 0
    return (1 << (j + 2)) if z % 8 == 1 else 0


def check(s, k):
    m = 1 << k
    vals = [(((s - 2) * n * n - (s - 4) * n) // 2) % m
            for n in range(m)]
    fibers = Counter(vals)
    assert sum(fibers.values()) == m
    if s % 4 == 2:
        assert len(fibers) == m
        assert all(count == 1 for count in fibers.values())
    elif s % 4 == 0:
        u = (s - 2) // 2
        b = -(s - 4) // 4
        alpha = (b * pow(u, -1, m)) % m
        uinv = pow(u, -1, m)
        for t in range(m):
            assert fibers.get(t, 0) == square_roots(
                k, (uinv * t + alpha * alpha) % m)
        predicted_image = ((1 << (k - 1)) + (4 if k % 2 == 0 else 5)) // 3
        assert len(fibers) == predicted_image
    else:
        r = pow(s - 2, -1, m)
        d = min(r - 1, m + 1 - r)
        assert Counter(fibers.get(t, 0) for t in range(m)) == Counter(
            {0: d, 1: m - 2 * d, 2: d})
        c = 2 * m + 1 - 2 * r
        for n, t in enumerate(vals):
            partner = c - n
            if 0 <= partner < m:
                assert partner != n
                assert vals[partner] == t and fibers[t] == 2
            else:
                assert fibers[t] == 1
        assert (d == 0) == ((s - 3) % m == 0)
        if k >= 2:
            assert (d == m // 2) == ((s - 3 - m // 2) % m == 0)
    return len(fibers)


if __name__ == '__main__':
    cases = 0
    residues = 0
    for s in range(3, 141):
        for k in range(1, 10):
            check(s, k)
            cases += 1
            residues += 1 << k
    for s in (3, 4, 5, 6, 7, 8, 9, 11, 13, 35, 70):
        check(s, 12)
        cases += 1
        residues += 1 << 12
    print('VERIFY_OK', 'parameter_pairs=', cases,
          'input_residues=', residues,
          'odd_pairing=exact', 'even_square_fibers=exact',
          'permutation_and_double_cover=checked')
