"""Finite reproducibility checks for two-step obstructions in fair tournaments.

Runs with Python 3 standard library only. Finite checks complement the proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

checks = 0

def check(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1


def tournament(n, bits):
    adjacency = [[False] * n for _ in range(n)]
    shift = 0
    for u in range(n):
        for v in range(u + 1, n):
            if bits >> shift & 1:
                adjacency[u][v] = True
            else:
                adjacency[v][u] = True
            shift += 1
    return adjacency


def failures(g):
    n = len(g)
    out = []
    for u in range(n):
        for v in range(n):
            if u == v or g[u][v]:
                continue
            if not any(g[u][w] and g[w][v] for w in range(n)):
                out.append((u, v))
    return out


for n in range(2, 7):
    pairs = [(u, v) for u in range(n) for v in range(n) if u != v]
    counts = {p: 0 for p in pairs}
    pair_counts = {ps: 0 for ps in combinations(pairs, 2)}
    anyfail = 0
    num_tournaments = 1 << comb(n, 2)
    for bits in range(num_tournaments):
        g = tournament(n, bits)
        F = failures(g)
        fs = set(F)
        anyfail += bool(F)
        for p in F:
            counts[p] += 1
        for pair in combinations(sorted(F), 2):
            pair_counts[pair] += 1
    p1 = Fraction(1, 2) * Fraction(3, 4)**(n-2)
    for p in pairs:
        check(Fraction(counts[p], num_tournaments) == p1,
              ('single', n, p))
    s1 = sum((Fraction(v, num_tournaments) for v in counts.values()), Fraction(0))
    s2 = sum((Fraction(v, num_tournaments) for v in pair_counts.values()), Fraction(0))
    check(s1 == Fraction(n*(n-1), 2) * Fraction(3, 4)**(n-2), ('S1',n))
    check(s1-s2 <= Fraction(anyfail, num_tournaments) <= s1, ('Bonferroni', n))
    if n >= 3:
        p2 = Fraction(1, 4) * Fraction(5, 8)**(n-3)
        pair_cluster_sum = Fraction(0)
        cluster_count = 0
        for (a,b),(c,d) in pair_counts:
            if (a == c or b == d):
                check(Fraction(pair_counts[((a,b),(c,d))],num_tournaments) == p2,
                      ('cluster',n,(a,b),(c,d)))
                pair_cluster_sum += Fraction(pair_counts[((a,b),(c,d))],num_tournaments)
                cluster_count += 1
        check(cluster_count == 2*n*comb(n-1,2), ('count',n))
        check(pair_cluster_sum == Fraction(n*(n-1)*(n-2),4)*Fraction(5,8)**(n-3),
              ('cluster-total',n))
    print(f'n={n}: tournaments={num_tournaments}, P(any failure)={Fraction(anyfail,num_tournaments)}')

# The external-vertex lemma: three distinct ordered implications hold for
# at most 9/16 of assignments. Enumerate all possible endpoint patterns.
for m in range(2, 7):
    arcs = [(u,v) for u in range(m) for v in range(m) if u != v]
    for family in combinations(arcs, 3):
        valid = sum(
            all(not ((bits>>v & 1) and not (bits>>u & 1)) for u,v in family)
            for bits in range(1 << m)
        )
        check(Fraction(valid, 1 << m) <= Fraction(9,16),
              ('external-three',m,family))

# For a shared-origin pair of obstructions, the remaining outside-vertex
# implication count is 5 out of 8; a three-obstruction shared-origin
# cluster has 9 out of 16.
check(sum(not((bits>>1 & 1) and not(bits & 1)) and
          not((bits>>2 & 1) and not(bits & 1))
          for bits in range(8)) == 5, 'two-star')
check(sum(all(not((bits>>v & 1) and not(bits & 1)) for v in (1,2,3))
          for bits in range(16)) == 9, 'three-star')
print(f'PASS: {checks} exact rational / exhaustive assertions')
