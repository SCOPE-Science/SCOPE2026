#!/usr/bin/env python3
"""Exact finite checks of gap sets in the full second Frobenius phase."""


def counting_formula(a, q, r):
    total = 0
    for j in range(q + 1):
        rem = r + j * a
        c = q - j
        low = max(0, rem - c)
        high = rem // 2
        total += max(0, high - low + 1)
    return total


def band_formula(a, s, r):
    m = (a - 1) // 2
    e = max(0, s - 1 - (r + 1) // 2) - max(0, s - 1 - r)
    return m + s + 1 + e


def exceptional_intervals(a, t):
    for h in range(1, (t - 1) // 3 + 1):
        q = a + t - h
        yield q * a + 2 * h, q * a + 2 * (t - 2 * h - 1)


def check():
    band_tests = 0
    gap_tests = 0
    brute_tests = 0
    a_cases = 0
    for a in range(5, 122, 2):
        a_cases += 1
        m = (a - 1) // 2
        cap = a * (a + m + 4) + a
        # Dynamic programming of 1/((1-z^a)(1-z^(a+1))(1-z^(a+2)))
        dp = [0] * (cap + 1)
        dp[0] = 1
        for coin in (a, a + 1, a + 2):
            for n in range(coin, cap + 1):
                dp[n] += dp[n - coin]
        for s in range(m + 3):
            for r in range(a):
                n = a * (a + s) + r
                expected = band_formula(a, s, r)
                assert counting_formula(a, a + s, r) == expected, (a, s, r, 'sum')
                assert dp[n] == expected, (a, s, r, 'DP')
                band_tests += 1
        for t in range(1, m + 3):
            p = m + t
            end = a * (a + t)
            holes = [False] * end
            expected_holes = ((t - 1) // 3) * (2*t - 3*((t - 1)//3) - 4)
            num = 0
            for lo,hi in exceptional_intervals(a,t):
                assert 0 <= lo <= hi < end
                for n in range(lo, hi + 1):
                    assert not holes[n]
                    holes[n] = True
                    num += 1
            assert num == expected_holes, (a, t, num, expected_holes)
            assert num == ((t-2)**2)//3
            for n in range(end):
                assert (dp[n] > p) == holes[n], (a, t, n, dp[n], p)
                gap_tests += 1
            for n in range(end, cap + 1):
                assert dp[n] > p, (a, t, n, 'tail')
                gap_tests += 1
        if a <= 17:
            for n in range(a * (a + 5) + 1):
                count = 0
                for x in range(n // a + 1):
                    for y in range((n - a*x) // (a+1) + 1):
                        count += (n - a*x - (a+1)*y) % (a+2) == 0
                assert dp[n] == count
                brute_tests += 1
    print('PASS odd_a=', a_cases,'band_cases=',band_tests,'gap_predicates=',gap_tests,'direct_triple_coefficients=',brute_tests)


if __name__ == '__main__':
    check()
