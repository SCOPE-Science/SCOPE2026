# Scientific review: Gamma popularity marks for microscopic Zipf occupancy records

## Correctness

**PASS.** The theorem is stated for fixed exponent \(a>1\), finite \(R\), exact Zipf weights, and a window of \(\lfloor\lambda n^{1-1/a}\rfloor\) future draws. The multinomial two-label identity establishes a uniform \(O(n^{-1})\) covariance approximation on compact normalized ranks. Together with the binomial marginal asymptotics and \(O(n^{1/a})\) relevant labels, it yields \(O(n^{-1/a})\) variance of the normalized random intensity. The explicit binomial small-count bound provides integrable small-rank and large-rank tails. The expected collision count is \(O(n^{-1/a})\); the post-history product Laplace functional then gives the conditional marked PPP, including the asserted compact-test rate. The Jacobian of \(y=cx^{-a}\) gives the exact Gamma shape \(r-1/a\). Verification in `CHECK.py` passed 1,710 exact/numerical assertions. These finite checks are secondary to the proof.

## Originality

**PASS, subject to historical-priority uncertainty.** The strongest close predecessor is Derbazi–Gnedin–Marynych, *Records in the Infinite Occupancy Scheme* (2023), whose Proposition 5 and Theorems 2–3 already give conditional and joint **unmarked** short-window Poisson records; no novelty is claimed for that projection. The present theorem retains the normalized label rank jointly with the exact occurrence time, identifies Gamma rank-popularity marks for every \(r\), and gives an explicit \(L^1\) convergence rate for compact Lipschitz Laplace tests in the fixed-draw setting. These claims cannot be inferred from the unmarked time-process law alone because that law forgets the label/predictive frequency. Abebe–Chebunin–Kovalevskii (2026) treat macroscopic Gaussian random outer measures, not this marked microscopic window. Targeted source/published-finding corpus comparisons did not reveal an explicit covering marked theorem, although a more general marked-process theorem may exist.

## Mathematical value

**PASS.** In a vocabulary/species-sampling model it matters not only *when* a previously rare label reaches its next multiplicity but also *which popularity range* supplies those records. The new rank-time process distinguishes first, second and higher records through a predictable Gamma-shape progression, independent of the event times and with a finite-window conditional approximation rate. The popularity composition is absent from the established time-only record law, so this is a natural new distributional invariant rather than a mere reparameterization of that law.

## Limits and closest literature

The result is restricted to deterministic exact Zipf frequencies, fixed record order and fixed window coefficient. It does not cover general slowly varying factors or dependent samples. Historical priority remains provisional, especially against unpublished or less readily searchable marked occupancy extensions. Sources: arXiv:2308.01739 (2023), Sections 5, 7, 8; arXiv:2602.13938 (2026), Theorem 2; Karlin's classical infinite-urn results. No independent examination has occurred.

Self-review: passed. Independent audit: not yet performed.
