"""Direct window verification of the four-marker circular prefix theorem.

Run: python3 verify.py
Only the Python standard library is needed. Finite checks support, but do not
replace, the unbounded proof in RESULT.md.
"""

DENOM = (1, -3, 4, -5, 6, -5, 4, -3, 1)


def word_from_gaps(gaps):
    return ''.join('1' + '0' * h for h in gaps)


def direct_roots(gaps):
    word = word_from_gaps(gaps)
    n = len(word)
    doubled = word + word
    maxima = [max(doubled[i:i + length].count('1') for i in range(n))
              for length in range(1, n + 1)]
    return {i for i in range(n)
            if all(doubled[i:i + length].count('1') == maxima[length - 1]
                   for length in range(1, n + 1))}


def gap_roots(gaps):
    smallest, largest = min(gaps), max(gaps)
    positions = []
    pos = 0
    for i, gap in enumerate(gaps):
        if gap == smallest and gaps[i - 1] == largest:
            positions.append(pos)
        pos += 1 + gap
    return set(positions)


def predicted_forbidden_counts(upper):
    # The rational generating series for gap-sum t is
    # z^3 / (1 - 3z + 4z^2 - 5z^3 + 6z^4 - 5z^5 + 4z^6 - 3z^7 + z^8).
    values = []
    for t in range(upper + 1):
        goal = 1 if t == 3 else 0
        value = goal - sum(DENOM[i] * values[t-i]
                           for i in range(1, min(t, len(DENOM)-1) + 1))
        values.append(value)
    return values


def main():
    tested = 0
    bad_necklaces = []
    for t in range(23):
        failures = 0
        for a in range(t + 1):
            for b in range(t-a + 1):
                for c in range(t-a-b + 1):
                    gaps = (a, b, c, t-a-b-c)
                    actual = direct_roots(gaps)
                    predicted = gap_roots(gaps)
                    if actual != predicted:
                        raise AssertionError(('root mismatch', gaps, actual, predicted))
                    failures += not actual
                    tested += 1
        if failures % 4:
            raise AssertionError(('nonintegral orbit count', t, failures))
        bad_necklaces.append(failures // 4)
    prediction = predicted_forbidden_counts(22)
    if bad_necklaces != prediction:
        raise AssertionError(('GF coefficient mismatch', bad_necklaces, prediction))
    assert bad_necklaces[:4] == [0, 0, 0, 1]
    example = (0, 2, 0, 0, 3)
    assert word_from_gaps(example) == '1100111000'
    assert gap_roots(example) == {0}
    assert direct_roots(example) == set()
    print('VERIFY_OK: 14950 four-gap configurations; all exact root sets;')
    print('          23 generating-function coefficients; five-marker boundary.')


if __name__ == '__main__':
    main()
