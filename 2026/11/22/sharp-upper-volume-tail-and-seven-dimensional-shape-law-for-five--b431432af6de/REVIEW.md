# Research assessment: sharp five-vertex upper-volume tail

## Correctness — PASS
The global maximum and equality class are supplied by the published five-vertex specialization of Horváth–Lángi, Theorem 2 (2014). Within each of the twenty labelled maximizing branches, the hull is the union of two pyramids over a common base, yielding the exact determinant expression in `RESULT.md`. The seven rotation-reduced coordinates give a zero gradient, a positive-definite Hessian with spectrum \(\{1/6,1/6,1/3,2/3,1,1,1\}\), and determinant \(1/162\). The normalized local measure has density \(1/(128\pi^3)\). The checked finite-dimensional ellipsoid volume then gives the exact coefficient \(24/7\). Compactness excludes nonmaximizing contributions, while coercivity and dominated convergence justify both the scalar limit and total-variation conditional shape law. The reproducible standalone symbolic checker passed. Risk: the independent high-level geometric derivation is not externally certified.

## Originality — PASS (historical priority provisional)
The 2014 global extremum and the regular triangular-bipyramid equality case are already known and excluded from the novelty claim. Bárány–Fodor–Vígh (arXiv:0906.0309, first public 2009) study bulk interior-uniform random-polytope intrinsic-volume variances for large \(n\); the sampling model and limit differ. Bonnet–O'Reilly (arXiv:1908.04033) study the same boundary-uniform sphere model but focus on facet heights and counts under asymptotic regimes for \(n\) and dimension, not the fixed-five upper-volume endpoint. Searches of known records for the five-spherical-point dipyramid, the \(7/2\) tail exponent, the numerical coefficient \(24/7\) and the seven-dimensional conditional ellipsoid yielded no statement implying the present combined result. Closest returned research records concerned four-point tetrahedral volume or higher-dimensional polytopes with different vertex counts. An unindexed source, including classical stability calculations, remains a genuine residual risk; a failed search is not a uniqueness proof.

## Value — PASS
A triangular bipyramid is the first non-simplex maximizer in three-dimensional unit-sphere polytope volume. The calculation identifies its exact stochastic rarity, including a nontrivial sharp coefficient, and the full conditioned seven-coordinate geometry rather than a routine deterministic restatement of the old maximizer. The contrast with the earlier tetrahedral five-half-power tail is motivated by the extra vertex and the geometric quotient dimension, while the explicit Hessian makes the endpoint probability independently reproducible. No unsupported general-dimension extension is claimed.

## Principal sources and limitations
[1] Bárány, Fodor and Vígh, *Intrinsic volumes of inscribed random polytopes in smooth convex bodies*, arXiv:0906.0309 (2009), DOI 10.1239/aap/1282924055. Its published primary MSC is 52A22.

[2] Horváth and Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496 (2014), Theorem 2.

[3] Bonnet and O'Reilly, *Facets of spherical random polytopes*, arXiv:1908.04033 (2019), DOI 10.1002/mana.202000314.

The claim treats fixed five-point surface-uniform sampling and only the leading upper-volume tail; general distribution, higher-order terms, other sampling and independent mathematical audit remain open.

Self-review: passed. Independent audit: not yet performed.
