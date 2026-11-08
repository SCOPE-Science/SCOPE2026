"""Reproduce exact fixed-weight subword covariance identities.

Requires only Python 3's standard library. Every composition and every
contiguous positive-integer word up to the stated finite size is checked;
the all-size theorem is proved symbolically in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction


def compositions(total):
    if total < 1:
        return
    for mask in range(1 << (total - 1)):
        parts = [1]
        for position in range(total - 1):
            if mask & (1 << position):
                parts.append(1)
            else:
                parts[-1] += 1
        yield tuple(parts)


def predicted_cov(total, word):
    length, weight = len(word), sum(word)
    residual = total - weight
    assert residual >= 0
    if residual == 0:
        return Fraction(2 * length - weight - 1, 1 << weight)
    numerator = ((2 * length - weight + 1) * residual
                 + 6 * length - 3 * weight - 1)
    return Fraction(numerator, 1 << (weight + 2))


def marked_count(residual):
    if residual == 0:
        return 1
    if residual == 1:
        return 2
    return (residual + 3) * (1 << (residual - 2))


def exhaustive(max_total=12):
    assertions = 0
    for total in range(1, max_total + 1):
        count = 1 << (total - 1)
        count_weighted = 0
        first = defaultdict(int)
        joint = defaultdict(int)
        for parts in compositions(total):
            length = len(parts)
            count_weighted += length
            for start in range(length):
                for stop in range(start + 1, length + 1):
                    word = parts[start:stop]
                    first[word] += 1
                    joint[word] += length
        assert Fraction(count_weighted, count) == Fraction(total + 1, 2)
        assertions += 1
        assert len(first) == (1 << total) - 1
        assertions += 1
        for word, word_count in first.items():
            weight = sum(word)
            t = total - weight
            assert word_count == marked_count(t)
            assertions += 1
            covariance = (Fraction(joint[word], count)
                          - Fraction(count_weighted * word_count, count * count))
            assert covariance == predicted_cov(total, word), (total, word, covariance)
            assertions += 1
            d = 2 * len(word) - weight
            if t == 0:
                sign = 0 if d == 1 else (1 if d > 1 else -1)
            else:
                sign = (-1 if d <= -1 else
                        1 if d >= 1 else
                        (0 if t == 1 else 1))
            actual = (covariance > 0) - (covariance < 0)
            assert actual == sign, (total, word, actual, sign)
            assertions += 1
        print('size %2d: %5d compositions, %5d patterns, all exact checks passed'
              % (total, count, len(first)))
    print('PASS:', assertions, 'exact identities/assertions')
    return assertions


if __name__ == '__main__':
    exhaustive()
