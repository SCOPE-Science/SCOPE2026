#!/usr/bin/env python3
"""Exhaustive finite checks for three-read reverse-complement greedy superstrings.

This is an experimental cross-check of a separate all-length symbolic proof.
Run: python3 three_rc_verifier.py
"""
from itertools import combinations, product, permutations
from functools import lru_cache
from fractions import Fraction

def reverse_complement(w):
    return ''.join('1' if c == '0' else '0' for c in reversed(w))

def orientations(w):
    return tuple(sorted(set((w, reverse_complement(w)))))

def canonical(w):
    return min(orientations(w))

def overlap(x, y):
    for n in range(min(len(x),len(y)), 0, -1):
        if x[-n:] == y[:n]:
            return n
    return 0

def optimum(words):
    # For equal-length, distinct reverse-complement classes, an optimum is a
    # maximally overlapping directed path through one orientation per class.
    m = len(words)
    best = m*len(words[0])
    for order in permutations(words):
        for oo in product(*(orientations(w) for w in order)):
            trial = sum(map(len, oo)) - sum(overlap(oo[i], oo[i+1]) for i in range(m-1))
            if trial < best:
                best = trial
    return best

def greedy_worst(words):
    @lru_cache(None)
    def rec(state):
        if len(state) == 1:
            return len(state[0])
        choices = []
        largest = -1
        for i in range(len(state)):
            for j in range(i+1, len(state)):
                for a in orientations(state[i]):
                    for b in orientations(state[j]):
                        for u,v in ((a,b),(b,a)):
                            o = overlap(u,v)
                            if o < largest:
                                continue
                            if o > largest:
                                largest = o
                                choices = []
                            merged = canonical(u+v[o:])
                            choices.append(tuple(sorted((merged,) + state[:i] + state[i+1:j] + state[j+1:])))
        return max(rec(t) for t in set(choices))
    return rec(tuple(sorted(words)))

for k in range(3,8):
    orbits=sorted({canonical(''.join(bits)) for bits in product('01',repeat=k)})
    tested=0; extremizers=0; larger=Fraction(0,1); witness=None
    predicted=Fraction(2*k,k+2)
    for triple in combinations(orbits,3):
        exact=optimum(triple)
        greedy=greedy_worst(triple)
        ratio=Fraction(greedy,exact)
        if ratio > predicted:
            raise AssertionError(('counterexample',k,triple,exact,greedy,predicted))
        if ratio==predicted:
            extremizers+=1
        if ratio>larger:
            larger=ratio;witness=(triple,exact,greedy)
        tested+=1
    assert larger==predicted
    print(f'k={k} orbits={len(orbits)} triples={tested} ratio={larger} equality_triples={extremizers} witness={witness}')

# Stress-test the special length-k+2 optimal case and the first-merge lemma.
for k in range(3,13):
    checked=0; mergers=0
    for bits in product('01',repeat=k+2):
        w=''.join(bits)
        windows=[w[j:j+k] for j in range(3)]
        if len({canonical(x) for x in windows})!=3:
            continue
        checked+=1
        for i,j in combinations(range(3),2):
            z=windows[3-i-j]
            for x in orientations(windows[i]):
                for y in orientations(windows[j]):
                    for u,v in ((x,y),(y,x)):
                        if overlap(u,v)!=k-1:
                            continue
                        c=u+v[-1:]
                        assert max(overlap(a,b) for a in orientations(c) for b in orientations(z) for a,b in ((a,b),(b,a)))>=1
                        mergers+=1
    print(f'lemma_k={k} distinct_orbit_hosts={checked} first_merges={mergers} status=ok')

for k in (3,4,5,6,7,8,12,20):
    target=('0'*k, '0'*(k-1)+'1', '1'+'0'*(k-1))
    assert optimum(target)==k+2
    # Check explicit greedy branch, no need to enumerate all merges for k=20.
    left='0'+'1'*(k-1)
    right='1'*(k-1)+'0'
    assert overlap(left,right)==k-1
    middle=left+right[k-1:]
    tail='0'*k
    last=max(overlap(a,b) for a in orientations(middle) for b in orientations(tail) for a,b in ((a,b),(b,a)))
    assert last==1
    print(f'sharp_k={k} optimum={k+2} greedy_branch={2*k} ratio={Fraction(2*k,k+2)}')
print('ALL FINITE CHECKS PASS; all-length proof is separate.')
