# Research review

## Correctness — PASS

The statement has explicit row-stochastic conventions, nonnegative off-diagonal rates, strictly positive total exit rates and step length, and independent order draws. In two states, the two exact ordered products and the full semigroup have the same scalar contraction \(e^{-(s+t)h}\); their affine equilibrium offsets are collinear. Strict monotonicity of \((1-e^{-zh})/z\) places the exact offset strictly between the two split offsets. The unique probability is derived explicitly for noncommuting generators, and shared equilibria give the commuting exception. Centered independent random affine intercepts then yield the exact finite-step second moment by a geometric series. The stated small-step expansion follows after accounting for its removable limits.

The three-state obstruction is exact: both product orders have identical transient trace by trace cyclicity, and their common value strictly exceeds the exact semigroup's transient trace for every positive step by strict convexity of \(z\mapsto\cosh(h\sqrt z)\). Therefore **even signed affine order weights cannot remove this discrepancy**. The included self-contained checker independently recomputes full matrices, finite-step order strings and the trace inequality for 448 finite assertions. It is corroborative rather than the source of proof. No infinite computation or independent verification is claimed.

## Originality — PASS, subject to publication-priority risk

Primary text comparisons separate this all-step **two-factor random-order exact expectation** from different mathematical conclusions. Veldman–Zuazua (arXiv:2109.13798) and Eisenmann–Stillfjord (arXiv:2210.05375) analyze randomized subproblem/splitting frameworks with convergence estimates, rather than a universal positive order-mixture identity. Childs–Ostrander–Su (arXiv:1805.08385) establish cancellation of the leading commutator under fair product-order randomization, but not a rate-calibrated exact semigroup for every positive step. Sumner (arXiv:1212.5311) studies the two-state Markov Lie geometry, not this exact probability, exact finite-horizon variance, or the strict three-state obstruction.

The final overlap check also inspected a random-order Langevin calibration result, which optimizes stationary Gaussian covariance rather than exact finite-time Markov means or the present three-state trace obstruction. The closely related published three-factor two-state splitting theorem (public research record `9b0eeef7eade`) is a **deterministic** exact factorization requiring a third exponential, unlike the present randomized mixture of the original two-factor orders. The published one-piece randomized generator-calibration theorem (record `543ac65eaf32`) samples a single importance-rescaled generator, not both full subflows in random order. The general fair-order trajectory central limit theorem (record `38d8d8425ab3`) already covers the small-step \(h^{3/2}\) strong-error *scale*: this scale alone is explicitly not asserted to be new. Neither that result nor its mean \(O(h^2)\) bound directly gives the present all-step exact weak identity or sharp dimension boundary.

Exact or equivalent consequences of more general Lie-algebra interpolation/product formulas may predate the sources read. Database searches and titles cannot certify global uniqueness or priority; that residual risk is real, especially for elementary two-state affine semigroup geometry.

## Value — PASS

The dimension-two identity is a motivated, structural exception to generic noncommuting Lie splitting: a randomized scheme using **only the two existing orderings** has exact ensemble mean at arbitrary step, and the exact strong-error expression makes the distinction between averaged correctness and sample-path correctness quantitative. The three-state trace obstruction proves the universality ends at the smallest possible higher dimension. The result is self-contained, naturally addresses numerical integration of finite Markov generators, and supplies useful rigorous positive/negative boundaries, without implying improved practical cost or full higher-dimensional methods.

## Limitations and sources

The theorem is specific to conservative two-state exact exponentials and the stated three-state example. Inaccessible general historical specializations remain a publication-priority risk. The numerical checks cover only finitely many rates and step sizes; independent mathematical and bibliographic audit are still absent.

Sources: Veldman–Zuazua https://arxiv.org/html/2109.13798v2 ; Eisenmann–Stillfjord https://link.springer.com/article/10.1007/s00211-024-01396-w ; Childs–Ostrander–Su https://arxiv.org/html/1805.08385v2 ; Sumner https://arxiv.org/html/1212.5311v1 ; and full public result documents https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-positive-three-factor-split-for-two-state-markov-genera--9b0eeef7eade , https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-unique-mean-exact-calibration-and-a-cantor-stationary-law-for-ra--543ac65eaf32 , and https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-gaussian-trajectory-error-law-for-random-order-lie-split--38d8d8425ab3 .

Self-review: passed. Independent audit: not yet performed.
