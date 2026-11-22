"""Second exact checker, with vector-space Fano lines and recursive Bellman equations.

Run: python3 check_xor.py. No third-party dependencies.
"""
from fractions import Fraction
from functools import lru_cache
from collections import Counter
from itertools import combinations

# Use 1..7 for nonzero F_2^3 vectors, instead of a cyclic Fano model.
triples = sorted({tuple(sorted((a,b,a^b))) for a,b in combinations(range(1,8), 2)})
assert len(triples) == 7
E = {(min(a-1,7+j),max(a-1,7+j)) for j,line in enumerate(triples) for a in line}
assert len(E)==21
nbr = [set() for _ in range(14)]
for a,b in E:
    nbr[a].add(b); nbr[b].add(a)
assert all(len(v)==3 for v in nbr)

@lru_cache(None)
def absorption(s):
    available = []
    for a in range(14):
        local = sum(bool(s & (1<<b)) for b in nbr[a])
        if bool(s & (1<<a)) != (local >= 2):
            available.append(a)
    if not available:
        return Fraction(int(s not in (0, (1<<14)-1)))
    return sum((absorption(s ^ (1<<a)) for a in available), Fraction()) / len(available)

N = 1 << 14
by_k = [Fraction(0) for _ in range(15)]
frequency = Counter()
for s in range(N):
    f = absorption(s)
    assert 0<=f<=1
    by_k[s.bit_count()] += f
    if s.bit_count()==3:
        frequency[f] += 1
assert absorption.cache_info().currsize == N
assert frequency == {Fraction(0): 308, Fraction(1,15): 56}
assert by_k[3] == Fraction(56,15)
C = [Fraction(56,15), Fraction(106896721,2083725),
     Fraction(216605875348939,8509411968750),
     Fraction(4672732892864737,4778885761650000)]
for x in [Fraction(j,14) for j in range(15)]:
    lhs = sum((by_k[k]*x**k*(1-x)**(14-k) for k in range(15)),Fraction())
    q = x*(1-x)
    rhs = q**3 * sum((c*q**j for j,c in enumerate(C)),Fraction())
    assert lhs == rhs
print('PASS: independent Fano lines and recursive rational Bellman equations')
print('full polynomial coefficients =', [str(v) for v in by_k])
print('unbiased nonconsensus probability =',sum(by_k,Fraction()) / N)
