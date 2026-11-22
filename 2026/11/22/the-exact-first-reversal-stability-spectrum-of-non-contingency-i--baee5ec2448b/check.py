"""Independent finite checks of one-arc-reversal non-contingency statement.

Usage: python check.py. Pure Python 3, no dependencies.
"""

def flip_tournament(n, i, j):
    """0-based indices; every initial arc a->b has a<b."""
    out = [sum(1 << k for k in range(v + 1, n)) for v in range(n)]
    out[i] ^= 1 << j
    out[j] |= 1 << i
    return out


def noncontingent(out, val):
    ans = 0
    for v, successors in enumerate(out):
        intersection = successors & val
        if intersection == 0 or intersection == successors:
            ans |= 1 << v
    return ans


def violations(out, val):
    inner = noncontingent(out, val)
    outer = noncontingent(out, inner)
    return inner & ~outer


def predicted(n, i, j):
    gap = j - i
    if gap == 1 or (j == n - 1 and gap == 2):
        return 0
    if j < n - 1:
        return 2 * gap - 1
    return 1


def main():
    cases = singletons = full_tests = 0
    for n in range(3, 10):
        for i in range(n):
            for j in range(i + 1, n):
                out = flip_tournament(n, i, j)
                got = sum(violations(out, 1 << s).bit_count()
                          for s in range(n))
                assert got == predicted(n, i, j), (n, i, j, got)
                singletons += n
                if n <= 8:
                    valid = all(violations(out, p) == 0
                                for p in range(1 << n))
                    assert valid == (predicted(n, i, j) == 0), (n, i, j)
                    full_tests += 1 << n
                cases += 1
    print('VERIFY_OK', 'reversals=', cases,
          'singleton_assignments=', singletons,
          'all_valuation_assignments=', full_tests)


if __name__ == '__main__':
    main()
