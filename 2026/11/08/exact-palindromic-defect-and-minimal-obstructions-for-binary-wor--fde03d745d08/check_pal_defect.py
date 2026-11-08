#!/usr/bin/env python3
"""Independent direct-factor checks for a bounded-run palindromic-defect identity.
All finite tests are corroboration, not a proof of the quantified theorem.
"""
from itertools import product
from random import Random


def make_word(lengths, first="0"):
    assert lengths and all(isinstance(n, int) and n >= 1 for n in lengths)
    first_index = int(first)
    return "".join(str((first_index + j) % 2) * n for j, n in enumerate(lengths))


def brute_defect(word):
    palindromes = set()
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            s = word[i:j]
            if s == s[::-1]:
                palindromes.add(s)
    return len(word) - len(palindromes)


def predicted_defect(lengths):
    r = len(lengths)
    assert 1 <= r <= 6
    if r <= 4:
        return 0
    a, b, c, d, e = lengths[:5]
    first = max(0, min(a, e) - c) if b != d else 0
    if r == 5:
        return first
    f = lengths[5]
    second = max(0, min(b, f) - d) if c != e else 0
    return first + second


def run():
    counts = []
    for r, upper in [(1, 8), (2, 8), (3, 8), (4, 7), (5, 7), (6, 5)]:
        checked = 0
        for ls in product(range(1, upper + 1), repeat=r):
            w = make_word(ls)
            assert predicted_defect(ls) == brute_defect(w), (ls, predicted_defect(ls), brute_defect(w))
            if r == 6:
                assert predicted_defect(ls) == predicted_defect(ls[:5]) + predicted_defect(ls[1:]), ls
            checked += 1
        counts.append((r, checked))
    rng = Random(20261105)
    larger = 0
    for r in (5, 6):
        for _ in range(600):
            ls = tuple(rng.randint(1, 16) for _ in range(r))
            assert predicted_defect(ls) == brute_defect(make_word(ls)), ls
            larger += 1
    smallest_bad = (2, 1, 1, 2, 2)
    assert predicted_defect(smallest_bad) == 1
    minimal_family = 0
    for c in range(1, 7):
        for b in range(1, 7):
            for d in range(1, 7):
                if b == d:
                    continue
                ls = (c + 1, b, c, d, c + 1)
                w = make_word(ls)
                assert brute_defect(w) == 1
                assert brute_defect(w[1:]) == 0 and brute_defect(w[:-1]) == 0
                minimal_family += 1
    # Count all minimal non-rich binary words with at most six runs,
    # and compare to the coefficient of 4*z**8/((1-z)**2*(1+z)*(1-z**3)).
    counts_by_length = []
    for n in range(1, 13):
        actual = 0
        for bits in product("01", repeat=n):
            w = "".join(bits)
            num_runs = 1 + sum(w[j] != w[j - 1] for j in range(1, n))
            if num_runs > 6:
                continue
            if brute_defect(w) > 0 and brute_defect(w[1:]) == 0 and brute_defect(w[:-1]) == 0:
                actual += 1
        formula = 0
        for c in range(1, (n - 5) // 3 + 1):
            m = n - 3*c - 2
            formula += 2 * (m - 1 - (m % 2 == 0))
        assert actual == formula, (n, actual, formula)
        counts_by_length.append(actual)
    seven = "010110010"
    assert brute_defect(seven) == 1
    assert brute_defect(seven[1:]) == 0
    assert brute_defect(seven[:-1]) == 0
    print("PASS: exhaustive per run count:", counts)
    print("PASS: seeded random length profiles:", larger)
    print("PASS: five-run minimal family tested:", minimal_family)
    print("PASS: minimal forbidden counts n=1..12:", counts_by_length)
    print("PASS: sharp seven-run boundary:", seven)


if __name__ == '__main__':
    run()
