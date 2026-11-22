"""Independent finite modular check for the fifth-power partial-sum image theorem.

Run: python3 check.py
The infinite classification rests on the accompanying mathematical proof.
"""
from collections import Counter


def expected_fiber(k, y):
    if k == 1:
        return 2
    if y == 0:
        return 1 << (k // 2)
    if y & 1:
        return (1 << min(2, k - 1)) if y % (1 << min(3, k)) == 1 else 0
    r = 0
    z = y
    while z % 2 == 0:
        z //= 2
        r += 1
    if r % 2:
        return 0
    a = r // 2
    j = k - 2*a
    return (1 << (a + min(2, j - 1))) if z % (1 << min(3, j)) == 5 % (1 << min(3, j)) else 0


def value_count(k):
    if k == 1:
        return 2
    return 1 + (1 << max(0, k-3)) + sum(
        1 << max(0, k-2*r-3) for r in range(1, (k-1)//2+1)
    )


def main():
    assertions = 0
    for k in range(1, 14):
        modulus = 1 << k
        period = 4 if k == 1 else modulus
        counts = [0] * modulus
        s = 0
        for n in range(period):
            s = (s + pow(n, 5, modulus)) % modulus
            counts[s] += 1
        for y in range(modulus):
            assert counts[y] == expected_fiber(k, y), (k, y, counts[y], expected_fiber(k,y))
            assertions += 1
        assert sum(c > 0 for c in counts) == value_count(k), k
        assertions += 1
        assert sum(counts) == period
        assertions += 1
        # The proposed period and its half-period are checked on all base indices.
        for n in range(period):
            half = period // 2
            # A block sum is the difference at a shifted index; compute directly.
            dh = sum(pow(n + j, 5, modulus) for j in range(1, half + 1)) % modulus
            df = (dh + sum(pow(n + half + j, 5, modulus) for j in range(1, half + 1))) % modulus
            assert df == 0, (k, n, df)
            assertions += 1
            if n == 0:
                some_half_failure = False
            if dh != 0:
                some_half_failure = True
        assert some_half_failure, k
        assertions += 1
    print('PASS:', assertions, 'exact modular and period assertions, levels 1..13')


if __name__ == '__main__':
    main()
