"""Exact-rational, standalone verification of random-priority dimer RSA on the Heawood graph.
Run with Python 3.10 or newer; uses only the standard library.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial

LINES = ((0,1,3),(0,2,5),(0,4,6),(1,2,6),
         (1,4,5),(2,3,4),(3,5,6))
EDGES = tuple((p,7+j) for j, line in enumerate(LINES) for p in line)
B = tuple((1 << u) | (1 << v) for u, v in EDGES)
assert len(EDGES) == 21 and len(set(EDGES)) == 21
assert all(sum(p in line for line in LINES) == 3 for p in range(7))
assert all(sum(p in line and q in line for line in LINES) == 1
           for p in range(7) for q in range(p+1,7))
checks = 3

# Method A: exact dynamic programming on the set of already occupied vertices.
@lru_cache(None)
def residual(mask):
    feasible = [z for z in B if (mask & z) == 0]
    if not feasible:
        return {mask.bit_count()//2: Fraction(1)}
    dist = defaultdict(Fraction)
    for e in feasible:
        for k, value in residual(mask | e).items():
            dist[k] += value/Fraction(len(feasible))
    return dict(dist)

terminal = residual(0)
expected = {5: Fraction(19,330), 6: Fraction(497,792),
            7: Fraction(1247,3960)}
assert terminal == expected
checks += len(terminal)
assert sum(terminal.values()) == 1
assert sum(k*p for k,p in terminal.items()) == Fraction(24779,3960)
checks += 2

# Method B: enumerate every maximal matching, then integrate the independent
# uniform arrival priorities. This does not use the state recursion above.
maximal = []
def enumerate_matchings(i, chosen, mask):
    if i == len(B):
        if all(mask & e for e in B):
            maximal.append(tuple(chosen))
        return
    enumerate_matchings(i+1, chosen, mask)
    if mask & B[i] == 0:
        chosen.append(i)
        enumerate_matchings(i+1, chosen, mask | B[i])
        chosen.pop()

enumerate_matchings(0, [], 0)
assert Counter(map(len,maximal)) == {5:42,6:168,7:24}
checks += 3

def exact_matching_probability(matching):
    k = len(matching)
    selected = set(matching)
    # Every discarded edge must be later than its earliest incident selected edge.
    adjacent = []
    for j, e in enumerate(B):
        if j not in selected:
            neighbors = [i for i, chosen in enumerate(matching) if e & B[chosen]]
            assert neighbors
            adjacent.append(neighbors)
    result = Fraction(0)
    for order in permutations(range(k)):
        rank = {idx:r for r,idx in enumerate(order)}
        a = [0]*k
        for neighbors in adjacent:
            a[min(rank[idx] for idx in neighbors)] += 1
        product = 1
        cumulative = 0
        for j in range(1,k+1):
            cumulative += a[-j]
            product *= (j+cumulative)
        result += Fraction(1,product)
    return result

classes = Counter()
aggregated = defaultdict(Fraction)
for m in maximal:
    p = exact_matching_probability(m)
    classes[(len(m),p)] += 1
    aggregated[len(m)] += p
    checks += 1
assert dict(aggregated) == expected
checks += 3
expected_classes = {
    (5,Fraction(19,13860)):42,
    (6,Fraction(261,98560)):28,
    (6,Fraction(8257,1995840)):56,
    (6,Fraction(91723,23950080)):84,
    (7,Fraction(1247,95040)):24,
}
assert dict(classes) == expected_classes
checks += 5
assert sum(count for count in classes.values()) == 234
checks += 1

# Independently check that the five orbit-class weights reproduce all three
# size probabilities and the terminal size expectation.
for k in expected:
    assert sum(q*count for (m,q), count in classes.items() if m == k) == expected[k]
    checks += 1

print('PASSED:',checks,'exact-rational identities and classifications')
print('Terminal matching sizes:',{k:str(v) for k,v in sorted(terminal.items())})
print('Output classes:',[(k,str(p),count) for (k,p),count in sorted(classes.items())])
print('Reachable occupied-vertex subsets:',residual.cache_info().currsize)
