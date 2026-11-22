"""Independent direct tests for the two-parameter MCS cut construction.

Run: python3 verify_mcs_cut.py
All positions in this source are zero-based; this finite check is not the infinite proof.
"""

def is_closed(t):
    if len(t) == 1:
        return True
    for k in range(1, len(t)):
        v = t[:k]
        if t[-k:] != v:
            continue
        count = sum(t[i:i + k] == v for i in range(len(t) - k + 1))
        if count == 2:
            return True
    return False


def is_maximal(w, left, right):
    return (is_closed(w[left:right + 1])
            and (left == 0 or not is_closed(w[left - 1:right + 1]))
            and (right == len(w) - 1 or not is_closed(w[left:right + 2])))


def make(a, eps):
    if a < 3 and (a, eps) != (2, 1):
        raise ValueError('out of scope')
    if eps not in (0, 1):
        raise ValueError('out of scope')
    return '11' + '0' * a + '1011101' + '0' * (a - 1 + eps)


def witnesses(a, eps):
    n = 2 * a + 8 + eps
    return ([(0, a + 5), (0, a + 7), (1, a + 3), (1, n - 1)]
            + [(j, 2 * a + 10 - j) for j in range(3, a + 1)]
            + [(a + 1, a + 4), (a + 1, a + 9), (a + 2, a + 8)])


def main():
    tests = 0
    intervals = 0
    full = 0
    for a in range(2, 31):
        for eps in (0, 1):
            if (a, eps) == (2, 0):
                continue
            word = make(a, eps)
            n = len(word)
            assert n == 2 * a + 8 + eps
            cut = a + 2
            expected = witnesses(a, eps)
            assert len(expected) == len(set(expected)) == a + 5 == n // 2 + 1
            for i, j in expected:
                assert 0 <= i <= cut < j < n
                assert is_maximal(word, i, j), (a, eps, (i, j))
                intervals += 1
            if a <= 9:
                actual = {(i, j)
                          for i in range(cut + 1)
                          for j in range(cut + 1, n)
                          if is_maximal(word, i, j)}
                assert actual == set(expected), (a, eps, actual ^ set(expected))
                full += 1
            tests += 1
    print(f'PASS: {tests} parameter instances; {intervals} distinct candidate MCS checks; '
          f'{full} complete cut enumerations; lengths 13 through 69')


if __name__ == '__main__':
    main()
