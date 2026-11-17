"""Finite transition-rule consistency checks for explicit nonreturning frequency-shift words.

Only Python's standard library is required. Finite-state enumeration is not an
infinite proof; see RESULT.md for the analytic argument.
"""
from math import gcd


def witness(a, b):
    assert isinstance(a, int) and isinstance(b, int)
    assert a > b >= 1 and gcd(a, b) == 1
    m = next(m for m in range(1, b + 1) if a * m % b == (b - 1) % b)
    q = (a * m - b + 1) // b
    assert q >= 1 and a * m == b * q + b - 1
    word = "0" * b + "1" * (a + 1) + "0" * m + "1" * q + "0"
    return word, m, q


def admissible_prefix(word, a, b):
    h = 0
    last = None
    for digit in word:
        if last == "1":
            assert digit == ("1" if h >= 0 else "0")
        h += a if digit == "0" else -b
        last = digit
    return True


def no_later_occurrence(a, b, steps=150):
    word, m, q = witness(a, b)
    admissible_prefix(word, a, b)
    prefix = [0] * len(word)
    for i in range(1, len(word)):
        k = prefix[i - 1]
        while k and word[k] != word[i]:
            k = prefix[k - 1]
        if word[k] == word[i]:
            k += 1
        prefix[i] = k
    # State: integer discrepancy, preceding digit (0/1), longest matched prefix.
    # Initial previous digit 0 merely permits either first digit.
    states = {(0, 0, 0)}
    for t in range(steps):
        nxt = set()
        for h, previous, matched in states:
            choices = ("0", "1") if previous == 0 else (("1",) if h >= 0 else ("0",))
            for digit in choices:
                hh = h + (a if digit == "0" else -b)
                k = matched
                while k and word[k] != digit:
                    k = prefix[k - 1]
                if word[k] == digit:
                    k += 1
                if k == len(word):
                    assert t - len(word) + 1 == 0, (a, b, t, word)
                    k = prefix[k - 1]
                nxt.add((hh, int(digit), k))
        states = nxt
    return len(states), len(word)


def main():
    cases = 0
    for b in range(1, 11):
        for a in range(b + 1, 2 * b + 3):
            if gcd(a, b) != 1:
                continue
            n, length = no_later_occurrence(a, b, steps=150)
            cases += 1
            print(f"a={a}, b={b}, marker_length={length}, final_reachable_states={n}")
    print(f"All passed: {cases} coprime parameter pairs, 150 positions each")


if __name__ == "__main__":
    main()
