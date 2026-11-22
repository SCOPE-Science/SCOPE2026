# Scientific review

## Correctness (PASS)

The final claim is exactly the maximum-degree-three full-support theorem, its resolvent sampling formula and uniform lower bound, with an exact degree-four obstruction. The trace expansion uses centered identity covariance, two independent draws of the **same** edge distribution, and symmetric idempotent averaging operators. The quadratic is strictly positive definite because its matrix is \(I/2+C^{\mathsf T}C/4\). The resolvent equation follows from simplex stationarity, with correct normalization. A contractive map on the cube proves resolvent nonnegativity, and the two endpoint equations imply the quantitative lower bound. The double-star KKT inequality certifies global optimality, including at the non-strict boundary; strict convexity certifies uniqueness. The delivered exact-rational checker passed all 526 graph cases; this is supplementary to the universal proof.

## Originality (PASS, with bibliographic risk)

Actual published-record and primary-literature searches found the foundational asymptotic-averaging-rate SDP of Boyd et al. and periodic deterministic convex-weight optimization, both different objectives. A pre-existing exact two-contact path result already gives the quadratic objective for general graphs and a path-only optimizer; the new universal support theorem, signless-resolvent formula on arbitrary subcubic graphs, quantitative bound and degree-four obstruction are not corollaries of its **path-specific conclusion**. A separate balanced-double-star bridge-deletion result concerns Laplacian spectral width, a different objective. Query matching and inspection did not identify an identical or stronger support theorem; this absence is evidence-limited, not proof that no equivalent unpublished or unindexed formulation exists.

## Value (PASS)

Whether a short-budget communication policy can discard a contact link is a structural design question that matters for graph connectivity and subsequent use of the same sampling law. The exact maximum-degree-three boundary provides a graph-size-independent guarantee, together with an explicit constructive distribution and nonzero probability margin. The degree-four double-star gives a sharp, naturally motivated loss-of-connectivity counterexample. The statement is stronger than a single numerical example and distinguishes finite-budget optimization from asymptotic connectivity-based designs.

## Closest literature and limitations

Boyd et al. (2004/2006) treat the same pairwise averaging operators but optimize an asymptotic spectral objective, not two-contact covariance-isotropic risk. *Towards optimal convex combination rules for gossiping* (2013) studies periodic deterministic schedules and an adjustable averaging coefficient. A prior two-contact path statement supplies the general objective but not the new all-subcubic positivity theorem. Only finite connected simple graphs, exactly two iid contacts, arithmetic averages, and covariance-isotropic initial disagreement are covered. Stronger equivalents in inaccessible historical sources remain possible; independent review has not been performed.

Self-review: passed. Independent audit: not yet performed.
