# Independent mathematical audit

## correctness

PASS

For any word, the normalized pair counts are the expected binary order vector after independently choosing one occurrence of each symbol. This puts them in the three-item ordering polytope, whose six vertices are realized by block words. In coordinates (x/(ab),1−y/(ac),z/(bc)), its description is the unit cube cut by sum between 1 and 2; active bounds show there are no nonbinary vertices. If two multiplicities are singleton, the applicable inequalities simply order the two counts of trailing copies of the remaining letter; inserting copies in the three gaps realizes every allowed pair. Otherwise relabel so a,b≥2. The proposed hole (0,1,ceil(b/a)) meets 0≤a ceil(b/a)−b≤a−1 and the box bounds, but x=0 forces all b ones before any zero, so any 02 pair forces at least b occurrences of 12. This proves failure of saturation for every such content. With a=1 the integer hull slice has bc+1−|cx−by| points. The realized slice is the sum of two complete integer intervals and the offset (b−x)y; within a binary gap swaps of adjacent unlike symbols trace every pair count from zero to its maximum. For the absolute-value sum, writing t=cx/b and f={t} gives sum_y |t−y|=t²−ct+c(c+1)/2+f(1−f); with q=b/g each j/q occurs g times for x=0,…,b−1 and the added x=b has f=0. Thus the fractional correction after multiplying by b is (b²−g²)/6, giving precisely the stated gcd hole term after subtraction. The formulas give zero holes when b=1 or c=1 and yield H:D→1:3 when both tend to infinity. A separate exhaustive check at (1,2,2) enumerated 30 words, 27 realized triples and 29 hull lattice points, identifying exactly (1,1,0) and (1,1,4) as holes. Replay by enumerating distinct permutations of 01122 and comparing their pair counts with the integer box and slab; saved details at /workspace/branches/321a18e3-a7a6-4a0a-bf0d-8cbf3d1362ba/record4-small-check.txt. The supplied verification scripts were not executed; finite checks cannot substitute for the all-content argument.

## originality

PASS

The distinct supported claims are the complete saturation threshold in the multiplicity-scaled integer lattice and the exact singleton lattice-hole law. The normalized hull shape is the standard three-item linear ordering polytope, and the attainable singleton count and interval parametrization are already covered by the distinct-marker record; the frozen proof credits that enumeration. No novelty is assigned to those ingredients. None of the inspected sources establishes the saturation and hole formulas.

## value

PASS

This resolves when a natural convex relaxation of fixed-content deck consistency is exact on the integer lattice and gives a uniform obstruction when it fails. The singleton law measures the gap between the convex model and actual words, including an arithmetic gcd term and a nonvanishing asymptotic fraction of holes. The value is in those classification and hole results, not the known hull shape or the already available attainable-deck count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
