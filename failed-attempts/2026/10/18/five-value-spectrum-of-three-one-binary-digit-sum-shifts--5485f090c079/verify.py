#!/usr/bin/env python3
"""Exact certificate for three-one binary digit-sum shift densities.

Only Python standard library; run with: python3 verify.py
"""
from fractions import Fraction

EXPECTED_COUNTS = (
    (43, 76, 164, 336),
    (76, 160, 320, 656),
    (164, 320, 640, 1312),
    (336, 656, 1312, 2688),
)
EXPECTED_VALUES = {Fraction(19, 32), Fraction(5, 8), Fraction(41, 64),
                   Fraction(21, 32), Fraction(43, 64)}


def canonical_bits(g, h):
    assert g >= 0 and h >= 0
    return [1] + [0] * g + [1] + [0] * h + [1]


def exact_dp_count(bits, allowed=3):
    """Count successful prefixes; all X_i are equiprobable binary digits."""
    bits = list(bits) + [0] * allowed
    dp = {(0, 0): 1}
    for t_bit in bits:
        new = {}
        for (carry, used), count in dp.items():
            for n_bit in (0, 1):
                nextcarry = (n_bit + t_bit + carry) // 2
                nextused = used + nextcarry
                if nextused <= allowed:
                    key = (nextcarry, nextused)
                    new[key] = new.get(key, 0) + count
        dp = new
    return sum(v for (carry, used), v in dp.items() if carry == 0)


def exact_density(t):
    assert t > 0 and t.bit_count() == 3
    bits = [(t >> i) & 1 for i in range(t.bit_length())]
    bit_count = len(bits) + 3
    return Fraction(exact_dp_count(bits), 2 ** bit_count)


def direct_residue_count(g, h):
    """Independent integer arithmetic via full residue enumeration."""
    t = 1 + (1 << (g + 1)) + (1 << (g + h + 2))
    length = 6 + g + h
    return sum(1 for n in range(1 << length)
               if (n + t).bit_count() >= n.bit_count())


def main():
    seen = set()
    for g in range(4):
        for h in range(4):
            bits = canonical_bits(g, h)
            count = exact_dp_count(bits)
            assert count == EXPECTED_COUNTS[g][h], (g, h, count)
            total = 1 << (6 + g + h)
            c = Fraction(count, total)
            seen.add(c)
            assert direct_residue_count(g, h) == count, (g, h)
    assert seen == EXPECTED_VALUES, seen
    assert min(seen) == Fraction(19, 32)
    assert max(seen) == Fraction(43, 64)

    # Extend the finite 4x4 table by the theorem's gap-saturation rule.
    for g in range(13):
        for h in range(13):
            compressed = Fraction(EXPECTED_COUNTS[min(g, 3)][min(h, 3)],
                                  1 << (6 + min(g, 3) + min(h, 3)))
            t = 1 + (1 << (g + 1)) + (1 << (g + h + 2))
            assert exact_density(t) == compressed, (g, h)
            assert exact_density(2 ** (g % 5) * t) == compressed
    print('VERIFY_OK: 16 exact table values, independent residue checks, '
          '169 gap tests and shift scaling')


if __name__ == '__main__':
    main()
