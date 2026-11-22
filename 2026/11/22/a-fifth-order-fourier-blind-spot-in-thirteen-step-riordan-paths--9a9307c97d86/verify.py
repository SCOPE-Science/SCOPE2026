"""Exact, self-contained verifier for the length-thirteen Riordan-path Walsh spectrum.

Run: python3 verify.py (Python 3.9+, standard library only).
"""
from collections import Counter
from fractions import Fraction


def enumerate_level_profiles(n):
    """Independently enumerate all U/H/D excursions with H forbidden at height zero."""
    masks = []

    def visit(i, height, horizontal_mask):
        if i == n:
            if height == 0:
                masks.append(horizontal_mask)
            return
        visit(i + 1, height + 1, horizontal_mask)  # U
        if height:
            visit(i + 1, height - 1, horizontal_mask)  # D
            visit(i + 1, height, horizontal_mask | (1 << i))  # H

    visit(0, 0, 0)
    return masks


def walsh_in_place(a):
    span = 1
    while span < len(a):
        for start in range(0, len(a), 2 * span):
            for j in range(start, start + span):
                x, y = a[j], a[j + span]
                a[j], a[j + span] = x + y, x - y
        span *= 2
    return a


def transfer_multiplier(n, frequency):
    """Independent height-state signed-path transfer (not an FWHT)."""
    states = [0] * (n + 1)
    states[0] = 1
    for i in range(n):
        following = [0] * (n + 1)
        sign = -1 if frequency & (1 << i) else 1
        for h, v in enumerate(states):
            if v == 0:
                continue
            if h < n:
                following[h + 1] += v       # up
            if h:
                following[h - 1] += v       # down
                following[h] += sign * v    # horizontal only above ground
        states = following
    return states[0]


def check():
    expected = {
        2: (1, 0, None, 1), 3: (1, 0, None, 1),
        4: (3, 0, None, 1), 5: (6, 16, 1, 2),
        6: (15, 0, None, 1), 7: (36, 8, 2, 2),
        8: (91, 0, None, 1), 9: (232, 64, 2, 2),
        10: (603, 0, None, 1), 11: (1585, 0, None, 1),
        12: (4213, 0, None, 1), 13: (11298, 176, 5, 2),
    }
    for n, (total, nzeros, minzero, gap) in expected.items():
        paths = enumerate_level_profiles(n)
        assert len(paths) == total, (n, len(paths), total)
        counts = [0] * (1 << n)
        for m in paths:
            counts[m] += 1
        transform = walsh_in_place(counts[:])
        assert transform[0] == len(paths)
        assert all(transform[s] == transfer_multiplier(n, s)
                   for s in range(1 << n)), 'independent frequency check failed'
        zeros = [s for s, v in enumerate(transform) if v == 0]
        assert len(zeros) == nzeros
        assert (min((s.bit_count() for s in zeros), default=None) == minzero)
        assert min(abs(x) for x in transform if x) == gap
        if n == 13:
            assert transform[110] == 0
            assert Counter(s.bit_count() for s in zeros) == {5:22, 6:66, 7:66, 8:22}
            assert sum(x != 0 for x in transform) == 8016
            assert sum(x > 0 for x in transform) == 4008
            assert sum(x < 0 for x in transform) == 4008
            ker_numerator = walsh_in_place([int(x != 0) for x in transform])
            assert Counter(abs(z) for z in ker_numerator) == {
                0: 7412, 16: 328, 32: 208, 48: 140, 64: 40,
                80: 26, 96: 16, 112: 14, 128: 4, 144: 2,
                176: 1, 8016: 1,
            }
            assert sum(abs(z) for z in ker_numerator) == 35360
            assert Fraction(sum(abs(z) for z in ker_numerator), 1 << 13) == Fraction(1105, 256)
            assert Fraction(max(abs(x) for x in transform), gap) == Fraction(5649)
    print('PASS: path census, all Walsh values, low-support boundary, projection kernel, endpoint norm')


if __name__ == '__main__':
    check()
