# Scientific review: finite circular Fourier-independence energy covariance

## Correctness

PASS. Under iid uniform torus sampling with independent coordinates and nonzero integer frequencies, the identity \(D_{p,q}=n^{-1}a_p^\top H b_q\), where \(H^2=H\), gives the exact mean energy. Haar character fourth-moment orthogonality distinguishes only no shared absolute frequency, one shared coordinate, and two shared coordinates with aligned/opposed signs. Explicit finite contractions yield the claimed four covariance values; an exact combinatorial pair count yields the rectangular-grid variance. The proof includes \(n=2\) and every finite frequency. The independent Laurent-polynomial checker executed all 45 exact-rational assertions successfully, including 33 checks based on direct constant-term extraction rather than the proof's projection contraction.

## Originality

PASS with historical-priority qualification. García-Portugués et al. (2021), Section 3 and Appendix B, define the empirical-characteristic-function discrepancy and derive first-order asymptotic linear covariance and permutation-calibrated omnibus testing; those results do not supply the present finite fourth-moment signed-frequency classification. Pfister et al. (2016), Propositions 3.10–3.11, cover much broader kernel-independence test classes but give asymptotic moment expansions, not this explicit finite-\(n\) Fourier covariance law or growing rectangular-grid variance. The nearest separate published circular Fourier-harmonic correlation result concerns uncentered **univariate** energies and cannot imply cross-frequency dependencies created by a **two-margin empirical product**. Searches for equivalent finite-null signed-frequency and rectangular-grid formulas did not identify dominating coverage. This is not a proof that all older literature has been exhausted; possible alternative derivations from general V-statistic identities remain a residual risk.

## Value

PASS. Weighted or truncated sums of Fourier discrepancies are a natural family of toroidal independence diagnostics. The exact variance gives a direct finite-sample second-moment calibration for a symmetric Fourier rectangle and quantifies non-negligible dependencies among modes sharing one marginal Fourier index. In particular it reveals a sharp structural difference between a fixed harmonic set, where off-mode covariances disappear, and frequency budgets with \(P+Q\) on the scale of \(n^2\), where those small covariances accumulate into an order-one relative variance correction. The full four-class law, including sign-reversal asymmetry, is mathematically distinct from simply substituting parameters into an asymptotic kernel formula.

## Closest literature and limits

- García-Portugués, Lafaye de Micheaux, Meintanis and Verdebout, *Nonparametric tests of independence for circular data based on trigonometric moments*, arXiv:2104.14620v1 (2021-04-29), Section 3 and Supplementary Appendix B. https://arxiv.org/html/2104.14620v1
- Pfister, Bühlmann, Schölkopf and Peters, *Kernel-based Tests for Joint Independence*, arXiv:1603.00285 (2016-03-01), Sections 2–3 and Appendix D.5. https://arxiv.org/pdf/1603.00285

The theorem is an exact second-moment statement under independent **uniform** marginals. It does not determine finite-sample quantiles, validate a general nonuniform null, prove test power, or establish a growing-grid central limit theorem. Both original definitions and broad kernel frameworks are acknowledged as prior work. An independent assessment of historical priority and the proof remains outstanding.

Self-review: passed. Independent audit: not yet performed.
