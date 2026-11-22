# Self-review

## Correctness — PASS

The action is free on every nonempty face because row rotation cannot preserve any labeled occupied column. Two edge orbits per ordered column pair and two triangle orbits per triple give an explicit quotient \(\Delta\)-complex. Its attaching words are recorded in RESULT.md, and the spanning-tree contraction and one/two-cell eliminations each remove a generator with a unique occurrence in a relator. The remaining attaching words are either freely trivial or degree \(\pm3\) in one loop. One degree-three cell gives the Moore complex; all other maps then become nullhomotopic and split as two-spheres. The number of spheres is exactly \(2\binom{n-1}{3}-n+1\). The standard-library certificate replays the exact word substitutions at nine widths; this is supporting finite verification, not the general proof.

## Originality — PASS relative to the inspected record

The classical literature addresses the unquotiented chessboard complex and its topology, and an earlier calculation of these particular cyclic-row quotients already establishes the fundamental groups and integral homology. This result expressly does not reclaim those invariants. Its new statement is the complete, infinite-family homotopy equivalence obtained from nonabelian attaching words. Identical homology and fundamental-group data alone do not generally determine the homotopy type of non-simply-connected two-dimensional CW complexes. Searches for equivalences under rook/matching, cyclic-row, alternating-row and Moore-space terminology disclosed no known theorem implying this precise decomposition. The closest recently inspected three-row classification concerns the unquotiented space. Risk: a hard-to-index equivalent equivariant cell calculation might exist.

## Value — PASS

The cyclic row action is canonical, free, and changes the topology from a simply connected sphere wedge to a space with order-three fundamental group. An explicit infinite-family Moore-space wedge model settles the attaching-map ambiguity left by previously determined homology. The width-five threshold is geometrically motivated; the same reduction controls every larger number of columns without finite extrapolation. This is a homotopy classification rather than a routine numerical increment.

## Scientific scope

The proof applies to the ordinary orbit space for every integer \(n\ge5\), not to homotopy orbits, other row actions or higher-row boards. Verification samples are not presented as an exhaustive test of infinitely many cases. The originality assessment is based on identified and materially inspected sources; publication priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
