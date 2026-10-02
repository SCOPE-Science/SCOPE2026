---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

Nested corner spectra of the stated two-parameter complex Hermitian Wigner ensemble admit explicit unbiased low-degree estimators of the diagonal second moment and off-diagonal fourth moment with the displayed variance and central limit theorem; the same parameters are recoverable by quadratic variation of the first two Brownian angular modes of the limiting field, implying mutual singularity for distinct parameter pairs.

## Correctness — PASS

The finite-corner part is self-contained: trace differences recover \(X_{kk}\) and the new column energy exactly; disjoint columns give independence; the standard fourth-moment identity yields the displayed harmonic correction and leading variance; strong laws and a triangular-array central limit theorem follow under the stated moments. Given the record's stated Brownian mode normalization, dyadic quadratic variation recovers the two variances and yields singularity. The actual finite verification script was inspected and corroborates the trace identities and variance formula, but finite computations are not used as proof.

**Checked sources.** assigned RESULT.md and actual verification script; Raposo, arXiv:2609.20707, primary abstract; Borodin, Moscow Mathematical Journal 2014

**Residual risks.** The recent Raposo full text was unavailable after open and institutional attempts, so the exact constants in the angular-mode normalization were not independently re-extracted.

## Originality — FAIL

The headline inference is mechanically obtained from ingredients already present in the source framework and classical probability. Nested traces determine the newly exposed diagonal and column energy by elementary matrix identities; unbiasedness, exact variance, strong consistency and the central limit theorem are standard moment calculations. Once the source identifies the two parameters with the first two Gaussian modes, Brownian quadratic variation and classical Gaussian equivalence/singularity theory directly give the field separation. Under the required implication-level standard, combining these routine consequences does not create an original theorem.

### Equivalent formulations

The claimed estimators are the first two trace increments followed by textbook sample-moment statistics, not a new spectral reconstruction mechanism.

### Broader coverage

The continuum singularity conclusion is a direct specialization of classical Gaussian-process theory once the mode variances are known.

### Exact database or table

Absence of a printed formula does not establish novelty because the formula is an immediate fourth-moment expansion of a sum of independent entries.

### Claim versus prior implication

Those prior implications cover the final claim at the audit's level of mathematical content even if the exact finite-sample formula is not separately stated.

**Checked sources.** https://arxiv.org/abs/2609.20707; https://www.mathjournals.org/mmj/2014-014-001/2014-014-001-002.html; classical Brownian quadratic-variation and Gaussian-measure theory

**Residual risks.** The exact Raposo full text was inaccessible, but the originality failure rests mainly on the routine implication structure, not on an assertion that the primary paper explicitly prints these formulas.

## Value — FAIL

The estimators and singularity statements are useful diagnostics, but they are textbook trace/moment and quadratic-variation deductions once the new two-parameter source model is given. The exact harmonic correction is a small calculation rather than a separately motivated unknown invariant, so the package does not clear the shared value bar.

**Residual risks.** The statistics may still be convenient for exposition or simulation.

## Limitations

- The finite-matrix formulas are for the complex Hermitian normalization.
- The exact normalization of the limiting angular modes could not be re-read in the full recent primary preprint; only its abstract was accessible after lawful full-text attempts.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
