# Independent mathematical audit

## correctness

PASS

The stationary convolution makes the relevant polynomials bounded. In dimensionless units, the generator applied to R=|X|² and H=X·n gives −2R+2H and 1−(1+α)H. Applying it to XᵀΣX and XᵀΣn gives their equal stationary means s/(1+α), since the heading marginal is ν. At redraw, the conditional value of H² is XᵀΣX, which closes the H², RH and R² equations without higher angular moments. Stationarity of R² gives E(RH)=E(R²); consequently the two-time centered system has equal initial covariances and solves to the displayed normalized kernel, including the repeated-root limit. The stationary variance is strictly positive and affine increasing in s. Its trace bounds are attained by isotropic covariance and symmetric antipodal laws, and their mixture realizes the whole interval. With a=2μ, b=μ+γ, the second and third right derivatives of K give −ab and ab(a+b), determining exactly the unordered pair. The swap is nontrivial and physically allowed exactly for γ≠μ, γ<3μ; γ=3μ would give a zero redraw rate. The mean depends only on ab. An independent symbolic check verified the variance factorization under the swap and the example 1/18 versus 1/63 (variance_swap_check.py in the independent algebra evidence); the sign is fixed by γ−μ at fixed ν and v. The frozen checker.py was inspected but not executed; VERIFICATION.md reports finite-check evidence only. No finite-data identifiability or stability is inferred.

## originality

PASS

There is exact indexed overlap for the normalized kernel in three-dimensional isotropic orientation, and the rate-exchange symmetry is already implicit in that kernel wherever it applies. The supported distinct claim is the centered, possibly anisotropic iid sphere-redraw result in arbitrary dimension with its explicit s-dependent variance, sharp angular envelope and full variance-resolved inverse classification in that scope. The narrower indexed result is not dismissed, nor is publication order inferred from the common date.

## value

PASS

The useful distinction is not the algebraic exponents alone: full radial relaxation shape and even the calibrated mean can leave a binary rate ambiguity, while a single stationary variance separates the assignments across all unchanged centered redraw laws. The sharp stationary fluctuation envelope quantifies how anisotropy affects amplitude while leaving shape invariant. This is an exact observability result in a natural model, not a claim about robust rate estimation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
