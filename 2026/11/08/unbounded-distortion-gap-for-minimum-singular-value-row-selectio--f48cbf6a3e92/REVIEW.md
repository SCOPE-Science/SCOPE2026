# Mathematical review

## Correctness

**PASS.** The claimed family is fully defined for every integer \(N\ge2\). Direct orthogonality and the exact two-dimensional invariant block of the SPD operator establish its condition number \(3\) and the Arnoldi basis identity. All full-rank row pairs fall into exactly four amplitude classes, and the strict inequalities \(\beta>\gamma>\varepsilon\) determine **all** global optima. The DEIM and Q-DEIM pivot conclusions are exact. For an orthonormal frame the whitening distortion equals the condition number of the sketched frame. The standalone checker verifies 95,274 finite row subsets, without treating this as the proof of the infinite result.

## Originality

**PASS, qualified.** Bergermann's arXiv:2604.07158v1 (sections 3–5) motivates maximum-smallest-singular-value selection and analyzes condition-number distortion, but its inspected equations and algorithms do not give the exact E-versus-condition optimality separation. Drmač–Gugercin arXiv:1505.00370v1 analyzes interpolation inverse norms, while Ipsen–Saibaba arXiv:2511.02740v2 gives complexity comparisons of subset criteria. Neither inspected analysis implies this explicit all-selector and actual DEIM/Q-DEIM separation on SPD Krylov spaces with fixed parent condition number. General E-optimal versus condition-optimal experimental-design distinctions remain a priority risk.

## Value

**PASS, scoped.** The demonstrated objective mismatch concerns precisely the two quantities used to motivate a recent deterministic Krylov-sketch design. Even perfect global optimization of the E-criterion cannot uniformly control the stated whitening metric, and the two named pivot procedures exhibit the same gap. The explicit uniformly SPD example rules out attributing the gap to parent ill-conditioning. This is a methodological boundary rather than a new practical row-selection recommendation; the condition-optimal sketch has entries vanishing as dimension grows and may be inferior in noisy arithmetic.

## Sources and residual limitations

Primary comparison: Bergermann (2026), arXiv:2604.07158v1, equations (3.5)–(3.6), Algorithms 4.1–4.2 and sections 4–5. Earlier comparisons: Drmač–Gugercin (2015/2016), arXiv:1505.00370v1, and Ipsen–Saibaba (2025/2026), arXiv:2511.02740v2. No claim of broad literature exhaustiveness or finite-precision advantage is made.

Self-review: passed. Independent audit: not yet performed.
