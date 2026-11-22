# Scientific review of cusp-diameter laws for hypocycloids

## Correctness — PASS

The curve's Euclidean arclength density is exactly \(2r(n-1)|\sin(nt/2)|\); integration gives \(8r(n-1)\). Strict containment of each open hypocycloid arc inside the triangle between its neighboring cusps and the origin identifies the convex hull as the regular cusp polygon. Diameter pairs therefore occur exactly at the farthest cusp pairs, which form a matching for even cusp counts and a cycle for odd counts. The cusp Taylor expansion and the integrated speed give first-order inward position \(v_j-s e^{it_j}+O(s^{3/2})\). Its projection along a diametral direction gives the strictly positive coefficient \(a_n\), with uniform control on all four one-sided approach combinations. Integration over a two-coordinate simplex yields the sharp probability constants and, by normalized \(L^1\) convergence, the marked Dirichlet law. The finite vector of nearest sample-to-cusp arclength distances has an exact multinomial survival expression and independent exponential limit. Joint continuous mapping gives the maximum-sample limit with its necessary shared-vertex dependencies. The complete proof is in RESULT.md; the bundled standalone checker independently reproduces geometric identities, convex-hull support and six asymptotic coefficients.

Risk: the theorem is fixed-parameter and finite-dimensional. No uniformity as the number of cusps increases is claimed. Numerical midpoint quadrature confirms coefficients at finite deficits but is not an infinite proof.

## Originality — PASS (subject to historical priority)

Actual semantic comparisons searched hypocycloid/deltoid/astroid arclength random chord extremes, curvature cusp reductions, and general parity-dependent diameter laws. The closest checked mathematical records cover (i) independent area-uniform points in an odd regular polygon with a two-dimensional Poisson corner-cone limit, and (ii) independent boundary-arclength points on **regular polygon edges**, refined as their side count diverges. Their full RESULT.md texts were inspected. Neither implies the cusp-arclength law of a fixed, nonpolygonal hypocycloid or the coupled exponential-cycle sample-extreme limit. The full accessible 2015 hypocycloid-division text concerns compass-and-straightedge constructibility; the 2013 AMS geometric exposition concerns rolling and group traces. The 2009 cycloidal-area article's accessible abstract concerns geometric areas, not probabilistic chord extremes. The source inspections and statement-level implication checks appear in AUDIT.json.

Risk: a classical source on hypocycloid random chords not indexed by the checked searches could overlap. The full 2009 cycloidal-area text was inaccessible; only its complete public abstract and metadata were examined. No independent historical-priority certification is asserted.

## Mathematical value — PASS

The ordinary hypocycloid family is a standard geometric object, and its cusp singularities make arclength loss fundamentally different from the smooth-curvature or polygon-interior models. The result completely resolves the upper chord tail at every fixed integer cusp count, locates exceptional endpoint shapes, and identifies an exact parity-dependent, correlated rare-sample diameter distribution. The shared-vertex dependence for odd cusp counts and the even matching reduction are not arbitrary parameter specializations: they describe structurally different extremal contact graphs for a natural family. The explicit coefficients, \(n=3\) distribution and reproducibility implementation can support subsequent geometric sampling and singular-boundary extremes.

Self-review: passed. Independent audit: not yet performed.
