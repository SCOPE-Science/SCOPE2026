"""Exact finite checks for the first parity-band breakdown of three consecutive coin denumerants.
No packages beyond the Python standard library are needed.
The exhaustive checks are corroboration, not a substitute for the symbolic proof.
"""

def gap_formula(a, level):
    assert a % 2 == 0 and a >= 6 and 1 <= level <= 4
    if level <= 3:
        k = a * (a + level)
        return set(range(k)) | {k + j for j in range(1, a, 2)}
    k = a * (a + 3)
    return (set(range(k + 2))
            | set(range(k + 3, k + a))
            | {k + a + 1}
            | set(range(k + a + 5, k + 2 * a, 2)))


def count_dp(a, end):
    den = [0] * (end + 1)
    den[0] = 1
    for c in (a, a + 1, a + 2):
        for n in range(c, end + 1):
            den[n] += den[n - c]
    return den


def count_direct(a, n):
    return sum(1 for x in range(n // a + 1)
               for y in range((n - a * x) // (a + 1) + 1)
               if (n - a * x - (a + 1) * y) % (a + 2) == 0)


def symbolic_count(a, j, r):
    q = a + j
    v = 0
    for e in range(3):
        t = q - e
        s = a * e + r
        if 0 <= s <= 2 * t:
            v += min(s, 2 * t - s) // 2 + 1
    return v


def main():
    total = 0
    tables = 0
    for a in range(6, 202, 2):
        # This upper bound exceeds every claimed gap and allows all-period checks.
        end = a * (a + 10)
        den = count_dp(a, end)
        for level in range(1, 5):
            p = a // 2 + level
            expected = gap_formula(a, level)
            observed = {n for n in range(end + 1) if den[n] <= p}
            assert observed == expected, (a, level, sorted(observed ^ expected)[:10])
            total += end + 1
            if level <= 3:
                k = a * (a + level)
                assert len(expected) == k + a // 2
                assert max(expected) == k + a - 1
            else:
                k = a * (a + 3)
                assert len(expected) == a * (a + 4) + a // 2 - 2
                assert max(expected) == a * (a + 5) - 1
                isolated = [n for n in expected if n >= 1 and n-1 not in expected and n+1 not in expected]
                assert len(isolated) == a // 2 - 1
        for j in range(2, 6):
            for r in range(a):
                assert symbolic_count(a, j, r) == den[a*(a+j)+r]
                tables += 1
    direct = 0
    for a in range(6, 22, 2):
        vals = count_dp(a, 5*a*a)
        for n in range(5*a*a + 1):
            assert count_direct(a, n) == vals[n]
            direct += 1
    print('PASS: 98 even bases (6 through 200), four p-level sets,',total,'DP comparisons;',tables,'local count comparisons;',direct,'independent triples.')


if __name__ == '__main__':
    main()
