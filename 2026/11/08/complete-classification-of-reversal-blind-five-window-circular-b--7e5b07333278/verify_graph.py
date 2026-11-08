"""Graph-first complete search of binary cyclic five-window reversal profiles.

Only the Python standard library is required. Run: python3 verify_graph.py
"""
from collections import defaultdict

WINDOW = 5

def reverse_five(x):
    return int(format(x, '05b')[::-1], 2)

# A reversal class is represented by its smaller five-bit integer.
representatives = sorted({min(x, reverse_five(x)) for x in range(32)})
assert len(representatives) == 20
class_index = {x: representatives.index(min(x, reverse_five(x))) for x in range(32)}

def minimum_rotation(word):
    return min(word[k:] + word[:k] for k in range(len(word)))

def classes_of(word):
    n = len(word)
    return {class_index[int(''.join(word[(i + j) % n] for j in range(5)), 2)]
            for i in range(n)}

cycles = defaultdict(set)
expanded = 0

def enumerate_closed_walks(initial, state, used, appended):
    """Follow each reversal class at most once in the binary four-bit-state graph."""
    global expanded
    expanded += 1
    depth = len(appended)
    if depth >= 5 and state == initial:
        prefix = [str((initial >> j) & 1) for j in (3, 2, 1, 0)]
        word = ''.join((prefix + appended)[:depth])
        assert len(classes_of(word)) == depth
        cycles[depth].add(minimum_rotation(word))
    if depth == len(representatives):
        return
    for bit in (0, 1):
        edge = (state << 1) | bit
        label_bit = 1 << class_index[edge]
        if not used & label_bit:
            enumerate_closed_walks(initial, edge & 15, used | label_bit,
                                   appended + [str(bit)])

for start in range(16):
    enumerate_closed_walks(start, start, 0, [])

expected = {
    6: ['001011', '001101'],
    7: ['0001011', '0001101', '0010111', '0011101'],
    8: ['00010111', '00011101', '00101011', '00110101'],
    9: ['000101011', '000110101', '001010111', '001110101'],
    10: ['0001010111', '0001110101'],
    12: ['000100110111', '000100111011', '000110111001', '000111011001'],
}
assert {n: sorted(words) for n, words in cycles.items()} == expected
assert expanded == 3242
assert sum(map(len, cycles.values())) == 20
for n, words in sorted(cycles.items()):
    masks = [classes_of(s) for s in words]
    assert all(a & b for a in masks for b in masks)
    print('n=%d necklaces=%d capacity=1' % (n, len(words)))
for n in range(5, 21):
    if n not in cycles:
        print('n=%d necklaces=0 capacity=0' % n)
print('GRAPH_COMPLETE_OK expanded=%d necklaces=20' % expanded)
