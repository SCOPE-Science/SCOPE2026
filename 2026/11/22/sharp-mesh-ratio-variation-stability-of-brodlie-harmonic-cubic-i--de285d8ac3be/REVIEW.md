# Scientific review

## Correctness — PASS
The explicit nonuniform harmonic selector has almost-everywhere nonnegative partial derivatives bounded by \(3(\ell+r)/(r+2\ell)\) for its right argument and \(3(\ell+r)/(2r+\ell)\) for its left argument. Each one-secant perturbation produces exactly three nonconstant Hermite cells. The central derivative is nonnegative because its normalized endpoint responses lie in \([0,3]\), and the two outer cells have exact basis variation \(8/27\). Finite telescoping plus lower semicontinuity yields the global upper estimate. Near-flat interior-step data approach every local coefficient, giving matching lower bounds; the scalar mesh-ratio function proves the finite/infinite dichotomy. The standalone checker passed 3,080 random comparisons, five asymptotic witnesses and exact-basis identities. Numerical tests are not used as infinite-grid proofs.

## Originality — PASS, qualified
The full Fritsch–Butland paper defines the nonuniform Brodlie selector and establishes one-input shape preservation, not the two-input variation norm. The inspected 2019 Aràndiga–Yáñez text compares approximation orders and restates the weighted mean without this perturbation identity. The previously published uniform harmonic-mean theorem gives only the special value \(59/27\), and the nonuniform Steffen theorem applies to a different slope rule and has a different mesh coefficient. The accessible 2013 Aràndiga abstract addresses order and monotonicity, but its full text remained unavailable (Oxford institutional VPN disconnected); this source and unindexed literature are residual priority risks. The new theorem does not claim the slope rule itself is new.

## Value — PASS
Nonuniform PCHIP/Brodlie interpolation is a standard shape-preserving reconstruction method, and stability to changes in measured ordinates is distinct from monotonicity of one reconstructed signal. The exact mesh-ratio coefficient provides a necessary and sufficient condition for a global BV perturbation bound on an arbitrary bi-infinite grid, locates sharp near-flat extremizing configurations, and measures how cell-length contrast degrades stability. It is not a renaming or a fixed-size numerical recomputation. The finite local factor \(377/105\) at successive lengths \((2,1,3)\) illustrates a nontrivial distinction from the Steffen formula \(107/27\), not a separate accepted claim.

## Limitations
Real data, fixed one-dimensional bi-infinite grids, the interior Brodlie weighted-harmonic rule, and the adjacent-increment seminorm only. No finite-endpoint PCHIP rule, knot-perturbation sensitivity or multivariate generalization is proved. The result is analytically derived and self-reviewed but independently unaudited. The 1984 source has a month-only print date; a later day-verified online record and the day-verified 2013 related paper are not represented as the original invention date.

Self-review: passed. Independent audit: not yet performed.
