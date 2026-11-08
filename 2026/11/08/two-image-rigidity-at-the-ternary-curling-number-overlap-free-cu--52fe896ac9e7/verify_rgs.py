#!/usr/bin/env python3
"""Complete symmetry-reduced enumeration for the ternary curling-image census."""
from collections import Counter
from pathlib import Path

PREFIX83 = '11211221211212211221211221121221122121121221211221121221122121122112122121121221121'
EXPECTED = {PREFIX83 + '1': 672, PREFIX83 + '2': 336}

def suffix_overlap(s):
    """A newly appended symbol creates an overlap iff a suffix has period p and length 2p+1."""
    n = len(s)
    return any(s[-(2*p+1):-p] == s[-(p+1):]
               for p in range(1, (n-1)//2+1))

def next_curl(s):
    """For overlap-free s, no cube is possible, so the curling number is 1 or 2."""
    n = len(s)
    return '2' if any(s[-2*p:-p] == s[-p:]
                      for p in range(1, n//2+1)) else '1'

def enumerate_states():
    states = {'': ''}
    terminal = None
    for n in range(1, 86):
        new_states = {}
        for w, c in states.items():
            biggest = max(map(int, w)) if w else -1
            for digit in range(min(2, biggest+1)+1):
                v = w + str(digit)
                if suffix_overlap(v):
                    continue
                d = c + next_curl(v)
                if suffix_overlap(d):
                    continue
                new_states[v] = d
        states = new_states
        if n == 84:
            terminal = dict(states)
        if n == 85:
            assert not states, 'unexpected length-85 word'
    return terminal

def main():
    assert len(PREFIX83) == 83
    states = enumerate_states()
    assert len(states) == 1008
    assert all(len(w) == 84 and len(set(w)) == 3 for w in states)
    assert Counter(states.values()) == Counter(EXPECTED)
    census = ''.join(w + '\t' + states[w] + '\n' for w in sorted(states))
    expected = Path(__file__).with_name('canonical84.tsv').read_bytes()
    assert census.encode('ascii') == expected, 'canonical census does not match regeneration'
    print('TERMINAL_CURL_RGS_VERIFY_OK 1008 672 336')

if __name__ == '__main__':
    main()
