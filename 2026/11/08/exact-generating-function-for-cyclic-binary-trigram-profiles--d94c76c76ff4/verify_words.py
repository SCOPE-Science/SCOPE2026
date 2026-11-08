"""Independent word-by-word verification of cyclic binary trigram profiles.

No external dependencies. Run: python verify_words.py
"""
from itertools import product


def coefficient(n):
    # Coefficient of the four disjoint realizable-support contributions.
    result = 2 + int(n % 2 == 0 and n >= 2)
    for t in range(1, n // 2 + 1):
        for b in range(1, t + 1):
            if 2 * t + b <= n:
                result += 2
            for d in range(1, t + 1):
                remaining = n - 2 * t - b - d
                if remaining >= 0:
                    result += remaining + 1
    return result


def profile(word):
    n = len(word)
    counts = [0] * 8
    for i in range(n):
        j = ((word[i] * 2 + word[(i + 1) % n]) * 2
             + word[(i + 2) % n])
        counts[j] += 1
    return tuple(counts)


def main():
    expected = [2, 3, 4, 6, 8, 13, 18, 27, 38, 53, 72, 98,
                128, 167, 214, 271]
    for n, wanted in enumerate(expected, 1):
        seen = {profile(bits) for bits in product((0, 1), repeat=n)}
        actual = len(seen)
        assert actual == wanted, (n, actual, wanted)
        assert actual == coefficient(n), (n, actual, coefficient(n))
    print('WORDS_VERIFY_OK lengths=1..16')


if __name__ == '__main__':
    main()
