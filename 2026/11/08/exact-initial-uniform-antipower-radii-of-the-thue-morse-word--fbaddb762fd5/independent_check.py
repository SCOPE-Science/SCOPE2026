#!/usr/bin/env python3
"""Separate morphic two-block exhaustive check for exact antipower radii."""
from itertools import product

DATA = [(3,5,0,44),(4,7,16,86),(5,9,16,144),(6,11,10,196),
        (7,11,0,240),(8,11,0,284),(9,13,64,360),(10,13,53,388)]

def morph(w): return ''.join(('01', '10')[int(x)] for x in w)

def all_factors(length):
    height = (length-1).bit_length()
    targets=[]
    for a,b in product('01', repeat=2):
        w=a+b
        for _ in range(height):w=morph(w)
        targets.extend(w[i:i+length] for i in range(len(w)-length+1))
    return set(targets)

def all_distinct_blocks(s, k, size):
    blocks=[s[i*size:(i+1)*size] for i in range(k)]
    return all(blocks[i] != blocks[j] for i in range(k) for j in range(i+1,k))

def main():
    for k, radius, pos, number in DATA:
        F=all_factors(k*radius)
        assert len(F) == number
        assert all(any(all_distinct_blocks(w, k, m) for m in range(1,radius+1)) for w in F)
        # Direct parity-of-binary-digit evaluation, not the morphic generator.
        lower=''.join(str((i.bit_count() & 1)) for i in range(pos,pos+k*(radius-1)))
        assert not any(all_distinct_blocks(lower,k,m) for m in range(1,radius))
    print('INDEPENDENT_CHECK_OK')

if __name__ == '__main__':main()
