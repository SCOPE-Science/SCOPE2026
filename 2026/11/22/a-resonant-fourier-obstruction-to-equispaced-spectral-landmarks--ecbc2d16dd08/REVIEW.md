# Independent mathematical audit

## correctness

PASS

Reconstructed the exact RKHS argument in RESULT.md §§1–3. The Fourier weights are symmetric, positive and exponentially decaying, yielding a real-analytic kernel; Vandermonde invertibility on consecutive modes gives strict positive definiteness. With normalized Haar measure the leading eigenvalues are 2,1,1 and the next is 1/2. The top frequency differences are ±1 and ±2, so each regular q-gon contributes a scalar Gram matrix for q=m/2≥3, including q=3. On the regular m-gon the k=0,±m samples coincide, and the unit vector (ψ₀−ψₘ−ψ₋ₘ)/√3 is orthogonal to all translates; its squared overlap with ψ₀ is 1/3. Equivalently, Fourier diagonalization gives a residual at t of 1−λ_t/(Σ_{k≡t mod m}λ_k), making the constant-mode obstruction explicit. On the two-coset set the equal-weight witnesses modulated at t reproduce all three top coefficients. The ±m coefficients vanish because q does not divide t−(±m) for t=±1, and for t=0 the shift π/m changes their phase by −1. The residual sum is thus bounded by (1/2+1+1)Σ_tail λ_k=(5/2)ε(1−2^{1−m}); the tail is strictly positive and no target mode is exactly a finite combination of translates, again by consecutive high-frequency Vandermonde invertibility. The explicit bounds and ratio are valid throughout the stated range, in exact arithmetic. The proof replays from these Fourier identities; the supplied floating-point checker was inspected, not executed, and is not the proof or a conditioning certificate. For the optional real unit-norm frame description, normalize the raw rows by √3.

## originality

PASS

The closest inspected prior work already gives the objective, tightness criteria, a qualitative nonoptimal-tight-design example on the sphere, and regular-circle aliasing for a Gaussian spectrum. It does not cover the rank-three circle counterexample with equal top-mode Grams, an analytic strictly positive kernel and an unbounded ratio. The exact indexed hit is the frozen record itself. The pass is for that precise comparison, not for qualitative insufficiency of tightness or for Fourier de-aliasing.

## value

PASS

Provides a quantitative obstruction to using a tight leading-mode sampling matrix as a proxy for the alignment objective: the Gram criteria coincide but the loss ratio is unbounded even with a fixed positive leading eigengap and an analytic strictly positive kernel. The two-coset witness exhibits the mechanism and a repair on the same circle and at the same sample size. The conclusion is not global optimality, not a counterexample for monotone or Gaussian spectra, and not an m-asymptotic for a single fixed kernel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
