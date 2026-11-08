"""Finite cross-checks for the marked-repetition spectrum of geometric-support words.

Run with Python 3; this does not replace the infinite proof in RESULT.md.
"""


def supported_word(base, length):
    marks = set()
    q = 1
    while q < length:
        marks.add(q)
        q *= base
    return bytes(int(i in marks) for i in range(length))


def predicted_starts(base, period, endpoint):
    q = 1
    a = 0
    while (base - 1) * q < period:
        q *= base
        a += 1
    if (base - 1) * q != period:
        return []
    low = max(0, 3 - base) if a == 0 else q // base + 1
    return [s for s in range(low, q + 1) if s + 2 * period <= endpoint]


def check():
    total = 0
    squares = 0
    length_tests = 0
    for base in range(2, 9):
        endpoint = 2400
        word = supported_word(base, endpoint)
        for period in range(1, 151):
            found = []
            for start in range(endpoint - 2 * period + 1):
                factor = word[start:start + 2 * period]
                if 1 not in factor:
                    continue
                total += 1
                if factor[:period] == factor[period:]:
                    found.append(start)
            expected = predicted_starts(base, period, endpoint)
            assert found == expected, (base, period, found[:20], expected[:20])
            squares += len(found)
            for start in found:
                first_mark = next(i for i in range(start, start + period) if word[i])
                offset = first_mark - start
                maximal_length = 2 * period + offset
                assert start + maximal_length < endpoint
                for size in range(2 * period, maximal_length + 1):
                    assert all(word[start + j] == word[start + j + period]
                               for j in range(size - period)), (base, period, start, size)
                    length_tests += 1
                assert word[start + maximal_length] != word[start + maximal_length - period]
                if period > 1:
                    for d in range(1, period):
                        assert any(word[start + j] != word[start + j + d]
                                   for j in range(2 * period - d)), (base, period, start, d)
    print('VERIFY_OK', 'bases=2..8', 'periods=1..150',
          'marked_square_windows=', total,
          'square_occurrences=', squares,
          'maximal_length_checks=', length_tests)


if __name__ == '__main__':
    check()
