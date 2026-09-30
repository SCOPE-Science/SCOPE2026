# Independent audit — 2026-09-29

**Record:** `2026/09/17/atom-safe-tunable-dkw-under-ate--c71ee97ffdf7`  
**Audited source tree:** `a95d5b0a81404e7ebed999f6506047b97600dcd9`  
**Repository:** `SCOPE-Science/SCOPE2026` at checked commit `253a0fe5d0217455660a277f9adb940030e567ad`  
**Overall independent-audit verdict:** **FAIL**

## Correctness — PASS

The mathematical statements check.  ATE bounded differences applied to empirical indicators gives the one-sided factor exp(-2nt^2/kappa), and the finite-bracket union bound yields Theorem 1.  For generalized quantiles, grouping repeated quantiles and using strict upper thresholds versus non-strict lower thresholds correctly gives the atom-safe width F(b_{k+1}-)-F(b_k)<=1/N and at most 2(N-1) nontrivial endpoint deviations.  Choosing N=ceil(2/r) recovers Roth's displayed bound without continuity, while N=n gives the fixed-r exponential rate -2r^2/kappa.  The finite-support specialization also follows directly from checking only the M-1 nontrivial CDF thresholds.

## Originality — FAIL

No exact prior statement was located, but the claimed research increment is a direct composition of two standard devices already present in the setup: ATE McDiarmid concentration and finite CDF bracketing/generalized quantiles.  The atom repair is the standard strict/non-strict endpoint convention, and the advertised factor-four rate improvement comes from leaving the bracketing resolution free and optimizing it instead of fixing Roth's convenient N.  This is a useful observation but not a sufficiently independent research contribution for a validated finding.

## Scientific value — FAIL

The result is technically correct and can be useful as a note or clarification, especially for discrete ATE models, but its central theorem package is essentially an elementary corollary/optimization of the cited concentration-plus-bracketing proof.  It does not introduce a new probabilistic mechanism, a sharp finite-sample constant, or a substantially new dependence theorem.  On the three-axis audit standard, that falls below the scientific-value threshold for retention as an accepted research finding.

## Publication disposition

The record is **not retained as a validated finding**.  Its mathematics is correct, but the independent audit rejects it on originality and scientific value.  The complete package should be relocated to the assignment-designated failed-attempt path; no mathematical-error claim is implied.

## Sources used in the independent comparison

- https://arxiv.org/abs/2606.12720 — Roth 2026; supplies the ATE bounded-differences input and states the compared DKW result with a continuous average marginal CDF.
- https://arxiv.org/abs/1405.0608 — Caputo--Menz--Tetali; background that ATE occurs naturally in discrete weakly dependent systems, explaining utility but not adding originality to the bracketing derivation.
- https://doi.org/10.1214/aop/1176990746 — Massart DKW background; classical i.i.d. DKW validity is not restricted to continuous distributions.

## Limitations and residual uncertainty

- Failure is on originality and scientific value, not correctness.
- A broad dependent-empirical-process literature was not exhaustively enumerated; the failure does not rely on claiming an identical earlier theorem, only on the elementary derivational character of the submitted contribution.

This independent audit is scoped to correctness, originality, and scientific value.  Repository material was used as evidence only; no GitHub modification was made during the audit.
