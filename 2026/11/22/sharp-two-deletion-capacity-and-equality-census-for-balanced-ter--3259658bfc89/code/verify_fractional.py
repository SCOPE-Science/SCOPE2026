#!/usr/bin/env python3
"""Exact rational primal/dual certificates for the natural two-deletion shadow LP.

The primal allows nonnegative weight on each of the 90 balanced source words,
with total weight at most one among sources producing any fixed four-symbol read.
The dual weights four-symbol reads and covers every source by weight at least one.
"""
from itertools import permutations,combinations
from fractions import Fraction as Q

sources = sorted(set(permutations((0,0,1,1,2,2))))
reads = sorted({tuple(w[i] for i in inds) for w in sources for inds in combinations(range(6),4)})
shadows = {w: {tuple(w[i] for i in inds) for inds in combinations(range(6),4)} for w in sources}
actions = [(p,r) for p in permutations((0,1,2)) for r in (False,True)]
def orbit(word):
    return {tuple(p[c] for c in (word[::-1] if reverse else word)) for p,reverse in actions}

primal = {w:Q(0) for w in sources}
for representative, weight in [('001122',Q(1,15)),('001212',Q(3,20)),
                               ('010221',Q(1,60)),('011220',Q(1,6)),
                               ('012021',Q(2,15))]:
    for w in orbit(tuple(map(int,representative))):
        assert primal[w] == 0
        primal[w] = weight
assert sum(primal.values()) == 5
for read in reads:
    assert sum((primal[w] for w in sources if read in shadows[w]),Q(0)) <= 1

dual = {r:Q(0) for r in reads}
for representative in ['0011','0012','0112','0120']:
    for read in orbit(tuple(map(int,representative))):
        assert dual[read] == 0
        dual[read] = Q(1,6)
assert sum(dual.values()) == 5
for w in sources:
    assert sum((dual[s] for s in shadows[w]),Q(0)) >= 1
print('primal_sum=5 dual_sum=5: rational LP optimum exactly 5')
print('positive_primal_words=',sum(v>0 for v in primal.values()))
print('positive_dual_reads=',sum(v>0 for v in dual.values()))
