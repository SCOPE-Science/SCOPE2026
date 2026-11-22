"""Reproduce exact seven-adic fourth-power-sum congruence image and fibers.
No dependencies beyond Python standard library.
"""
from collections import Counter

P = 7


def F(n):
    numerator = n * (n + 1) * (2 * n + 1) * (3 * n * n + 3 * n - 1)
    assert numerator % 30 == 0
    return numerator // 30


def derivative_numerator(n):
    return 30 * n * n * (n + 1) * (n + 1) - 1


def critical_root(k):
    """Unique solution in 1+7Z_7 to F'(c)=0, modulo 7**k."""
    c = 1
    q = 7
    assert derivative_numerator(c) % q == 0
    for level in range(2, k + 1):
        z = [c + q * t for t in range(7)
             if derivative_numerator(c + q * t) % (7*q) == 0]
        assert len(z) == 1
        c = z[0]
        q *= 7
    return c


def square_root_fibers(m):
    q = 7**m
    return Counter((t*t) % q for t in range(q))


def predicted_fiber(y, k, c, squares):
    q = 7**k
    residue = y % 7
    if k == 1:
        return {0: 3, 1: 1, 3: 1, 4: 1, 6: 1}.get(residue, 0)
    if residue == 0:
        return 2 + 7 * (y % 49 == 0)
    if residue in (3, 4):
        return 1
    if residue not in (1, 6):
        return 0
    A = F(c) % q
    unit = (c * (c + 1) * (2*c + 1)) % q
    if residue == 6:
        A, unit = (-A) % q, (-unit) % q
    delta = (y - A) % q
    if delta % 49:
        return 0
    m = 7**(k-2)
    if m == 1:
        return 7
    z = (delta // 49 * pow(unit, -1, m)) % m
    return 7 * squares.get(z, 0)


def predicted_image_count(k):
    if k == 1:
        return 5
    m = k - 2
    square_count = 1 + sum(3 * 7**(m - 2*j - 1) for j in range((m+1)//2))
    return 3 * 7**(k-1) + 2 * square_count


def main():
    checked = 0
    results = []
    for k in range(1, 7):
        q = 7**k
        c = critical_root(k)
        squares = square_root_fibers(max(0, k-2))
        H = Counter()
        s = 0
        for n in range(q):
            assert F(n) % q == s
            H[s] += 1
            s = (s + pow(n+1, 4, q)) % q
            checked += 1
        assert s == 0, ('least candidate period', k)
        assert len(H) == predicted_image_count(k)
        assert sum(H.values()) == q
        for y in range(q):
            assert H.get(y, 0) == predicted_fiber(y, k, c, squares), (k, y, H.get(y, 0))
            checked += 1
        results.append((k, q, len(H), sorted(Counter(H.values()).items())))
    print('PASS', checked, 'exact checks')
    for k, q, image, spectrum in results:
        print('k=', k, 'modulus=', q, 'image=', image, 'positive_fibers=', spectrum)
    # A 7-adic normalized Morse coordinate has a unit Jacobian, and the
    # exceptional middle branch has linear unit term modulo seven.
    assert critical_root(2) == 43
    assert F(critical_root(2)) % 343 == 50
    assert 240 % 7 == 2
    assert (1 * 2 * 3) % 7 == 6
    print('Critical point and quadratic-sheet normalization checks PASS')

if __name__ == '__main__':
    main()
