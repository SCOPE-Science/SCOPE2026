# Scientific review: Gaussian diagonal Fourier extensions

## Correctness — PASS

The exact Fourier-fiber minimizer follows from Cauchy–Schwarz with positive stationary kernel weights. Completing the square produces the Gaussian theta collision quotient without a missing scaling factor. Splitting the doubled theta sum by parity proves the duplication formula. The Jacobi product proves strict phase monotonicity, including nonzero curvatures at the endpoints; rational residue orbits, irrational equidistribution and the spectral theorem yield the sharp bounds and spectral laws. The two nearest Gaussian atoms give the large-localization parity asymptotics. The standalone checker passed 599 supplementary numerical comparisons after source extraction; numerical tests do not certify the universal arguments.

## Originality — PASS relative to inspected evidence

The general subgroup minimal-norm extension Fourier representation and generic norm/lower-norm principle in D. Winkle (2026) are explicitly recognized as prior work. The narrowly claimed additional result is the *strict theta collision-profile phase ordering*, the exact reduced-denominator parity law for high-localization conditioning, and the rational-atomic versus irrational-continuous spectral-edge distribution. Searches for Gaussian diagonal subgroup theta collision ratios, rational/irrational anisotropy, parity denominators and equivalent spectral descriptions found no prior statement establishing these particular conclusions. The exact theta-product identity itself is classical and not claimed. Relevant harmonic-analysis results in the available mathematical database concern different Fock, Hardy/Bergman or general kernel operators. The Winkle manuscript abstract explicitly mentions one-dimensional torus subgroups, however, and its inaccessible complete text could contain an overlapping example; this is a material priority risk, not a verified negative comparison of its full text.

## Value — PASS

The anisotropy ratio in an ordinary Gaussian torus covariance gives an abrupt and complete **arithmetic stability dichotomy** in the strong-spectral-localization limit: odd rational denominators asymptotically flatten the entire extension spectrum, while even denominators and irrational parameters retain a factor-two squared condition number. The exact finite-versus-continuous spectral classification and universal inverse-square-root edge densities clarify which Fourier modes are least stable and whether the sharp lower bound is ever attained. These are natural spectral conditioning invariants for minimum-norm kernel prediction, not an arbitrary finite parameter slice or a renaming of the generic extension principle.

## Closest literature and limitations

- D. Winkle, *Minimal-Norm Extensions of Stationary Kernels on Subgroups of Locally Compact Abelian Groups and Gaussian Conditioning*, arXiv:2608.04853 (2026-08-05): abstract and public metadata inspected; full text unavailable. Generic Fourier-fiber and sharp-norm principles are prior and excluded from the new claim.
- NIST DLMF, §20.5.3/20.5.9: full displayed Jacobi triple product inspected; this is an explicit classical proof ingredient.
- Existing result records involving theta-lattice curvature, Gaussian Fock spectral counting and twisted Hardy diagonal traces: different settings, no demonstrated implication of the Gaussian torus denominator-parity classification.

Limitations: coordinate-separable Gaussian weights; fixed diagonal circle; each asymptotic fixes its anisotropy fraction. No general stationary-kernel extension principle, arbitrary subgroup result or independent validation is claimed. The inaccessible motivating primary manuscript leaves a specific bibliographic precedence risk. Equality and nonattainment assertions are proven analytically, not inferred from finite sampling.

Self-review: passed. Independent audit: not yet performed.
