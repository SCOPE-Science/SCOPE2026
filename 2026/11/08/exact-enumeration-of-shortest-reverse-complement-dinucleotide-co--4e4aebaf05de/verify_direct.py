#!/usr/bin/env python3
"""Direct, exhaustive census of optimal reverse-complement dinucleotide cycles.

Python 3.10+, standard library only. Run in the same directory as catalog.txt.
Prints DIRECT_VERIFY_OK if all assertions pass.
"""
import itertools
from pathlib import Path

ALPHABET = 'ACGT'
COMPLEMENT = dict(zip(ALPHABET, 'TGCA'))


def rc(word):
    return ''.join(COMPLEMENT[c] for c in reversed(word))


def canon(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def rc_orbit(pair):
    return min(pair, rc(pair))


def maps_preserving_complement():
    result = []
    for p in itertools.permutations(ALPHABET):
        f = dict(zip(ALPHABET, p))
        if all(f[COMPLEMENT[c]] == COMPLEMENT[f[c]] for c in ALPHABET):
            result.append(f)
    return result


def main():
    classes = {rc_orbit(a + b) for a in ALPHABET for b in ALPHABET}
    assert len(classes) == 10
    representative_cycles = set()
    rooted_count = 0
    for letters in itertools.product(ALPHABET, repeat=10):
        w = ''.join(letters)
        encountered = {rc_orbit(w[i] + w[(i + 1) % 10]) for i in range(10)}
        if len(encountered) == 10:
            rooted_count += 1
            representative_cycles.add(canon(w))
    assert rooted_count == 5440
    assert len(representative_cycles) == 544
    assert all(len({rc_orbit(w[i] + w[(i + 1) % 10]) for i in range(10)}) == 10
               for w in representative_cycles)
    saved = Path(__file__).with_name('catalog.txt').read_text(encoding='utf-8').splitlines()
    assert len(saved) == 544 and saved == sorted(representative_cycles)

    # The reverse complement of a cycle changes every non-palindromic
    # dinucleotide choice and therefore fixes no optimal cycle.
    assert not any(canon(rc(w)) == w for w in representative_cycles)
    assert (len(representative_cycles) // 2) == 272

    maps = maps_preserving_complement()
    assert len(maps) == 8
    fixed_by_operation = {}
    for f in maps:
        name = ''.join(f[c] for c in ALPHABET)
        for reversed_complemented in (False, True):
            count = 0
            for w in representative_cycles:
                transformed = ''.join(f[c] for c in w)
                if reversed_complemented:
                    transformed = rc(transformed)
                count += (canon(transformed) == w)
            fixed_by_operation[(name, int(reversed_complemented))] = count
    expected = {('ACGT', 0): 544, ('CATG', 1): 24, ('GTAC', 1): 24}
    assert {k: v for k, v in fixed_by_operation.items() if v} == expected
    assert sum(fixed_by_operation.values()) == 592
    assert sum(fixed_by_operation.values()) // 16 == 37

    unseen = set(representative_cycles)
    orbit_sizes = {}
    while unseen:
        w = min(unseen)
        orbit = set()
        for f in maps:
            transformed = ''.join(f[c] for c in w)
            orbit.add(canon(transformed))
            orbit.add(canon(rc(transformed)))
        assert orbit <= representative_cycles
        unseen -= orbit
        orbit_sizes[len(orbit)] = orbit_sizes.get(len(orbit), 0) + 1
    assert orbit_sizes == {8: 6, 16: 31}
    print('DIRECT_VERIFY_OK rooted=5440 necklaces=544 physical=272 classes=37')


if __name__ == '__main__':
    main()
