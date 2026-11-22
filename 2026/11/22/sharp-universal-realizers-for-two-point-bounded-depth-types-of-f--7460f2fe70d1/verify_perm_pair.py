#!/usr/bin/env python3
"""Independent finite checks for two-point bounded-depth equality profiles of permutations."""
from functools import lru_cache
from itertools import combinations_with_replacement


def signature(d, length_x, offset_x, length_y, offset_y, same):
    # Literal equality matrix for the ordered list of 2(d+1) terms.
    lhs = [(0, (offset_x + i) % length_x) for i in range(d+1)]
    rhs = [(0 if same else 1, (offset_y + j) % length_y) for j in range(d+1)]
    terms = lhs + rhs
    return tuple(int(terms[i] == terms[j]) for i in range(len(terms)) for j in range(i+1, len(terms)))


def types_for_cycle_family(d, cycles):
    out = set()
    for i, x in enumerate(cycles):
        for h in range(x):
            out.add(signature(d, x, 0, x, h, True))
        for j, y in enumerate(cycles):
            if j == i:
                continue
            out.add(signature(d, x, 0, y, 0, False))
    return out


def universal_types(d):
    # Every possible within-cycle equality signature is represented by some
    # cycle length <= 2d+2, and every disconnected type by two cycles of
    # lengths <=d+1. Hence this independent finite model covers all types.
    out=set()
    for x in range(1,2*d+4):
        for h in range(x):
            out.add(signature(d,x,0,x,h,True))
    for x in range(1,d+2):
        for y in range(1,d+2):
            out.add(signature(d,x,0,y,0,False))
    return out


def partitions(n, low=1):
    if n == 0:
        yield ()
    for v in range(low,n+1):
        for suffix in partitions(n-v,v):
            yield (v,)+suffix


def check():
    tests=0
    for d in range(1,6):
        witness=tuple([k for k in range(1,d+1) for _ in range(2)]+list(range(d+1,2*d+2)))
        target=universal_types(d)
        assert len(target)==2*d*d+5*d+2, (d,len(target))
        assert types_for_cycle_family(d,witness)==target, d
        assert sum(witness)==(d+1)*(5*d+2)//2
        tests+=3
        # A proper subfamily of an optimal witness cannot cover all profiles.
        for i in range(len(witness)):
            assert types_for_cycle_family(d,witness[:i]+witness[i+1:])!=target
            tests+=1
        print('DEPTH',d,'TYPE_COUNT',len(target),'MIN_SIZE',sum(witness),'CYCLES',witness)
    # Exhaustively search every smaller cycle partition at depths 1 and 2.
    for d in (1,2):
        target=universal_types(d)
        limit=(d+1)*(5*d+2)//2
        for n in range(1,limit):
            for p in partitions(n):
                assert types_for_cycle_family(d,p)!=target, (d,n,p)
                tests+=1
        print('EXHAUSTIVE_NO_SMALLER',d, 'BELOW',limit)
    print('VERIFY_OK',tests)


if __name__=='__main__':
    check()
