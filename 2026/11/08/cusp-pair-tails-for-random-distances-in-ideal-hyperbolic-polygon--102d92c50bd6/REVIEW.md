# Scientific review: cusp-pair distance tail

## Correctness

**PASS.** For each ideal vertex, a sufficiently deep horoball intersects the polygon in a vertical strip after a suitable Möbius isometry, with exact area density proportional to \(e^{-u}\,du\). For points in two *different* cusps, the curvature-\(-1\) distance is \(u+v+\kappa_{ij}\) plus a uniformly exponentially small depth error. The Gamma-two survival integral gives \((R+1)e^{-R}\); integrating the error strip costs only \(O_P(e^{-R})\). Two points in the same cusp or involving the compact core contribute only \(O_P(e^{-R})\). The polygon area is exactly \((n-2)\pi\), which yields the displayed normalization. The ideal-quadrilateral coefficient and extremizer follow by direct substitution and the exact identity \(t^2/(t-1)-4=(t-2)^2/(t-1)\).

The accompanying deterministic checks verify cusp distance normalizations and coefficient identities; independent fixed-seed simulation checks the order and magnitude of the tail. Finite samples do not establish the infinite-distance theorem.

## Originality

**PASS under the documented best-knowledge comparison; independent historical priority is unverified.** The closest inspected primary works concern (i) deterministic billiard lengths in ideal hyperbolic polygons, and (ii) geometric statistics of random *shapes* of ideal quadrilaterals. Their statements do not imply an area-uniform **two-point** distance tail inside a fixed ideal polygon. Earlier local distance-statistic findings for a single hyperbolic cusp, and small-distance-to-boundary formulas for ideal polygons, likewise do not provide the cross-cusp \(R e^{-R}\) coefficient or its quadrilateral extremum. Searches using ambient pair distance, cusp convolution, cross-ratio, and long-distance-tail aliases did not reveal an equivalent statement. Failure to locate one is not proof of worldwide novelty; an older stochastic-hyperbolic-geometry formula remains a priority risk.

## Mathematical value

**PASS.** A finite-area ideal polygon has infinite diameter, so its pairwise distance distribution has an intrinsically geometric long-distance regime. The theorem identifies the universal exponential rate, the extra linear factor arising from two independently deep *distinct* cusps, and an explicit Möbius-invariant leading coefficient that distinguishes shapes. The regular ideal quadrilateral is a unique sharp minimizer of this nonlocal statistic. The formula also supplies a tractable benchmark for distance-based sampling in cusped regions.

## Limits and closest sources

The \(O_P(e^{-R})\) remainder applies to a fixed convex all-ideal polygon and is not uniform in degenerating moduli. The direct checks do not constitute an external audit. Closest primary sources: Castle--Peyerimhoff--Siburg (2011, DOI: 10.3934/dcds.2011.29.893), Parker--Peyerimhoff--Siburg (arXiv:1607.07383), and Martin (arXiv:1807.06202). The first two concern billiard length; the last concerns random ideal-quadrilateral shapes and associated punctured-torus invariants. The associated area-pair distance law is a different object.

Self-review: passed. Independent audit: not yet performed.
