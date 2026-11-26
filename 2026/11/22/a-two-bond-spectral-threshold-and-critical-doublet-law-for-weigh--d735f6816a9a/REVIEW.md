# Independent mathematical audit

## correctness

PASS

For finite matching, decay gives u₀=az u₁ and u_(m+1)=az u_m, so the interior Jacobi recurrence has effective coefficients a²z at both endpoints; its determinant is (1−a²z²)²−(a²−1)²z^(2m+2). The second secular channel has one interior root exactly when β(m−1)>2; at equality a direct bounded-tail solution is affine on sites 1,…,m with slope −βu₁=βu_m, hence u_m=−u₁. There is no square-summable band solution. The frozen fixed-a split follows from root deviations ±β/(2a^(m+2)) and the energy derivative −β/2, correct but covered. In the narrowed result, uniform convergence on compact κ intervals and two-sided positive-root sign brackets justify the two discrete spectral limits. Exact threshold distinguishes fixed γ=2 from a moving coupling. For the moving threshold, dividing the minus equation by z² gives the positive product displayed in the repair with x=(m−1)(−log z). Its first factor is ≥1 and its increasing second factor forces x→0 when Δ→0+, with uniform Taylor coefficient 1/2+1/(m−1). Thus Δ/x→1 and m(−log z)/Δ→1 without a rate constraint; cosh gives the ratio 1/2. For γ_m=2+s/m, mΔ=s−2m/(m−1), so there is no second state at s=2 despite zero limiting detuning, and the positive quartic coefficient is correct for s>2. Replay: repaired proof and independently performed cancellation-safe bisection reproduced in repaired VERIFICATION.md. Frozen VERIFICATION.md and verify.py were read but not executed; finite eigensolvers do not certify infinite spectral completeness.

## originality

PASS

PASS is for the repaired discrete weak-binding convergence, especially the uniform arbitrarily small positive detuning law and quartic lattice window. The exact same-model finite spectrum and fixed-enhancement law are demonstrably covered, and the limiting continuum double-delta spectrum is also credited, not passed as new. None of the actual nearest statements inspected establishes the moving-coupling lattice scaling or the relative detuning error control for this model.

## value

PASS

Fixed-amplitude tunneling is not a uniform estimate when localization length grows with bond separation. The repair quantifies the two competing lengths and resolves the lattice's moving binding window: above a positive detuning tending to zero at any rate it determines the actual secondary gap, not just whether a root exists. The explicit m^−4 regime distinguishes a missing state from a shallow bound state where the continuum m^−2 limit alone cannot. This is the useful lattice result, not the threshold renaming or the already known continuum doublet.

The dated certificate retains the supplied scientific assessment, sources and limitations.
