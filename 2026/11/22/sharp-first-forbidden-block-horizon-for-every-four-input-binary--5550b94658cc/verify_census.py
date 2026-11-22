"""Independent reproducibility check for the four-input binary CA census.

Run with Python 3: python verify_fourinput.py
Uses no external packages. Counts every rule by a graph search whose vertices
are sets of possible three-bit input suffixes.
"""
from collections import Counter, deque
from itertools import product

EXPECTED = {None:582, 1:2, 2:688, 3:4252, 4:10288,
            5:16348, 6:15688, 7:9900, 8:4676, 9:1996,
            10:684, 11:304, 12:56, 13:32, 14:8,
            16:16, 17:12, 18:4}
EXTREMALS = (5482, 22184, 43351, 60053)


def transitions(rule):
    # For each three-symbol suffix and requested output, its possible
    # new suffixes, obtained by appending the next input bit.
    edges = [[0, 0] for _ in range(8)]
    for a,b,c,d in product((0,1), repeat=4):
        before = (a<<2)|(b<<1)|c
        after = (b<<2)|(c<<1)|d
        digit = (rule >> ((a<<3)|(b<<2)|(c<<1)|d)) & 1
        edges[before][digit] |= (1<<after)
    return edges


def first_absence(rule, return_words=False):
    edges = transitions(rule)
    seen = {255}
    level = [(255, '')]
    depth = 0
    while level:
        next_level = []
        missing = []
        for state,word in level:
            for digit in (0,1):
                after = 0
                for suffix in range(8):
                    if state & (1<<suffix):
                        after |= edges[suffix][digit]
                nxt = word + str(digit)
                if after == 0:
                    missing.append(nxt)
                elif after not in seen:
                    seen.add(after)
                    next_level.append((after, nxt))
        if missing:
            if return_words:
                return depth+1, missing
            return depth+1
        level = next_level
        depth += 1
    return (None, []) if return_words else None


def directly_occurs(rule, word):
    n = len(word)
    target = ''.join(str(x) for x in word)
    for bits in product((0,1), repeat=n+3):
        result = ''.join(str((rule >> (8*bits[i]+4*bits[i+1]+2*bits[i+2]+bits[i+3]))&1)
                         for i in range(n))
        if result == target:
            return True
    return False


def absent_count(rule, length):
    edges = transitions(rule)
    counts = {255:1}
    for _ in range(length):
        next_counts = {}
        for state,mult in counts.items():
            for digit in (0,1):
                after = 0
                for suffix in range(8):
                    if state & (1<<suffix):
                        after |= edges[suffix][digit]
                next_counts[after] = next_counts.get(after,0) + mult
        counts = next_counts
    return counts.get(0,0)


def main():
    hist = Counter()
    longest = []
    for rule in range(1<<16):
        d = first_absence(rule)
        hist[d] += 1
        if d == 18:
            longest.append(rule)
    assert hist == EXPECTED, (hist, EXPECTED)
    assert tuple(longest) == EXTREMALS, longest
    assert sum(hist.values()) == 65536
    for rule in EXTREMALS:
        assert absent_count(rule,17)==0
        assert absent_count(rule,18)==8
    assert first_absence(5482, True)[1][0] == '100101010010100101'
    assert first_absence(43351, True)[1][0] == '010010110101101010'
    for rule in (0,1,5,255,5482,22184,43351,60053,65535):
        d = first_absence(rule)
        for n in range(1, min(d or 8,8)+1):
            # Exhaustively check all length-n output words and all length n+3 input blocks.
            pre = {''.join(str((rule>>(8*bits[i]+4*bits[i+1]+2*bits[i+2]+bits[i+3]))&1)
                           for i in range(n)) for bits in product((0,1),repeat=n+3)}
            assert (len(pre) == 2**n) == (d is None or n < d), (rule,n,len(pre),d)
    print('PASS complete 65536-rule independent Python census; histogram', sorted(((-1 if k is None else k),v) for k,v in hist.items()))
    print('PASS exactly four maximizers',longest)
    print('PASS direct block-enumeration cross-checks')

if __name__ == '__main__':
    main()
