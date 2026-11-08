"""Finite exact-integer checks for a positional subtractive tiling theorem.

The accompanying proof, not these finite checks, establishes the infinite claims.
"""
from fractions import Fraction
from itertools import product


def digit_pair(n, base, belongs_to_a, max_steps=1000):
    """Return the unique candidate nonnegative digit pair for b-a=n."""
    a = b = 0
    quotient, weight, i = n, 1, 0
    while quotient != 0:
        if i >= max_steps:
            raise AssertionError("digit recurrence did not terminate in test range")
        if belongs_to_a(i):
            digit = (-quotient) % base
            a += digit * weight
            quotient = (quotient + digit) // base
        else:
            digit = quotient % base
            b += digit * weight
            quotient = (quotient - digit) // base
        i += 1
        weight *= base
    assert b - a == n
    return a, b


def check_periodic():
    count = 0
    finite_pairs = 0
    for base in (2, 3, 4, 5):
        for period in (2, 3, 4, 5):
            for mask in range(1, (1 << period) - 1):
                is_a = lambda i, m=mask, p=period: bool((m >> (i % p)) & 1)
                for n in range(-350, 351):
                    a, b = digit_pair(n, base, is_a)
                    assert a >= 0 and b >= 0
                    assert max(a, b) + 1 <= 1 + base ** (period + 1) * abs(n) if n else True
                    count += 1
                # Independent direct finite digit-product enumeration.
                a_values = [sum(d * base ** i for i, d in enumerate(ds))
                            for ds in product(*[range(base) if is_a(i) else (0,) for i in range(6)])]
                b_values = [sum(d * base ** i for i, d in enumerate(ds))
                            for ds in product(*[range(base) if not is_a(i) else (0,) for i in range(6)])]
                differences = [b - a for a in a_values for b in b_values]
                assert len(differences) == len(set(differences))
                finite_pairs += len(differences)
    print('PERIODIC_DIGIT_CHECK_OK tested_signed_integers=', count,
          'direct_finite_pairs=', finite_pairs, 'bases=2..5 periods=2..5')


def check_mechanical():
    total = 0
    for alpha in (Fraction(1, 5), Fraction(2, 5), Fraction(1, 2),
                  Fraction(3, 5), Fraction(4, 5)):
        is_a = lambda i, x=alpha: ((i + 1) * x.numerator // x.denominator
                                    - i * x.numerator // x.denominator) == 1
        for n in range(-1000, 1001):
            a, b = digit_pair(n, 2, is_a)
            assert b - a == n
            total += 1
        assert all(sum(is_a(i) for i in range(N)) == N * alpha.numerator // alpha.denominator
                   for N in range(1, 101))
    print('MECHANICAL_SUPPORT_CHECK_OK tested_signed_integers=', total)


def check_gap_witness():
    for r in (2, 4, 8, 12):
        is_a = lambda i, length=r: i < length or (i >= length and (i - length) % 2 == 1)
        a, b = digit_pair(1, 2, is_a)
        assert (a, b) == (2 ** r - 1, 2 ** r)
        # Switching the two supports exchanges positive and negative witnesses.
        a2, b2 = digit_pair(-1, 2, lambda i: not is_a(i))
        assert (a2, b2) == (2 ** r, 2 ** r - 1)
    print('GAP_WITNESS_CHECK_OK lengths=2,4,8,12')


if __name__ == '__main__':
    check_periodic()
    check_mechanical()
    check_gap_witness()
    print('VERIFY_OK exact_integers=yes finite_tests_only=yes')
