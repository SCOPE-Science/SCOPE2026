#!/usr/bin/env python3
"""Reproduce finite checks for a period-doubling prefix first-collision theorem.

This is finite corroboration, not an infinite proof. Requires Python 3.9+ only.
"""

def from_substitution(minimum):
    word = '0'
    while len(word) < minimum:
        word = ''.join('01' if c == '0' else '00' for c in word)
    return word


def from_valuations(count):
    return ''.join(str(((i+1 & -(i+1)).bit_length()-1) % 2)
                   for i in range(count))


def prediction(length):
    if length == 1:
        return (2, 0)
    scale = 1 << (length.bit_length()-1)
    if 2 * length < 3 * scale:
        return (3 * scale // 2, scale)
    return (2 * scale, 0)


def observed_first_collision(word, length):
    seen = {}
    for start in range(len(word)-length+1):
        factor = word[start:start+length]
        if factor in seen:
            return start, seen[factor]
        seen[factor] = start
    raise AssertionError('Insufficient finite prefix')


def run():
    word = from_substitution(16384)
    arith = from_valuations(16384)
    assert word[:16384] == arith
    assert '0000' not in word and '11' not in word
    lengths = 1024
    for length in range(1, lengths+1):
        j, i = observed_first_collision(word, length)
        assert (j,i) == prediction(length), (length,(j,i),prediction(length))
    # Direct desubstitution comparison for both parity classes, without
    # invoking first-collision data or the closed formula.
    for m in range(2,40):
        for a in range(16):
            for b in range(16):
                for parity in (0,1):
                    for n in (2*m,2*m+1):
                        lhs = word[2*a+parity:2*a+parity+n] == word[2*b+parity:2*b+parity+n]
                        reduced = m + (n%2 and parity==1)
                        rhs = word[a:a+reduced] == word[b:b+reduced]
                        assert lhs == rhs, (a,b,parity,n)
    print('VERIFY_OK independent_generators=16384')
    print('VERIFY_OK exhaustive_first_collision_and_unique_previous_source_lengths=1..1024')
    print('VERIFY_OK two_parity_desubstitution_length_cases_m=2..39,a,b=0..15')
    print('VERIFY_OK maximal_zero_run_below_four=yes')
    for n in (1,2,3,4,5,6,7,8,11,12,16,23,24,31,32,47,48,63,64,95,96,127,128):
        print(f'EXAMPLE length={n} repeated_at={prediction(n)[0]} previous_at={prediction(n)[1]}')

if __name__ == '__main__':
    run()
