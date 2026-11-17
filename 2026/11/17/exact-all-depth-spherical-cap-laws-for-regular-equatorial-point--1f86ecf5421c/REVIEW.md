# Scientific review: equal-equator spherical-cap depth law

## Correctness — PASS
For each \(n\ge3\) and \(0<r<\pi/2\), conditioning on uniform sphere height gives an equally spaced longitude lattice with cap halfwidth \(L_r(z)\). The exact clipped ramp probability for each depth has an integral antiderivative \(zL_r(z)+B_r(z)\), and evaluating at the depth boundaries yields the stated elementary tail probabilities. Complementation and parity handle the hemisphere and larger radii, while local expansion \(L_{r_k+\varepsilon}(z)=r_k+\varepsilon-\frac12\cot(r_k)z^2+\cdots\) gives the sharp \(3/2\)-onsets. Uniform Taylor expansion near the hemisphere produces the quadratic uncovered coefficient. The self-contained code passed 490 distinct checks against a separately integrated formula, exact mean and normalization, and geometric enumeration; the proof, not those tests, covers all cardinalities and radii.

## Originality — PASS (priority remains provisional)
The primary geometric-covering literature on spherical dispersion provides extremal covering questions, not this full equatorial cap multiplicity law. Materially read published records on circularly centered Euclidean disk unions prove area and radial union optimization, which addresses a depth-zero issue, but not the entire depth distribution or higher-depth threshold hierarchy. Materially read tetrahedral-cap multiplicity results concern noncoplanar four-center geometry, not the equatorial \(n\)-gon. Distinct random-cap coverage work has random site locations and cannot imply the deterministic fixed-site law without further arguments. Record searches by exact objects and aliases did not reveal a dominating formulation. Unindexed historical sources and a partially inspected primary covering paper remain residual priority risks; failed search is not a proof of novelty.

## Mathematical value — PASS
The answer is a complete exact probability distribution for a natural geometric family at *all* radii, with a sequence of distinct higher-order contact thresholds and sharp noninteger onset exponents. It refines elementary covered-area questions to arbitrary multiplicity, identifies the parity collapse at the hemispherical boundary, and supplies precise benchmarks for spherical coverage geometry. This is more than a renaming of the elementary angular lattice and its value does not rely on numerical experiments.

## Limitations
The result does not classify general sphere coverings or random sites. Only the explicitly stated equal-spaced equatorial setting is proved, no independent mathematical audit has been performed, and historical priority can be revised by discovery of equivalent literature.

Self-review: passed. Independent audit: not yet performed.
