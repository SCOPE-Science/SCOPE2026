#!/usr/bin/env python3
"""Check the dyadic joint binary digit-weight support and sharp witnesses."""

def expected(r):
    support = {(0, 0)}
    support.update((a, 2 * a) for a in range(1, (r + 1)//2 + 1))
    support.update(((b + t)//2, b) for b in range(2, r + 1)
                   for t in range(2, r + 1) if (b + t) % 2 == 0)
    return support


def verify():
    enumerated = 0
    for r in range(1, 16):
        actual = {(n.bit_count(), (3 * n).bit_count()) for n in range(1 << r)}
        wanted = expected(r)
        assert actual == wanted, (r, actual.symmetric_difference(wanted))
        assert len(actual) == r * (r - 1)//2 + 2
        enumerated += 1 << r

    constructions = 0
    for a in range(1, 51):
        bits = '10' * (a - 1) + '1'
        n = int(bits, 2)
        assert (n.bit_count(), (3 * n).bit_count()) == (a, 2 * a)
        assert len(bits) == 2 * a - 1
        for b in range(2, 2 * a - 1):
            t = 2 * a - b
            assert t >= 2
            if t >= b:
                bits = '10' * (a - b) + '1' * b
            else:
                bits = '1' * t + '01' * (a - t)
            n = int(bits, 2)
            assert (n.bit_count(), (3 * n).bit_count()) == (a, b), (a, b, bits)
            assert len(bits) == max(t, b)
            constructions += 1
    print('VERIFY_OK dyadic_levels=1..15 exhaustive_n=', enumerated,
          'distinct_support=PASS witnesses=', constructions,
          'sharp_minimal_lengths=PASS')


if __name__ == '__main__':
    verify()
