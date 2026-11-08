# Scientific review

## Correctness
PASS. The defining inequalities and the changes of affine hull at maximal cardinality are independently verified against Gill--Linusson, Section 2, and Torres, Theorem 3.1. The proof explicitly projects coordinate, row, and column normals to the proper tangent spaces, then uses summed inequalities and the uniform point for matching upper/lower radius bounds. Equality conditions establish necessity and sufficiency of the complete center loci, their relative-interior dimensions, and all stated contact counts. Numerical linear programs in `verify.py` corroborate 175 finite cases but play no role as proof of the universal statements. A separate exact check confirms both integer threshold examples.

## Originality
PASS, subject to historical priority risk. Gill--Linusson (2009) proves the underlying faces and examines combinatorial, not Euclidean, diameter. Torres (2023) generalizes the matrix inequalities and studies normality, not inballs. Heuer--Striker (2020) studies the all-ranks partial-permutation polytope rather than this fixed-cardinality slice. The closest known square fixed-cardinality inball theorem (2026 record 6c3de65c0b12) explicitly excludes rectangular shapes and maximal-cardinality endpoints. Its square incenter locus is a scaled Birkhoff polytope, whereas the present rectangular result has asymmetrical row- and column-controlled phases and an affine-hull change at full row rank. Searches for radius, Chebyshev center, fixed-rank partial permutation matrices, and transportation analogues found no dominating equivalent. The possibility of an unindexed calculation remains.

## Mathematical value
PASS. This is a complete intrinsic Euclidean inball classification for an independently motivated infinite family of assignment polytopes, not a single arbitrary finite instance. Aspect ratio decides whether positive-dimensional optimal-center sets appear; the nonmaximal and maximal matching ranks have different affine geometries and distinct transportation-type center loci. The sharp, integer-realizable transitions and unbounded incenter dimensions quantify a feature of the family invisible to its usual face-count and graph-diameter descriptions. No downstream theorem is required for this structural classification to be useful.

## Limits and comparison
The result is confined to genuine rectangular matrices \(m<n\), the canonical Frobenius metric, and all integer matching cardinalities \(1\le k\le m\). The unrelated square full-rank Birkhoff endpoint is not included. Earlier literature establishes the polytope halfspaces and some related square geometry, so those premises are not claimed new. Numerical verification does not establish priority. No independent mathematical audit is asserted.

Self-review: passed. Independent audit: not yet performed.
