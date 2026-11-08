"""Independent direct occurrence and symmetry verification of order-five upwords.

Usage: python3 verify.py upwords_order5.txt [actual-enumerator-output.txt]
"""
import collections
import itertools
import pathlib
import sys


def covered_targets(word):
    seen = collections.Counter()
    for start in range(len(word) - 4):
        template = word[start:start + 5]
        for bits in itertools.product('01', repeat=template.count('*')):
            bit_iter = iter(bits)
            target = ''.join(next(bit_iter) if char == '*' else char for char in template)
            seen[target] += 1
    return seen


def complement(word):
    return word.translate(str.maketrans('01', '10'))


def main():
    expected = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8').splitlines()
    assert expected == sorted(set(expected))
    assert len(expected) == 1328
    expected_counts = {26: 8, 27: 32, 28: 32, 29: 136, 30: 352, 33: 768}
    assert dict(sorted(collections.Counter(map(len, expected)).items())) == expected_counts
    target_set = {''.join(bits) for bits in itertools.product('01', repeat=5)}
    for word in expected:
        assert set(word) <= set('01*') and word.count('*') == 2
        assert covered_targets(word) == {target: 1 for target in target_set}
    orbits = {}
    wordset = set(expected)
    for word in expected:
        orbit = {word, word[::-1], complement(word), complement(word[::-1])}
        assert len(orbit) == 4 and orbit <= wordset
        orbits[min(orbit)] = orbit
    assert len(orbits) == 332
    assert dict(sorted(collections.Counter(map(len, orbits)).items())) == {26: 2, 27: 8, 28: 8, 29: 34, 30: 88, 33: 192}
    if len(sys.argv) > 2:
        independently_generated = pathlib.Path(sys.argv[2]).read_text(encoding='utf-8').splitlines()
        assert independently_generated == expected
    print('VERIFY_OK words=1328 orbits=332 counts=' + str(expected_counts))


if __name__ == '__main__':
    main()
