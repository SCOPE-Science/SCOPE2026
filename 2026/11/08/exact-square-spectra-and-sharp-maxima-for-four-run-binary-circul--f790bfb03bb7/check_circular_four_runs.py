"""Independent exhaustive checks for the four-run circular-square theorem.

Usage: python verify_four_run_circular_squares.py
Pure Python 3, no dependencies. This is finite validation, not an infinite proof.
"""

from itertools import product
from collections import defaultdict
from random import Random


def predicted(a, b, c, d):
    monochromatic = max(a, c) // 2 + max(b, d) // 2
    if a == c and b == d:
        mixed = a + b
    elif a == c:
        mixed = min(b, d) + 1
    elif b == d:
        mixed = min(a, c) + 1
    else:
        mixed = 1
    return monochromatic, mixed


def direct_by_slicing(w):
    n = len(w)
    double = w + w
    found = set()
    for start in range(n):
        for half in range(1, n // 2 + 1):
            left = double[start:start + half]
            right = double[start + half:start + 2 * half]
            if left == right:
                found.add(left + right)
    return found


def direct_by_character_comparison(w):
    n = len(w)
    found = set()
    for start in range(n):
        for half in range(1, n // 2 + 1):
            if all(w[(start + j) % n] == w[(start + half + j) % n]
                   for j in range(half)):
                word = ''.join(w[(start + j) % n] for j in range(2 * half))
                found.add(word)
    return found


def predicted_literals(a, b, c, d):
    """Construct all proposed square words from the transition-case proof."""
    result = {'0' * (2 * j) for j in range(1, max(a, c) // 2 + 1)}
    result.update('1' * (2 * j) for j in range(1, max(b, d) // 2 + 1))
    if a >= c and d >= b:
        result.add(('0' * c + '1' * b) * 2)
    if c >= a and b >= d:
        result.add(('0' * a + '1' * d) * 2)
    if b >= d and a >= c:
        result.add(('1' * d + '0' * c) * 2)
    if d >= b and c >= a:
        result.add(('1' * b + '0' * a) * 2)
    if b == d:
        p, q = min(a, c), b
        for u in range(1, p):
            result.add('0' * u + '1' * q + '0' * p + '1' * q + '0' * (p - u))
    if a == c:
        p, q = a, min(b, d)
        for u in range(1, q):
            result.add('1' * u + '0' * p + '1' * q + '0' * p + '1' * (q - u))
    return result


def assess(w, a, b, c, d, squares):
    observed_mono = sum(set(s) == {t} for s in squares for t in ('0', '1'))
    observed_mixed = len(squares) - observed_mono
    expected = predicted(a, b, c, d)
    explicit = predicted_literals(a, b, c, d)
    assert squares == explicit, (a, b, c, d, sorted(squares ^ explicit))
    assert (observed_mono, observed_mixed) == expected, (
        a, b, c, d, observed_mono, observed_mixed, expected)
    return len(squares)


def target_max(n):
    if n == 4:
        return 2
    if n % 4 == 3:
        return 3 * n // 4 - 1
    return 3 * n // 4


def main():
    count = 0
    max_by_length = defaultdict(int)
    for n in range(4, 22):
        for a in range(1, n - 2):
            for b in range(1, n - a - 1):
                for c in range(1, n - a - b):
                    d = n - a - b - c
                    w = '0' * a + '1' * b + '0' * c + '1' * d
                    squares = direct_by_slicing(w)
                    max_by_length[n] = max(max_by_length[n], assess(w,a,b,c,d,squares))
                    count += 1
        assert max_by_length[n] == target_max(n), (n,max_by_length[n],target_max(n))
    random = Random(20261103)
    additional = 0
    for _ in range(300):
        a,b,c,d = [random.randrange(1, 29) for _ in range(4)]
        w = '0'*a + '1'*b + '0'*c + '1'*d
        exact = direct_by_character_comparison(w)
        expected = direct_by_slicing(w)
        assert exact == expected, (a,b,c,d)
        assess(w,a,b,c,d,exact)
        additional += 1
    print('PASS: all {} positive run quadruples of total length 4..21; full literal square sets match'.format(count))
    print('PASS: 300 independent modular-index random tests; exact square sets agree')
    print('PASS: exact fixed-length maxima n=4..21')
    print('Maxima:', [(n,max_by_length[n]) for n in range(4,22)])


if __name__ == '__main__':
    main()
