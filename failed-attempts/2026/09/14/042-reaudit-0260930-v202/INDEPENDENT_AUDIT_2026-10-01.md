# Independent audit — SCOPE-20260914-042

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For the stated energy-supercritical focusing NLS regime, there is a finite-codimensional manifold containing genuinely nonradial data whose solutions exhibit the same quantized type-II ground-state blow-up rates and norm behavior as in the radial MRR construction.

## Correctness

**FAIL** — The cited MRR theorem is radial. The package proves only a finite angular Morse-index observation and then asserts that the nonlinear MRR trapping, Lyapunov, high-Sobolev, profile, and shooting argument transfers verbatim. That step is not justified: the NLS nonlinearity couples spherical-harmonic sectors, so favorable centrifugal terms do not decouple the nonlinear estimates or establish the required full nonradial modulation and error closure. The numerical threshold script is illustrative and cannot fill this theorem-level gap.

## Originality

**PASS** — The exact nonradial NLS extension was not found in Resultary or the primary literature checked. MRR proves the quantized construction for spherically symmetric data, while Collot establishes a nonradial analogue for the semilinear heat equation, not this NLS theorem. Thus the claimed extension is best-of-knowledge original, although unproved here.

### Equivalent formulations

Aliases and equivalent formulations were compared against the closest primary sources; the assessment follows implication rather than title matching.

### Broader coverage

The checked broader theorems do not imply the exact final claim under the same hypotheses.

### Exact database or table

No finite database/table comparison is decisive for this theorem claim.

### Claim versus prior implication

The exact nonradial NLS extension was not found in Resultary or the primary literature checked. MRR proves the quantized construction for spherically symmetric data, while Collot establishes a nonradial analogue for the semilinear heat equation, not this NLS theorem. Thus the claimed extension is best-of-knowledge original, although unproved here.

## Value

**PASS** — A genuine nonradial extension of the quantized type-II NLS construction would remove a major symmetry restriction in a difficult supercritical blow-up problem and is mathematically substantial.

## Source inspections

- Type II blow up for the energy supercritical NLS — https://arxiv.org/abs/1407.1415 — NOT_COVERING: The established theorem is radial and supplies the quantized rate being imported.
- Nonradial type II blow up for the energy-supercritical semilinear heat equation — https://arxiv.org/abs/1604.02856 — RELATED_NOT_COVERING: It concerns the heat equation, not NLS.
- Published-results semantic search — https://github.com/Resultary/2026/tree/main/2026/9/14/SCOPE042 — NO_STRONGER_MATCH_FOUND: The exact record was the direct match; no distinct published SCOPE theorem was found that supplies the claimed extension.

## Residual risks

- Literature search is best-of-knowledge and cannot exclude an obscure or unindexed source.
- The audit credits only inspected proofs, source material, and fresh computations described above.

## Disposition

FAILED
