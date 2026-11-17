"""Exact finite-cut checks for one-level block-Haar contrast reflection.
Scientific verification only; no external packages are needed.
"""
from fractions import Fraction
from random import Random


def reflect(x, length):
    n = len(x)
    assert length % 2 == 0 and n % length == 0
    half = length // 2
    out = list(x)
    for start in range(0, n, length):
        left = sum(x[start:start + half], Fraction(0)) / half
        right = sum(x[start + half:start + length], Fraction(0)) / half
        contrast = left - right
        for k in range(start, start + half):
            out[k] -= contrast
        for k in range(start + half, start + length):
            out[k] += contrast
    return out


def variation(x):
    return sum((abs(x[k + 1] - x[k]) for k in range(len(x) - 1)), Fraction(0))


def coefficient(length, blocks):
    boundary_count = 0 if blocks == 1 else (1 if blocks == 2 else 2)
    if length == 2:
        return Fraction(1 + boundary_count)
    return Fraction(1) + (2 + boundary_count) * (1 - Fraction(2, length))


def test():
    count = 0
    witness_count = 0
    for length in range(2, 26, 2):
        for blocks in range(1, 7):
            n = length * blocks
            predicted = coefficient(length, blocks)
            best = Fraction(0)
            argmax = None
            for j in range(1, n):
                x = [Fraction(int(k >= j)) for k in range(n)]
                v = variation(reflect(x, length))
                if v > best:
                    best, argmax = v, j
                assert v <= predicted, (length, blocks, j, v, predicted)
                count += 1
            assert best == predicted, (length, blocks, best, predicted)
            assert argmax is not None
            witness_count += 1
    rng = Random(837201)
    samples = 0
    for length, blocks in [(2, 1), (2, 4), (4, 3), (6, 3), (8, 1), (10, 2), (16, 4)]:
        n = length * blocks
        for _ in range(50):
            x = [Fraction(rng.randrange(-31, 32), rng.randrange(1, 13)) for _ in range(n)]
            assert variation(reflect(x, length)) <= coefficient(length, blocks) * variation(x)
            assert reflect(reflect(x, length), length) == x
            samples += 1
    print('EXACT_ALL_STEPS_AND_SHARP_WITNESSES_PASS', count, witness_count)
    print('EXACT_GENERAL_INPUT_AND_INVOLUTION_CHECKS_PASS', samples)
    print('ALL_BLOCK_HAAR_VARIATION_CHECKS_PASS')

if __name__ == '__main__':
    test()
