# Scientific review: directional-energy dichotomy for Steiner ellipses

## Correctness — PASS

A centered ellipse has a positive-definite \(2\times2\) matrix with fixed determinant \(D\). Horizontal chord-centering makes its new matrix diagonal with entries \(A_{11}\) and \(D/A_{11}\); this is also a known formula in the prior ellipse literature. Rotating the direction produces the exact scalar map

\[
u_m=u_{m-1}\frac{u_{m-1}+\cos2\delta_m}{1+u_{m-1}\cos2\delta_m}.
\]

The denominator cannot vanish. The squared-ratio loss is precisely \((1-u^2)\sin^22\delta/(1+u\cos2\delta)^2\), giving the claimed monotonicity and explicit exponential bound. Conversely, finite angular energy gives a summable relative-loss series, and the anisotropy product stays positive unless one factor is exactly zero. The countability assertion follows from nonzero rational iterates. For harmonic angle increments the positivity and density arguments are explicit. The independent matrix checker passed all tests; finite tests are not used as an infinite proof.

## Originality — PASS, provisional priority

Actual primary-material comparisons were made against the 2026 random generalized-Steiner study of Kipp–Sagmeister, Bianchi–Burchard–Gronchi–Volčič's square-summable shape theorem, and Ulivelli's 2026 all-sequence convergence-in-shape result with its ellipse proof. Existing work covers ellipse preservation, broad shape convergence and dense-direction nonconvergence; these are explicitly credited. The reviewed claim is narrower in body class but differently quantified: a *necessary and sufficient condition on an arbitrary fixed direction sequence for universal disk convergence within ellipses*, with exact finite-step exceptional eccentricities, and a quantitative angular-energy estimate. No inspected statement or located mathematical-record summary directly implies all those assertions. This assessment is not an exhaustive historical proof of priority; older ellipse-specific presentations remain possible.

## Mathematical value — PASS

The natural distinction between reaching a Euclidean disk and merely converging up to rotations is central to deterministic symmetrization. The result classifies all angular inputs without randomness or a finite-direction assumption, identifies genuine finite-step resonances, supplies a certified rate, and describes the entire orbit of limits for an explicit dense-direction counterexample. These answer a motivated convergence question rather than merely recalculating a known table or testing arbitrary parameters.

## Scope and risks

Only centered planar ellipses are covered; it does not imply universal circularization for general planar convex bodies. The bound is uniform but not presented as optimally sharp. The motivating first public source is arXiv:2610.05113v1 (2026-10-04); the comparison arXiv:2611.21167v1 appeared on 2026-11-16. Residual risk: a historical equivalent reformulation could exist outside the primary text and indexed records examined.

Self-review: passed. Independent audit: not yet performed.
