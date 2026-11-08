# Scientific review: sharp Frobenius diameter of partial alternating-sign-matrix polytopes

## Correctness — PASS

The source establishes that the objects whose convex hull defines the polytope are precisely its vertices [1, Proposition 4.3]. Independently, binary column prefixes bound the count of negative entries in row \(i\) by \(i-1\), so the sum of squares of one vertex is at most \(m^2\). Each negative inner-product contribution consumes a negative entry in one of the two matrices. These estimates give the global squared diameter bound. Equality forces maximal negatives in every row, unit row sums, all negative entries matched with opposite positive entries, and no overlapping positives. Row-prefix automata force the bottom row's two unmatched positives to bracket alternating overlapping signs, requiring \(2m\) columns. Equality then forces successive rows by interlacing and column-prefix exhaustion, yielding the unique staggered-diamond pair for each column selection. Constructed pairs meet all constraints and achieve the claimed bound. The transpose reduction covers tall rectangles. The separate strict-convexity argument excludes nonvertex diametral endpoints. Exhaustive integer checker tests and construction checks corroborate the analytic argument but do not certify all sizes.

## Originality — PASS, with residual priority risk

Full primary text [1] was checked at its definition, vertex theorem, inequality theorem, face lattice, and projection sections. It establishes no Euclidean/Frobenius diameter or complete diametral-pair count. The relevant sections of [2] address a distinguished family of faces and order/flow equivalences, which cannot bound all distances in the full polytope. [3] studies projected partial permutohedra; a nonisometric projection cannot transfer ambient Frobenius distance identities. Searches by the equivalent descriptions “partial alternating sign matrix”, “sign restricted matrix”, “rectangular signed matrix”, “Frobenius distance”, and explicit threshold/diamond-pattern parameters yielded no covering statement. Distinct published Euclidean-diameter statements for partial permutohedra concern the projection and do not cover the claim. The exhaustive historical literature has not been established: a formula in earlier sign-matrix or six-vertex-model literature remains possible.

## Mathematical value — PASS

This identifies a global Euclidean invariant of a canonical infinite family of signed polyhedra with complicated face structure, including a sharp rectangular aspect-ratio transition and a complete, nontrivial enumeration of farthest vertex pairs. The extremizers are forced into nested staggered alternating diamonds by the interaction of horizontal and vertical prefix restrictions. Their squared diameter grows quadratically in the shorter side, unlike the linear upper scale for the contained nonnegative partial-permutation matrices. This resolves a natural entire saturation regime, not a selected numerical example or isolated parameter slice.

## Scope and unresolved matters

There is no exact subthreshold diameter formula. Both geometry and counts depend on the standard matrix-coordinate metric. The finite checks are not an all-size proof. Historical priority remains provisional pending external literature review, and independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
