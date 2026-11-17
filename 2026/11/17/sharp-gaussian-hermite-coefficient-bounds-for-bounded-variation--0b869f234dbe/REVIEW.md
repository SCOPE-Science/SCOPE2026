# Review of sharp Gaussian Hermite coefficient bounds

## Correctness

**PASS.** Rodrigues' identity and finite-measure Stieltjes duality give the exact BV coefficient norm. The Sonin energy identity, \(E'(x)=-2xy'(x)^2/n\), forces first-oscillation maximizers for all degrees. In even degrees, a rescaled initial-value ODE gives the first positive root displacement and the amplitude correction; combining its perturbation with the central-binomial expansion yields both sharp two-term parity formulas. The input class intentionally contains non-Lebesgue-integrable half-line indicators. The included verifier checks the key algebraic identities, critical amplitudes and asymptotic coefficients.

## Originality

**PASS, subject to historical priority risk.** The inspected primary texts of Krasikov (2004) and Vemuri (2008) have respectively a different Hermite weight and much stronger Gaussian/Fourier hypotheses. The DLMF supplies classical polynomial identities but not the claimed sharp BV coefficient theorem. Published Laguerre BV-coefficient results offer methodological analogies, not direct Hermite implications. The accessible published-index entry was a summary rather than an inspected full source, so no whole-document exclusion is asserted for it. The four implication comparisons, exact queries and accessible source material appear in AUDIT.json.

## Mathematical value

**PASS.** The result identifies precise worst-case jump geometry for an entire classical Gaussian coefficient family, establishes the sharp \(n^{-3/4}\) scale, and reveals a sign-changing first correction controlled by parity. These facts sharpen coefficient regularity estimates for functions with jumps, without claiming a whole-series approximation theorem.

## Limits

The result concerns real one-dimensional globally finite-variation data and standard Gaussian polynomial coefficients, not Hermite functions on Lebesgue space, multivariate chaos, weighted total variation, or joint coefficient norms. An independent mathematical audit and an exhaustive historical priority search have not been performed.

Self-review: passed. Independent audit: not yet performed.
