# Scientific audit — SCOPE-20260913-025

Date: 2026-10-01 UTC

## Final claim

For the symmetric two-cut quartic Hermitian model with potential x^4/4-2x^2, the cubic-trace variance has distinct even and odd subsequential limits given by the record’s explicit multi-cut fluctuation formulas and numerical evaluations, so the full variance limit does not exist.

## Correctness

**PASS** — The equilibrium support and filling-period calculation were reconstructed, including normalization of the two-cut equilibrium density. The filling response coefficient is 4 pi divided by the positive A-period, as obtained from the z-to-infinity expansion of the normalized holomorphic differential. Independent high-precision evaluation reproduces the stated coefficient and widely separated even/odd variance limits. The nonconvergence conclusion is robust to the displayed numerical precision.

Residual risk: The decimal evaluations are high-precision numerical values rather than formal interval enclosures; the audit accepts the exact formula plus stable numerical evaluation, not a machine-checked decimal certificate.

## Originality

**FAIL** — The governing Gaussian-plus-discrete-Gaussian fluctuation law, oscillating filling fractions, and coupling through the derivative with respect to filling fractions are already supplied by the general multi-cut fluctuation theory of Borot–Guionnet and Shcherbina. The record specializes that framework to one symmetric quartic potential and one cubic statistic. Under implication-based originality, an explicit parameter specialization is covered even when the same decimals are not tabulated in the source.

Residual risk: There may be value as a numerical worked example, but that does not restore originality of the mathematical claim.

### Equivalent formulations

The general theorem expresses multi-cut linear-statistic fluctuations as a Gaussian part plus an oscillating discrete filling contribution, which is the mechanism used here.

### Broader coverage

Shcherbina treats linear-eigenvalue-statistic fluctuations in the multi-cut regime broadly, dominating this one-potential specialization.

### Exact database or table

No separate exact numerical table was found, but absence of a table does not overcome coverage by the general theorem.

### Claim versus prior implication

Substituting the symmetric quartic spectral data and cubic test statistic into the prior fluctuation formula yields the qualitative even/odd nonconvergence mechanism; the record’s main difference is explicit evaluation.

## Value

**FAIL** — After the coefficient correction, the surviving content is essentially a high-precision evaluation of a known general theorem at one reference parameter. No new structural phenomenon, boundary theorem, motivated exact invariant, or independently useful classification beyond that specialization is established.

Residual risk: The example can still be pedagogically useful as a benchmark, but the current scientific-value bar excludes routine parameter substitution and numerical evaluation.

## Sources inspected

- Asymptotic expansion of beta matrix models in the multi-cut regime — https://doi.org/10.1017/fms.2023.129 — COVERING: General theory gives Gaussian plus discrete Gaussian fluctuations with oscillating filling center and derivative coupling.
- Fluctuations of linear eigenvalue statistics of beta matrix models in the multi-cut regime — https://arxiv.org/abs/1205.7062 — COVERING: Provides the general multi-cut fluctuation framework specialized by the record.
- Published finding SCOPE025 — https://github.com/Resultary/2026/tree/main/2026/9/13/SCOPE025 — SELF_MATCH_ONLY: Exact matching indexed finding is this record; the decisive coverage comes from the primary general theorems.

## Disposition

FAILED
