"""Direct finite validation of closed factors for increasing-gap marker words.

Run: python3 verify.py
Uses only Python standard library. The brute-force half is deliberately independent
of the proof's first-return classification: it inspects all word factors and borders.
"""
from itertools import combinations


def marker_word(gaps):
    return '1' + ''.join('0' * g + '1' for g in gaps)


def occurs_only_at_ends(s, border):
    q = len(border)
    places = []
    for i in range(len(s) - q + 1):
        if s[i:i + q] == border:
            places.append(i)
    return places == [0, len(s) - q]


def is_closed_brute(s):
    if len(s) == 1:
        return True
    return any(s[:q] == s[-q:] and occurs_only_at_ends(s, s[:q])
               for q in range(1, len(s)))


def brute_factors(gaps):
    w = marker_word(gaps)
    distinct = {w[i:j] for i in range(len(w)) for j in range(i + 1, len(w) + 1)}
    return {f for f in distinct if is_closed_brute(f)}


def classified_factors(gaps):
    k = len(gaps)
    ans = {'0' * a for a in range(1, gaps[-1] + 1)}
    ans |= {'0' * a + '1' + '0' * a for a in range(gaps[-2] + 1)} if k >= 2 else {'1'}
    for j in range(k):
        preceding = gaps[j-1] if j > 0 else 0
        following = gaps[j] if j < k - 1 else 0
        ans |= {'0' * a + '1' + '0' * gaps[j] + '1' + '0' * b
                for a in range(preceding + 1) for b in range(following + 1)}
    return ans


def formula(gaps):
    prev = gaps[-2] if len(gaps) >= 2 else 0
    return gaps[-1] + 2 * (prev + 1) + sum(
        ((gaps[j-2] if j >= 2 else 0) + 1) * (gaps[j-1] + 1)
        for j in range(1, len(gaps)))


def main():
    cases = 0
    total = 0
    for k in range(1, 7):
        for gaps in combinations(range(1, 14), k):
            b = brute_factors(gaps)
            p = classified_factors(gaps)
            assert b == p, (gaps, 'unpredicted', sorted(b-p)[:4], 'missing', sorted(p-b)[:4])
            assert len(p) == formula(gaps), (gaps, len(p), formula(gaps))
            cases += 1
            total += len(b)
    assert cases == 4095 and total == 797251, (cases, total)
    for k in range(1, 16):
        gaps = list(range(1, k + 1))
        assert formula(gaps) == (k ** 3 + 8 * k) // 3
    print('PASS: 4095 distinct increasing-gap vectors, 797251 closed-factor instances; ramp identity k=1..15')


if __name__ == '__main__':
    main()
