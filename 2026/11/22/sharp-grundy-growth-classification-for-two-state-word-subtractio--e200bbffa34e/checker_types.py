#!/usr/bin/env python3
"""Independent exhaustive mex check for the two-state word-suffix game."""
from itertools import product

TRANSITIONS = {
    'Z': (0, 0),  # reset to rejecting state
    'I': (0, 1),  # identity
    'T': (1, 0),  # exchange
    'O': (1, 1),  # reset to accepting state
}

def predicted(word, transition):
    types = [transition[ch] for ch in word]
    # Return exact pointwise value when O is absent.
    if 'O' in types:
        return None
    if 'T' not in types:
        return 0
    if 'Z' not in types:
        return types.count('T') % 2
    blocks = ''.join(types).split('Z')
    return sum('T' in block for block in blocks) if blocks[-1].count('T') % 2 else 0

def run(alphabet, limit):
    table = {chr(97+i):t for i,t in enumerate(alphabet)}
    transforms = {ch:TRANSITIONS[t] for ch,t in table.items()}
    values = {'':0}
    maxes = []
    checked = 0
    for n in range(1,limit+1):
        high = 0
        for letters in product(table, repeat=n):
            w = ''.join(letters)
            options = set()
            for cut in range(n):
                state = 0
                for ch in w[cut:]:
                    state = transforms[ch][state]
                if state == 1:
                    options.add(values[w[:cut]])
            actual = 0
            while actual in options: actual += 1
            values[w] = actual
            expected = predicted(w, table)
            if expected is not None:
                assert actual == expected, (alphabet,w,actual,expected)
            high = max(high, actual)
            checked += 1
        maxes.append(high)
    has_o = 'O' in alphabet
    has_z = 'Z' in alphabet
    has_t = 'T' in alphabet
    has_i = 'I' in alphabet
    for n,m in enumerate(maxes,1):
        expected = (n if has_o else (n+1)//2 if has_z and has_t
                    else 1 if has_t and has_i else n%2 if has_t
                    else 0)
        assert m == expected, (alphabet,n,m,expected)
    return checked

def main():
    total=0
    # Every possible 3-letter transition assignment, including the 2-letter
    # and unary assignments as degenerate repeated-transform cases.
    for alpha in product('ZITO',repeat=3):
        total += run(alpha,8)
    print('PASS: 64 ternary transition tables, lengths 1..8; words checked:',total)

if __name__=='__main__': main()
