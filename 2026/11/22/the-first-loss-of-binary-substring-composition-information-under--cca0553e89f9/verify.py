"""Exhaustive finite certificate: two power sums of substring weights.

Run with Python 3.10 or later: python verify.py
No third-party packages, randomness, or external inputs are required.
"""
from collections import Counter, defaultdict

EXPECTED_MOMENT_CLASSES = (2, 3, 6, 10, 20, 36, 72, 135, 272, 528, 1050)
EXCEPTIONAL = {
    frozenset(('00100111001', '00110110001', '10001101100', '10011100100')),
    frozenset(('01100011011', '01110010011', '11001001110', '11011000110')),
}


def statistics_prefix(w):
    n = len(w)
    prefix = [0]
    for bit in w:
        prefix.append(prefix[-1] + int(bit))
    moments, spectra = [], []
    for length in range(1, n + 1):
        hist = [0] * (length + 1)
        for i in range(n - length + 1):
            hist[prefix[i + length] - prefix[i]] += 1
        moments.append((sum(j * c for j, c in enumerate(hist)),
                        sum(j * j * c for j, c in enumerate(hist))))
        spectra.append(tuple(hist))
    cubic3 = sum(j ** 3 * c for j, c in enumerate(spectra[2])) if n >= 3 else 0
    return tuple(moments), tuple(spectra), cubic3


def statistics_direct(w):
    n = len(w)
    moments, spectra = [], []
    for length in range(1, n + 1):
        window_weights = [sum(int(w[t]) for t in range(i, i + length))
                          for i in range(n - length + 1)]
        moments.append((sum(window_weights), sum(v * v for v in window_weights)))
        spectra.append(tuple(window_weights.count(j) for j in range(length + 1)))
    return tuple(moments), tuple(spectra), (
        sum(sum(int(w[t]) for t in range(i, i + 3)) ** 3
            for i in range(n - 2)) if n >= 3 else 0)


def validate():
    for n, expected in enumerate(EXPECTED_MOMENT_CLASSES, start=1):
        by_moment = defaultdict(list)
        for number in range(1 << n):
            w = format(number, f'0{n}b')
            a = statistics_prefix(w)
            b = statistics_direct(w)
            assert a == b, (n, w, a, b)
            by_moment[a[0]].append((w, a[1], a[2]))
        assert len(by_moment) == expected, (n, len(by_moment))
        failures = []
        by_full = set()
        for key, fiber in by_moment.items():
            distinct_full = {record[1] for record in fiber}
            by_full.update(distinct_full)
            repaired = {(record[1], record[2]) for record in fiber}
            assert len(repaired) == len(distinct_full)  # cubic3 separates all differing full spectra
            if len(distinct_full) > 1:
                failures.append(frozenset(record[0] for record in fiber))
                assert len(distinct_full) == 2 and len(fiber) == 4
                for full in distinct_full:
                    pair = [rec[0] for rec in fiber if rec[1] == full]
                    assert len(pair) == 2 and pair[0] == pair[1][::-1]
                assert {len({record[1] for record in fiber if record[2] == z})
                        for z in {record[2] for record in fiber}} == {1}
        assert (not failures) if n < 11 else set(failures) == EXCEPTIONAL
        if n == 11:
            assert len(by_full) == 1052
            assert Counter(len(v) for v in by_moment.values()) == {1: 64, 2: 980, 4: 6}
            assert len(failures) == 2
            for failure in failures:
                vals = defaultdict(list)
                for w in failure:
                    vals[statistics_prefix(w)[2]].append(w)
                assert len(vals) == 2 and sorted(map(len, vals.values())) == [2, 2]
            print('n=11 exceptional moment fibers:')
            for failure in sorted(map(sorted, failures)):
                print('  ', ', '.join(failure))
        print(f'n={n:2d} sources={1<<n:4d} moment_profiles={len(by_moment):4d} '
              f'full_profiles={len(by_full):4d} split_fibers={len(failures)}')
    print('VERIFY_OK: all 4094 binary sources of lengths 1..11 checked by two methods')

if __name__ == '__main__':
    validate()
