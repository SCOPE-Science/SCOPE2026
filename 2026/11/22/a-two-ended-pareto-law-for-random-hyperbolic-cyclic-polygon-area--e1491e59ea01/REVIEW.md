# Scientific review: limiting area-deficit law for hyperbolic cyclic polygons

## Correctness — PASS

The fixed-circle polygon area is reconstructed by an independent Poincaré-disk angle derivation and Gauss--Bonnet. Strict pairwise gap averaging establishes the unique area maximizer for every finite radius, including polygons whose cyclic gap exceeds \(\pi\). The passage to the limit is pointwise for strictly positive gaps, and anchored gaps have the exact Dirichlet density. A two-small-gap probability bound isolates a single angular collision and establishes the Pareto tail and its moment cutoff. The local positive Hessian at the unique regular minimum gives the lower-end coefficient, with the factor \(1/\sqrt n\) verified from the determinant of the simplex quadratic form. Conditional marks follow by conditioning the Dirichlet law on a small selected gap. The standalone numerical checker passed 1,310 deterministic assertions, and no infinite statement is inferred solely from the tests.

**Residual scientific risks:** This is a fixed-\(n\), iterated-limit theorem. It makes no unproved simultaneous \(R,t\) uniformity claim, finite-sample statistical assertion, or implication for different sampling measures. The analytic tail proof is insensitive to a small finite set of near-coinciding gaps only after the explicit two-gap error is estimated.

## Originality — PASS, with provisional historical priority

The 2013 primary study of hyperbolic cyclic quadrilateral area formulas and the 2015 cyclic-polygon existence/uniqueness analysis supply deterministic foundations only. The closest public same-sampling-model finding gives a complete **mean** formula and its logarithmically enhanced asymptotic, but explicitly excludes distribution and higher moments. A second same-sampling-model finding instead scales the **number of vertices** with circle radius and proves a critical Gaussian crossover. The most closely resembling Pareto results treat a **horocycle-segment triangle** or a **cyclic triangle inradius**, not fixed-\(n\) hyperbolic-circle polygon area. Statement-level comparison reveals no prior theorem that provides the exact cotangent-limit distribution with both endpoint coefficients and both marked limits. Bibliographic coverage is not exhaustive: an older equivalent via geometric angle spacings remains a specific priority risk.

## Mathematical value — PASS

The boundary between typical and mean geometric error is structurally motivated: known mean deficits scale as \(Re^{-R}\), but a typical fixed-\(n\) deficit scales as \(e^{-R}\). The theorem resolves this discrepancy by an explicit infinite-mean limit and sharp rare-collision probability. It also identifies the opposite, near-regular regime through a natural \((n-1)/2\)-dimensional quadratic exponent and an exact coefficient. Conditional shape laws describe the geometry at both extremes, rather than merely supplying a reparameterization of an existing mean formula. This supplies usable benchmarks for random hyperbolic polygon asymptotics while not claiming a general or uniform radius theorem.

## Sources, comparisons and limits

- Abrosimov–Mednykh, arXiv:1302.4919v1 (2013), Section 4.2: deterministic hyperbolic cyclic quadrilateral area formulas.
- Kouřimská–Skuppin–Springborn, arXiv:1506.08069v1 (2015), Section 4: cyclic hyperbolic polygon existence and uniqueness at fixed side lengths.
- *Finite polylogarithmic mean-area laws for random hyperbolic cyclic polygons* (2026), full result and proof: finite-\(n\) means, no distribution/higher-moment law.
- *A critical logarithmic-radius crossover for random hyperbolic cyclic-polygon area* (2026), full result: joint large-\(n\) regime, not fixed-\(n\) Pareto limits.
- *A Pareto area-deficit law for triangles sampled on expanding hyperbolic horocycles* (2026), full result: horocycle-segment sampling and different coefficient.
- *A universal half-Pareto incircle deficit in large random hyperbolic triangles* (2026), full result: different geometric invariant and exponent.

Numerical verification is corroborative. The result has not undergone independent mathematical or historical review.

Self-review: passed. Independent audit: not yet performed.
