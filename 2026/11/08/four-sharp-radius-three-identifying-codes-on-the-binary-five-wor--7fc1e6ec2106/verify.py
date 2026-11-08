#!/usr/bin/env python3
"""Exact finite certificate for radius-three identifying codes on binary five-words."""
from itertools import product

WORDS = [''.join(x) for x in product('01', repeat=5)]
PREFIXES = [''.join(x) for x in product('01', repeat=4)]


def inball(word):
    ans = {word}
    for d in (1, 2, 3):
        for bits in product('01', repeat=d):
            ans.add(''.join(bits) + word[:5-d])
    return frozenset(ans)


BALL = {word: inball(word) for word in WORDS}

# The pairwise separation constraints below are independently checkable
# consequences of the 32 in-balls, not assumptions about any candidate code.
UNIT = [
    ('00001', '00000', '00001'),
    ('00101', '00100', '00101'),
    ('01001', '01000', '01000'),
    ('01011', '01010', '01011'),
    ('01101', '01100', '01100'),
    ('10011', '10010', '10011'),
    ('10101', '10100', '10100'),
    ('10111', '10110', '10111'),
    ('11011', '11010', '11010'),
    ('11111', '11110', '11110'),
]
TRIPLES = [
    ('00100', '00010', ('01001','10010','11001')),
    ('11101', '11011', ('00110','01101','10110')),
]
DOUBLES = [
    ('00010', '00001', ('00010','10001')),
    ('00011', '00001', ('00011','10001')),
    ('11110', '11100', ('01110','11100')),
    ('11110', '11101', ('01110','11101')),
]


def selected(mask):
    return frozenset(PREFIXES[i] + str((mask >> i) & 1) for i in range(16))


def signatures(code):
    return [frozenset(BALL[word] & code) for word in WORDS]


def identifies(code):
    ids = signatures(code)
    return all(ids) and len(set(ids)) == len(WORDS)


def complement(code):
    return frozenset(''.join('1' if c == '0' else '0' for c in w) for w in code)


def main():
    assert len(WORDS) == 32 and len(PREFIXES) == 16
    for p in PREFIXES:
        # If neither p0 nor p1 is selected, those two vertices cannot be
        # distinguished by a code. Hence 16 is an unconditional lower bound.
        assert (BALL[p+'0'] ^ BALL[p+'1']) <= {p+'0', p+'1'}

    for v, w, mandatory in UNIT:
        assert BALL[v] ^ BALL[w] == {mandatory}
    for v, w, differences in TRIPLES + DOUBLES:
        assert BALL[v] ^ BALL[w] == set(differences)

    fixed = {p[:-1]: int(p[-1]) for _, _, p in UNIT}
    # Two of the three alternatives in each triple are already excluded.
    for p in ('11001', '00110'):
        assert p[:-1] not in fixed
        fixed[p[:-1]] = int(p[-1])
    # Paired two-term comparisons force the other two choices, independent
    # of the choices at prefixes 0001 and 1110.
    fixed.update({'1000': 1, '0111': 0})
    assert len(fixed) == 14
    assert set(PREFIXES) - set(fixed) == {'0001', '1110'}

    expected = []
    for f0001 in range(2):
        for f1110 in range(2):
            f = dict(fixed)
            f['0001'] = f0001
            f['1110'] = f1110
            mask = sum(f[p] << i for i, p in enumerate(PREFIXES))
            expected.append(mask)
            code = selected(mask)
            assert all(w in code for w in (p+str(bit) for p, bit in fixed.items()))
            assert identifies(code), (mask, code)

    # Independent of the forcing proof, inspect all 2^16 one-per-prefix
    # selections. This also guards against a transcription mistake.
    found = [mask for mask in range(1 << 16) if identifies(selected(mask))]
    assert found == sorted(expected) == [6949, 6951, 23333, 23335], found

    orbits = set()
    for mask in found:
        code = selected(mask)
        mate = complement(code)
        matching = [i for i in found if selected(i) == mate]
        assert len(matching) == 1
        orbits.add(tuple(sorted((mask, matching[0]))))
    assert len(orbits) == 3, orbits

    print('VERIFY_OK')
    print('minimum_cardinality=16')
    print('optimal_labeled_codebooks=4')
    print('prefix_masks=' + ','.join(str(x) for x in found))
    print('complement_orbits=3')


if __name__ == '__main__':
    main()
