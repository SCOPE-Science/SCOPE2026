"""Independent literal insertion-channel and two-gram-profile enumeration.

Run: python3 verify_direct.py
No packages beyond Python's standard library are required.
"""
from itertools import product
from collections import Counter

PAIRS = ('00', '01', '10', '11')


def profile(word):
    return tuple(sum(word[i:i+2] == pair for i in range(len(word) - 1))
                 for pair in PAIRS)


def inserted_profiles(word):
    return {profile(word[:i] + a + word[i:])
            for i in range(len(word) + 1) for a in '01'}


def local_formula(word):
    return (1 + (word[0] == word[-1]) + ('0' in word) + ('1' in word)
            + ('00' in word) + ('11' in word))


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a+b
    return a


def lucas(k):
    a, b = 2, 1
    for _ in range(k):
        a, b = b, a+b
    return a


def closed_distribution(n):
    if n == 1:
        return (2, 0, 0, 0)
    f = fibonacci(n + 2)
    l = lucas(n - 1)
    p = (-1) ** n
    return (1+p,
            2*f - 2*l + 1 - 3*p,
            2**(n-1) + 4*l - 2*f - 3 + 3*p,
            2**(n-1) - 2*l + 1 - p)


def test():
    for n in range(1, 17):
        observed = Counter()
        saturated = []
        for bits in product('01', repeat=n):
            word = ''.join(bits)
            actual = len(inserted_profiles(word))
            predicted = local_formula(word)
            assert actual == predicted, (n, word, actual, predicted)
            assert 3 <= actual <= 6, (n, word)
            observed[actual] += 1
            if actual == 6:
                saturated.append(word)
        expected = closed_distribution(n)
        assert tuple(observed[k] for k in (3, 4, 5, 6)) == expected, (n, observed, expected)
        assert sum(expected) == 2**n, (n, expected)
        if n < 5:
            assert not saturated
        if n == 5:
            assert set(saturated) == {'00110', '01100', '10011', '11001'}
        print(f'n={n:2d} C3,C4,C5,C6={expected}')
    print('PASS: literal insertion and frequency-vector tests through n=16')


if __name__ == '__main__':
    test()
