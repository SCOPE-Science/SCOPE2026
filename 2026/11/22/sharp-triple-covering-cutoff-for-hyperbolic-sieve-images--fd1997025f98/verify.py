#!/usr/bin/env python3
"""Exact finite certificate for triple hyperbolic-image coverage.

Only Python 3 standard library; no external data or packages.  Every triple
of distinct normalized nonzero parameters is visited for each prime <149.
"""
from itertools import combinations

EXPECTED = {
    3:0,5:4,7:16,11:60,13:92,17:152,19:153,23:176,
    29:224,31:155,37:168,41:120,43:84,47:115,53:52,
    59:0,61:60,67:0,71:0,73:12,79:0,83:0,89:0,
    97:0,101:0,103:0,107:0,109:0,113:0,127:0,131:0,
    137:0,139:0,
}


def primes_below(bound):
    return [p for p in range(3, bound, 2)
            if all(p % d for d in range(2, int(p**0.5)+1))]


def character_nonimage_masks(p):
    squares = {x*x % p for x in range(p)}
    inv4 = pow(4,-1,p)
    masks=[]
    for A in range(1,p):
        by_disc = sum(1 << t for t in range(p) if (t*t-A) % p not in squares)
        a = A*inv4 % p
        image = { (a*x + pow(x,-1,p)) % p for x in range(1,p) }
        by_image = sum(1 << t for t in range(p) if t not in image)
        assert by_disc == by_image, ('two-model mismatch',p,A)
        masks.append(by_disc)
    return masks


def all_covering_triples(p, masks):
    triples=[]
    for i in range(p-1):
        for j in range(i+1,p-1):
            pair = masks[i] & masks[j]
            for k in range(j+1,p-1):
                if not (pair & masks[k]):
                    triples.append((i+1,j+1,k+1))
    return triples


def main():
    assert primes_below(149)==sorted(EXPECTED)
    for p in primes_below(149):
        masks=character_nonimage_masks(p)
        triples=all_covering_triples(p, masks)
        assert len(triples)==EXPECTED[p], (p,len(triples),EXPECTED[p])
        if p==73:
            squares={x*x%p for x in range(1,p)}
            predicted={tuple(sorted((s%p,8*s%p,64*s%p))) for s in squares}
            assert len(predicted)==12
            assert set(triples)==predicted, ('extremal triple shapes',triples)
        print(p,len(triples))
    assert [p for p,c in EXPECTED.items() if c>0]==[
        5,7,11,13,17,19,23,29,31,37,41,43,47,53,61,73]
    print('VERIFY_OK: finite coverage and extremal parameter classification')

if __name__=='__main__':
    main()
