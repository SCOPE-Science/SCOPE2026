#!/usr/bin/env python3
"""Exact, standalone census of predecessor-boundary synchronization for ECA images.

Only the standard library is required. Usage: python verify.py [--csv PATH]
"""
import csv
import itertools
import sys
from collections import Counter, deque


def image_set(rule, mask, symbol):
    out = 0
    for u in range(4):
        if mask & (1 << u):
            for c in range(2):
                triple = 2*u + c
                if ((rule >> triple) & 1) == symbol:
                    out |= 1 << (2*(u & 1) + c)
    return out


def classify(rule):
    # Exact breadth-first closure of the at most 15 nonempty sets of pairs.
    distance = {15: 0}
    witness = {15: ''}
    queue = deque([15])
    while queue:
        mask = queue.popleft()
        for symbol in (0, 1):
            nxt = image_set(rule, mask, symbol)
            if nxt != 0 and nxt not in distance:
                distance[nxt] = distance[mask] + 1
                witness[nxt] = witness[mask] + str(symbol)
                queue.append(nxt)
    singles = [mask for mask in distance if mask.bit_count() == 1]
    if singles:
        length = min(distance[mask] for mask in singles)
        shortest = min(witness[mask] for mask in singles if distance[mask] == length)
    else:
        length = None
        shortest = ''
    return length, shortest, distance


def direct_word_maps(rule, length):
    # Independent encoding: enumerate every length-(length+2) input word,
    # compute its outputs directly, and record its final TWO input bits.
    table = {}
    for inp in itertools.product((0,1), repeat=length+2):
        out = tuple((rule >> (4*inp[i]+2*inp[i+1]+inp[i+2])) & 1
                    for i in range(length))
        pair = 2*inp[-2] + inp[-1]
        table[out] = table.get(out, 0) | (1 << pair)
    return table


def census():
    rows = []
    sizes = Counter()
    extrema = []
    direct_checks = 0
    minimal_checks = 0
    for rule in range(256):
        length, word, visited = classify(rule)
        sizes['never' if length is None else length] += 1
        if length == 6:
            extrema.append(rule)
        # A second implementation directly enumerates all input strings.
        # A reachable word w can be validated at every length <=6, and
        # minimality for each synchronizing rule follows independently.
        direct_shortest = None
        shortest_count = 0
        for n in range(1,7):
            direct = direct_word_maps(rule, n)
            for bits in itertools.product((0,1), repeat=n):
                mask = 15
                for bit in bits:
                    mask = image_set(rule, mask, bit)
                if mask != direct.get(bits, 0):
                    raise AssertionError((rule, n, bits, mask, direct.get(bits, 0)))
                direct_checks += 1
            count = sum(mask.bit_count() == 1 for mask in direct.values())
            if count and direct_shortest is None:
                direct_shortest = n
                shortest_count = count
        assert length == direct_shortest, (rule, length, direct_shortest)
        minimal_checks += 1
        # Closure, including all successor subsets, proves nonexistence if
        # no singleton is in the reachable set; not a bounded word search.
        for mask in visited:
            for bit in (0,1):
                successor = image_set(rule, mask, bit)
                assert not successor or successor in visited
        if length is not None:
            # The BFS distance gives the exact shortest witness length.
            assert len(word) == length and image_of_word(rule, word).bit_count() == 1
        rows.append((rule, -1 if length is None else length, word,
                     len(visited), shortest_count))
    assert sizes == {1:24,2:90,3:72,4:12,5:4,6:4,'never':50}, sizes
    assert extrema == [37,91,164,218], extrema
    assert {r[0]:r[2] for r in rows if r[1] == 6} == {
        37:'100101',91:'010010',164:'100101',218:'010010'}
    assert max(r[3] for r in rows) <= 15
    return rows, sizes, direct_checks, minimal_checks


def image_of_word(rule, word):
    mask = 15
    for symbol in word:
        mask = image_set(rule, mask, int(symbol))
    return mask


if __name__ == '__main__':
    data, counts, checks, mins = census()
    if len(sys.argv) == 3 and sys.argv[1] == '--csv':
        with open(sys.argv[2], 'w', newline='', encoding='utf-8') as fp:
            writer = csv.writer(fp, lineterminator='\n')
            writer.writerow(['rule', 'shortest_length_minus_one_if_absent',
                             'lex_first_shortest_witness', 'reachable_nonempty_subsets',
                             'number_of_shortest_words'])
            writer.writerows(data)
    elif len(sys.argv) != 1:
        raise SystemExit('usage: python verify.py [--csv PATH]')
    print('VERIFY_OK: 256 elementary rules; shortest-boundary lengths',
          {str(k):counts[k] for k in (1,2,3,4,5,6,'never')},
          '; maximum 6 attained exactly by rules 37,91,164,218;',
          checks, 'independent output-word/preimage-set equalities;',
          mins, 'independent shortest-length comparisons;',
          'all reachable-subset transition closures certified')
