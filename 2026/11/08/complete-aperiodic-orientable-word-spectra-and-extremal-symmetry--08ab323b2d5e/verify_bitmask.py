"""Reversal-pair bitmask traversal of aperiodic binary orientable words.

Usage: python3 verify_bitmask.py [ENUMERATION.json]
Pure Python 3 standard library; the traversal is exact, not randomized.
"""
import json
import sys
from collections import Counter


def reverse_bits(word, n):
    result = 0
    for _ in range(n):
        result = (result << 1) | (word & 1)
        word >>= 1
    return result


def count_span(n, maximum):
    width = 1 << n
    suffix_mask = (1 << (n - 1)) - 1
    rev = [reverse_bits(x, n) for x in range(width)]
    pairs = sorted({min(x, rev[x]) for x in range(width) if x != rev[x]})
    index = {value: i for i, value in enumerate(pairs)}
    label = [-1] * width
    for x in range(width):
        if x != rev[x]:
            label[x] = index[min(x, rev[x])]
    by_length = Counter()
    optimum = []

    def extend(word, state, mask):
        by_length[len(word)] += 1
        if len(word) == maximum + 1:
            return
        if len(word) == maximum:
            optimum.append(word)
        for digit in ('0', '1'):
            v = (state << 1) | int(digit)
            k = label[v]
            if k >= 0 and not (mask & (1 << k)):
                extend(word + digit, v & suffix_mask, mask | (1 << k))

    for tail in range(1 << (n - 1)):
        head = tail  # the omitted leading bit is 0
        k = label[head]
        if k >= 0:
            extend(format(head, f'0{n}b'), head & suffix_mask, 1 << k)

    optimum.sort()
    complement = lambda x: x.translate(str.maketrans('01', '10'))
    full = set(optimum) | {complement(w) for w in optimum}
    group_orbits = {min(w, w[::-1], complement(w), complement(w[::-1])) for w in full}
    fixed = [w for w in full if w == complement(w[::-1])]
    assert len(full) == 2 * len(optimum)
    assert by_length[maximum + 1] == 0
    assert all(w.count('1') * 2 == maximum for w in optimum)
    return {
        'max_length': maximum,
        'labeled_length_counts': {str(i): 2 * by_length[i] for i in range(n, maximum + 2)},
        'first_bit_zero_maximizers': optimum,
        'first_bit_zero_prefix_counts': dict(sorted(Counter(w[:n] for w in optimum).items())),
        'first_bit_zero_suffix_counts': dict(sorted(Counter(w[-n:] for w in optimum).items())),
        'maximizer_count': len(full),
        'reverse_complement_fixed_count': len(fixed),
        'symmetry_orbits': len(group_orbits),
        'orbit_size_two': len(fixed) // 2,
        'orbit_size_four': (len(full) - len(fixed)) // 4,
        'maximum_weight_distribution': {str(k): v for k, v in sorted(Counter(w.count('1') for w in full).items())},
    }


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'ENUMERATION.json'
    with open(path, encoding='utf-8') as file:
        expected = json.load(file)
    for span, maximum in ((6, 26), (7, 48)):
        observed = count_span(span, maximum)
        assert observed == expected['spans'][str(span)], f'span {span}: mismatch'
        print(f'span={span} words={observed["maximizer_count"]} '
              f'orbits={observed["symmetry_orbits"]} length+1={observed["labeled_length_counts"][str(maximum + 1)]}')
    print('VERIFY_BITMASK_OK')


if __name__ == '__main__':
    main()
