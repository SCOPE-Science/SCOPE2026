# Scientific review

## Correctness — PASS
The exact probability law is normalized area of a disk clipped by a lattice Voronoi polygon. Its radial derivative is the angular measure remaining after excluding a finite union of circular intervals. The foot of each Voronoi facet lies strictly in its relative interior, so the corresponding newborn angular interval cannot be masked by another facet; the elementary square-root expansion gives precisely \(4m\sqrt{2/d}\) as a signed coefficient. Already-active endpoints are locally Lipschitz even at vertex events. Thus every genuine facet group is detected with multiplicity, and no other radius registers a nonzero square-root coefficient. The numerical verifier independently checks finite sample instances but is not used as the infinite proof.

## Originality — PASS (subject to historical priority)
The 2014 obtuse-superbase literature gives the geometric facet classification, and the 2014 homogeneous-distance article supplies distance-law context. The 2021 preprint version of Mémoli–Needham, Proposition 5.16, already asserts recoverability of the planar lattice point set from critical radii; therefore global injectivity itself is not original here. Their discussion provides a single lens-area expression and qualitative multiplicities of critical radii, but not the present two-sided local square-root formula for all genuine facet distances or the proof that vertex-threshold collisions cannot masquerade as new facets. Their later Example 3.18 is in fact a reflection-equivalent lattice pair. Kurlin (2022) explains the isometry classification using root invariants, independently of any radial law. The accepted claim is restricted to the precise universal singularity coefficient and no-spurious-threshold theorem, with full historical priority still provisional.

## Mathematical value — PASS
The exact singularity formula is a quantitative geometric tomography invariant: it reads *all* genuine Voronoi facet classes and their multiplicities from a local two-sided asymptotic of a scalar distance law. It remains valid at equal-length collisions and distinguishes facet singularities from Voronoi-vertex events, which are genuinely different geometrically. The complete, non-generic coefficient law sharpens earlier qualitative discussions of critical radii and is useful for precise reconstruction algorithms; it is not a restatement of the already-published global injectivity conclusion. Sampling stability and higher-dimensional analogues are not asserted.

## Scope and residual risks
This is exact-law, unoriented metric reconstruction; finite empirical samples do not certify the singular coefficients. Global historical priority is provisional, and this review is not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
