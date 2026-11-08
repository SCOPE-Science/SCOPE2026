"""Finite consistency checks for arithmetic subsequences of power-support words.

The mathematical theorem is proved separately; these are finite cross-checks.
Run: python3 verify.py
"""
from itertools import combinations
from math import gcd


def power_pattern(base, start, step, length):
    powers = set()
    p = 1
    cap = start + step * (length - 1)
    while p <= cap:
        powers.add(p)
        p *= base
    return tuple(int(start + step * t in powers) for t in range(length))


def sharp_weight(base, length):
    cutoff = (base - 1) * (length - 1) + 1
    size = 1
    while cutoff >= base:
        cutoff //= base
        size += 1
    return size


def minimizer(base, count):
    positions = tuple((base**j - 1) // (base - 1) for j in range(count))
    size = positions[-1] + 1
    return tuple(int(t in positions) for t in range(size))


def exact_exponent_spans():
    tested = 0
    unique = 0
    for base in range(2, 10):
        for count in range(3, 7):
            minimum = (base ** (count - 1) - 1) // (base - 1)
            optimizers = []
            for exps in combinations(range(12), count):
                terms = [base ** x for x in exps]
                common_step = 0
                for v in terms[1:]:
                    common_step = gcd(common_step, v - terms[0])
                span = (terms[-1] - terms[0]) // common_step
                assert span >= minimum, (base, count, exps, span, minimum)
                if span == minimum:
                    optimizers.append(exps)
                tested += 1
            expected = [tuple(range(e, e + count)) for e in range(13 - count)]
            assert optimizers == expected, (base, count, optimizers, expected)
            unique += len(optimizers)
    return tested, unique


def brute_samples():
    tests = 0
    maxima = 0
    for base in range(2, 8):
        for length in range(1, 26):
            expected = sharp_weight(base, length)
            max_seen = 0
            for start in range(0, 161):
                for step in range(1, 121):
                    word = power_pattern(base, start, step, length)
                    max_seen = max(max_seen, sum(word))
                    assert sum(word) <= expected, (base, length, start, step)
                    tests += 1
            assert max_seen == expected, (base, length, expected, max_seen)
            maxima += 1
        for count in range(3, 6):
            word = minimizer(base, count)
            assert len(word) == (base**(count-1)-1)//(base-1)+1
            observed = {power_pattern(base, s, d, len(word)) for s in range(0, 161) for d in range(1, 121) if sum(power_pattern(base,s,d,len(word))) >= count}
            if (base ** (count-1)-1)//(base-1)+1 <= 26:
                assert observed == {word}, (base,count,observed)
    return tests, maxima

if __name__ == '__main__':
    tested,unique=exact_exponent_spans()
    samples,maxima=brute_samples()
    print(f'VERIFY_OK exponent_sets={tested} exact_minimizers={unique} sample_windows={samples} maxima_cases={maxima}')
