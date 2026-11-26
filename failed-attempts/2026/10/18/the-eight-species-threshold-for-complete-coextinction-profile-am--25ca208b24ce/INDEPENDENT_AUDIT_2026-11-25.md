# Independent mathematical audit

## correctness

PASS

Independent integer census: enumerate all labelled m-by-n zero-one matrices through m+n=8; test nonempty, distinct rows and columns; test connectivity by requiring a shared pollinator across every nontrivial plant cut. Partition the admissible labels into orbits by traversing adjacent row and column swaps. For d deletions, compute the t-th binomial moment of the extinct-plant count as the sum of binom(n-s,d-s) over t-element plant subsets whose neighborhoods have union size s; then invert in t. This different enumeration and histogram algorithm matches every row of certificate.json. There are 28 classes through seven vertices and no collision. At (4,4) there are 57 classes, 5 colliding buckets and 6 excess classes. Both explicit matrices pass all filters; the shared histogram matches at all five depths; both sorted degree multisets are (1,2,2,3), while the four-cycle counts are 0 and 1. The all-size plant degree formula follows from the first binomial moment over d and exact triangular inversion; at k=1 the survivor histogram gives pollinator degrees directly. For independent retention, division by (1-u)^n and substitution u/(1-u) reduce the basis-independence claim to independence of monomials. This proves the claimed finite cutoff and infinite-scope degree assertion separately. Frozen artifacts were inspected, not executed.

## originality

FAIL

The October 13 published catalogue statement supplies an equivalent eight-vertex collision and a stronger lower-side-size reconstruction theorem under the same connectivity, sampling and two-guild twin restrictions. This is precise positive coverage of the central claim, not an inference from an inaccessible paper or similar ecological language. The indexed statement does not establish identity of the witness matrices or coverage of the supplementary all-size degree inversion.

## value

FAIL

A sharp boundary for full distributional reconstruction is well motivated, but the already-covered threshold and the matched-degree nature of its obstruction supply no new incremental value here. The explicit four-cycle contrast usefully certifies this witness but does not add an independent structural theorem; the projection to both degree multisets is a routine linear extraction and the small census counts are ancillary corroboration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
