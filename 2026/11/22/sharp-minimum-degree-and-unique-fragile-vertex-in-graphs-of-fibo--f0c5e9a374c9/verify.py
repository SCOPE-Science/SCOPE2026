"""Reproducible finite checks for the minimum-degree theorem on q-decreasing words.

Requires only Python 3.9+ standard library. Finite checks corroborate but do not
replace the all-length proof in RESULT.md.
"""
from itertools import product


def is_q_decreasing(word, q):
    # Independent direct scan of zero-runs and immediately subsequent one-runs.
    i = 0
    n = len(word)
    while i < n:
        if word[i] == '1':
            while i < n and word[i] == '1':
                i += 1
            continue
        a = 0
        while i < n and word[i] == '0':
            a += 1
            i += 1
        b = 0
        while i < n and word[i] == '1':
            b += 1
            i += 1
        if b >= q * a:
            return False
    return True


def permitted_flip_count(word, q):
    total = 0
    for j in range(len(word)):
        flipped = word[:j] + ('0' if word[j] == '1' else '1') + word[j + 1:]
        if is_q_decreasing(flipped, q):
            total += 1
    return total


def expected_minimum(q, n):
    return min(n, q)


def expected_multiplicity(q, n):
    if n <= q:
        return 2 ** n
    if n == q + 1:
        return q + 1
    if n == q + 2:
        return 2
    return 1


def main():
    # Exhaustively test a variety of parameter pairs including every boundary
    # regime; compare literal input words and all n one-bit alterations.
    tested_inputs = 0
    tested_parameters = 0
    for q in range(2, 9):
        for n in range(1, min(13, q + 5)):
            tested_parameters += 1
            minimum = n + 1
            minima = set()
            for bits in product('01', repeat=n):
                word = ''.join(bits)
                if not is_q_decreasing(word, q):
                    continue
                tested_inputs += 1
                degree = permitted_flip_count(word, q)
                if degree < minimum:
                    minimum, minima = degree, {word}
                elif degree == minimum:
                    minima.add(word)
            assert minimum == expected_minimum(q, n), (q, n, minimum)
            assert len(minima) == expected_multiplicity(q, n), (q, n, minima)
            if n == q + 2:
                assert minima == {'1' * n, '00' + '1' * q}, (q, n, minima)
            if n >= q + 3:
                assert minima == {'1' * n}, (q, n, minima)
    print(f'VERIFY_OK parameter_pairs={tested_parameters} admissible_words={tested_inputs}')


if __name__ == '__main__':
    main()
