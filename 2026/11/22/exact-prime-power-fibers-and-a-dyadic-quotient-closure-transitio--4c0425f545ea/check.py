"""Independent finite checks for local-image and quotient-closure formulas.

All statements about unbounded levels require the accompanying mathematical proof;
this program checks finite prime-power instances directly from the recurrence.
"""
from collections import Counter


def sequence_period(a, mod):
    x, y = 1, 1
    values = []
    seen = set()
    for i in range(10 * mod + 10):
        if i and (x, y) == (1, 1):
            return values
        if (x, y) in seen:
            raise AssertionError('state repeat before returning to initial state')
        seen.add((x, y))
        values.append(x)
        x, y = y, (a * y + x) % mod
    raise AssertionError('finite orbit bound exceeded')


def valuation(a, p):
    h = 0
    while a % p == 0:
        a //= p
        h += 1
    return h


def verify_regular(a, p, k):
    h = valuation(a, p)
    assert h >= 1 and (p != 2 or h >= 2)
    mod = p ** k
    vals = sequence_period(a, mod)
    expected_period = 1 if k <= h else 2 * p ** (k - h)
    assert len(vals) == expected_period, (a, p, k, len(vals), expected_period)
    freq = Counter(vals)
    expected = {r: (1 if k <= h else 2)
                for r in range(mod) if r % (p ** min(h, k)) == 1 % (p ** min(h, k))}
    assert freq == expected, (a, p, k, freq, expected)
    if k > h:
        half = expected_period // 2
        for parity in (0, 1):
            assert set(vals[parity::2]) == set(expected), (a, p, k, parity)
    return len(vals)


def verify_dyadic_exception(a, k):
    assert a % 4 == 2
    mod = 2 ** k
    vals = sequence_period(a, mod)
    residues = set(vals)
    quotients = {u * pow(v, -1, mod) % mod for u in residues for v in residues}
    assert quotients == set(range(1, mod, 2)), (a, k, quotients)
    if k >= 3:
        for r in (1, 7):
            target = {v for v in range(mod) if v % 8 == r}
            assert target.issubset(residues), (a, k, r, target - residues)
    return len(vals)


def main():
    tests = 0
    covered = 0
    for p in [2, 3, 5, 7, 11]:
        for h in [1, 2, 3]:
            if p == 2 and h == 1:
                continue
            for u in [-5, -2, -1, 1, 2, 5]:
                if u % p == 0:
                    continue
                a = (p ** h) * u
                for k in range(1, 7):
                    if p ** k > 10000:
                        break
                    covered += verify_regular(a, p, k)
                    tests += 1
    dyadic = 0
    for a in [-30, -26, -22, -18, -14, -10, -6, -2, 2, 6, 10, 14, 18, 22, 26, 30]:
        for k in range(3, 11):
            dyadic += verify_dyadic_exception(a, k)
            tests += 1
    print(f'PASS {tests} complete-period finite tests; {covered + dyadic} recurrence terms; every regular prime-power fiber and dyadic unit quotient checked')

if __name__ == '__main__':
    main()
