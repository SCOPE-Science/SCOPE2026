#!/usr/bin/env python3
"""Exact 128-case certificate for palindromic-factor frequencies.

This script has no nonstandard dependencies. The all-index result additionally
uses the elementary block identity and primitive uniform substitution proved
in RESULT.md; finite prefix checks below are diagnostic only.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction


def bitword(n):
    return (n & (n >> 1)).bit_count() & 1


def child(state, digit):
    u, v, parity = state
    return (u, u ^ parity, 0) if digit == 0 else (u ^ parity, v, 1)


def letter_from_state(state, offset):
    a, b, parity = state
    if offset < 16:
        return a ^ bitword(offset) ^ (parity & (offset >> 3))
    t = offset - 16
    return b ^ bitword(t) ^ ((parity ^ 1) & (t >> 3))


def local_word(state, offset, length):
    return ''.join(str(letter_from_state(state, offset + j)) for j in range(length))


STATES = [(a, b, p) for a in (0, 1) for b in (0, 1) for p in (0, 1)]
COUNTS = {
    1: (['0','1'],64),
    2: (['00','11'],32),
    3: (['000','010','101','111'],16),
    4: (['0000','0110','1001','1111'],4),
    5: (['00100','01110','10001','11011'],8),
    6: (['010010','011110','100001','101101'],4),
    7: (['0001000','0100010','1011101','1110111'],2),
    8: (['00100100','01000010','10111101','11011011'],2),
    10: (['0001001000','0010000100','1101111011','1110110111'],2),
    12: (['000010010000','111101101111'],1),
    14: (['01111011011110','10000100100001'],1),
}
# Exact start sets for all palindromes of length >= 7: map to (offset mod 16,
# permitted three-bit state codes for (r(q),r(q+1),q mod 2)).
HIGH = {
    '0001000': (11, ['001','100']),
    '0100010': (14, ['000','101']),
    '1011101': (14, ['011','110']),
    '1110111': (11, ['010','111']),
    '00100100': (1, ['000','010']),
    '01000010': (13, ['001','100']),
    '10111101': (13, ['010','111']),
    '11011011': (1, ['100','110']),
    '0001001000': (0, ['000','010']),
    '0010000100': (12, ['001','100']),
    '1101111011': (12, ['010','111']),
    '1110110111': (0, ['100','110']),
    '000010010000': (15, ['001']),
    '111101101111': (15, ['111']),
    '01111011011110': (14, ['111']),
    '10000100100001': (14, ['001']),
}


def certificate():
    visited = {(0, 0, 0)}
    queue = deque(visited)
    while queue:
        s = queue.popleft()
        for d in (0,1):
            child_s = child(s,d)
            if child_s not in visited:
                visited.add(child_s)
                queue.append(child_s)
    assert visited == set(STATES)
    assert all(sum(child(t,d) == s for t in STATES for d in (0,1)) == 2 for s in STATES)
    # Every state can be reached from every other state after four input bits:
    assert all({child(child(child(child(s,a),b),c),d)
                for a in (0,1) for b in (0,1) for c in (0,1) for d in (0,1)}
               == set(STATES) for s in STATES)
    allcases = {}
    for length in range(1,17):
        occurrences = defaultdict(set)
        for state in STATES:
            for residue in range(16):
                w = local_word(state,residue,length)
                if w == w[::-1]:
                    occurrences[w].add((residue,''.join(map(str,state))))
        expected = COUNTS.get(length, ([],0))
        assert sorted(occurrences) == expected[0], (length,sorted(occurrences))
        assert all(len(cases) == expected[1] for cases in occurrences.values())
        if length >= 7:
            for w,cases in occurrences.items():
                residue, codes = HIGH[w]
                assert cases == {(residue,z) for z in codes}, (length,w,cases)
        allcases[length] = occurrences
    assert set(HIGH) == {w for length in (7,8,10,12,14) for w in COUNTS[length][0]}
    return allcases


def diagnostic(allcases):
    n = 1 << 17
    word = ''.join(str(bitword(i)) for i in range(n+16))
    checked = 0
    for length in range(1,17):
        for i in range(n):
            direct = word[i:i+length]
            condition = direct == direct[::-1]
            state = (bitword(i//16),bitword(i//16+1),(i//16)&1)
            assert ((i%16,''.join(map(str,state))) in allcases[length].get(direct, set())) == condition
            checked += 1
    # Scattered locations far beyond the tested prefix.
    for k in range(10000):
        q = (1 << 25) + k * 2237
        state = (bitword(q), bitword(q+1),q&1)
        for t in (0,1,7,14,15,16,25,30):
            assert letter_from_state(state,t) == bitword(16*q+t)
    return checked


if __name__ == '__main__':
    cases = certificate()
    tested = diagnostic(cases)
    print('VERIFY_OK exact_cases=2048 primitive_state_power=4 direct_windows='+str(tested)+' long_position_checks=80000')
