# Scientific review: equatorial bifurcation in pole-anchored spherical triangles

## Correctness — PASS

For each colatitude \(0<\theta<\pi\), the triple-product / dot-product formula gives exactly \(A_\theta=2\operatorname{Arg}(1+qe^{i\Delta})\), with \(q=\tan^2(\theta/2)\) and folded uniform gap \(\Delta\in[0,\pi]\). The correct \(\operatorname{atan2}\) quadrant is essential for southern latitudes. The two inverse branches above the equator and the unique inverse below it yield the three closed CDF expressions with their correct support endpoints. The event \(A_\theta>\pi\) is exactly \(\Delta>\pi-\arccos(1/q)\). Conditional uniformity of its rescaled endpoint gap is finite-parameter exact; a fixed-gap Taylor expansion yields the weak heavy-tailed limit. Continuity of a general gap density at \(\pi\) proves the biased-sampling extension. Quantiles and monotonicity prove identifiability. The standard-library checker independently evaluates spherical angles and verifies the formulas, but the argument is analytic and does not rely on finite tests.

## Originality — PASS, with a historical-priority caveat

The closest accessible full paper, Finch and Jones, *Random Spherical Triangles* (arXiv:1009.5329, first version 2010-09-27), addresses three points uniformly distributed over the **whole sphere** and its unconditional area density. It does not specialize to one fixed pole and two equal-colatitude boundary points, or state the universal conditional equatorial boundary layer. The public report *Dilogarithmic mean area of random fixed-latitude spherical triangles* treats **three random vertices on the latitude circle**, with a different symmetric expectation and a degenerate equator, not the anchored model. The earlier Le (1989) article gives cap-interior shape densities; only its abstract was accessible, so possible unexpected reductions cannot be conclusively excluded. A 2011 geometric discussion supplies an isosceles spherical triangle area identity but no stochastic transition, conditioned endpoint marks or smooth-sampling universality. The deterministic Girard and solid-angle identities are not claimed to be original. This is an implication-level comparison rather than a title match or an assertion that a failed search proves novelty.

## Value — PASS

The equator is a genuine geodesic bifurcation: the area support gains the entire interval \((\pi,2\pi)\) abruptly south of it, yet the new mass emerges only at square-root order. The conditional overshoot has a universal heavy-tailed law driven by nearly antipodal azimuthal endpoints. A strict stochastic inverse recovers north or south colatitude from the complete area law, unlike the reflection ambiguity for three random points on one latitude circle. The invariance of the conditional shape under arbitrary smooth positive azimuthal biases makes the result useful as a boundary model for pole-fan spherical triangulations and robustness of area sampling. These statements are mathematically sharper than the underlying deterministic spherical-triangle identity.

## Sources and unresolved risks

Full text was read for Finch and Jones (2010/2015) and the closely related fixed-latitude mean-area report. Direct published abstracts were examined for Le (1989) and van Oosterom--Strackee (1983), with a separate publicly available solid-angle implementation supplying the exact formula. Exact comparable queries were run against a mathematical-results index and general literature. Le's full text remained inaccessible; institutional access required an unavailable authorized connection. A specialized older stochastic treatment not indexed by the searches is a residual priority risk. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
