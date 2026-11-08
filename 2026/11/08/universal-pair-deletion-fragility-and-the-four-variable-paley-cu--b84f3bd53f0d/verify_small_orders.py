#!/usr/bin/env python3
"""Exact finite field checks for three-extension multiplicity in P(29), P(37), P(41).
This proves the finite base cases by exhaustive integer arithmetic; the infinite
large-order assertion uses the separate character-sum proof in RESULT.md.
"""
from itertools import combinations
from collections import Counter


def sample(p):
    squares = {a*a % p for a in range(1, p)}
    assert len(squares) == (p-1)//2 and -1 % p in squares
    neighbors = [frozenset((i+s) % p for s in squares) for i in range(p)]
    overall_min = p
    multiplicities = Counter()
    scarce_pairs = set()
    for a,b,c in combinations(range(p),3):
        witnesses = [[] for _ in range(8)]
        for x in range(p):
            if x in (a,b,c):
                continue
            mask = 4*(x in neighbors[a])+2*(x in neighbors[b])+(x in neighbors[c])
            witnesses[mask].append(x)
        for positions in witnesses:
            sz = len(positions)
            multiplicities[sz] += 1
            overall_min = min(overall_min,sz)
            if sz == 2:
                scarce_pairs.add(tuple(sorted(positions)))
    two_pairs = set(combinations(range(p),2))
    assert overall_min == 2, (p,overall_min)
    assert scarce_pairs == two_pairs, (p,len(scarce_pairs),len(two_pairs))
    return dict(q=p, triples=p*(p-1)*(p-2)//6,
                checked_patterns=8*p*(p-1)*(p-2)//6,
                least_witnesses=overall_min,
                scarce_pairs=len(scarce_pairs),
                all_pairs=len(two_pairs),
                multiplicity_two_patterns=multiplicities[2])


def main():
    for p in (29,37,41):
        print(sample(p))
    print('PASS: every pattern has at least two witnesses, and every vertex pair is the entire witness set of a pattern.')

if __name__ == '__main__':
    main()
