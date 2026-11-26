"""Exact finite-state certificate for length-three factor-presence profiles.

Run with Python 3; the entire state space has only 4*256=1024 pairs.
"""
from collections import defaultdict
from itertools import product


def advance(states):
    """One new bit, retaining the final two bits and all seen triples."""
    return {
        ((2 * state + bit) % 4, mask | (1 << (2 * state + bit)))
        for state, mask in states
        for bit in (0, 1)
    }


def support(states):
    return {mask for _state, mask in states}


def raw_support(n):
    found = set()
    for bits in product((0, 1), repeat=n):
        mask = 0
        for i in range(n - 2):
            e = 4 * bits[i] + 2 * bits[i + 1] + bits[i + 2]
            mask |= 1 << e
        found.add(mask)
    return found


def main():
    states = { (state, 0) for state in range(4) }  # all length-2 binary prefixes
    by_length = {}
    for n in range(3, 19):
        states = advance(states)
        by_length[n] = states
    observed = [len(support(by_length[n])) for n in range(3, 12)]
    assert observed == [8, 15, 27, 48, 72, 94, 100, 103, 101], observed
    assert [len(support(by_length[n])) for n in range(11, 17)] == [101, 103, 101, 103, 101, 103]
    assert len(by_length[11]) == 196
    assert by_length[11] == by_length[17]  # exact state equality => period 6 for ALL future n
    assert by_length[12] == by_length[18]
    even = support(by_length[10])
    odd = support(by_length[11])
    assert even == support(by_length[12])
    assert odd.issubset(even)
    assert even - odd == {46, 116}
    for n in range(3, 16):
        assert support(by_length[n]) == raw_support(n), n
    print('CERTIFIED: R(3..11)=8,15,27,48,72,94,100,103,101')
    print('CERTIFIED: from n=10, 103 even and 101 odd support spectra')
    print('CERTIFIED: E(11)=E(17), 196 ordered (state,mask) pairs')
    print('CERTIFIED: only-even support bitmasks 46 (0x2e) and 116 (0x74)')
    print('CERTIFIED: independent exhaustive direct words n=3..15')

if __name__ == '__main__':
    main()
