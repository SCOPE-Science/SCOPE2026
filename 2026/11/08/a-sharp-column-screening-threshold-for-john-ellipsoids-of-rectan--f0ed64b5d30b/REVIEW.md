# Self-review

## Correctness
PASS. The normalized simplex contact vectors have exactly zero weighted barycenter and identity weighted second moment. Their block embeddings satisfy the same John criterion for a direct-sum ellipsoid in the product of simplices. The column support equals \((m+\sqrt m)/(n+1)\), which makes containment, necessity, and strict/equality contact cases exact. Eigenvalues and determinant yield the stated volume. Standalone exact-rational and integer arithmetic checks reproduce the critical identities and boundary examples. The universal proof is analytical; numerical checks are ancillary.

## Originality
PASS, with provisional historical priority. Heuer–Striker's Section 3 supplies the rectangular matrix inequality description but no maximum-volume ellipsoid. Eisley–Matsushita–Vindas-Meléndez study matching-polytope integrality and Gorenstein properties. The closest publicly available John-ellipsoid result handles square, not rectangular, matching polytopes, with all facet orbits contacting; its complete result has been compared and explicitly excludes nonsquare matrices. The present theorem is the sharp *if-and-only-if* screening threshold and the exceptional square-index boundary for rectangular polytopes. Searches by object, dual terms, ellipsoid equivalence, and phase parameters identified no prior equivalent claim. Residual risk: a general earlier result about John ellipsoids of simplex products cut by transport margins could indirectly imply this threshold.

## Mathematical value
PASS. A natural family of complete-bipartite matching polytopes has a sharp metric transition: an explicit certified product-envelope John ellipsoid survives all extra column facets exactly in a computable range. The contact combinatorics changes precisely on an infinite integer family of boundary dimensions; the theorem supplies all semiaxes, the volume, and a genuine contrast with the known square case. It does not purport to solve the complementary unscreened range.

## Limitations and closest literature
The statement assumes \(m,n\ge2\), canonical inequalities, and the Frobenius metric. It neither extends to arbitrary graphs nor evaluates the non-screened mixed-aspect-ratio regime. Primary context: Heuer and Striker, arXiv:2012.09901; Eisley et al., arXiv:2407.08820; *Exact John ellipsoid of the doubly substochastic matrix polytope* (square setting). Earlier equivalent literature and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
