#!/usr/bin/env python3
"""Exact finite tests for the marked covering-pair law in random tournaments.
These tests do not establish the large-size theorem; see its analytic proof.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import factorial

checks = 0
for n in range(3, 7):
    edges = list(combinations(range(n), 2))
    total = 1 << len(edges)
    event_multiplicity = Counter()
    named_event_count = 0
    conditional_scores = Counter()
    conditional_patterns = Counter()
    strict_extremes = 0
    exactly_one = 0
    for mask in range(total):
        out = [set() for _ in range(n)]
        for j, (a, b) in enumerate(edges):
            (out[a] if (mask >> j) & 1 else out[b]).add(b if (mask >> j) & 1 else a)
        covering_pairs = [(x, y) for x in range(n) for y in range(n)
                          if x != y and y in out[x] and out[y].issubset(out[x])]
        event_multiplicity[len(covering_pairs)] += 1
        if (0, 1) in covering_pairs:
            named_event_count += 1
            conditional_scores[len(out[0]), len(out[1])] += 1
            patterns = tuple((int(z in out[0]), int(z in out[1])) for z in range(2, n))
            assert all(t in ((1, 1), (1, 0), (0, 0)) for t in patterns)
            conditional_patterns[patterns] += 1
        if len(covering_pairs) == 1:
            exactly_one += 1
            x, y = covering_pairs[0]
            degrees = [len(s) for s in out]
            if degrees[x] > max(degrees[z] for z in range(n) if z != x) and degrees[y] < min(degrees[z] for z in range(n) if z != y):
                strict_extremes += 1
    p = Fraction(1, 2) * Fraction(3, 4) ** (n-2)
    assert Fraction(named_event_count, total) == p
    checks += 1
    # Every specified allowed orientation-pattern word is exactly equiprobable under covering.
    from itertools import product
    for word in product(((1,1), (1,0), (0,0)), repeat=n-2):
        assert Fraction(conditional_patterns[word], named_event_count) == Fraction(1, 3)**(n-2)
        checks += 1
    # Full bivariate score probability is the multinomial three-type image.
    m = n-2
    for dx in range(n):
        for dy in range(n):
            a = dy; b = dx-1-dy; c = m-a-b
            want = (Fraction(factorial(m), factorial(a)*factorial(b)*factorial(c))
                    * Fraction(1,3)**m) if min(a,b,c) >= 0 else Fraction(0)
            got = Fraction(conditional_scores[dx,dy], named_event_count)
            assert got == want, (n,dx,dy,got,want)
            checks += 1
    assert sum(event_multiplicity.values()) == total
    assert sum(k*v for k,v in event_multiplicity.items()) == n*(n-1)*named_event_count
    assert strict_extremes <= exactly_one <= total
    checks += 3
    print('n=', n, 'labeled_tournaments=', total,
          'P(cover)=', Fraction(sum(v for k,v in event_multiplicity.items() if k>0), total),
          'P(unique pair and rank extremes)=', Fraction(strict_extremes,total))
print('PASS:',checks,'exact assertions')
