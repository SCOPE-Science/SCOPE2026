"""Independent finite checks of a theorem about maximal periodic factors.

Only Python's standard library is needed. Run with `python verify.py`.
"""
from collections import Counter
from fractions import Fraction


def direct_runs(word):
    """Enumerate intervals and verify least period and maximality directly."""
    n = len(word)
    runs = set()
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i + 1
            for p in range(1, width // 2 + 1):
                if any(word[k] != word[k + p] for k in range(i, j + 1 - p)):
                    continue
                if any(all(word[k] == word[k + q] for k in range(i, j + 1 - q))
                       for q in range(1, p)):
                    continue
                if i > 0 and word[i - 1] == word[i - 1 + p]:
                    continue
                if j + 1 < n and word[j + 1] == word[j + 1 - p]:
                    continue
                runs.add((i, j, p))
                break
    return runs


def predicted_runs(a, b, c):
    """Expected exact set of (zero-based start, inclusive end, period)."""
    result = set()
    if a >= 2:
        result.add((0, a - 1, 1))
    if b >= 2:
        result.add((a + 1, a + b, 1))
    if c >= 2:
        result.add((a + b + 2, a + b + 1 + c, 1))
    if b == 0:
        result.add((a, a + 1, 1))
    elif a + c >= b:
        result.add((a - min(a, b), a + b + 1 + min(c, b), b + 1))
    return result


def four_run_count(n):
    if n < 8:
        return 0
    t = n - 8
    h = min(t, (t + 2) // 2)
    return (h + 1) * (2 * t + 2 - h) // 2


def four_run_from_gf(n):
    # Coefficient of z^(n-8) in (1-z)^(-3) minus
    # z^3/((1-z)(1-z^2)^2), evaluated by explicit convolution.
    if n < 8:
        return 0
    t = n - 8
    all_triples = (t + 1) * (t + 2) // 2
    bad = sum((r + 1) for r in range((t - 3) // 2 + 1)) if t >= 3 else 0
    return all_triples - bad


def convolution(x, y, stop):
    out = [0] * (stop + 1)
    for i, a in enumerate(x[:stop + 1]):
        if not a:
            continue
        for j, b in enumerate(y[:stop + 1 - i]):
            out[i + j] += a * b
    return out


def rational_gf_coefficients(u, stop):
    """Truncated coefficients of the displayed rational bivariate GF at fixed u."""
    B = [1, 1] + [u] * max(0, stop - 1)
    B = B[:stop + 1]
    Bsq = convolution(B, B, stop + 1)
    Bcube = convolution(Bsq, B, stop)
    Bz2 = [B[k // 2] if k % 2 == 0 else 0 for k in range(stop + 2)]
    Bz2sq = convolution(Bz2, Bz2, stop + 1)
    out = []
    ksums = 0
    for s in range(stop + 1):
        if s >= 2:
            m = s - 2
            ksums += Bsq[m] - int(m == 0) - Bz2sq[m + 1]
        T = Bsq[s] + (Bsq[s - 1] if s >= 1 else 0) - int(s == 1) + u * ksums
        out.append(Bcube[s] + (u - 1) * T)
    return out


def main():
    instances = 0
    distribution = {}
    for zeros in range(0, 19):
        frequencies = Counter()
        for a in range(zeros + 1):
            for b in range(zeros - a + 1):
                c = zeros - a - b
                word = '0' * a + '1' + '0' * b + '1' + '0' * c
                actual = direct_runs(word)
                expected = predicted_runs(a, b, c)
                assert actual == expected, (a, b, c, actual, expected)
                instances += 1
                frequencies[len(actual)] += 1
        n = zeros + 2
        assert sum(frequencies.values()) == n * (n - 1) // 2
        assert frequencies[4] == four_run_count(n) == four_run_from_gf(n)
        distribution[n] = dict(frequencies)
    for u in range(5):
        coefficients = rational_gf_coefficients(u, 18)
        for s in range(19):
            actual = sum(num * u ** count for count, num in distribution[s + 2].items())
            assert coefficients[s] == actual, ('gf', u, s, coefficients[s], actual)
    for n in range(2, 150):
        assert four_run_count(n) == four_run_from_gf(n)
    assert [max(distribution[n]) for n in range(2, 20)] == [
        1,1,2,2,3,3,4,4,4,4,4,4,4,4,4,4,4,4]
    assert distribution[8][4] == 1
    assert distribution[9][4] == 3
    assert distribution[10][4] == 6
    assert distribution[11][4] == 9
    assert abs(Fraction(four_run_count(10000), 10000*9999//2) - Fraction(3,4)) < Fraction(1,1000)
    print('VERIFY_OK', 'full_run_sets', instances,
          'maximum_n2_to_n19', [max(distribution[n]) for n in range(2,20)],
          'four_run_n8_to_n11', [distribution[n][4] for n in range(8,12)])


if __name__ == '__main__':
    main()
