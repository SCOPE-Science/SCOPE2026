#!/usr/bin/env python3
"""Independent finite checks of the paperfolding dyadic Abelian-power theorem.

This is supporting finite evidence; the infinite statements use the proof in RESULT.md.
Run: python3 verify.py (stdlib only).
"""

from itertools import product


def folding(n, instructions):
    assert n >= 1
    v = (n & -n).bit_length() - 1
    odd = n >> v
    return (1 if odd % 4 == 1 else -1) * instructions(v)


def build_prefix(length, instructions):
    pref = [0] * (length + 1)
    for n in range(1, length + 1):
        pref[n] = pref[n - 1] + folding(n, instructions)
    return pref


def block(pref, i, length):
    return pref[i + length - 1] - pref[i - 1]


def instruction_variants():
    fixed = (
        (1,), (-1,), (1, -1), (1, 1, -1),
        (1, -1, -1, 1, 1), (-1, -1, 1, -1, 1, 1, -1)
    )
    for v in fixed:
        yield lambda k, v=v: v[k % len(v)]


def test_one(instr, span=65536, max_k=7):
    largest = 1 << max_k
    pref = build_prefix(span + 4 * largest, instr)
    assertions = 0
    for k in range(max_k + 1):
        length = 1 << k
        signs = []
        pair = cube = four = 0
        for i in range(1, span + 1):
            sums = tuple(block(pref, i + j * length, length) for j in range(4))
            if k:
                assert sums[0] in (-2, 0, 2)
                assertions += 1
            signs.append(sums[0])
            pair += sums[0] == sums[1]
            cube += sums[0] == sums[1] == sums[2]
            four += sums[0] == sums[1] == sums[2] == sums[3]
        if k == 0:
            targets = (0.5, 0.125)
        else:
            targets = (0.25, 0.0625)
            for v, target in ((-2, 0.25), (0, 0.5), (2, 0.25)):
                assert abs(signs.count(v) / span - target) < 0.0035
                assertions += 1
        assert abs(pair / span - targets[0]) < 0.0035, (k, 'pair', pair)
        assert abs(cube / span - targets[1]) < 0.0035, (k, 'cube', cube)
        assert four == 0, (k, 'four', four)
        assertions += 3
        if k >= 2:
            shift = k - 1
            for i in range(1, 2000):
                j = (i + (1 << shift) - 1) >> shift
                tail = lambda v: instr(v + shift)
                direct = sum(folding(z, tail) for z in (j, j + 1))
                assert block(pref, i, length) == direct
                assertions += 1
    return assertions


def test_exhaustive_instruction_prefixes():
    # At positions up to this limit only instruction levels 0..9 can be read.
    # Exhaust all 2^8 instruction assignments for a small exact boundary test.
    assertions = 0
    for signs in product((1, -1), repeat=8):
        inst = lambda k, s=signs: s[k] if k < len(s) else 1
        pref = build_prefix(256, inst)
        for k in range(6):
            L = 1 << k
            for i in range(1, 256 - 4 * L + 2):
                ss = [block(pref, i + h * L, L) for h in range(4)]
                assert not (ss[0] == ss[1] == ss[2] == ss[3])
                if k:
                    assert ss[0] in (-2, 0, 2)
                assertions += 1
    return assertions


if __name__ == '__main__':
    total = test_exhaustive_instruction_prefixes()
    for instructions in instruction_variants():
        total += test_one(instructions)
    print('VERIFY_OK assertions=', total,
          'exhaustive_instruction_prefixes=256',
          'long_instruction_patterns=6',
          'checked_lengths=1,2,4,8,16,32,64,128')
