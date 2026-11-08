# Scientific assessment of the square-index occupancy covariance window

## Correctness — PASS

For fixed positive indices the mixed factorial-moment formula follows by counting occupancies of one and two specified boxes. The log-ratio identity is valid whenever the number of balls exceeds the sum of the fixed indices, which holds in the asymptotic regime. The expansion through order \(m^{-2}\) is uniform on compact positive load intervals. At the square-index degeneracy the first-order coefficient is exactly a square, while the next coefficient is exactly one; this proves the stated limit and strict signs off the two boundary values. The accompanying checker independently confirms the exact covariance by complete finite allocation enumeration (720 cases), the algebraic cancellation (300 cases), and illustrative convergence (14 diagnostics).

The finite checks do not establish the infinite asymptotic; that part rests on the explicit Taylor remainder bound in the proof. The theorem does not assert boundary signs or uniformity in growing indices.

## Originality — PASS, with priority qualifications

The exact mixed occupancy moments and the leading fixed-load covariance matrix are not new and are not claimed as new. Békéssy's original generating function encodes finite joint moments; Barbour–Gnedin's infinite-box analysis treats mixed covariances and the possible normal limit correlations; Sagitov's general multinomial expansion records first-order mixed covariance with an unspecified bounded next remainder. The inspected statements do not supply an explicit order-one limit or the positive \(m^{-1/2}\) load window at the square-index *double* cancellation. The closest indexed published occupancy result concerns richness versus a single occupancy frequency, rather than cross-covariance between two distinct frequency coordinates.

The main priority risk is implicit coverage by a historical multivariate saddle-point or higher-order expansion. An inaccessible full text of Sevast'yanov–Chistyakov's classical local-limit paper remains a specific source gap. The result is therefore a carefully delimited asymptotic consequence, not a sweeping novelty claim about multinomial moments.

## Value — PASS

The exactly square-indexed pairs are the complete degeneracy family of the classical first-order covariance coefficient. At the central load, the limiting covariance is strictly positive despite zero first-order asymptotics, while nearby fixed loads have negative covariance. The universal parabolic critical profile quantifies an actual finite-sample dependence reversal invisible to the usual multivariate Gaussian covariance approximation. This gives a structurally motivated finite-size correction for canonical occupancy frequency statistics and explains why first-order zero correlation is misleading in their critical regime.

The result is restricted to fixed indices and equal box probabilities and is not a general theorem about arbitrary occupancy models.

Self-review: passed. Independent audit: not yet performed.
