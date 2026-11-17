# Scientific review: microscopic radial deficits of random cyclic polygons

## Correctness

**PASS.** The exact chord-intersection identity fixes Euclidean normalization; a multinomial-to-Poisson limit gives joint nearest-neighbor gaps at every fixed finite tuple; an exponential spacing tail yields uniform integrability of second moments. The renewal split at the first point to the right supplies the exact covariance, including the correct zero-lag variance. The product-of-exponentials integral gives the Bessel marginal. `verify_cyclic_radial.py` passed direct Euclidean polygon and independent renewal checks. The proof does not infer asymptotics from simulations.

## Originality

**PASS, provisional best-knowledge comparison.** The motivating 2026 paper treats exactly three sampled circle points at fixed interior radius and recovers a dilogarithm, but not a growing-sample two-point radial-error covariance. Wendel's central semicircle formula, Sonnleitner's maximum-error Gumbel theorem, and prior fixed-sample logarithmic boundary-absorption/rare center-clearance results concern different regimes. The closest coverage/inclusion literature (Jewell–Romano 1982) may imply a one-point formula but no matching two-point covariance was identified from accessible material. Its full text was unavailable; this is a named priority risk, not evidence of noncoverage. No unconditional claim of historical novelty is made.

## Mathematical value

**PASS.** A fixed angular query becomes highly correlated with a second query separated by order \(1/n\), and the exact positive covariance \(4\pi^4e^{-u}(3+3u+u^2/2)\) quantifies that dependence, including its decay length and variance. The natural boundary inclusion transition at radial depth \(1/n^2\) receives an explicit Bessel law. These are interpretable, nontrivial local invariants of random geometric approximation; the covariance also warns that a purely local integration misses fixed-count global fluctuations.

## Closest literature and limits

The primary paper was read in its full arXiv text; the 2025 Hausdorff work was read directly; the two named published boundary-absorption/clearance results were read in their research result statements and proofs. Jewell–Romano's 1982 full text was not accessible after open-access searching and an institutional-access attempt. The result assumes uniform circle-boundary sampling, finitely many microscopic query locations, and no independent mathematical validation. The numerical tests were extracted and executed from the actual standalone checker.

Self-review: passed. Independent audit: not yet performed.
