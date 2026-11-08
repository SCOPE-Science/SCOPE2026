"""Independent finite checks for cyclic-orbit lifting in paperfolding words.

Run with Python 3: python verify.py
The finite checks are diagnostic; the all-length result follows from the proof.
"""
from collections import defaultdict, Counter
from itertools import product


def direct_word(instructions, length):
    result = []
    for index in range(length):
        value = index + 1
        exponent = (value & -value).bit_length() - 1
        odd_part = value >> exponent
        bit = instructions[exponent]
        result.append(str(bit if odd_part % 4 == 1 else 1 - bit))
    return ''.join(result)


def recursive_word(instructions, length):
    if length == 0:
        return ''
    odd_track = recursive_word(instructions[1:], length // 2) if length > 1 else ''
    result = [''] * length
    for j in range((length + 1) // 2):
        result[2*j] = str(instructions[0] ^ (j % 2))
    for j, bit in enumerate(odd_track):
        result[2*j+1] = bit
    return ''.join(result)


def factors_with_positions(word, length):
    found = {}
    for i in range(len(word) - length + 1):
        block = word[i:i+length]
        if block not in found:
            found[block] = i
    return found


def rotation_representative(word):
    return min(word[i:]+word[:i] for i in range(len(word)))


def classes(words):
    result = defaultdict(set)
    for word in words:
        result[rotation_representative(word)].add(word)
    return result


def lift(word, index, first_instruction):
    return ''.join(str(first_instruction ^ ((index+j) % 2)) + bit
                   for j, bit in enumerate(word))


def check_case(instructions, length, check_lengths):
    x = direct_word(instructions, length)
    y = direct_word(instructions[1:], length // 2)
    assert x[:2048] == recursive_word(instructions, 2048)
    assert x[1::2] == y
    for n in check_lengths:
        words = factors_with_positions(y, n)
        expanded = factors_with_positions(x, 2*n)
        # Allouche's exact factor counts imply completeness if these sizes match.
        assert len(words) == 4*n, (n, len(words))
        assert len(expanded) == 8*n, (n, len(expanded))
        low = classes(words)
        high = classes(expanded)
        assert len(low) == len(high), (n, len(low), len(high))
        assert Counter(2*len(v) for v in low.values()) == Counter(len(v) for v in high.values()), n
        induced = defaultdict(set)
        for word, pos in words.items():
            eword = lift(word, pos, instructions[0])
            assert eword == x[2*pos:2*pos+2*n]
            assert eword in expanded
            induced[rotation_representative(word)].add(rotation_representative(eword))
        assert all(len(images) == 1 for images in induced.values())
        assert len({next(iter(images)) for images in induced.values()}) == len(low)
        for lowclass, image in induced.items():
            dest = next(iter(image))
            assert len(high[dest]) == 2*len(low[lowclass])
        assert set(next(iter(images)) for images in induced.values()) == set(high)
    return len(check_lengths)


def run():
    seeds = [tuple((mask >> (i % 8)) & 1 for i in range(32)) for mask in range(16)]
    seeds += [tuple(0 for _ in range(32)), tuple(1 for _ in range(32))]
    ns = (8, 12, 16, 20, 24, 28, 32, 36, 40, 48, 64, 96)
    num = 0
    for bits in seeds:
        num += check_case(bits, 32768, ns)
    standard = direct_word((1,)*32, 32768)
    assert len(classes(factors_with_positions(standard, 4))) == 3
    assert len(classes(factors_with_positions(standard, 8))) == 4
    base = [(n,len(classes(factors_with_positions(standard,n)))) for n in (8,12,16,20,24)]
    print('VERIFY_OK', 'instruction_sequences=',len(seeds), 'length_pairs=',num,
          'base_cyclic_counts=',base, 'n4_exception=',(3,4))


if __name__ == '__main__':
    run()
