# Mathematical review: exact polar volumes of ratio-bounded simplex central polytopes

## Correctness — PASS

The claim concerns \(m\ge2\), real \(c>1\), and the intrinsic Euclidean polar of the barycenter-translated coordinate-ratio polytope. The proof establishes that its primal vertices are precisely the two-level points indexed by all nonempty proper coordinate subsets. Its polar vertices come from the complete irredundant inequality system. The polar facet at each two-level primal vertex is the orthogonal Cartesian product of two scaled regular simplices. Multiplication of the exact facet volume by the exact origin-to-facet distance and summation over subset sizes yields the displayed formula with no missing or overlapping interior volumes.

The special \(c=2\) values were independently checked in exact rational arithmetic; Qhull volumes of all directly constructed polar vertices agree for \(m=2,\ldots,7\) and three distinct ratios. The accompanying executable completes 177,492 exact support/identity assertions and 18 independent geometric convex-hull volume checks. The proof, not these finite checks, covers all real \(c>1\) and all integer \(m\ge2\). The primal beta formula follows from normalized exponential random variables. The Santaló-point claim uses the standard uniqueness and affine-equivariance of the Santaló point plus permutation symmetry.

## Originality — PASS, provisional

Kazakov, *Generalization of Marion's Theorem*, arXiv:2606.02087v1 (2026), proves the primal \(c=2\) volume, describes the two-level vertices and discusses facet structure. Section 5 specifically suggests studying the dual polytope and its volume. It does not give the polar-volume sum here; the present theorem evaluates that open direction and extends the parameter to all real \(c>1\).

The closest related general geometric literature has materially different scope. Rietsch and Williams (2025) work with convex hulls of unweighted type-A roots and signed coordinate vectors, not the weighted, centered \(e_i-ce_j\) family; their full-text root-polytope definitions and polar section do not establish this formula. Filliman (1992) provides a general formula for dual volumes but no matching specialization was found in accessible metadata; such a general computational identity is not itself the evaluated all-dimensional binomial sum. Mészáros (2009) concerns triangulations and volumes of unweighted root polytopes, not the parameter-dependent weighted family. Multiple searches under the Marion, deltoidal-dodecahedron, bounded-ratio-simplex, asymmetric-root-polytope, polar-volume, and Mahler-volume formulations, together with comparison to the accessible historical claims, identified no equivalent statement or stronger theorem giving this formula. Absence of search hits is not proof of priority.

Residual risks include an unindexed equivalent formula for weighted complete directed root configurations, and incomplete access to the full 1992 general polar-volume paper. Independent historical-priority review is still needed.

## Mathematical value — PASS

The main motivating 2026 paper explicitly leaves the dual volume for further investigation. An exact all-dimensional closed expression for that volume is therefore a natural, missing geometric invariant rather than an arbitrary computation. The polar's complete facet decomposition into products of simplices explains why an exponential facet census collapses to a one-dimensional binomial sum. The theorem also gives the Santaló volume product, which is affine invariant across all nondegenerate simplices and was not determined by the prior primal-volume calculation. Both the actual edge-trisection case and the continuous ratio deformation are covered in one statement.

## Limits and status

The individual polar Euclidean volume uses the induced Euclidean metric in the canonical regular-simplex coordinates; only the volume product is affine invariant. Finite checks do not constitute a second proof of the universal formula. Historical novelty and all computations require independent audit before a certified priority claim.

Self-review: passed. Independent audit: not yet performed.
