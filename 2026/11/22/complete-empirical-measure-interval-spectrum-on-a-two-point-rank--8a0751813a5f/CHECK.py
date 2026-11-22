"""Exact finite-prefix checks for the two-run interval realization.

These checks test arithmetic identities only; the theorem is proved analytically.
"""
from fractions import Fraction


def ceil_fraction(x):
    return -(-x.numerator // x.denominator)


def run_interval(a, b, stages):
    a, b = Fraction(a), Fraction(b)
    assert Fraction(0) <= a < b <= Fraction(1)
    n_total, zeros = 1, 0  # initial symbol 1
    out = []
    for n in range(1, stages + 1):
        lo = a + (b - a) / (4 * (n + 1))
        hi = b - (b - a) / (4 * (n + 1))
        before = Fraction(zeros, n_total)
        assert before < hi
        na = ceil_fraction((hi * n_total - zeros) / (1 - hi))
        assert na >= 1
        n_total += na
        zeros += na
        top = Fraction(zeros, n_total)
        assert top >= hi and top - hi <= Fraction(1, n_total)
        nb = ceil_fraction((zeros - lo * n_total) / lo)
        assert nb >= 1
        n_total += nb
        bottom = Fraction(zeros, n_total)
        assert bottom <= lo and lo - bottom <= Fraction(1, n_total)
        assert before < top and bottom < top
        out.append((na, nb, top, bottom))
    return out


def convergent_lengths(c, stages):
    c = Fraction(c)
    if c == 0:
        return [(n, n * n) for n in range(1, stages + 1)]
    if c == 1:
        return [(n * n, n) for n in range(1, stages + 1)]
    return [(max(1, ceil_fraction(c * n * n)),
             max(1, ceil_fraction((1 - c) * n * n)))
            for n in range(1, stages + 1)]


if __name__ == '__main__':
    for a, b in [(Fraction(1, 4), Fraction(3, 4)),
                 (Fraction(0), Fraction(1)),
                 (Fraction(0), Fraction(1, 2)),
                 (Fraction(1, 2), Fraction(1))]:
        seq = run_interval(a, b, 5)
        assert all(x[0] > 0 and x[1] > 0 for x in seq)
        print('interval', a, b, 'stages=', len(seq),
              'last-top=', seq[-1][2], 'last-bottom=', seq[-1][3])
    assert [p[:2] for p in run_interval(Fraction(1,4), Fraction(3,4), 2)] == [(3, 6), (14, 35)]
    for c in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1)]:
        pairs = convergent_lengths(c, 200)
        zero_count = sum(x for x, _ in pairs)
        total = sum(x+y for x,y in pairs)
        err = abs(Fraction(zero_count, total) - c)
        assert err < Fraction(1, 10)
        print('convergent', c, 'frequency=', Fraction(zero_count,total))
    print('PASS: exact rational finite-prefix checks')
