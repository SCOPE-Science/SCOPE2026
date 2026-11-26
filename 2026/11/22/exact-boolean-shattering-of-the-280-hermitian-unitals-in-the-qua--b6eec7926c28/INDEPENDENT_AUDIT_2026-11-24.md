# Independent mathematical audit

## correctness

PASS

Independently enumerated all 293,930 nine-point subsets using lines defined by normalized projective covectors over F4. Exactly 280 have line intersections in {1,3}, matching the XORs of nonconcurrent line triples. Such a triple is projectively equivalent to the coordinate triangle, whose XOR is the zero set of the identity Hermitian form. Conversely nonsingular Hermitian forms are congruent and their zero loci are unitals. Instead of the supplied trace loops, tallied global containing-unital multiplicities and performed Boolean Möbius inversion on each contained six-set: all 64 counts are positive on each of 23,520 sets, with minimum count 1. Every contained five-set occurs twice, every contained six-set once. The all-positive pattern forces containment; any contained support of size at most six extends to a shattered six-set, whereas a six-positive/seventh-negative request fails by six-set uniqueness. This gives the exact polynomial 1+21z+210z^2+1330z^3+5880z^4+17640z^5+23520z^6 and purity. The independent run also gives the collinear/noncollinear three-point complement split 3,360/20,160. It is exhaustive in PG(2,4), not an extrapolation. Replay: python3 /workspace/branches/independent_unitals.py.

## originality

PASS

The family and its geometric construction are classical. The additional assertion is local universality on every contained six-set of the restricted 280-member family, with the sharp obstruction and full face counts. No checked source establishes that assertion or a theorem giving it by specialization.

## value

PASS

For a canonical finite incidence family the answer tells exactly which six membership queries admit every labeling, not just the maximum number of queries. Uniqueness at six pinpoints the first obstruction, and the exact support counts and complement types distinguish incidence cases that a generic VC upper bound cannot resolve. This is useful for point-query and finite-design comparisons without assuming generalization to higher field orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
