"""Exact finite exhaustive checks for binary four-window permutation-burst spheres.
Run with Python 3: python checker.py
The unbounded theorem is proved in RESULT.md; this checker is a finite cross-check.
"""
from itertools import permutations, product
from collections import Counter


def direct_ball(word):
    n = len(word)
    outputs = set()
    for start in range(n - 3):
        for block in set(permutations(word[start:start + 4])):
            outputs.add(word[:start] + block + word[start + 4:])
    return outputs


def expression(word):
    n = len(word)
    return (1 + sum(word[i] != word[i + d]
                    for d in (1, 2, 3) for i in range(n - d))
            + sum(sum(word[i:i + 4]) == 2 for i in range(n - 3)))


def predicted_maximizers(n):
    seeds = ((0, 0, 1, 1), (0, 1, 1, 0), (1, 1, 0, 0),
             (1, 0, 0, 1), (0, 1, 0, 1), (1, 0, 1, 0))
    return {tuple(seed[i % 4] for i in range(n)) for seed in seeds}


def test():
    tested = 0
    histogram = {}
    for n in range(4, 13):
        maxima = set()
        maxval = -1
        for word in product((0, 1), repeat=n):
            actual = len(direct_ball(word))
            derived = expression(word)
            assert actual == derived, (n, word, actual, derived)
            if actual > maxval:
                maxval, maxima = actual, {word}
            elif actual == maxval:
                maxima.add(word)
            tested += 1
        assert maxval == 3 * n - 6, (n, maxval)
        assert maxima == predicted_maximizers(n), (n, maxima)
        assert len(maxima) == 6
        histogram[n] = (maxval, len(maxima))
    print("PASS direct-channel-vs-formula; total words", tested)
    print("PASS sharp maxima and six equality words", histogram)

if __name__ == '__main__':
    test()
