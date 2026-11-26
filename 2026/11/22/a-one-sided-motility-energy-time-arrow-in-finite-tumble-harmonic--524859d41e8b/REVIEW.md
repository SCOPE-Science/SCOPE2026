# Independent mathematical audit

## correctness

PASS

The complete revised RESULT.md and SLOGAN.txt are in /workspace/repairs/1/. The theorem and its domain are retained. With k=a+c and ℓ=a+1, the generator gives LR=c−kR, L(US)=R−ℓUS and L(U²)=2US−2U²+2δ. The stationary covariance inputs are V=ac/k², V/ℓ and 2V/[ℓ(k+2)] in that order; the last follows from the R·U² balance and the mean of U², c/(kℓ)+δ. Solving the triangular transform and subtracting the autonomous backward covariance gives 2ac/[ℓk(k+2)] times [2/((s+2)(s+k))+(k+2)/((s+2)(s+k)(s+ℓ))]. Both inverse convolution kernels are strictly positive at every positive lag without divisions by rate differences. Setting s=0 gives the area, and the two-fold convolution's linear term gives the slope. At a=c=1 the profile is t(1+t)e^(−2t)/4, with area 1/8, slope 1/4 and maximum at 1/√2. The independent centered thermal OU component contributes zero to both mixed covariances: its square is independent of R and the cross term has zero mean conditionally on the motor. The repair states the exact rational transform rather than a fixed pole count. In the combined numerator factor 2s+2ℓ+k+2, substitution of s=−k gives a−c+4, so s+k cancels at c=a+4 and the remaining transform is exactly 4ac/[ℓk(k+2)(s+2)(s+ℓ)]. Substitution of s=−2 and s=−ℓ gives 3a+c and k+2, so neither remaining factor cancels. This check and positivity also hold when ℓ=2 on that line. Independent bounded semigroup/quadrature comparisons at distinct and coincident rates agreed within 9.3×10⁻¹⁶; the tested rates, lags, formulas and numerical differences are recorded in /workspace/branches/fa7b2abf-1961-4121-8679-a185da51908f/independent_notes.md. The frozen verifier was inspected, not run; its Monte Carlo starts the motor in stationarity but the position at zero with burn-in 18, at a=c=1 and lag one. The replacement correctly calls that check a finite burn-in approximation, not exact stationary sampling. The revised claim compares the two covariances and does not infer causation, a position-only arrow, or entropy production.

## originality

PASS

The model and several routes to computing moments are established. The retained contribution is the explicit stationary mixed-lag antisymmetry and its strict all-rate, all-lag sign. The inspected literature provides inputs or raw multipoint moment machinery, not this evaluated sign conclusion. The replacement now explicitly credits the inspected position-only arrow in the same finite-tumble model; that arrow can change sign and does not evaluate the mixed motor-position law. The cancellation remark is algebra from the retained transform, not a separate priority claim.

## value

PASS

With simultaneous measurements of the run flag and position, time ordering can be tested directly even where equal-time information cannot distinguish the two lags. The exact all-rate sign, closed profile and invariance under independent additive diffusion provide a quantitative benchmark for a joint observable absent from the position-only literature comparison. The conclusion concerns the population covariance, not the precision of its empirical estimate or a causal inference from that estimate. The scope and numerical clarifications leave this value intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
