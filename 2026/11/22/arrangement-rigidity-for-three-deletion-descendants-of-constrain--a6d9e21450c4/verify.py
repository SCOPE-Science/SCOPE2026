"""Independent finite checks of the exact three-deletion theorem.

Run with Python 3: python verify.py
No third-party packages are required.
"""
from itertools import combinations, groupby, product
from math import comb


def run_formula(word):
    assert len(word) >= 3 and word.startswith('10')
    assert '00' not in word and '111' not in word
    lengths = [len(tuple(group)) for _, group in groupby(word)]
    r = len(lengths)
    d = sum(length == 2 for length in lengths)
    tail_penultimate = int(lengths[-2] == 2)
    tail_last = int(lengths[-1] == 2)
    return (comb(r, 3) - (r - 2) * (r - 3)
            + (2 * r - 7) * d + tail_penultimate
            - (r - 5) * tail_last)


def brute_three(word):
    n = len(word)
    return len({''.join(word[i] for i in range(n) if i not in removed)
                for removed in map(set, combinations(range(n), 3))})


def greedy_three(word):
    """Independent automaton count, one state per earliest ending index."""
    n = len(word)
    ahead = [(n + 1, n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        a = list(ahead[i + 1])
        a[int(word[i])] = i + 1
        ahead[i] = tuple(a)
    levels = [0] * (n + 1)
    levels[0] = 1
    for _ in range(n - 3):
        nxt = [0] * (n + 1)
        for pos, ways in enumerate(levels):
            if ways:
                for target in ahead[pos]:
                    if target <= n:
                        nxt[target] += ways
        levels = nxt
    return sum(levels)


def fibonacci_word(m):
    assert m >= 0
    a, b = '0', '1'
    if m == 0:
        return a
    if m == 1:
        return b
    for _ in range(2, m + 1):
        a, b = b, b + a
    return b


def fib_number(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def fibonacci_formula(m):
    assert m >= 2
    odd = m % 2
    r = 2 * fib_number(m - 1) + odd
    d = fib_number(m - 2) - odd
    tail = int(m % 2 == 0 and m >= 4)
    return (comb(r, 3) - (r - 2) * (r - 3)
            + (2 * r - 7) * d + tail)


def main():
    tested = 0
    for n in range(3, 21):
        for suffix in product('01', repeat=n - 2):
            w = '10' + ''.join(suffix)
            if '00' in w or '111' in w:
                continue
            assert run_formula(w) == brute_three(w), (w, run_formula(w))
            tested += 1
    for m in range(3, 18):
        w = fibonacci_word(m)
        assert len(w) == fib_number(m + 1)
        assert fibonacci_formula(m) == run_formula(w)
        assert greedy_three(w) == run_formula(w)
    assert fibonacci_formula(2) == 0
    print(f'VERIFY_OK: {tested} exhaustive restricted words; '
          '15 Fibonacci depths, two independent counting methods')


if __name__ == '__main__':
    main()
