"""Exact Walsh-spectrum check for the 13-dimensional third-order Fibonacci cube.

Only Python standard library is needed. Finite checks are exhaustive at their stated lengths.
"""
from collections import Counter


def allowed(mask, length, run_limit=3):
    # A forbidden run exists iff r successive bitwise right shifts intersect.
    common = mask
    for offset in range(1, run_limit):
        common &= mask >> offset
    return common == 0


def fwht(values):
    values = list(values)
    span = 1
    while span < len(values):
        for start in range(0, len(values), 2 * span):
            for j in range(start, start + span):
                a, b = values[j], values[j + span]
                values[j], values[j + span] = a + b, a - b
        span *= 2
    return values


def direct_dp(length, frequency, run_limit=3):
    # Sum over every allowed word without constructing a Walsh matrix.
    state = [1] + [0] * (run_limit - 1)
    for position in range(length):
        updated = [0] * run_limit
        phase = -1 if (frequency >> position) & 1 else 1
        for trailing, value in enumerate(state):
            updated[0] += value
            if trailing + 1 < run_limit:
                updated[trailing + 1] += phase * value
        state = updated
    return sum(state)


def inspect(length, run_limit=3):
    support = [int(allowed(s, length, run_limit)) for s in range(1 << length)]
    spectrum = fwht(support)
    # Independent exact state recurrence for every character.
    for frequency, value in enumerate(spectrum):
        assert value == direct_dp(length, frequency, run_limit), (length, frequency)
    zeros = [i for i, val in enumerate(spectrum) if val == 0]
    counts = Counter(i.bit_count() for i in zeros)
    return sum(support), zeros, counts, spectrum


def main():
    expected_low = {1: 1, 2: 1, 5: 2, 6: 2, 9: 2, 10: 2, 13: 3}
    for n in range(1, 14):
        number, zeros, hist, spectrum = inspect(n)
        expected_singular = (n % 4 in (1, 2))
        assert bool(zeros) == expected_singular, n
        if zeros:
            assert min(hist) == expected_low[n], (n, hist)
        else:
            assert number % 2 == 1, n
        if n == 13:
            assert number == 3136
            assert len(zeros) == 1296
            assert len(spectrum) - len(zeros) == 6896
            assert hist == {3:4,4:33,5:93,6:198,7:280,8:295,9:223,10:118,11:42,12:9,13:1}
            assert {tuple(j + 1 for j in range(n) if i & (1 << j)) for i in zeros if i.bit_count() == 3} == {
                (1,7,9), (1,9,11), (3,5,13), (5,7,13)
            }
            assert min(abs(x) for i,x in enumerate(spectrum) if i.bit_count() == 1) == 274
            assert min(abs(x) for i,x in enumerate(spectrum) if i.bit_count() == 2) == 2
            print('n=13 support=3136 rank=6896 nullity=1296')
            print('n=13 zero-degree histogram:', sorted(hist.items()))
            print('n=13 four cubic zero masks:', (1,7,9), (1,9,11), (3,5,13), (5,7,13))
    # Separate variable-run-length check of the recurrence-backed period law.
    for r in range(2, 7):
        for n in range(1, 11):
            total, zeros, _, sp = inspect(n, r)
            expected = n % (r + 1) in (0, r)
            assert (len(zeros) == 0) == expected
            assert (total % 2 == 1) == expected
    print('PASS: two independent exact algorithms agree at every tested mask')

if __name__ == '__main__':
    main()
