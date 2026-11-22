"""Literal and arithmetic checks for distinct circular squares with three marked positions.

Standard-library only. All finite checks supplement the unrestricted proof.
"""
from itertools import permutations
from random import Random


def literal_squares(gaps):
    word = ''.join('1' + '0' * x for x in gaps)
    n = len(word)
    doubled = word + word
    result = set()
    for start in range(n):
        for half in range(1, n // 2 + 1):
            left = doubled[start:start + half]
            if left == doubled[start + half:start + 2 * half]:
                result.add(left + left)
    return result


def structural_squares(gaps):
    largest = max(gaps)
    ans = {'0' * (2 * t) for t in range(1, largest // 2 + 1)}
    for i, middle in enumerate(gaps):
        preceding = gaps[(i - 1) % 3]
        following = gaps[(i + 1) % 3]
        for left in range(max(0, middle - following), min(middle, preceding) + 1):
            root = '0' * left + '1' + '0' * (middle - left)
            ans.add(root + root)
    return ans


def count_formula(gaps):
    a, b, c = sorted(gaps)
    if a == b == c:
        return c // 2 + a + 1
    if a == b:
        return c // 2 + a + 1 + max(0, 2 * a - c + 1)
    if b == c:
        return c // 2 + a + 1 + min(c + 1, 2 * a + 2)
    return c // 2 + 2 * a + 2 + max(0, a + b - c + 1)


def largest_count(n):
    m, residue = divmod(n, 3)
    if residue == 0:
        return n - 4 + m // 2, (m - 2, m - 1, m)
    if residue == 1:
        return n - 6 + (m + 1) // 2, (m - 2, m - 1, m + 1)
    return n - 6 + (m + 1) // 2, (m - 2, m, m + 1)


def test():
    literal_cases = 0
    for n in range(3, 37):
        total_zeroes = n - 3
        for p in range(total_zeroes + 1):
            for q in range(total_zeroes - p + 1):
                r = total_zeroes - p - q
                gaps = (p, q, r)
                direct = literal_squares(gaps)
                structural = structural_squares(gaps)
                assert direct == structural, (gaps, direct ^ structural)
                assert len(direct) == count_formula(gaps), gaps
                literal_cases += 1
    print('Literal/structural/formula equality, all three-gap words, lengths 3..36:', literal_cases, 'PASS')

    small_maxima = (1, 1, 3, 3, 4, 6, 6, 7, 8, 10, 10, 11,
                    13, 13, 14, 17, 16, 17, 20, 20, 21, 24)
    enumerated = 0
    for n in range(3, 161):
        total_zeroes = n - 3
        maximum = -1
        best = set()
        for p in range(total_zeroes + 1):
            for q in range(total_zeroes - p + 1):
                r = total_zeroes - p - q
                count = count_formula((p, q, r))
                if count > maximum:
                    maximum = count
                    best = {(p, q, r)}
                elif count == maximum:
                    best.add((p, q, r))
                enumerated += 1
        if n < 25:
            assert maximum == small_maxima[n - 3], (n, maximum)
        else:
            predicted, gaps = largest_count(n)
            assert maximum == predicted, (n, maximum, predicted)
            assert best == set(permutations(gaps)), (n, best, gaps)
    print('Finite-length extrema, lengths 3..160, all gap compositions:', enumerated, 'PASS')
    print('Small-length maxima n=3..24:', list(small_maxima))

    rng = Random(20261120)
    for _ in range(300):
        n = rng.randrange(25, 1001)
        p = rng.randrange(n - 2)
        q = rng.randrange(n - 2 - p)
        r = n - 3 - p - q
        largest, _ = largest_count(n)
        assert count_formula((p, q, r)) <= largest
    print('Deterministic random large-parameter extremal checks:', 300, 'PASS')

    first_excess = None
    for n in range(3, 161):
        if n < 25:
            maximum = small_maxima[n - 3]
        else:
            maximum = largest_count(n)[0]
        if maximum > n:
            first_excess = n
            break
    assert first_excess == 30
    assert count_formula((8, 9, 10)) == 31
    print('First length with square diversity exceeding circumference:', first_excess, 'PASS')
    print('Independent infinite proof required: finite tests do not certify all lengths.')


if __name__ == '__main__':
    test()
